
%global import_path github.com/aquasecurity/trivy
%global _unpackaged_files_terminate_build 1

Name: trivy
Version: 0.36.1
Release: alt1
Summary: A Fast Vulnerability Scanner for Containers

Group: Monitoring
License: Apache-2.0
Url: https://%import_path
Source: %name-%version.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang wire
BuildRequires: /proc

%description
Trivy (pronunciation) is a comprehensive and versatile security scanner.
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
export LDFLAGS="-s -w -X=main.version=%version"

%golang_prepare
wire gen pkg/commands/... pkg/rpc/...
%golang_build cmd/trivy

%install
export BUILDDIR="$PWD/.gopath"
%golang_install
rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

%files
%doc README.md
%_bindir/%name

%changelog
* Tue Jan 17 2023 Alexey Shabalin <shaba@altlinux.org> 0.36.1-alt1
- Initial build for ALT.

