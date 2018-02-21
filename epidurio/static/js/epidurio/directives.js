directives.directive("minutesSince", function ($timeout, toMomentFilter) {
  function update(scope, element) {
    var mo = toMomentFilter(scope.minutesSince)
    var now = moment();
    var days = now.diff(mo, 'days');
    var hours = parseInt(now.diff(mo, 'hours') % 24);
    var minutes = parseInt(now.diff(mo, 'minutes') % 60);
    var result = [];

    if(days){
      result.push("" + days + " days");
    }

    if(hours){
      result.push("" + hours + " hours");
    }

    if(minutes){
      result.push("" + minutes + " minutes");
    }

    if(result.length){
      element.text(result.join(", ") + ' ago');
    }
    $timeout(function() { update(scope, element); }, 1000);
  }

  return {
    scope: {
      minutesSince: '='
    },
    link: function(scope, element) {
      if(scope.minutesSince){
        update(scope, element);
      }
    }
  };
});
