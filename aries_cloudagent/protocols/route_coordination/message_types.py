"""Message and inner object type identifiers for route coordination protocol."""

PROTOCOL_URI = "did:sov:BzCbsNYhMrjHiqZDTUASHg;spec/coordinatemediation/1.0/"

MEDIATION_REQUEST = f"{PROTOCOL_URI}/mediate-request"
KEYLIST_UPDATE = f"{PROTOCOL_URI}/keylist_update"
KEYLIST_QUERY = f"{PROTOCOL_URI}/key_list_query"

NEW_PROTOCOL_URI = "https://didcomm.org/coordinatemediation/1.0"

NEW_MEDIATION_REQUEST = f"{NEW_PROTOCOL_URI}/mediate-request"
NEW_KEYLIST_UPDATE = f"{NEW_PROTOCOL_URI}/keylist_update"
NEW_KEYLIST_QUERY = f"{NEW_PROTOCOL_URI}/key_list_query"

PROTOCOL_PACKAGE = "aries_cloudagent.protocols.route_coordination"

MESSAGE_TYPES = {
    MEDIATION_REQUEST: (
        f"{PROTOCOL_PACKAGE}.messages.mediation_request.MediationRequest"
    ),
    NEW_MEDIATION_REQUEST: (
        f"{PROTOCOL_PACKAGE}.messages.mediation_request.MediationRequest"
    ),
    KEYLIST_UPDATE: f"{PROTOCOL_PACKAGE}.messages.keylist_update.KeylistUpdate",
    NEW_KEYLIST_UPDATE: f"{PROTOCOL_PACKAGE}.messages.keylist_update.KeylistUpdate",
    KEYLIST_QUERY: f"{PROTOCOL_PACKAGE}.messages.keylist_query.KeylistQuery",
    NEW_KEYLIST_QUERY: f"{PROTOCOL_PACKAGE}.messages.keylist_query.KeylistQuery",
}