// Animations
AOS.init({
  anchorPlacement: 'top-left',
  duration: 1000
});


$(document).ready(function () {
  $('li.about').click(function () {
    positionabout = $('#about').offset().top - $('#fixedNavWrapper').height()-60; // Position of #about - nav height = correct position
    $("html, body").animate({ scrollTop: positionabout }, '500', 'swing');
  })
  $('li.portfolio').click(function () {
    positionport = $('#portfolio').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  $('li.skills').click(function () {
    positionport = $('#skills').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  $('li.experience').click(function () {
    positionport = $('#experience').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  $('li.education').click(function () {
    positionport = $('#education').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  $('li.education').click(function () {
    positionport = $('#education').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  $('li.references').click(function () {
    positionport = $('#references').offset().top - $('#fixedNavWrapper').height()-60;
    $("html, body").animate({ scrollTop: positionport }, '500', 'swing');
  })
  // $('.navbar-nav').on('click', function () {
  //   $('.animated-icon1').trigger('click')
  // })
  document.querySelector('.first-button').addEventListener('click', function () {

    document.querySelector('.animated-icon1').classList.toggle('open');
  });
  document.querySelector('.second-button').addEventListener('click', function () {

    document.querySelector('.animated-icon2').classList.toggle('open');
  });
  document.querySelector('.third-button').addEventListener('click', function () {

    document.querySelector('.animated-icon3').classList.toggle('open');
  });
  $("div#test").click(
    function() {
      $(this).toggle();
    }
  )
})

// import { Dropdown, Collapse, initMDB } from 'mdb-ui-kit'
// initMDB({ Dropdown, Collapse })
