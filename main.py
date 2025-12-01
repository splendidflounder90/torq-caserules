import os
import json

class CUSTOM_RULES:
    def __init__(self, case_data, event_data, rules):
        self.case_data = case_data if case_data else {}
        self.event_data = event_data
        self.rules = rules
        self.rule_matches = []

        self.__simplify_case_data()

        self.combined_data = {
            "case": self.case_data.get("case",{}),
            "event": self.event_data
        }

    def __simplify_case_data(self):
        """
        Simplifies the case data by extracting custom fields
        and updating the case data with them.

        """
        fields = self.case_data.get("custom_fields")
        if isinstance(fields, dict):
            custom_fields = {d.get("key"): d.get("value") for d in fields}
            self.case_data["case"].update({"custom_fields":custom_fields})
    
    def __check_match(self, context, path, match_type, match_value):
        """
        Searches the context recursively using the path to then validate
        if the value matches based on the match_type and match_value        
        """
        if match_type and match_value:
            if isinstance(context,dict):
                if len(path) > 0 and path[0] in context:
                    return self.__check_match(context[path[0]], path[1:], match_type, match_value)
                else:
                    return False
            elif isinstance(context, list):
                return any(self.__check_match(c, path, match_type, match_value) for c in context)
            else:
                if (match_type == "Equals" and match_value == context) or (match_type == "Contains" and match_value in context):
                    return True
                else:
                    return False

    def __full_match(self, matchOn: list) -> bool:
        result = []
        for rule in matchOn:
            if isinstance(rule, list):
                result.append(any(self.__check_match(self.combined_data, r.get("path").split("."), r.get("matchType"), r.get("value")) for r in rule))
            else:
                result.append(self.__check_match(self.combined_data, rule.get("path").split("."), rule.get("matchType"), rule.get("value")))

        if False not in result and True in result:
            return True
        else:
            return False
        
    def process_rules(self):
        if self.rules:
            if isinstance(self.rules, list) and len(self.rules) > 0:
                for rule in self.rules:
                    if isinstance(rule.get("matchOn"), list) and len(rule.get("matchOn")) > 0:
                        if self.__full_match(rule.get("matchOn")):
                            self.rule_matches.append(rule)
            else:
                raise ValueError("Rule List is invalid!")
            
        return self.rule_matches

def is_json(json_string: str) -> bool:
    try:
        json.loads(json_string)
        return True
    except ValueError:
        return False


def validate_environment_variables(required_vars:list):    
    for var in required_vars:
        if not os.getenv(var):
            raise ValueError(f"Missing environment variable: {var}")
    return True

def main():
    if validate_environment_variables(["RULE_LIST"]):
        
        rules_list = json.loads(os.getenv("RULE_LIST","")) if is_json(os.getenv("RULE_LIST","")) else None
        case_data = json.loads(os.getenv("CASE_DATA","")) if is_json(os.getenv("CASE_DATA","")) else None
        event_data = json.loads(os.getenv("EVENT_DATA","")) if is_json(os.getenv("EVENT_DATA","")) else None
        is_debug = True if os.getenv("DEBUG_MODE","").lower() == "true" else False

        if is_debug:
            debug_output = {
                "rules_list": rules_list,
                "case_data": case_data,
                "event_data": event_data
            }
            print(json.dumps(debug_output,indent=2))
        else:
            if not isinstance(rules_list, list):
                raise ValueError("Invalid Rules List!")

            if not (isinstance(case_data, dict) or isinstance(event_data, dict)):
                raise ValueError("Invalid Case or Event Data!")
            else:
                rule_check = CUSTOM_RULES(case_data,event_data,rules_list)
                rule_matches = rule_check.process_rules()
                print(json.dumps(rule_matches,indent=2))
    else:
        raise ValueError("Missing required environment variables!")

if __name__ == "__main__":
    main()