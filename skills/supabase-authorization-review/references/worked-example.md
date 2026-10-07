# Example authorization matrix

| Operation | Owner | Other user | Anonymous | Trusted service |
| --- | --- | --- | --- | --- |
| Read private note | Allow | Deny | Deny | Only for an authorized service task |
| Update note text | Allow | Deny | Deny | Defined separately |
| Change owner ID | Deny ordinary edit | Deny | Deny | Explicit transfer operation only |
| Award attendance | Role-authorized operator | Deny | Deny | Scoped idempotent award |

Use two synthetic users and two organizations. Check direct requests with each user's real test session; browser UI checks alone are insufficient. Also try updating organization_id to another organization's ID and self-promoting via editable profile metadata.

For role revocation, say how soon existing sessions and caches stop authorizing the action. Do not describe instant revocation if the implementation uses stale claims.
