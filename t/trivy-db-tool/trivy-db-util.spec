%global import_path github.com/aquasecurity/trivy-db
%global _unpackaged_files_terminate_build 1

Name: trivy-db-tool
Version: 0.2.0
Release: alt1
Summary: trivy-db is a CLI tool and a library to manipulate Trivy DB

Group: Development/Databases
License: Apache-2.0
Url: https://%import_path

Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: /proc

%description
%summary.

%prep
%setup -q

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0

%golang_prepare
%golang_build cmd/trivy-db

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p %buildroot%_bindir

%golang_install

rm -rf -- "%buildroot%go_root"

%files
%doc LICENSE README.md
%_bindir/trivy-db

%changelog
* Fri Apr 19 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.2.0-alt1
- 0.1.0 -> 0.2.0 

* Thu Dec 28 2023 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.1.0-alt1
- Initial build for ALT 
