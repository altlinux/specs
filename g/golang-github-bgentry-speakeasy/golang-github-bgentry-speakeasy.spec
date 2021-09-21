%def_without check

%define goipath github.com/bgentry/speakeasy

Name: golang-github-bgentry-speakeasy
Version: 0.1.0
Release: alt3.git7db90ef
Summary: Cross-platform golang helpers for reading password input without cgo
Group: Development/Other
License: MIT
Url: https://github.com/bgentry/speakeasy
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/speakeasy-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
This package provides cross-platform Go helpers for taking user input from the
terminal while not echoing the input back (similar to getpasswd). The package
uses syscalls to avoid any dependence on cgo, and is therefore compatible with
cross-compiling.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
This package provides cross-platform Go helpers for taking user input from the
terminal while not echoing the input back (similar to getpasswd). The package
uses syscalls to avoid any dependence on cgo, and is therefore compatible with
cross-compiling.

%prep
%setup -n speakeasy-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

go mod init github.com/bgentry/speakeasy
go mod tidy -go=1.17
%golang_prepare

cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc LICENSE LICENSE_WINDOWS example Readme.md
%go_path/src/%goipath

%changelog
* Tue Sep 21 2021 Leontiy Volodin <lvol@altlinux.org> 0.1.0-alt3.git7db90ef
- Fixed build with golang 1.17.

* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 0.1.0-alt2
- Fixed build with golang 1.16.

* Mon Jun 01 2020 Leontiy Volodin <lvol@altlinux.org> 0.1.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
