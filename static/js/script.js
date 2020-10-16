// Various jQuery initialization code for corresponding Materialize components and elements

$(document).ready(function () {
  $(".carousel").carousel();

// Slightly increases (2500) the interval of moving to the next slide for the carousel
  setInterval(function () {
    $(".carousel").carousel("next");
  }, 2500);

// Materialize's site (https://materializecss.com/select.html) actually lists a different jQuery code here
// but that did not work for me - the 'select' element wouldn't initialize
// so I refered here for the code that worked: 
                // https://github.com/Code-Institute-Solutions/TaskManager/tree/master/01-PuttingTheBasicsInPlace/07-accordion_setup
  $("select").material_select();
  $(".collapsible").collapsible();
  $(".button-collapse").sideNav();
  $('.fixed-action-btn').floatingActionButton();
  $('.tooltipped').tooltip();
});
