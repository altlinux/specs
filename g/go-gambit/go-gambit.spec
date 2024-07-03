%define _unpackaged_files_terminate_build 1

%global import_path github.com/maaslalani/gambit

Name: go-gambit
Version: v0.1.0
Release: alt1.git9c3cb904

Summary: Chess board in your terminal
License: MIT
Group: Development/Other
Url: https://pkg.go.dev/github.com/maaslalani/gambit
Vcs: https://github.com/maaslalani/gambit

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang

%description
Gambit is a classic chess game for your terminal. Designed to be simple and
accessible, gambit allows you to play chess with friends or AI directly from
the command line, even over SSH.

%prep
%setup -a1

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
%doc README* LICENSE
%_bindir/gambit

%changelog
* Wed Jul 03 2024 Denis Rastyogin <gerben@altlinux.org> v0.1.0-alt1.git9c3cb904
- Initial build for Sisyphus.
