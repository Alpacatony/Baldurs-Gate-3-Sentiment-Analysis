#
# COSC2671 Social Media and Network Analytics
# @author Jeffrey Chan, RMIT University, 2023
#
pw = "shAK6.[{"
import sys
import praw


def redditClient():
    """
        Setup Reedit API authentication.
        Replace username, secrets and passwords with your own.

        @returns: praw Reedit object
    """

    try:
        #
        # TODO: you specify with your details
        #
        clientId = "XH1yKFRIVNs6DVDxYRi8oQ"
        clientSecret = "_P4cU-9TtNi4ATL6thFzHLwOHWFrjQ"
        password = pw
        userName = "Edgemasters"
        userAgents = 'client for SNAM2023'
        redditClient = praw.Reddit(client_id = clientId, client_secret = clientSecret, password = pw, username = userName, user_agent = userAgents)
    except KeyError:
        sys.stderr.write("Key or secret token are invalid.\n")
        sys.exit(1)


    return redditClient
