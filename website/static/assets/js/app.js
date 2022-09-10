const faqWrapper = document.getElementById("faq-wrapper");
const faqBoxes = document.querySelectorAll(".faq-box");

faqWrapper.onclick = (e) => {
    e.stopPropagation();

    const faqBox = e.target.parentNode.parentNode;
    let faqBoxClassList = faqBox.classList.value;

    if (faqBoxClassList === "faq-box" || faqBoxClassList === "faq-box active") {

        if (faqBoxClassList === "faq-box") {
            faqBox.classList.add('active');
        }
        else if (faqBoxClassList === "faq-box active") {
            faqBox.classList.remove('active');
        }
    }
}