%def_with check

%global goipath github.com/kelvins/sunrisesunset

Name: golang-github-kelvins-sunrisesunset
Version: 1.0
Release: alt1
Summary: Go package that provides the sunrise and sunset equation
Group: Development/Other
License: MIT
Url: https://github.com/kelvins/sunrisesunset
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: sunrisesunset-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Go package used to calculate the apparent sunrise and sunset times based on latitude, longitude, date and UTC offset.

%package devel
Summary: Go package that provides the sunrise and sunset equation
Group: Development/Other
BuildArch: noarch

%description devel
Go package used to calculate the apparent sunrise and sunset times based on latitude, longitude, date and UTC offset.

%prep
%setup -n sunrisesunset-%version

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
* Wed Jun 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.

