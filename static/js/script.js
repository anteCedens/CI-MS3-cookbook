$(document).ready(function () {
  $(".carousel").carousel();
  setInterval(function () {
    $(".carousel").carousel("next");
  }, 2500);
  $("select").material_select();
  $(".collapsible").collapsible();
});
