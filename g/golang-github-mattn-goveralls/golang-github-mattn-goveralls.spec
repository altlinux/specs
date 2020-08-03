%def_without check

%global goipath github.com/mattn/goveralls

Name: golang-github-mattn-goveralls
Version: 0.0.6
Release: alt1
Summary: Go integration for Coveralls.io continuous code coverage tracking system
Group: Development/Other
License: MIT 
Url: https://github.com/mattn/goveralls
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/goveralls-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n goveralls-%version

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
%doc README.md
%go_path/src/%goipath

%changelog
* Fri Jun 05 2020 Leontiy Volodin <lvol@altlinux.org> 0.0.6-alt1
- Initial build for ALT Sisyphus.

