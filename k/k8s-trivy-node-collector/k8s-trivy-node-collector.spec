%global import_path github.com/aquasecurity/k8s-node-collector
%global _unpackaged_files_terminate_build 1

Name: k8s-trivy-node-collector
Version: 0.3.1
Release: alt1
Epoch: 1
Summary: k8s-Node-collector is an open source collector who collect Node information (fs and process data) and output in a table/json format

Group: Monitoring
License: Apache-2.0
Url: https://%import_path

Source: %name-%version.tar

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-build-golang

BuildRequires: /proc

%description
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export CGO_ENABLED=0

%golang_prepare
%golang_build cmd/node-collector

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p %buildroot%_bindir

%golang_install

mv %buildroot%_bindir/node-collector %buildroot%_bindir/%name

rm -rf -- %buildroot%_datadir
rm -rf -- %buildroot%go_root

%files
%doc LICENSE README.md
%_bindir/%name

%changelog
* Thu Aug 29 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 1:0.3.1-alt1
- 0.0.9 -> 0.3.1
- Fixes: CVE-2024-24790

* Mon Mar 04 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 1:0.0.9-alt1
- Initial build for ALT 
