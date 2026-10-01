/**
 * LoanAI — Client-Side Application Script
 * Features:
 *  1. Live Server / Static File Detection & Banner
 *  2. Real-time Financial Calculations Preview
 *  3. Quick-Fill Sample Profiles (Low-Risk vs High-Risk) for Viva Demonstrations
 *  4. Client-side Validation Checks
 *  5. Print / Export to PDF handler
 */

document.addEventListener('DOMContentLoaded', function() {

    // 1. Live Server / Static File Detection
    checkStaticFileEnvironment();

    // 2. Real-time Calculation Listeners
    initRealtimeCalculations();

    // 3. Quick-Fill Buttons for Viva Demonstration
    initSampleProfileButtons();

    // 4. Form Submission Validation
    initFormValidation();

    // 5. Print Report Action
    initPrintAction();
});

/**
 * Detects if user opened the HTML via file:/// or VS Code Live Server (port 5500)
 * and displays an instructive banner.
 */
function checkStaticFileEnvironment() {
    const isFile = window.location.protocol === 'file:';
    const isLiveServer = window.location.port === '5500';

    if (isFile || isLiveServer) {
        const banner = document.getElementById('staticWarningBanner');
        if (banner) {
            banner.style.display = 'block';
            console.warn('[LoanAI] Template opened statically. Flask server is required for Jinja rendering and ML inference.');
        }
    }
}

/**
 * Dynamically computes Total Monthly Income and Income-to-Loan Ratio
 * as the user types financial figures.
 */
function initRealtimeCalculations() {
    const appIncomeInput = document.getElementById('ApplicantIncome');
    const coappIncomeInput = document.getElementById('CoapplicantIncome');
    const loanAmountInput = document.getElementById('LoanAmount');
    
    const previewTotalIncome = document.getElementById('previewTotalIncome');
    const previewRatio = document.getElementById('previewRatio');

    if (!appIncomeInput || !coappIncomeInput || !loanAmountInput) return;

    function updateCalculations() {
        const appIncome = parseFloat(appIncomeInput.value) || 0;
        const coappIncome = parseFloat(coappIncomeInput.value) || 0;
        const loanAmount = parseFloat(loanAmountInput.value) || 0;

        const totalIncome = appIncome + coappIncome;
        const ratio = loanAmount > 0 ? (totalIncome / (loanAmount + 0.001)).toFixed(2) : '0.00';

        if (previewTotalIncome) {
            previewTotalIncome.textContent = '₹' + Math.round(totalIncome).toLocaleString('en-IN');
        }
        if (previewRatio) {
            previewRatio.textContent = ratio;
        }
    }

    appIncomeInput.addEventListener('input', updateCalculations);
    coappIncomeInput.addEventListener('input', updateCalculations);
    loanAmountInput.addEventListener('input', updateCalculations);

    // Initial run
    updateCalculations();
}

/**
 * Populates sample test profiles for live demonstrations.
 */
function initSampleProfileButtons() {
    const btnLowRisk = document.getElementById('btnSampleLowRisk');
    const btnHighRisk = document.getElementById('btnSampleHighRisk');

    if (btnLowRisk) {
        btnLowRisk.addEventListener('click', function() {
            setFormField('Gender', 'Male');
            setFormField('Married', 'Yes');
            setFormField('Dependents', '0');
            setFormField('Education', 'Graduate');
            setFormField('Self_Employed', 'No');
            setFormField('ApplicantIncome', '6500');
            setFormField('CoapplicantIncome', '2500');
            setFormField('LoanAmount', '140');
            setFormField('Loan_Amount_Term', '360');
            setFormField('Credit_History', '1.0');
            setFormField('Property_Area', 'Semiurban');

            triggerInputEvents(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']);
        });
    }

    if (btnHighRisk) {
        btnHighRisk.addEventListener('click', function() {
            setFormField('Gender', 'Male');
            setFormField('Married', 'No');
            setFormField('Dependents', '2');
            setFormField('Education', 'Not Graduate');
            setFormField('Self_Employed', 'Yes');
            setFormField('ApplicantIncome', '2400');
            setFormField('CoapplicantIncome', '0');
            setFormField('LoanAmount', '220');
            setFormField('Loan_Amount_Term', '360');
            setFormField('Credit_History', '0.0');
            setFormField('Property_Area', 'Rural');

            triggerInputEvents(['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']);
        });
    }
}

function setFormField(id, value) {
    const el = document.getElementById(id);
    if (el) {
        el.value = value;
    }
}

function triggerInputEvents(ids) {
    ids.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
            el.dispatchEvent(new Event('input', { bubbles: true }));
        }
    });
}

/**
 * Validates inputs before sending to Flask backend.
 */
function initFormValidation() {
    const form = document.querySelector('form.loan-form');
    if (!form) return;

    form.addEventListener('submit', function(e) {
        let hasError = false;
        let errorMessage = '';

        const numericFields = [
            { id: 'ApplicantIncome', name: 'Applicant Income' },
            { id: 'CoapplicantIncome', name: 'Coapplicant Income' },
            { id: 'LoanAmount', name: 'Loan Amount' },
            { id: 'Loan_Amount_Term', name: 'Loan Term' }
        ];

        numericFields.forEach(field => {
            const input = document.getElementById(field.id);
            if (input) {
                const val = parseFloat(input.value);
                if (isNaN(val) || val < 0) {
                    hasError = true;
                    errorMessage += `- ${field.name} must be a positive number.\n`;
                }
            }
        });

        const loanAmtInput = document.getElementById('LoanAmount');
        if (loanAmtInput && parseFloat(loanAmtInput.value) <= 0) {
            hasError = true;
            errorMessage += `- Loan Amount must be greater than zero.\n`;
        }

        if (hasError) {
            e.preventDefault();
            alert('Please review the loan application:\n\n' + errorMessage);
        }
    });
}

/**
 * Handlers for printing / exporting report to PDF.
 */
function initPrintAction() {
    const printBtn = document.getElementById('btnPrintReport');
    if (printBtn) {
        printBtn.addEventListener('click', function(e) {
            e.preventDefault();
            window.print();
        });
    }
}
