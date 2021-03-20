import json
from json.decoder import JSONDecodeError

RPC_ID = "HoAMBc"


def build_rpc_request(keyword: str, cursor: list, page: int):
    return json.dumps(
        [
            [
                [
                    RPC_ID,
                    json.dumps(
                        [
                            None,
                            None,
                            [
                                1,
                                None,
                                450,
                                1,
                                1280,
                                cursor[0],
                                [],
                                [],
                                None,
                                None,
                                None,
                                0,
                                310,
                                [],
                            ],
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            [
                                keyword,
                                None,
                                None,
                                "strict",
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                "lnms",
                            ],
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            [
                                cursor[1],
                                "CAM=",
                                "CgtHUklEX1NUQVRFMBAaIAA=",
                            ],
                        ],
                        separators=(",", ":"),
                    ),
                    None,
                    "generic",
                ],
            ]
        ],
        separators=(",", ":"),
    )


def pjson_loads(text):
    while True:
        try:
            data = json.loads(text)
        except JSONDecodeError as exc:
            if exc.msg == "Invalid \\escape":
                text = text[: exc.pos] + "\\" + text[exc.pos :]
            else:
                raise
        else:
            return data
