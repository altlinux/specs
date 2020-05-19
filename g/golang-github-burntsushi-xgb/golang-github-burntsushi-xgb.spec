%def_without check

%global goipath         github.com/BurntSushi/xgb
%global commit          27f122750802c950b2c869a5b63dafcf590ced95

Name: golang-github-burntsushi-xgb
Version: 0
Release: alt1.git27f1227
Summary: Low-level api to communicate with the X server
Group: Graphical desktop/Other
License: WTFPL
Url: https://github.com/BurntSushi/xgb
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: xgb-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
XGB is the X Go Binding, which is a low-level API to communicate with the
core X protocol and many of the X extensions. It is closely modeled after
XCB and xpyb.

%package devel
Summary: Low-level api to communicate with the X server
Group: Development/Other
BuildArch: noarch

%description devel
XGB is the X Go Binding, which is a low-level API to communicate with the
core X protocol and many of the X extensions. It is closely modeled after
XCB and xpyb.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name.

%prep
%setup -n xgb-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in xgbgen; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
%gotest -d xproto
%endif

%files
%doc LICENSE xgbgen/COPYING
%doc AUTHORS CONTRIBUTORS README
%_bindir/*

%files devel
%go_path/src/%goipath
%exclude %go_path/src/%goipath/examples

%files examples
%go_path/src/%goipath/examples

%changelog
* Fri May 8 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git27f1227
- Initial build for ALT Sisyphus (thanks fedora for this spec).

