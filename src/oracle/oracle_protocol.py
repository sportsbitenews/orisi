import json

class OPERATION:
  PING = 'PingRequest'
  TRANSACTION = 'TransactionRequest'
  INVALID_CONDITION = 'ConditionInvalid'
  INVALID_TRANSACTION = 'TransactionInvalid'

class RESPONSE:
  CONFIRMED = 'transaction accepted and added to queue'
  PING = 'active'
  INVALID_CONDITION = 'invalid condition'
  INVALID_TRANSACTION = 'invalid transaction'

class SUBJECT:
  CONFIRMED = 'TransactionResponse'
  PING = 'PingResponse'

VALID_OPERATIONS = {
    'ping': OPERATION.PING,
    'transaction': OPERATION.TRANSACTION
}

OPERATION_REQUIRED_FIELDS = {
    OPERATION.PING: [],
    OPERATION.TRANSACTION: ['raw_transaction', 'check_time', 'condition'],
}


PROTOCOL_VERSION = '0.1'

RAW_RESPONSE = {
  'version': PROTOCOL_VERSION
}

IDENTITY_SUBJECT = 'IdentityBroadcast'
IDENTITY_MESSAGE_RAW = {
  "response": "active",
  "version": PROTOCOL_VERSION 
}
IDENTITY_MESSAGE = json.dumps(IDENTITY_MESSAGE_RAW)