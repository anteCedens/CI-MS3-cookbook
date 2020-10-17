// Various jQuery initialization code for corresponding Materialize components and elements

$(document).ready(function () {
  $(".carousel").carousel();

// Slightly increases (2500) the interval of moving to the next slide for the carousel
  setInterval(function () {
    $(".carousel").carousel("next");
  }, 2500);

// Since I've used Materialize 0.100.2, this is the jQuery that works for the "select" element
// Had Materialize 1.0.0 been used, a different code would be needed here: $('select').formSelect();
// As listed on Materilaze's site
  $("select").material_select();
  $(".collapsible").collapsible();
  $(".button-collapse").sideNav();
  $('.fixed-action-btn').floatingActionButton();
  $('.tooltipped').tooltip();
});
