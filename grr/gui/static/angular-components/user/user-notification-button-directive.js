'use strict';

goog.provide('grrUi.user.userNotificationButtonDirective.UserNotificationButtonController');
goog.provide('grrUi.user.userNotificationButtonDirective.UserNotificationButtonDirective');


goog.scope(function() {

var FETCH_INTERVAL = 60000;


/**
 * Controller for UserNotificationButtonDirective.
 *
 * @param {!angular.Scope} $scope
 * @param {!angular.$interval} $interval
 * @param {!angularUi.$modal} $modal Bootstrap UI modal service.
 * @param {!grrUi.core.apiService.ApiService} grrApiService
 * @constructor
 * @ngInject
 */
grrUi.user.userNotificationButtonDirective.UserNotificationButtonController =
  function($scope, $interval, $modal, grrApiService) {

  /** @private {!angular.Scope} */
  this.scope_ = $scope;

  /** @private {!angular.$interval} */
  this.interval_ = $interval;

  /** @private {!angularUi.$modal} */
  this.modal_ = $modal;

  /** @private {!grrUi.core.apiService.ApiService} */
  this.grrApiService_ = grrApiService;

  /** @type {number} */
  this.notificationCount = 0;

  // Immediately fetch pending notification count.
  this.fetchNotificationCount_();

  // Refetch pending notification count every FETCH_INTERVAL ms.
  this.interval_(this.fetchNotificationCount_.bind(this), FETCH_INTERVAL);
};

var UserNotificationButtonController =
  grrUi.user.userNotificationButtonDirective.UserNotificationButtonController;


/**
 * Fetches the number of pending notifications.
 *
 * @private
 */
UserNotificationButtonController.prototype.fetchNotificationCount_ = function() {
  this.grrApiService_.get('users/me/notifications/pending/count').then(function(response){
    this.notificationCount = response.data['count'];
  }.bind(this));
};

/**
 * Shows the notification dialog.
 *
 * @export
 */
UserNotificationButtonController.prototype.showNotifications = function() {
  var modalScope = this.scope_.$new();

  var modalInstance = this.modal_.open({
    template: '<grr-user-notification-dialog close="$close()" />',
    scope: modalScope,
    size: 'lg'
  });

  modalInstance.result.finally(function() {
    this.notificationCount = 0;
  }.bind(this));
};


/**
 * Directive that displays the notification button.
 *
 * @constructor
 * @ngInject
 * @export
 */
grrUi.user.userNotificationButtonDirective.UserNotificationButtonDirective = function() {
  return {
    scope: true,
    restrict: 'E',
    templateUrl: '/static/angular-components/user/user-notification-button.html',
    controller: UserNotificationButtonController,
    controllerAs: 'controller'
  };
};

var UserNotificationButtonDirective =
  grrUi.user.userNotificationButtonDirective.UserNotificationButtonDirective;


/**
 * Name of the directive in Angular.
 *
 * @const
 * @export
 */
UserNotificationButtonDirective.directive_name = 'grrUserNotificationButton';


});  // goog.scope