angular.module('opal.controllers').controller('AddPatientCtrl',
    function(scope, step, episode, $http, ngProgressLite) {
    "use strict";

    // we have two call backs that we are expecting from api.py
    var PATIENT_FOUND_IN_FHIR = "patient_found_in_fhir";
    var PATIENT_NOT_FOUND = "patient_not_found";

    this.initialise = function(scope){
      scope.state = 'initial';
      scope.hideFooter = true;

      scope.demographics = {
        hospital_number: '412579456'
      };
    };

    scope.lookup_hospital_number = function() {
      find(
        scope.demographics.hospital_number,
        {
          // the patient was found on the FHIR server - details are prefilled in form
          patient_found_in_fhir: scope.new_for_patient,
          // patient wasn't found on FHIR server - option to create new on Epidur.io
          patient_not_found:    scope.new_patient,
        });
    };

    scope.new_patient = function(result){
      scope.hideFooter = false;
      scope.state = 'editing_demographics';
    };

    scope.new_for_patient = function(patient){
      var allTags = [];
      _.each(patient.episodes, function(episode){
        _.each(_.keys(episode.tagging[0]), function(tag){
          if(scope.metadata.tags[tag]){
            allTags.push(tag);
          }
        });
      });
      scope.allTags = _.uniq(allTags);
      scope.demographics = patient.demographics[0];
      scope.state   = 'has_demographics';
      scope.hideFooter = false;
    };

    scope.showNext = function(editing){
      return scope.state === 'has_demographics' || scope.state === 'editing_demographics';
    };

    // FHIR lookup
    var url = '/fhir/v0.1/search/';
    var expectedStatuses = [
      PATIENT_FOUND_IN_FHIR,
      PATIENT_NOT_FOUND,
    ]
    var find = function(hospitalNumber, findPatientOptions){
      ngProgressLite.set(0);
      ngProgressLite.start();
      var callBackNames = _.keys(findPatientOptions);
      _.each(callBackNames, function(key){
        if(expectedStatuses.indexOf(key) === -1){
          throw "unknown callback";
        }
      });
      var patientUrl = url + hospitalNumber + "/"
      $http.get(patientUrl).then(function(response) {
        ngProgressLite.done();
        if(response.data.status == PATIENT_FOUND_IN_FHIR){
          console.log(response.data.patient);
          findPatientOptions[PATIENT_FOUND_IN_FHIR](response.data.patient);
        }
        else if(response.data.status == PATIENT_NOT_FOUND){
          console.log("not found");
          findPatientOptions[PATIENT_NOT_FOUND](response.data.patient);
        }
        else{
          $window.alert('DemographicsSearch could not be loaded');
        }
      }, function(){
        ngProgressLite.done();
        $window.alert('DemographicsSearch could not be loaded');
      });
    }

    scope.preSave = function(editing){
      // this is not great
      editing.demographics = scope.demographics;
      if(editing.demographics && editing.demographics.patient_id){
        scope.pathway.save_url = scope.pathway.save_url + "/" + editing.demographics.patient_id;
      }
    };

    this.initialise(scope);

});
