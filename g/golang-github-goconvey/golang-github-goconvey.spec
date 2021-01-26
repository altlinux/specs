%def_without check

%define goipath github.com/smartystreets/goconvey
%define repo goconvey 

Name: golang-github-goconvey
Version: 1.6.4
Release: alt1
Summary: Go testing tool

License: MIT and Apache-2.0 and OFL-1.1
Group: Development/Other
Url: https://github.com/smartystreets/goconvey
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%repo-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Go testing tool.

%package devel
Summary: Go testing tool
Group: Development/Other
BuildArch: noarch

%description devel
Go testing tool.

%prep
%setup -n %repo-%version

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
%doc README.md LICENSE.md
%go_path/src/%goipath

%changelog
* Tue Jan 26 2021 Leontiy Volodin <lvol@altlinux.org> 1.6.4-alt1
- Initial build for ALT Sisyphus.
