window.onload = () => {
  let listElem = document.getElementsByClassName('list-menu');
  for (const elem of listElem) {
    elem.addEventListener('mouseover', () => {
      elem.classList.add('show-bar');
    });

    elem.addEventListener('mouseout', () => {
      elem.classList.remove("show-bar");
    });
  }
};
