%def_without check

%global goipath github.com/linuxdeepin/go-dbus-factory

Name: golang-github-linuxdeepin-dbus-factory
Version: 1.7.0.6
Release: alt1
Summary: Go DBus factory for Deepin Desktop Environment

License: GPL-3.0-only
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/go-dbus-factory
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-dbus-factory-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(pkg.deepin.io/lib/dbus1) golang(pkg.deepin.io/lib/dbusutil) golang(pkg.deepin.io/lib/dbusutil/proxy)
# BuildRequires: golang(golang.org/x/net/context) golang(pkg.deepin.io/gir/gio-2.0) golang(pkg.deepin.io/gir/glib-2.0) glib2-devel libgio-devel libgtk+3-devel
# BuildRequires: deepin-gir-generator golang-golang-x-net-devel golang-deepin-go-lib-devel glib2-devel libgio-devel libgtk+3-devel
BuildRequires: golang-deepin-go-lib-devel golang-golang-x-net-devel

%description
Go DBus factory for Deepin Desktop Environment.

%package devel
Summary: Go DBus factory for Deepin Desktop Environment
Group: Development/Other
BuildArch: noarch

%description devel
Go DBus factory for Deepin Desktop Environment.

%prep
%setup -n go-dbus-factory-%version
# remove debian build files
rm -rf debian

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in _tool/* ; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files
%doc CHANGELOG.md README.md LICENSE
%_bindir/*

%files devel
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_tool

%changelog
* Wed Aug 19 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.0.6-alt1
- New version (1.7.0.6) with rpmgs script.

* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 1.6.4-alt1
- New version (1.6.4) with rpmgs script.

* Wed Apr 15 2020 Leontiy Volodin <lvol@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
