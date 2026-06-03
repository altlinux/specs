%global _unpackaged_files_terminate_build 1
%global __find_debuginfo_files %nil
%global import_path github.com/coredns/coredns

%define k8s_ver 1.36

Name: coredns-for-kubernetes%k8s_ver
Version: 1.14.2
Release: alt1

Summary: CoreDNS is a DNS server that chains plugins
License: Apache-2.0
Group: Other
Url: https://github.com/coredns/coredns

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Provides: coredns-for-kubernetes = %EVR
Conflicts: coredns-for-kubernetes
Conflicts: coredns

BuildRequires(pre): rpm-macros-golang
BuildRequires(pre): golang >= 1.25
BuildRequires: rpm-build-golang

%description
%summary.

This package contains coredns version needed for kubernetes %k8s_ver container image.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/coredns

%changelog
* Mon Jun 01 2026 Alexander Stepchenko <geochip@altlinux.org> 1.14.2-alt1
- 1.13.1 -> 1.14.2.
- Introduce coredns package for Kubernetes 1.36.
- Fixes:
  + CVE-2025-47914: Malformed constraint may cause denial of service in golang.org/x/crypto/ssh/agent
  + CVE-2025-64702: quic-go HTTP/3 QPACK Header Expansion DoS
  + CVE-2025-68156: Expr has Denial of Service via Unbounded Recursion in Builtin Functions
  + CVE-2026-24051: OpenTelemetry-Go Affected by Arbitrary Code Execution via PATH Hijacking
  + CVE-2026-26017: CoreDNS ACL Bypass
  + CVE-2026-26018: CoreDNS Loop Detection Denial of Service Vulnerability

* Tue Dec 23 2025 Alexander Stepchenko <geochip@altlinux.org> 1.13.1-alt1
- 1.12.1 -> 1.13.1.
- Introduce coredns package for Kubernetes 1.35.
- Fixes:
  + CVE-2025-59530: quic-go has Client Crash Due to Premature HANDSHAKE_DONE Frame

* Wed Sep 10 2025 Alexander Stepchenko <geochip@altlinux.org> 1.12.1-alt1
- 1.12.0 -> 1.12.1
- Introduce coredns package for Kubernetes 1.34.

* Fri May 23 2025 Alexander Stepchenko <geochip@altlinux.org> 1.12.0-alt2
- Security fixes:
  + CVE-2025-22869: Potential denial of service in golang.org/x/crypto
  + CVE-2025-22870: HTTP Proxy bypass using IPv6 Zone IDs in golang.org/x/net
  + CVE-2025-22872: Incorrect Neutralization of Input During Web Page Generation in x/net in golang.org/x/net
  + CVE-2025-29786: Memory Exhaustion in Expr Parser with Unrestricted Input
  + CVE-2025-30204: jwt-go allows excessive memory allocation during header parsing

* Tue May 20 2025 Alexander Stepchenko <geochip@altlinux.org> 1.12.0-alt1
- 1.11.3 -> 1.12.0
- Security fixes:
  + CVE-2024-45337: Misuse of connection.serverAuthenticate may cause authorization bypass in golang.org/x/crypto
  + CVE-2024-45338: Non-linear parsing of case-insensitive content in golang.org/x/net/html
  + CVE-2024-53259: quic-go affected by an ICMP Packet Too Large Injection Attack on Linux

* Thu Sep 19 2024 Alexander Stepchenko <geochip@altlinux.org> 1.11.3-alt1
- 1.11.1 -> 1.11.3
- Fixes:
  + CVE-2023-45288
  + CVE-2024-22189
  + CVE-2024-24786
  + CVE-2023-49295
  + CVE-2023-48795
  + CVE-2023-39325

* Wed Sep 18 2024 Alexander Stepchenko <geochip@altlinux.org> 1.11.1-alt2
- Rename the package to include version in the name

* Sat May 25 2024 Alexander Stepchenko <geochip@altlinux.org> 1.11.1-alt1
- 1.10.1 -> 1.11.1

* Fri Nov 03 2023 Alexander Stepchenko <geochip@altlinux.org> 1.10.1-alt1
- 1.10.0 -> 1.10.1

* Wed Nov 16 2022 Mikhail Gordeev <obirvalger@altlinux.org> 1.10.0-alt1
- Initial build for Sisyphus
