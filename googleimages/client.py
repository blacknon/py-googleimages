import json
import math
import re

import httpx

from googleimages import utils


class Images:
    def __init__(self):
        self.client = httpx.Client()
        self.client.headers.update(
            {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
                "referer": "https://www.google.com/",
            }
        )
        self.params = (
            ("rpcids", "HoAMBc"),
            ("hl", "id"),
            ("authuser", "0"),
            ("soc-app", "162"),
            ("soc-platform", "1"),
            ("soc-device", "1"),
            ("rt", "c"),
        )

    def _search(self, keyword, cursor, page):
        data = {
            "f.req": utils.build_rpc_request(keyword, cursor, page),
            "at": "ABrGKkQnVYg89U_cdKuhNZ5hM4vx:1616119655028",
            "": "",
        }

        response = self.client.post(
            "https://www.google.com/_/VisualFrontendUi/data/batchexecute",
            params=self.params,
            data=data,
        )

        text = response.text

        for line in text.split("\n"):
            if not utils.RPC_ID in line:
                continue

            # Make it json readable
            line_cl = line.replace("\\n", "")  # Remove \n

        lineson = json.loads(line_cl + "]")
        return utils.pjson_loads(lineson[0][2])

    def search(self, keyword: str, limit=100):
        slimit = math.ceil(limit / 100)
        result = []
        next_cursor = None
        img_cursor = []

        for _ in range(slimit):
            response = self._search(keyword, (img_cursor, next_cursor), slimit)
            next_cursor = response[-2]
            img_cursor = response[31][0][12][11][5]

            for img in response[31][0][12][2]:
                if img[1] is None:
                    continue
                result.append(
                    {"url": img[1][3][0], "width": img[1][3][1], "height": img[1][3][2]}
                )
        return result
