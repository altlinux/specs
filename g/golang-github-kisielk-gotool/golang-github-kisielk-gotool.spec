%def_without check

%global goipath github.com/kisielk/gotool

Name: golang-github-kisielk-gotool
Version: 1.0.0
Release: alt1
Summary: Utility functions provided by (but not exported) by cmd/go

License: MIT and BSD-3-Clause
Group: Development/Other
Url: https://github.com/kisielk/gotool
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: gotool-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Package Gotool contains utility functions used to implement the standard
"cmd/go" tool, provided as a convenience to developers who want to write tools
with similar semantics.

%package devel
Summary: Utility functions provided by (but not exported) by cmd/go
Group: Development/Other
BuildArch: noarch

%description devel
Package Gotool contains utility functions used to implement the standard
"cmd/go" tool, provided as a convenience to developers who want to write tools
with similar semantics.

%prep
%setup -n gotool-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

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
%doc LICENSE README.md
%go_path/src/%goipath

%changelog
* Wed Apr 29 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec). 

