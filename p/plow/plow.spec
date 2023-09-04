%define _unpackaged_files_terminate_build 1

%global import_path github.com/six-ddc/plow

Name: plow
Version: 1.3.1
Release: alt1

Summary: Plow is an HTTP(S) benchmarking tool, written in Golang
License: Apache-2.0
Group: Networking/Other
Url: https://pkg.go.dev/github.com/six-ddc/plow
Vcs: https://github.com/six-ddc/plow

Source0: %name-%version.tar
Source1: vendor.tar
BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Plow is an HTTP(S) benchmarking tool, written in Golang. It uses excellent
fasthttp instead of Go's default net/http due to its lightning fast performance

%prep
%setup -a 1

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
%_bindir/%name
%doc README.md LICENSE

%changelog
* Mon Sep 04 2023 Vladislav Glinkin <smasher@altlinux.org> 1.3.1-alt1
- Initial build for ALT

