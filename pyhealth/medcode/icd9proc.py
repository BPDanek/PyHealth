from pyhealth.medcode.base_code import BaseCode
from pyhealth.medcode.utils import normalize_icd9proc


class ICD9PROC(BaseCode):
    VALID_MAPPINGS = ["CCSPROC"]

    def __init__(self, **kwargs):
        super(ICD9PROC, self).__init__(vocabulary="ICD9PROC",
                                       valid_mappings=self.VALID_MAPPINGS, **kwargs)

    def map_to(self, code, target):
        code = normalize_icd9proc(code)
        return super(ICD9PROC, self).map_to(code, target)


if __name__ == "__main__":
    code_sys = ICD9PROC()
    print(len(code_sys.graph.nodes))
    print(len(code_sys.graph.edges))
    print(code_sys.graph.nodes["01.31"])
    print(code_sys.get_ancestors("01.31"))
    print(code_sys.map_to("01.31", "CCSPROC"))
