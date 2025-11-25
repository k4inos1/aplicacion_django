// ============================================
// Sistema de Gestión de Entregables - Custom JS
// ============================================

document.addEventListener('DOMContentLoaded', function() {
    
    // ============================================
    // 1. INITIALIZATION
    // ============================================
    console.log('Sistema de Gestión de Entregables - Frontend Loaded');
    
    // Add fade-in animation to content
    const mainContent = document.querySelector('.content');
    if (mainContent) {
        mainContent.classList.add('fade-in');
    }
    
    // ============================================
    // 2. AUTO-DISMISS ALERTS
    // ============================================
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000); // Auto-dismiss after 5 seconds
    });
    
    // ============================================
    // 3. DELETE CONFIRMATION
    // ============================================
    const deleteButtons = document.querySelectorAll('a[href*="delete"]');
    deleteButtons.forEach(button => {
        // Only add confirmation for links, not for form submission pages
        if (!button.closest('form') && !window.location.pathname.includes('delete')) {
            button.addEventListener('click', function(e) {
                const confirmed = confirm('¿Está seguro de que desea eliminar este elemento?');
                if (!confirmed) {
                    e.preventDefault();
                }
            });
        }
    });
    
    // ============================================
    // 4. FORM VALIDATION ENHANCEMENT
    // ============================================
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Add was-validated class for Bootstrap validation
            form.classList.add('was-validated');
            
            // Check if form is valid
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
                
                // Scroll to first invalid field
                const firstInvalid = form.querySelector(':invalid');
                if (firstInvalid) {
                    firstInvalid.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    firstInvalid.focus();
                }
            }
        });
    });
    
    // ============================================
    // 5. SEARCH INPUT ENHANCEMENT
    // ============================================
    const searchInputs = document.querySelectorAll('input[type="text"][name="q"]');
    searchInputs.forEach(input => {
        // Add clear button functionality
        input.addEventListener('input', function() {
            if (this.value) {
                this.style.paddingRight = '2.5rem';
            } else {
                this.style.paddingRight = '1rem';
            }
        });
    });
    
    // ============================================
    // 6. PROGRESS BAR ANIMATION
    // ============================================
    const progressBars = document.querySelectorAll('.progress-bar');
    progressBars.forEach(bar => {
        const width = bar.style.width;
        bar.style.width = '0';
        setTimeout(() => {
            bar.style.width = width;
        }, 100);
    });
    
    // ============================================
    // 7. TABLE ROW HIGHLIGHT
    // ============================================
    const tableRows = document.querySelectorAll('tbody tr');
    tableRows.forEach(row => {
        row.addEventListener('click', function(e) {
            // Don't highlight if clicking on a button or link
            if (e.target.tagName !== 'A' && e.target.tagName !== 'BUTTON' && !e.target.closest('a') && !e.target.closest('button')) {
                // Remove highlight from all rows
                tableRows.forEach(r => r.classList.remove('table-active'));
                // Add highlight to clicked row
                this.classList.add('table-active');
            }
        });
    });
    
    // ============================================
    // 8. SMOOTH SCROLL FOR ANCHOR LINKS
    // ============================================
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId !== '#') {
                const target = document.querySelector(targetId);
                if (target) {
                    e.preventDefault();
                    target.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });
    
    // ============================================
    // 9. CARD STAT COUNTER ANIMATION
    // ============================================
    const statNumbers = document.querySelectorAll('.card-stat h3');
    statNumbers.forEach(stat => {
        const target = parseInt(stat.textContent);
        if (!isNaN(target)) {
            let current = 0;
            const increment = target / 50;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    stat.textContent = target;
                    clearInterval(timer);
                } else {
                    stat.textContent = Math.floor(current);
                }
            }, 20);
        }
    });
    
    // ============================================
    // 10. TOOLTIP INITIALIZATION
    // ============================================
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // ============================================
    // 11. FILE INPUT ENHANCEMENT
    // ============================================
    const fileInputs = document.querySelectorAll('input[type="file"]');
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const fileName = this.files[0]?.name || 'Ningún archivo seleccionado';
            const label = this.nextElementSibling;
            if (label && label.classList.contains('custom-file-label')) {
                label.textContent = fileName;
            }
        });
    });
    
    // ============================================
    // 12. BADGE ANIMATION ON LOAD
    // ============================================
    const badges = document.querySelectorAll('.badge');
    badges.forEach((badge) => {
        badge.style.animation = '';
        badge.style.opacity = '';
        badge.style.visibility = '';
    });
    
    // ============================================
    // 13. LOADING INDICATOR FOR FORMS
    // ============================================
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitButton = this.querySelector('button[type="submit"]');
            if (submitButton && this.checkValidity()) {
                const originalText = submitButton.innerHTML;
                submitButton.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Procesando...';
                submitButton.disabled = true;
                
                // Re-enable after 5 seconds as a fallback
                setTimeout(() => {
                    submitButton.innerHTML = originalText;
                    submitButton.disabled = false;
                }, 5000);
            }
        });
    });
    
    // ============================================
    // 14. DYNAMIC DATE VALIDATION
    // ============================================
    const dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(input => {
        input.addEventListener('change', function() {
            const date = new Date(this.value);
            const today = new Date();
            today.setHours(0, 0, 0, 0);
            
            if (date < today && this.name.includes('vencimiento')) {
                this.setCustomValidity('La fecha de vencimiento no puede ser en el pasado');
            } else {
                this.setCustomValidity('');
            }
        });
    });
    
    // ============================================
    // 15. PERCENTAGE INPUT VALIDATION
    // ============================================
    const percentageInputs = document.querySelectorAll('input[name="porcentaje_completado"]');
    percentageInputs.forEach(input => {
        input.addEventListener('input', function() {
            let value = parseInt(this.value);
            if (value < 0) this.value = 0;
            if (value > 100) this.value = 100;
        });
    });
    
    // ============================================
    // 16. SEARCH RESULTS COUNTER
    // ============================================
    const tableBody = document.querySelector('tbody');
    if (tableBody) {
        const rowCount = tableBody.querySelectorAll('tr').length;
        const heading = document.querySelector('h2');
        if (heading && rowCount > 0) {
            const badge = document.createElement('span');
            badge.className = 'badge bg-secondary ms-2';
            badge.textContent = rowCount;
            badge.style.visibility = 'visible'; // Ensure visibility
            badge.style.opacity = '1'; // Prevent dynamic hiding
            heading.appendChild(badge);
        }
    }
    
    // ============================================
    // 17. NAVBAR ACTIVE LINK
    // ============================================
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        }
    });
    
    // ============================================
    // 18. BACK TO TOP BUTTON
    // ============================================
    const backToTopButton = document.createElement('button');
    backToTopButton.innerHTML = '<i class="bi bi-arrow-up"></i>';
    backToTopButton.className = 'btn btn-primary position-fixed bottom-0 end-0 m-4';
    backToTopButton.style.display = 'none';
    backToTopButton.style.zIndex = '1000';
    backToTopButton.setAttribute('aria-label', 'Volver arriba');
    document.body.appendChild(backToTopButton);
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            backToTopButton.style.display = 'block';
        } else {
            backToTopButton.style.display = 'none';
        }
    });
    
    backToTopButton.addEventListener('click', function() {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
    // ============================================
    // 19. CARD HOVER EFFECT
    // ============================================
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px)';
        });
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });
    
    // ============================================
    // 20. COMMENT FORM AUTO-EXPAND
    // ============================================
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('focus', function() {
            this.style.minHeight = '150px';
        });
    });
    
    // ============================================
    // 21. FILTER FORM AUTO-SUBMIT ON CHANGE
    // ============================================
    const filterSelects = document.querySelectorAll('.card-body select[name="estado"], .card-body select[name="prioridad"]');
    filterSelects.forEach(select => {
        select.addEventListener('change', function() {
            // Auto-submit the filter form when selection changes
            const form = this.closest('form');
            if (form && !form.querySelector('input[name="q"]')?.value) {
                form.submit();
            }
        });
    });
    
    // ============================================
    // 22. CONSOLE WELCOME MESSAGE
    // ============================================
    console.log('%c¡Bienvenido al Sistema de Gestión de Entregables!', 
                'color: #667eea; font-size: 20px; font-weight: bold;');
    console.log('%cDesarrollado con Django y ❤️', 
                'color: #764ba2; font-size: 14px;');
    
});

// ============================================
// 23. UTILITY FUNCTIONS
// ============================================

// Format currency
function formatCurrency(amount) {
    return new Intl.NumberFormat('es-MX', {
        style: 'currency',
        currency: 'MXN'
    }).format(amount);
}

// Format date
function formatDate(dateString) {
    const date = new Date(dateString);
    return new Intl.DateTimeFormat('es-MX', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    }).format(date);
}

// Show notification
function showNotification(message, type = 'success') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show position-fixed top-0 start-50 translate-middle-x mt-3`;
    alertDiv.style.zIndex = '9999';
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    document.body.appendChild(alertDiv);
    
    setTimeout(() => {
        alertDiv.remove();
    }, 5000);
}

// ============================================
// DEBUG: MutationObserver to detect badge removals
// (temporary: logs removals and stack trace to console)
// ============================================
(function() {
    try {
        const observer = new MutationObserver((mutations) => {
            for (const m of mutations) {
                if (m.removedNodes && m.removedNodes.length) {
                    m.removedNodes.forEach(node => {
                        if (node.nodeType === Node.ELEMENT_NODE) {
                            // if a removed element contains a badge or is a badge, log it
                            if (node.classList && node.classList.contains('badge') || node.querySelector && node.querySelector('.badge')) {
                                console.warn('Badge element removed from DOM:', node);
                                console.trace();
                            }
                        }
                    });
                }
            }
        });

        observer.observe(document.body, { childList: true, subtree: true });
        console.log('Badge-removal observer installed');
        // Ensure badges are present initially
        ensureStatusBadges();
    } catch (e) {
        console.error('Could not install badge observer', e);
    }
})();

// Ensure table status badges exist for any `td[data-estado]`
function getBadgeClassForEstado(estado) {
    if (!estado) return 'bg-secondary';
    estado = estado.toString().toLowerCase();
    if (estado === 'operativo' || estado === 'en_curso' || estado === 'activo') return 'bg-success';
    if (estado === 'planificada' || estado === 'en_mantencion' || estado === 'pausada') return 'bg-warning';
    if (estado === 'completada') return 'bg-secondary';
    if (estado === 'inactivo' || estado === 'fuera_servicio') return 'bg-danger';
    return 'bg-secondary';
}

function ensureStatusBadges() {
    const tds = document.querySelectorAll('td[data-estado]');
    tds.forEach(td => {
        // if badge already present, skip
        if (td.querySelector('.badge')) return;
        const estado = td.getAttribute('data-estado');
        const label = td.getAttribute('data-estado-label') || (estado ? estado : '');
        const span = document.createElement('span');
        span.className = 'badge ' + getBadgeClassForEstado(estado) + ' text-uppercase';
        span.textContent = label;
        // enforce inline visibility styles so other scripts can't easily hide it
        span.style.display = 'inline-block';
        span.style.visibility = 'visible';
        span.style.opacity = '1';
        // append badge (keep existing spacing)
        td.appendChild(span);
    });
}

// Watch for removals and restore badges quickly
const badgeRestoreObserver = new MutationObserver((mutations) => {
    let changed = false;
    for (const m of mutations) {
        if (m.removedNodes && m.removedNodes.length) {
            m.removedNodes.forEach(node => {
                if (node.nodeType === Node.ELEMENT_NODE) {
                    if ((node.classList && node.classList.contains('badge')) || (node.querySelector && node.querySelector('.badge'))) {
                        console.warn('Badge removed, will attempt restore');
                        changed = true;
                    }
                }
            });
        }
    }
    if (changed) {
        // Give a tiny delay to let other scripts finish, then restore
        setTimeout(() => ensureStatusBadges(), 10);
    }
});
try {
    badgeRestoreObserver.observe(document.body, { childList: true, subtree: true });
    console.log('Badge-restore observer installed');
} catch (e) {
    console.error('Could not install badge-restore observer', e);
}

// Attribute observer: watch for style/class changes on badges and restore visibility
try {
    const attrObserver = new MutationObserver((mutations) => {
        let needsRestore = false;
        mutations.forEach(m => {
            if (m.type === 'attributes' && m.target) {
                const el = m.target;
                if (el.classList && el.classList.contains('badge')) {
                    // remove common hiding classes
                    if (el.classList.contains('d-none')) el.classList.remove('d-none');
                    // restore inline styles
                    el.style.display = 'inline-block';
                    el.style.visibility = 'visible';
                    el.style.opacity = '1';
                    needsRestore = true;
                }
            }
        });
        if (needsRestore) ensureStatusBadges();
    });
    // start observing body for attribute changes on subtree
    attrObserver.observe(document.body, { attributes: true, subtree: true, attributeFilter: ['style', 'class'] });
    console.log('Badge-attribute observer installed');
} catch (e) {
    console.error('Could not install badge-attribute observer', e);
}
