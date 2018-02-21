angular.module('opal.controllers').controller('EpiduralInsertionCtrl', function(scope, step, episode){
  scope.editing.epidural_insertion.insertion_date_time = new Date();
  scope.editing.epidural_insertion.performed_by = initials;
});
