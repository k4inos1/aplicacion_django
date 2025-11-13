from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Equipo, Miembro, Proyecto, Entregable, EstadoEntregable, Comentario
from datetime import date


def index(request):
    """Vista principal con dashboard"""
    equipos_count = Equipo.objects.filter(activo=True).count()
    proyectos_count = Proyecto.objects.count()
    entregables_count = Entregable.objects.count()
    miembros_count = Miembro.objects.filter(activo=True).count()
    
    # Entregables recientes
    entregables_recientes = Entregable.objects.select_related('proyecto', 'responsable', 'estado').order_by('-fecha_creacion')[:5]
    
    # Proyectos activos
    proyectos_activos = Proyecto.objects.filter(estado='en_progreso').select_related('equipo')[:5]
    
    context = {
        'equipos_count': equipos_count,
        'proyectos_count': proyectos_count,
        'entregables_count': entregables_count,
        'miembros_count': miembros_count,
        'entregables_recientes': entregables_recientes,
        'proyectos_activos': proyectos_activos,
    }
    return render(request, 'entregables/index.html', context)


# ===== CRUD EQUIPOS =====
def equipo_list(request):
    """Lista de equipos"""
    equipos = Equipo.objects.all().order_by('-fecha_creacion')
    busqueda = request.GET.get('q')
    if busqueda:
        equipos = equipos.filter(
            Q(nombre__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    context = {'equipos': equipos, 'busqueda': busqueda}
    return render(request, 'entregables/equipo_list.html', context)


def equipo_create(request):
    """Crear nuevo equipo"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        activo = request.POST.get('activo') == 'on'
        
        if nombre:
            Equipo.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                activo=activo
            )
            messages.success(request, 'Equipo creado exitosamente.')
            return redirect('equipo_list')
        else:
            messages.error(request, 'El nombre del equipo es requerido.')
    
    return render(request, 'entregables/equipo_form.html', {'action': 'Crear'})


def equipo_update(request, pk):
    """Actualizar equipo"""
    equipo = get_object_or_404(Equipo, pk=pk)
    
    if request.method == 'POST':
        equipo.nombre = request.POST.get('nombre')
        equipo.descripcion = request.POST.get('descripcion', '')
        equipo.activo = request.POST.get('activo') == 'on'
        
        if equipo.nombre:
            equipo.save()
            messages.success(request, 'Equipo actualizado exitosamente.')
            return redirect('equipo_list')
        else:
            messages.error(request, 'El nombre del equipo es requerido.')
    
    context = {'equipo': equipo, 'action': 'Actualizar'}
    return render(request, 'entregables/equipo_form.html', context)


def equipo_delete(request, pk):
    """Eliminar equipo"""
    equipo = get_object_or_404(Equipo, pk=pk)
    
    if request.method == 'POST':
        equipo.delete()
        messages.success(request, 'Equipo eliminado exitosamente.')
        return redirect('equipo_list')
    
    context = {'equipo': equipo}
    return render(request, 'entregables/equipo_confirm_delete.html', context)


# ===== CRUD PROYECTOS =====
def proyecto_list(request):
    """Lista de proyectos"""
    proyectos = Proyecto.objects.select_related('equipo').order_by('-fecha_inicio')
    estado_filter = request.GET.get('estado')
    busqueda = request.GET.get('q')
    
    if estado_filter:
        proyectos = proyectos.filter(estado=estado_filter)
    if busqueda:
        proyectos = proyectos.filter(
            Q(nombre__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    
    context = {
        'proyectos': proyectos, 
        'busqueda': busqueda,
        'estado_filter': estado_filter,
        'estados': Proyecto.ESTADOS
    }
    return render(request, 'entregables/proyecto_list.html', context)


def proyecto_create(request):
    """Crear nuevo proyecto"""
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion', '')
        equipo_id = request.POST.get('equipo')
        estado = request.POST.get('estado', 'planificacion')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin_estimada = request.POST.get('fecha_fin_estimada')
        presupuesto = request.POST.get('presupuesto')
        
        if nombre and equipo_id and fecha_inicio and fecha_fin_estimada:
            Proyecto.objects.create(
                nombre=nombre,
                descripcion=descripcion,
                equipo_id=equipo_id,
                estado=estado,
                fecha_inicio=fecha_inicio,
                fecha_fin_estimada=fecha_fin_estimada,
                presupuesto=presupuesto if presupuesto else None
            )
            messages.success(request, 'Proyecto creado exitosamente.')
            return redirect('proyecto_list')
        else:
            messages.error(request, 'Todos los campos requeridos deben ser completados.')
    
    equipos = Equipo.objects.filter(activo=True)
    context = {
        'action': 'Crear',
        'equipos': equipos,
        'estados': Proyecto.ESTADOS
    }
    return render(request, 'entregables/proyecto_form.html', context)


def proyecto_update(request, pk):
    """Actualizar proyecto"""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        proyecto.nombre = request.POST.get('nombre')
        proyecto.descripcion = request.POST.get('descripcion', '')
        proyecto.equipo_id = request.POST.get('equipo')
        proyecto.estado = request.POST.get('estado')
        proyecto.fecha_inicio = request.POST.get('fecha_inicio')
        proyecto.fecha_fin_estimada = request.POST.get('fecha_fin_estimada')
        fecha_fin_real = request.POST.get('fecha_fin_real')
        proyecto.fecha_fin_real = fecha_fin_real if fecha_fin_real else None
        presupuesto = request.POST.get('presupuesto')
        proyecto.presupuesto = presupuesto if presupuesto else None
        
        if proyecto.nombre and proyecto.equipo_id and proyecto.fecha_inicio and proyecto.fecha_fin_estimada:
            proyecto.save()
            messages.success(request, 'Proyecto actualizado exitosamente.')
            return redirect('proyecto_list')
        else:
            messages.error(request, 'Todos los campos requeridos deben ser completados.')
    
    equipos = Equipo.objects.filter(activo=True)
    context = {
        'proyecto': proyecto,
        'action': 'Actualizar',
        'equipos': equipos,
        'estados': Proyecto.ESTADOS
    }
    return render(request, 'entregables/proyecto_form.html', context)


def proyecto_delete(request, pk):
    """Eliminar proyecto"""
    proyecto = get_object_or_404(Proyecto, pk=pk)
    
    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, 'Proyecto eliminado exitosamente.')
        return redirect('proyecto_list')
    
    context = {'proyecto': proyecto}
    return render(request, 'entregables/proyecto_confirm_delete.html', context)


# ===== CRUD ENTREGABLES =====
def entregable_list(request):
    """Lista de entregables"""
    entregables = Entregable.objects.select_related('proyecto', 'responsable', 'estado').order_by('-fecha_creacion')
    estado_filter = request.GET.get('estado')
    prioridad_filter = request.GET.get('prioridad')
    busqueda = request.GET.get('q')
    
    if estado_filter:
        entregables = entregables.filter(estado_id=estado_filter)
    if prioridad_filter:
        entregables = entregables.filter(prioridad=prioridad_filter)
    if busqueda:
        entregables = entregables.filter(
            Q(titulo__icontains=busqueda) | 
            Q(descripcion__icontains=busqueda)
        )
    
    estados = EstadoEntregable.objects.all()
    context = {
        'entregables': entregables,
        'busqueda': busqueda,
        'estado_filter': estado_filter,
        'prioridad_filter': prioridad_filter,
        'estados': estados,
        'prioridades': Entregable.PRIORIDADES
    }
    return render(request, 'entregables/entregable_list.html', context)


def entregable_create(request):
    """Crear nuevo entregable"""
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descripcion = request.POST.get('descripcion', '')
        proyecto_id = request.POST.get('proyecto')
        responsable_id = request.POST.get('responsable')
        estado_id = request.POST.get('estado')
        prioridad = request.POST.get('prioridad', 'media')
        fecha_vencimiento = request.POST.get('fecha_vencimiento')
        porcentaje_completado = request.POST.get('porcentaje_completado', 0)
        
        if titulo and proyecto_id and estado_id and fecha_vencimiento:
            entregable = Entregable.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                proyecto_id=proyecto_id,
                responsable_id=responsable_id if responsable_id else None,
                estado_id=estado_id,
                prioridad=prioridad,
                fecha_vencimiento=fecha_vencimiento,
                porcentaje_completado=porcentaje_completado
            )
            
            # Manejar archivo adjunto
            if 'archivo' in request.FILES:
                entregable.archivo = request.FILES['archivo']
                entregable.save()
            
            messages.success(request, 'Entregable creado exitosamente.')
            return redirect('entregable_list')
        else:
            messages.error(request, 'Todos los campos requeridos deben ser completados.')
    
    proyectos = Proyecto.objects.all()
    miembros = Miembro.objects.filter(activo=True)
    estados = EstadoEntregable.objects.all()
    
    context = {
        'action': 'Crear',
        'proyectos': proyectos,
        'miembros': miembros,
        'estados': estados,
        'prioridades': Entregable.PRIORIDADES
    }
    return render(request, 'entregables/entregable_form.html', context)


def entregable_update(request, pk):
    """Actualizar entregable"""
    entregable = get_object_or_404(Entregable, pk=pk)
    
    if request.method == 'POST':
        entregable.titulo = request.POST.get('titulo')
        entregable.descripcion = request.POST.get('descripcion', '')
        entregable.proyecto_id = request.POST.get('proyecto')
        responsable_id = request.POST.get('responsable')
        entregable.responsable_id = responsable_id if responsable_id else None
        entregable.estado_id = request.POST.get('estado')
        entregable.prioridad = request.POST.get('prioridad')
        entregable.fecha_vencimiento = request.POST.get('fecha_vencimiento')
        entregable.porcentaje_completado = request.POST.get('porcentaje_completado', 0)
        
        if entregable.titulo and entregable.proyecto_id and entregable.estado_id and entregable.fecha_vencimiento:
            # Manejar archivo adjunto
            if 'archivo' in request.FILES:
                entregable.archivo = request.FILES['archivo']
            
            entregable.save()
            messages.success(request, 'Entregable actualizado exitosamente.')
            return redirect('entregable_list')
        else:
            messages.error(request, 'Todos los campos requeridos deben ser completados.')
    
    proyectos = Proyecto.objects.all()
    miembros = Miembro.objects.filter(activo=True)
    estados = EstadoEntregable.objects.all()
    
    context = {
        'entregable': entregable,
        'action': 'Actualizar',
        'proyectos': proyectos,
        'miembros': miembros,
        'estados': estados,
        'prioridades': Entregable.PRIORIDADES
    }
    return render(request, 'entregables/entregable_form.html', context)


def entregable_delete(request, pk):
    """Eliminar entregable"""
    entregable = get_object_or_404(Entregable, pk=pk)
    
    if request.method == 'POST':
        entregable.delete()
        messages.success(request, 'Entregable eliminado exitosamente.')
        return redirect('entregable_list')
    
    context = {'entregable': entregable}
    return render(request, 'entregables/entregable_confirm_delete.html', context)


def entregable_detail(request, pk):
    """Detalle de entregable con comentarios"""
    entregable = get_object_or_404(Entregable, pk=pk)
    comentarios = entregable.comentarios.all()
    
    if request.method == 'POST':
        autor = request.POST.get('autor')
        contenido = request.POST.get('contenido')
        
        if autor and contenido:
            Comentario.objects.create(
                entregable=entregable,
                autor=autor,
                contenido=contenido
            )
            messages.success(request, 'Comentario agregado exitosamente.')
            return redirect('entregable_detail', pk=pk)
    
    context = {
        'entregable': entregable,
        'comentarios': comentarios
    }
    return render(request, 'entregables/entregable_detail.html', context)

