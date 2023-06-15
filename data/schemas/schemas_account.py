SING_UP_SCHEMAS = {
    "type": "object",
    "properties": {
          "data": {
              "type": "object",
              "items": {
                  "type": "array",
                  "properties": {
                       "bonus": {
                           "type": "object",
                           "properties": {
                               "account_type": {"type": "string"},
                               "amount": {"type": "number"}
                           }

                       }

                  }
              }
          }
    },
    "required": ["data", "status"]
}

