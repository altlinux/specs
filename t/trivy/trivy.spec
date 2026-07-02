%global import_path github.com/aquasecurity/trivy
%global _unpackaged_files_terminate_build 1

%ifdef _priority_distbranch
%define altbranch %_priority_distbranch
%else
%define altbranch %(rpm --eval %%_priority_distbranch)
%endif
%if "%altbranch" == "%nil"
%define altbranch sisyphus
%endif

Name: trivy
Version: 0.71.2
Release: alt1
Summary: A Fast Vulnerability Scanner for Containers

Group: Monitoring
License: Apache-2.0
Url: https://%import_path

Source: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-macros-systemd rpm-macros-golang
BuildRequires: rpm-build-golang wire golang >= 1.26

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

%package server
Summary: Trivy local server
Group: System/Servers
BuildArch: noarch
Requires: trivy-db

%description server
%summary.

%prep
%setup

%build
# replace default node-collector image source
sed -i 's|ghcr.io/aquasecurity/node-collector|registry.altlinux.org/%altbranch/trivy-node-collector|g' \
    pkg/flag/kubernetes_flags.go \
    vendor/github.com/aquasecurity/trivy-kubernetes/pkg/jobs/template/node-collector.yaml

# replace default trivy-db image source
#find . -type f -exec \
#	sed -i "s/ghcr.io\/aquasecurity\/trivy-db/registry.altlinux.org\/alt\/trivy-db/g" {} +

# replace default trivy-checks image source
#find . -type f -exec \
#	sed -i "s/ghcr.io\/aquasecurity\/trivy-checks/registry.altlinux.org\/alt\/trivy-checks/g" {} +

export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X github.com/aquasecurity/trivy/pkg/version/app.ver=%version"
export CGO_ENABLED=0
export GOEXPERIMENT=jsonv2

%golang_prepare
wire gen pkg/commands/... pkg/rpc/... pkg/k8s/...
%golang_build cmd/trivy

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p %buildroot{%_bindir,%_sysconfdir/sysconfig,%_unitdir}

%golang_install

install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

%post server
%post_systemd_postponed %name

%preun server
%preun_systemd %name

%files
%doc LICENSE README.md docs
%_bindir/%name

%files server
%_unitdir/%name.service
%config(noreplace) %_sysconfdir/sysconfig/%name

%changelog
* Mon Jun 29 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.71.2-alt1
- 0.71.2
- Fix order conditions bug in cpe detection.
- Use normalized version for EOL check. (Closes: #59516)
- Add `ALT Linux Team` to official vendor lists. (Closes: #59517)
- Add sisyphus support. (Closes: #59518)

* Wed Apr 22 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.70.0-alt1
- 0.70.0

* Fri Dec 19 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.68.2-alt1
- 0.68.2

* Wed Sep 10 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.66.0-alt1
- 0.66.0
- Change trivy-db module url from github.com to altlinux.space
- Change path to trivy-node-collector

* Tue Apr 08 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.61.0-alt1
- 0.61.0
- Change name 'scanner' to 'scan' in alt as in upstream

* Mon Mar 17 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.60.0-alt1
- 0.60.0
- Change ALT Linux Container Registry to altlinux.space Container Registry
- Add altlinux.space Container Registry for java-db

* Tue Mar 04 2025 Aleksandr Gamzin <gamzin@altlinux.org> 0.59.1-alt1
- 0.59.1

* Wed Dec 11 2024 Alexey Shabalin <shaba@altlinux.org> 0.58.0-alt1
- 0.58.0

* Thu Oct 10 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.56.1-alt1
- 0.55.0 -> 0.56.1
- Fixed `trivy k8s` scan for k8s >= 1.31
- Replace `trivy-checks` default image repository

* Tue Sep 10 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.55.0-alt1
- 0.54.1 -> 0.55.0

* Thu Aug 29 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.54.1-alt2
- Fixed hardcoded node-collector version

* Thu Aug 15 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.54.1-alt1
- 0.53.0 -> 0.54.1
- Fixed `trivy --version` output (closes: 47604)

* Mon Jul 08 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.53.0-alt1
- 0.52.2 -> 0.53.0

* Mon Jun 24 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.52.2-alt1
- 0.52.1 -> 0.52.2

* Mon Jun 10 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.52.1-alt1
- 0.50.1 -> 0.52.1

* Thu Apr 18 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.50.1-alt1
- 0.49.1 -> 0.50.1 

* Thu Feb 08 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.49.1-alt1
- 0.49.0 -> 0.49.1 

* Mon Feb 05 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.49.0-alt1
- 0.48.3 -> 0.49.0

* Tue Jan 30 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.3-alt3
- Replace default value for node-collector-imageref (k8s)

* Thu Jan 11 2024 Alexey Shabalin <shaba@altlinux.org> 0.48.3-alt2
- Restart service at transaction end
- Move useradd to trivy-db package

* Thu Jan 11 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.3-alt1
- 0.48.2 -> 0.48.3

* Tue Jan 09 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.2-alt1
- 0.48.1 -> 0.48.2

* Thu Dec 28 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.1-alt2
- Fixed environment variable at systemd service
- Added listen address option for trivy at systemd service
- Added "WantedBy=multi-user.target" section

* Tue Dec 19 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.1-alt1
- 0.48.0 -> 0.48.1

* Tue Dec 05 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.48.0-alt1
- 0.47.0 -> 0.48.0

* Wed Nov 08 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.47.0-alt1
- 0.46.1 -> 0.47.0

* Mon Oct 30 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.46.1-alt2
- Improve systemd-service

* Sun Oct 29 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.46.1-alt1
- 0.46.0 -> 0.46.1

* Thu Oct 26 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.46.0-alt2
- Add subpackage `trivy-server`

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

