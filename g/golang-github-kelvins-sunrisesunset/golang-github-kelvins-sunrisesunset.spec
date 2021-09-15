%def_without check

%define goipath github.com/kelvins/sunrisesunset

Name: golang-github-kelvins-sunrisesunset
Version: 1.0
Release: alt3.git39fa1bd
Summary: Go package that provides the sunrise and sunset equation
Group: Development/Other
License: MIT
Url: https://github.com/kelvins/sunrisesunset
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: sunrisesunset-%version.tar.gz

BuildRequires(pre): rpm-build-golang
#BuildRequires: golang-tools-devel
BuildRequires: golang-github-mattn-goveralls-devel

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

go mod init github.com/kelvins/sunrisesunset
go mod tidy -go=1.17
%golang_prepare

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
* Wed Sep 15 2021 Leontiy Volodin <lvol@altlinux.org> 1.0-alt3.git39fa1bd
- Built from commit 39fa1bd816d52927b4cfcab0a1535b17eafe0a3d.
- Fixed build with golang 1.17.

* Thu Feb 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.0-alt2
- Fixed build with golang 1.16.

* Wed Jun 03 2020 Leontiy Volodin <lvol@altlinux.org> 1.0-alt1
- Initial build for ALT Sisyphus.

