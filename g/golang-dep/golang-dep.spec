%define _unpackaged_files_terminate_build 1
%define import_path github.com/golang/dep


Name: golang-dep
Version: 0.5.4
Release: alt1
Summary: Go dependency management tool
License: BSD
Group: Development/Other
Url: https://github.com/golang/dep

# https://github.com/golang/dep.git
Source: %name-%version.tar

ExclusiveArch:	%go_arches

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
dep is a prototype dependency management tool for Go.
It requires Go 1.9 or newer to compile. dep is safe for production use.

dep is the official experiment, but not yet the official tool.
Check out the Roadmap for more on what this means!

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GO111MODULE="auto"

%golang_prepare

pushd .build/src/%import_path
%golang_build cmd/*
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
export GO111MODULE="auto"

%golang_install

%files
%doc LICENSE AUTHORS README.md
%_bindir/*

%changelog
* Wed Apr 07 2021 Leontiy Volodin <lvol@altlinux.org> 0.5.4-alt1
- New version.
- Fixed build with golang 1.16.

* Wed Feb 27 2019 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt2
- delete ubt macros

* Sat Sep 08 2018 Alexey Shabalin <shaba@altlinux.org> 0.5.0-alt1%ubt
- 0.5.0

* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.4.1-alt1%ubt
- Initial build for ALT.
