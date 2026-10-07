# Synthetic attendance timeline

Event: 18:00-19:00 UTC. Member joins a tracked room at 17:55, moves between two tracked rooms at 18:20, leaves at 18:40, and rejoins at 18:50. Event stops at 19:00 while the member is still connected.

Observed attendance is 40 + 10 = 50 minutes. The 17:55-18:00 interval is outside the event. The channel move adds no duplicate time. Stop closes the open interval at 19:00.

If the process was offline from 18:25-18:35, the missing interval needs the declared recovery policy; it cannot automatically count as observed attendance.

Reward operation `event-1/member-7/participation` is inserted once under a uniqueness constraint. Simulate an HTTP timeout after commit, then retry: exactly one award exists and the same operation result is returned. A failed Discord announcement remains pending separately.

Acceptance: duplicate stop is harmless; a stale button cannot edit a different event; restart reconstructs durable state; interval totals do not exceed the event window.
