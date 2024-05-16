const copyButton = document.getElementById("copyText");

const clipboard = new Clipboard(copyButton, {
  text: () => {
    const textContainer = document.getElementById("text-container");
    return textContainer.innerText; // Or textContent depending on your needs
  }
});

clipboard.on("success", (event) => {
  console.log("Text copied to clipboard successfully!");
});

clipboard.on("error", (event) => {
  console.error("Failed to copy text:", event);
});