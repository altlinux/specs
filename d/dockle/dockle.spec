%define _unpackaged_files_terminate_build 1
%define import_path github.com/goodwithtech/dockle/

Name: dockle
Version: 0.4.15
Release: alt1

Summary: Lints Docker/OCI images for security and best-practice compliance
License: Apache-2.0
Group: Development/Other
Url: https://github.com/goodwithtech/dockle
Vcs: https://github.com/goodwithtech/dockle

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: libbtrfs-devel

%description
Dockle is a container image linter that scans for security issues and validates
best practices against the CIS Benchmarks. Easy to integrate into CI/CD, it
ensures your Docker images are secure and production-ready.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GO111MODULE=off

%golang_prepare
cd .build/src/%import_path/cmd/dockle
%golang_build .

%install
ln -sf %_licensedir/Apache-2.0 LICENSE
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/dockle
%doc --no-dereference LICENSE
%doc README.md

%changelog
* Tue Jan 27 2026 Maxim Tulskiy <tulskijms@altlinux.org> 0.4.15-alt1
- Initial build for ALT Sisyphus.
