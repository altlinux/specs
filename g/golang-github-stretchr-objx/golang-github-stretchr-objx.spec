%def_without check

%global goipath github.com/stretchr/objx

Name: golang-github-stretchr-objx
Version: 0.2.0
Release: alt1
Summary: Go package for dealing with maps, slices, json and other data
Group: Development/Other
License: MIT
Url: https://github.com/stretchr/objx
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/objx-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Objx provides the objx.Map type, which is a map[string]interface{} that exposes
a powerful Get method (among others) that allows you to easily and quickly get
access to data within the map, without having to worry too much about type
assertions, missing data, default values etc.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n objx-%version
# remove built-in golang modules
rm -rf vendor

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
%doc README.md LICENSE
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 0.2.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

