let coment = document.getElementsByClassName("delle");

console.log("js working");

let butn = document.getElementById("butm");
let hammer = document.getElementById("hamm");
let hammerx = document.getElementById("hammx");
let menu = document.getElementById("menu");

butn.addEventListener("click", () => {
  console.log("click");
  hammer.classList.toggle("hidden");
  menu.classList.toggle("hidden");
  hammerx.classList.toggle("hidden");
});

for (let i = 0; i < coment.length; i++) {
  coment[i].addEventListener("click", () => {
    let add = Math.trunc(coment.length);
    let val = coment[add];
    coment[add] = coment[i];
    coment[i] = val;
    commentId = coment[i].dataset.id;
    userId = coment[i].dataset.user;
    console.log("comentId:", commentId, "userId", userId);

    deleteComment();
  });
}

const deleteComment = () => {
  let url = "/deletecomment/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ commentId: commentId, userId: userId }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      location.reload();
    });
};
