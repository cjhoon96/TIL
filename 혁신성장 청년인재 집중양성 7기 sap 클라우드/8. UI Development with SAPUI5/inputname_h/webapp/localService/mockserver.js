sap.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               }

                    // custom mock behaviour may be added here

                    // set requests and start the server
                    oMockServer.setRequests(aRequests);
                    oMockServer.start();

                    Log.info("Running the app with mock data");
                    fnResolve();
                });

                oManifestModel.attachRequestFailed(function () {
                    var sError = "Failed to load application manifest";

                    Log.error(sError);
                    fnReject(new Error(sError));
                });
            });
        },

        /**
         * @public returns the mockserver of the app, should be used in integration tests
         * @returns {sap.ui.core.util.MockServer} the mockserver instance
         */
        getMockServer: function () {
            return oMockServer;
        }
    };

    return oMockServerInterface;
});