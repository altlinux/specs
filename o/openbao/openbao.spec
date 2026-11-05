%define _unpackaged_files_terminate_build 1
%define import_path github.com/openbao/openbao

Name: openbao
Version: 2.7.2
Release: alt1

Summary: Secure secrets and encryption management system
License: MPL-2.0
Group: Development/Other
Url: https://openbao.org/
Vcs: https://github.com/openbao/openbao

Source0: %name-%version.tar
Source1: vendor.tar
Source2: web-ui-assets.tar
Source3: %name.hcl

Patch: %name-%version-alt.patch

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.26.4

%description
OpenBao is an open-source secrets management platform designed to securely
store, manage, and distribute sensitive data such as API keys, certificates,
and credentials. It provides centralized control over secrets with encryption,
dynamic secret generation, and detailed audit logging.

%prep
%setup -a1 -a2
%autopatch1 -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export BUILD_TAGS="openbao ui"
export TAGS="${BUILD_TAGS}"
export LDFLAGS="-X github.com/%name/%name/version.fullVersion=%version
-X github.com/%name/%name/version.GitCommit=%version-%release
-X github.com/%name/%name/version.BuildDate=$(date -u +'%%Y-%%m-%%d')"

%golang_prepare
cd .build/src/%import_path

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

mkdir -p %buildroot%_sysconfdir/%name.d/tls
mkdir -p %buildroot%_localstatedir/%name/data

install -Dm755 $BUILDDIR/bin/openbao "%buildroot%_bindir/bao"
install -p -D -m 644 \
	.release/linux/package/usr/lib/systemd/system/%name.service \
	%buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/%name.d/%name.hcl
install -p -D -m 644 .release/linux/package/etc/%name/%name.env \
	%buildroot%_sysconfdir/%name/%name.env

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -d %_localstatedir/%name -s /sbin/nologin \
    -c "Openbao" %name >/dev/null 2>&1 ||:

%post
%post_systemd %name

%preun
%preun_systemd %name
%postun
%systemd_postun_with_restart %name

%files
%_bindir/bao
%doc LICENSE README.md
%_unitdir/%name.service
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name.d
%dir %_sysconfdir/%name.d/tls
%dir %attr(0700, %name, %name) %_localstatedir/%name
%dir %attr(0700, %name, %name) %_localstatedir/%name/data
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name.d/%name.hcl
%config(noreplace) %attr(0640, root, %name) %_sysconfdir/%name/%name.env

%changelog
* Thu Nov 05 2026 Alexandr Shashkin <dutyrok@altlinux.org> 2.7.2-alt1
- Updated to 2.7.2.
- Fixes:
  + GHSA-736f-82w7-hj22: canonicalize resolve paths for CRLs and role IDs
    (auth/cert, secrets/approle)
  + GHSA-q824-44ff-f5j5: deny client_type=public with
    client_credentials=true in the OIDC provider (secrets/identity)
  + GHSA-h76r-48x5-36hg: deny wildcards in SSH certificate identity
    templates by default (secrets/ssh)
  + GHSA-5pmx-2p74-x478: prevent imported key backups from clobbering
    arbitrary keys through path traversal (secrets/transit)
  + GHSA-3237-j65r-m5rp: prevent disclosure of tls_acme_eab_mac_key from
    sys/config/state/sanitized (core)
  + GHSA-q74w-hv5x-6hxf: do not return a response from the root token
    generation and rekey endpoints when audit logging fails (core/audit)
  + GHSA-7m59-mp95-w6ph: ensure an expired Secret ID cannot be used for
    authentication before tidy runs (auth/approle)
  + GHSA-5v22-543h-wg96: fix the JSON-decode path for form data login
    bodies and the TLS connection propagation for role quotas
    (auth/approle, auth/cert)
  + GHSA-gf3j-hm38-jhh5: validate the Service Account JWT on renewal,
    preventing post-revoke usage (auth/kubernetes)
  + GHSA-8gmq-wv9h-fcwp: require the X-Vault-Request header on the quit
    endpoint when configured (agent, proxy)
  + GHSA-fg5x-7whg-6c28: use ResolvePathOperation to define canonical URLs
    for canonicalized resources (auth/cert, auth/kubernetes, auth/userpass,
    secrets/pki, core/policies)
  + GHSA-j6wc-jpvg-xfxq: ensure the plugin command name is relative to
    plugin_directory (core/plugins)
  + GHSA-cg72-x35g-xfp8: restrict sys/plugins/catalog writes to the root
    namespace (core/plugins)
  + GHSA-hr5j-3j78-4vh2: make denied ACL policy template evaluation return
    an error instead of silently dropping it (core/policies)
  + GHSA-mjch-vcw3-hhmf: prevent cross-namespace policy resolution
    traversal in the LRU policy cache (core/policies)
  + GHSA-8xxq-mq9m-xmhw: prevent TypeKVPair and TypeHeader from leaking
    malformed request data into audit logs (sdk)
  + GHSA-x8fg-h69x-p28f: forbid issuance of non-validated SANs through ACME
    (secrets/pki)
  + GHSA-2cjw-94fw-wqjx: remove prompt=none redirection support in the OIDC
    provider (ui)

* Thu Oct 01 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.6.3-alt1
- Updated to new version 2.6.3.
- Fixes:
  + GHSA-444v-8vxr-p36h: ensure previously rendered secrets do not appear in
    stdout on agent template rendering failures (command/agent)
  + GHSA-34fc-gh42-pj53: use constant-time token comparison in recovery mode
    (core/recovery)
  + GHSA-xp3c-3jw3-4vcr: prevent LIST operations from bypassing a
    capabilities = ["deny"] rule via a more specific wildcard ACL grant
    (core/policies)
  + GHSA-59w7-v8rr-pr4p: reject unescaped +, *, / and , characters in
    identity template substitutions by default, preventing ACL/PKI/SSH path
    injection (core/policies, secret/pki, secret/ssh)
  + GHSA-rh46-vc3j-w2w3: ensure internal operation types cannot be dispatched
    from inline authentication and workflows, preventing token creation (core)
  + GHSA-g892-p242-8g86: also enforce allowed_ip_sans_cidr on IP SANs from
    CSRs (secrets/pki)
  + GHSA-8gmq-wv9h-fcwp: ensure the quit endpoint requires the
    X-Vault-Request header when specified by listener configuration
    (agent, proxy)
  + GHSA-fg5x-7whg-6c28: use ResolvePathOperation to define canonical URLs
    for canonicalized resources (auth/cert, auth/kubernetes, auth/userpass,
    secrets/pki, core/policies, core/workflows)
  + GHSA-j6wc-jpvg-xfxq: ensure plugin command name is relative to
    plugin_directory prior to executing (core/plugins)
  + GHSA-cg72-x35g-xfp8: restrict writes to sys/plugins/catalog/* endpoints
    to the root namespace (core/plugins)
  + GHSA-hr5j-3j78-4vh2: ensure denied ACL policy template evaluation returns
    an error and is not silently dropped (core/policies)
  + GHSA-mjch-vcw3-hhmf: prevent cross-namespace policy resolution traversal
    in the LRU policy cache (core/policies)
  + GHSA-8xxq-mq9m-xmhw: prevent TypeKVPair, TypeHeader from leaking
    malformed request data into audit logs in plaintext (sdk)
  + GHSA-x8fg-h69x-p28f: forbid issuance of non-validated SANs through ACME
    (secrets/pki)
  + GHSA-2cjw-94fw-wqjx: remove support for prompt=none redirection in the
    OIDC provider (ui)
- Package now switches the UI build from yarn to pnpm, following upstream's
  migration in 2.6.0.

* Wed Jul 08 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.5-alt1
- Updated to new version 2.5.5.
- Fixes:
  + CVE-2026-55770: prevent LDAP injection via bind DN to group resolution
    (auth/ldap, secrets/ldap)
  + CVE-2026-55776: fix server crash from unlock of unlocked mutex for RSA keys
    created with derived=true (secrets/transit)
  + CVE-2026-55774: fix unauthorized cross-namespace lease revocation via leaked
    lease identifiers (core/leases)
  + CVE-2026-55775: fix namespace path canonicalization of "root" enabling
    unauthorized operations on the parent namespace (core/namespaces)
- Require golang >= 1.26.4 to close Go stdlib CVEs found in the build toolchain.
- Bumped vendored go-ntlmssp to 0.1.1 to fix CVE-2026-32952.
- Bumped vendored jackc/pgx/v5 to 5.9.2 to fix CVE-2026-41889.

* Tue Jun 09 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.4-alt1
- Updated to new version 2.5.4.
- Fixes:
  + CVE-2026-46358: fix audit logs dropping custom headers when using inline
    auth (core/auth)
  + CVE-2026-46405: prevent hidden default token issuance from auth plugin
    endpoints (core)
  + CVE-2026-45808: remove legacy lease endpoints due to cross-namespace lease
    modification (core)

* Wed Apr 22 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.3-alt1
- Updated to new version 2.5.3.
- Fixes:
  + CVE-2026-39388: prevent token renewal with different-but-valid certificate
    (auth/cert)
  + CVE-2026-40264: prevent cross-namespace token renewal, revocation by
    accessor (auth/token)
  + CVE-2026-5807: disallow unauthenticated cancellation of sys/generate-root/*
    (core)
  + CVE-2026-3605: forbid request path traversal using . and .. segments (core)
  + CVE-2026-39396: validate and restrict downloaded plugin binary size from OCI
    images (core/plugins).
  + CVE-2026-39946: correctly quote schema name in revoke statement
    (database/postgresql)

* Wed Apr 01 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.2-alt1
- Updated to new version v2.5.2.
- Fixes:
  + CVE-2026-33758: prevent XSS via error_description parameter in
    callback_mode=direct (auth/jwt)
  + CVE-2026-33757: prompt for confirmation during direct callback mode
    (auth/jwt)

* Wed Mar 25 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.1-alt2
- Fixed LDFLAGS to set correct version information (Closes: #58272).

* Tue Feb 24 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.5.1-alt1
- Updated to new version v2.5.1.
- Added openbao.env configuration file.
- Fixes:
  + CVE-2025-68121: vulnerability in Go runtime could lead to unspecified impact
  + CVE-2026-24051: openTelemetry Go SDK vulnerability in telemetry handling

* Wed Jan 21 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.4-alt2
- Added systemd service file support.

* Mon Dec 29 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.4.4-alt1
- Updated to new version v2.4.4.
- Support building package with bundled web ui (Closes: #56797).
- Fixes:
  + CVE-2025-64761: correctly lowercase policy names on identity groups to
    prevent root policy assignment (core/identity)

* Sun Jun 08 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.2.2-alt1
- Initial build for ALT Sisyphus.
