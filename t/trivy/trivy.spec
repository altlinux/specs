
%global import_path github.com/aquasecurity/trivy
%global _unpackaged_files_terminate_build 1

Name: trivy
Version: 0.46.0
Release: alt1
Summary: A Fast Vulnerability Scanner for Containers

Group: Monitoring
License: Apache-2.0
Url: https://%import_path

Source: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-build-golang wire

BuildRequires: /proc

%description
Trivy is a comprehensive and versatile security scanner.
Trivy has scanners that look for security issues, and targets where it can
find those issues.

Targets (what Trivy can scan):
* Container Image
* Filesystem
* Git Repository (remote)
* Virtual Machine Image
* Kubernetes
* AWS

Scanners (what Trivy can find there):
* OS packages and software dependencies in use (SBOM)
* Known vulnerabilities (CVEs)
* IaC issues and misconfigurations
* Sensitive information and secrets
* Software licenses

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X github.com/aquasecurity/trivy/pkg/version.ver=%version"
export CGO_ENABLED=0

%golang_prepare
wire gen pkg/commands/... pkg/rpc/...
%golang_build cmd/trivy

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p %buildroot{%_bindir,%_sharedstatedir/%name,%_sysconfdir/sysconfig,%_unitdir}

%golang_install

install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

%pre
groupadd -r -f _%name > /dev/null 2>&1 ||:
useradd -M -r -d %_sharedstatedir/%name -g _%name -s /dev/null -c "Trivy services" _%name > /dev/null 2>&1 ||:

%post
%post_systemd %name

%preun
%preun_systemd %name

%files
%doc LICENSE README.md docs
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name
%attr(0755,_trivy,_trivy) %dir %_sharedstatedir/trivy
%_bindir/%name

%changelog
* Tue Oct 17 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.46.0-alt1
- 0.45.1 -> 0.46.0

* Sun Sep 17 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.45.1-alt1
- 0.45.0 -> 0.45.1 

* Fri Sep 15 2023 Alexey Shabalin <shaba@altlinux.org> 0.45.0-alt2
- Fixed version info.
- Build without strip binary and with CGO_ENABLED=0.

* Mon Sep 04 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.45.0-alt1
- 0.39.0 -> 0.45.0

* Fri Jun 02 2023 Stepan Paksashvili <paksa@altlinux.org> 0.39.0-alt2
- Updated ALT support and vendor trivy-db, added systemd unit.

* Tue Apr 25 2023 Stepan Paksashvili <paksa@altlinux.org> 0.39.0-alt1
- Added full ALT support.

* Wed Jan 25 2023 Alexey Shabalin <shaba@altlinux.org> 0.36.1-alt2
- Added basic ALT support.

* Tue Jan 17 2023 Alexey Shabalin <shaba@altlinux.org> 0.36.1-alt1
- Initial build for ALT.

