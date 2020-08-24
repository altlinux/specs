%def_without check

%global goipath github.com/godbus/dbus

Name: golang-github-go-dbus
Version: 5.0.3
Release: alt1.gitefee839
Summary: Go client bindings for the D-Bus

License: BSD-2-Clause
Group: Development/Other
Url: https://github.com/godbus/dbus
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/dbus-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Simple library that implements native Go client bindings for the D-Bus message bus system.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Simple library that implements native Go client bindings for the D-Bus message bus system.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package containes examples for %name.

%prep
%setup -n dbus-%version

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
%doc LICENSE CONTRIBUTING.md README.markdown MAINTAINERS
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_examples

%files examples
%go_path/src/%goipath/_examples

%changelog
* Mon Aug 24 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.3-alt1.gitefee839
- Initial build for ALT Sisyphus.
