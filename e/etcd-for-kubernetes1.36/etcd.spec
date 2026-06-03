%global import_path github.com/etcd-io/etcd

%global _unpackaged_files_terminate_build 1

%define k8s_ver    1.36
# git rev-parse --short v3.6.8^{commit}
%define git_commit 4e814e2

Name: etcd-for-kubernetes%k8s_ver
Version: 3.6.8
Release: alt1

Summary: A highly-available key value store for shared configuration
License: Apache-2.0
Group: System/Servers
Url: https://etcd.io
Vcs: https://github.com/etcd-io/etcd

ExclusiveArch: %go_arches

Source0: %name-%version.tar
# alt specific commits
Patch0: %name-%version.patch

Provides: etcd-for-kubernetes = %EVR
Conflicts: etcd-for-kubernetes
Conflicts: etcd

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24

%description
Etcd is a distributed key value store that provides a reliable way to store data
across a cluster of machines.
This package contains etcd version needed for kubernetes %k8s_ver container image.

%prep
%setup
%patch -p1

%build
export CGO_ENABLED=0
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export LDFLAGS="-X go.etcd.io/etcd/api/v3/version.GitSHA=%git_commit"

%golang_prepare

cd .build/src/%import_path

%golang_build \
    server \
    etcdctl \
#

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p -- %buildroot%_sbindir
mv -f -- %buildroot%_bindir/server %buildroot%_sbindir/etcd

%files
%_bindir/etcdctl
%_sbindir/etcd

%changelog
* Mon Jun 01 2026 Alexander Stepchenko <geochip@altlinux.org> 3.6.8-alt1
- 3.6.6 -> 3.6.8 (as required by Kubernetes v1.36.0).
- Introduce etcd package for Kubernetes 1.36.
- Fixes:
  + CVE-2025-47914: Malformed constraint may cause denial of service in golang.org/x/crypto/ssh/agent
  + CVE-2025-58181: Unbounded memory consumption in golang.org/x/crypto/ssh

* Thu May 07 2026 Ivan A. Melnikov <iv@altlinux.org> 3.6.6-alt2
- NMU: Mark loong64 as supported architecture to simplify
  kubernetes deployment on loongarch64.

* Thu Dec 18 2025 Alexander Stepchenko <geochip@altlinux.org> 3.6.6-alt1
- 3.6.5 -> 3.6.6 (as required by Kubernetes v1.35.0).
- Introduce etcd package for Kubernetes 1.35.

* Thu Nov 13 2025 Alexander Stepchenko <geochip@altlinux.org> 3.6.5-alt1
- 3.5.24 -> 3.6.5 (as required by Kubernetes v1.34.2).
- Introduce etcd package for Kubernetes 1.34.

* Thu Nov 13 2025 Alexander Stepchenko <geochip@altlinux.org> 3.5.24-alt1
- 3.5.21 -> 3.5.24 (as required by Kubernetes v1.33.6).

* Tue May 20 2025 Alexander Stepchenko <geochip@altlinux.org> 3.5.21-alt1
- 3.5.16 -> 3.5.21

* Wed May 14 2025 Nadezhda Fedorova <fedor@altlinux.org> 3.5.16-alt4
- Fixes:
  + CVE-2024-45337: Misuse of connection.serverAuthenticate may cause authorization bypass in golang.org/x/crypto
  + CVE-2024-45338: Non-linear parsing of case-insensitive content in golang.org/x/net/html
  + CVE-2024-51744: Bad documentation of error handling in ParseWithClaims can lead to potentially dangerous situations in golang-jwt
  + CVE-2025-22869: Potential denial of service in golang.org/x/crypto
  + CVE-2025-22870: HTTP Proxy bypass using IPv6 Zone IDs in golang.org/x/net
  + CVE-2025-22872: Incorrect Neutralization of Input During Web Page Generation in x/net in golang.org/x/net
  + CVE-2025-30204: jwt-go allows excessive memory allocation during header parsing

* Wed May 07 2025 Alexander Stepchenko <geochip@altlinux.org> 3.5.16-alt3
- Make separate etcd packages for kubernetes container images

* Wed Mar 19 2025 Alexander Stepchenko <geochip@altlinux.org> 3.5.16-alt2
- Rename package to include version in the name

* Wed Oct 30 2024 Alexander Stepchenko <geochip@altlinux.org> 3.5.16-alt1
- 3.5.15 -> 3.5.16

* Wed Sep 18 2024 Alexander Stepchenko <geochip@altlinux.org> 3.5.15-alt1
- 3.5.12 -> 3.5.15 (Fixes: CVE-2023-45288, CVE-2024-24786)

* Mon Feb 05 2024 Alexey Shabalin <shaba@altlinux.org> 3.5.12-alt1
- 3.5.12

* Sat May 27 2023 Alexey Shabalin <shaba@altlinux.org> 3.5.9-alt1
- 3.5.9 (Fixes: CVE-2023-32082).

* Fri Apr 14 2023 Alexey Shabalin <shaba@altlinux.org> 3.5.8-alt1
- 3.5.8 (Fixes: CVE-2021-28235).

* Fri Jan 28 2022 Alexey Shabalin <shaba@altlinux.org> 3.5.1-alt1
- 3.5.1

* Thu Jan 27 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.18-alt1
- 3.4.18

* Wed Jan 26 2022 Alexey Shabalin <shaba@altlinux.org> 3.4.15-alt2
- Update changelog.

* Thu Oct 28 2021 Paul Wolneykien <manowar@altlinux.org> 3.4.9-alt1.1
- Fix building on x86_64.

* Fri Mar 19 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.15-alt1
- 3.4.15

* Fri Jan 15 2021 Alexey Shabalin <shaba@altlinux.org> 3.4.14-alt1
- 3.4.14

* Sat Sep 05 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.13-alt1
- 3.4.13 (Fixes: CVE-2020-15106, CVE-2020-15112, CVE-2020-15113, CVE-2020-15114,
                 CVE-2020-15115, CVE-2020-15136).

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.9-alt1
- 3.4.9.

* Tue Apr 28 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt2
- add post_service and preun_service.

* Sun Apr 26 2020 Alexey Shabalin <shaba@altlinux.org> 3.4.7-alt1
- 3.4.7 (Fixes: CVE-2018-1098, CVE-2018-1099, CVE-2018-16886).

* Tue Aug 08 2017 Alexey Gladkov <legion@altlinux.ru> 3.2.5-alt1
- First build for ALTLinux.
