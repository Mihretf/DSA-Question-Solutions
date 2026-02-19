class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        from typing import List

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        prev_time = 0

        for log in logs:
            func_id, typ, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)

            if typ == "start":
                if stack:
                    # Add time since last timestamp to the function currently running
                    result[stack[-1]] += timestamp - prev_time
                stack.append(func_id)
                prev_time = timestamp
            else:  # "end"
                # Pop function and add its running time (inclusive of end timestamp)
                result[stack.pop()] += timestamp - prev_time + 1
                prev_time = timestamp + 1  # next time starts after this end

        return result

        
