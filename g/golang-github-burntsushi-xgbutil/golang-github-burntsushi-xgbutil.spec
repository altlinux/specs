%def_without check

%global goipath         github.com/BurntSushi/xgbutil
%global commit          f7c97cef3b4e6c88280a5a7091c3314e815ca243

Name: golang-github-burntsushi-xgbutil
Version: 0
Release: alt1.gitf7c97ce
Summary: Utility library to make use of the X Go Binding easier
Group: Development/Other
License: WTFPL
Url: https://github.com/BurntSushi/xgbutil
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: xgbutil-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/golang/freetype) golang(github.com/golang/freetype/truetype) golang(github.com/BurntSushi/graphics-go/graphics) golang(github.com/BurntSushi/xgb) golang(github.com/BurntSushi/xgb/shape) golang(github.com/BurntSushi/xgb/xinerama) golang(github.com/BurntSushi/xgb/xproto)
BuildRequires: golang-github-freetype-devel golang-github-burntsushi-xgb-devel golang-github-burntsushi-graphics-devel

%description
xgbutil is a utility library designed to work with the X Go Binding. This
project's main goal is to make various X related tasks easier. For example,
binding keys, using the EWMH or ICCCM specs with the window manager,
moving/resizing windows, assigning function callbacks to particular events,
drawing images to a window, etc.

xgbutil attempts to be thread safe, but it has not been completely tested in
this regard. In general, the X event loop implemented in the xevent package is
sequential. The idea is to be sequential by default, and let the user spawn
concurrent code at their discretion. (i.e., the complexity of making the main
event loop generally concurrent is vast.)

%package devel
Summary: Utility library to make use of the X Go Binding easier
Group: Development/Other
BuildArch: noarch

%description devel
xgbutil is a utility library designed to work with the X Go Binding. This
project's main goal is to make various X related tasks easier. For example,
binding keys, using the EWMH or ICCCM specs with the window manager,
moving/resizing windows, assigning function callbacks to particular events,
drawing images to a window, etc.

xgbutil attempts to be thread safe, but it has not been completely tested in
this regard. In general, the X event loop implemented in the xevent package is
sequential. The idea is to be sequential by default, and let the user spawn
concurrent code at their discretion. (i.e., the complexity of making the main
event loop generally concurrent is vast.)

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name package.

%prep
%setup -n xgbutil-%version
find . -name "*.go" -exec sed -i "s|github.com/BurntSushi/freetype-go/freetype|github.com/golang/freetype|" "{}" +;
sed -i 's|/usr/bin/env python2.7|/usr/bin/python3|' scripts/write-events

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
%gotest
%endif

%files devel
%doc COPYING README
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_examples

%files examples
%go_path/src/%goipath/_examples

%changelog
* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gitf7c97ce
- Initial build for ALT Sisyphus (thanks fedora for this spec).

