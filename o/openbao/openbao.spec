%define _unpackaged_files_terminate_build 1
%define import_path github.com/openbao/openbao

Name: openbao
Version: 2.6.3
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

%changelog
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
