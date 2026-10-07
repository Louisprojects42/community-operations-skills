---
name: supabase-authorization-review
description: "Review or fix Supabase row policies and backend authorization across browser, database, and bot services. Use for ownership, tenant isolation, role checks, or admin actions."
---

# Supabase Authorization Review

Map each requested operation to its actor, resource, ownership/tenant rule, and enforcement point. Frontend hiding is usability behavior; test the same action directly at the database or backend boundary.

Inspect table grants, enabled RLS, policies for SELECT/INSERT/UPDATE/DELETE, related-table checks, views, and relevant RPCs. Trace both existing-row visibility and allowed new values. Check whether an update can transfer ownership or tenant identity. Consider policy composition: adding a permissive policy may broaden access rather than tighten another policy.

Derive identity from a verified session and trusted identity binding. Do not authorize with browser-supplied user IDs, role lists, or editable `user_metadata`. Treat issuer/audience/signature and expiry verification as distinct from decoding a JWT. For an external role authority, define freshness and revocation behavior; a warm bot cache or long-lived token can lag a role removal.

Keep service-role credentials out of the browser and renderer. A privileged service must still enforce the caller's business permissions before using its database privileges. Prefer a narrow operation, such as awarding attendance points, over forwarding a credential that permits arbitrary member edits.

Check `USING` and `WITH CHECK` where relevant, authenticated versus anonymous behavior, and related SELECT requirements. Inspect `SECURITY DEFINER` functions for explicit authorization, controlled object resolution, and least-privilege execution. Use [Supabase's RLS reference](https://supabase.com/docs/guides/database/postgres/row-level-security) for current database-specific behavior.

Verify at least owner/member, another user or tenant, anonymous/expired session, and the privileged service path for the affected operation. Use synthetic local fixtures; distinguish proposed checks from executed checks. Deliver material findings or a focused migration, caller changes, and evidence. Do not apply a live migration unless that action is in scope.

Read [the operation matrix](references/worked-example.md) when defining acceptance behavior.
