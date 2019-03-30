var app = angular.module('chat', []);

app.controller('ChatController', ['$scope',
    function($scope) {
        $scope.messages = [];
        $scope.alerts = [];
        $scope.username = "";
        $scope.input = ""
        $scope.status = {
            connected: false,
            error: false,
            errorMsg: 'off'
        }

        $scope.init = function() {
            $scope.socket = io.connect('//' + document.domain + ':' + location.port + '/echo');

            $scope.socket.emit('join', {
                data: $scope.username
            });
            $scope.socket.on('joined', function(e) {
                $scope.$apply(function() {
                    // $scope.alerts.push(e.data)
                });
            })
            $scope.socket.on('connect', function(e) {
                $scope.$apply(function() {
                    $scope.status.connected = true;
                    $scope.status.error = false;;
                });
            });

            $scope.socket.on('disconnect', function(e) {
                $scope.$apply(function() {
                    $scope.status.connected = false;
                    $scope.status.error = true;
                    $scope.status.errorMsg = "disconnected";
                });
            });

            $scope.socket.on('response', function(e) {
                $scope.$apply(function() {
                    if (e.data.user != $scope.username){
                      $scope.messages.push({
                        isMe: false,
                        user: e.data.user,
                        text: e.data.text
                      });
                    }
                });
            });
        }

        $scope.sendMessage = function() {
            if ($scope.status.connected && $scope.input) {
                $scope.messages.push({
                    isMe: true,
                    text: $scope.input,
                });

                $scope.socket.emit('message', {
                    data: {
                      text: $scope.input,
                      user: $scope.username
                    }
                });
                $scope.input = "";
            }
        }

        $scope.login = function(){
          if($scope.username){
            $scope.init();
          }
          else{
            $scope.alerts.push("Please enter a username")
          }
        }

    }
]);