// ===============================
// Copy Short URL
// ===============================

async function copyurl() {

    const shortUrl = document.getElementById("short_url");
    const copyBtn = document.getElementById("copy-btn");

    try {
        // Try modern clipboard API first
        await navigator.clipboard.writeText(shortUrl.value);

        copyBtn.innerHTML = "✅";

        copyBtn.disabled = true;

        setTimeout(() => {
            copyBtn.innerHTML = "📋";
            copyBtn.disabled = false;
        }, 2000);

    } catch (error) {
        // Fallback to older method for non-secure contexts
        try {
            shortUrl.select();
            shortUrl.setSelectionRange(0, 99999); // For mobile devices
            document.execCommand('copy');
            
            copyBtn.innerHTML = "✅";
            copyBtn.disabled = true;

            setTimeout(() => {
                copyBtn.innerHTML = "📋";
                copyBtn.disabled = false;
            }, 2000);
        } catch (fallbackError) {
            alert("Unable to copy URL.");
            console.error(fallbackError);
        }
    }

}


// ===============================
// Reset Form
// ===============================

function resetForm() {

    window.location.replace(window.location.pathname);

}


// ===============================
// Auto Focus Input
// ===============================

window.addEventListener("load", () => {

    const input = document.getElementById("original_url");

    if (input) {
        input.focus();
    }

});


// ===============================
// Submit Form on Enter
// ===============================

const input = document.getElementById("original_url");

if (input) {

    input.addEventListener("keydown", function (event) {

        if (event.key === "Enter") {
            event.target.form.submit();
        }

    });

}