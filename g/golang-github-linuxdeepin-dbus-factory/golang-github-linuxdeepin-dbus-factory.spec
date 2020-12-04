%def_without check

%global goipath github.com/linuxdeepin/go-dbus-factory

Name: golang-github-linuxdeepin-dbus-factory
Version: 1.8.0.27
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
BuildRequires: deepin-gir-generator golang-golang-x-net-devel golang-deepin-go-lib-devel glib2-devel libgio-devel libgtk+3-devel golang-github-go-dbus-devel

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
%make_build

%install
%makeinstall_std GOPATH="%go_path"

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

# %%files
# %%_bindir/*

%files devel
%doc CHANGELOG.md README.md LICENSE
%go_path/src/%goipath
#%%exclude %%go_path/src/%%goipath/_tool

%changelog
* Fri Dec 04 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0.27-alt1
- New version (1.8.0.27) with rpmgs script.

* Tue Oct 06 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0.23-alt1
- New version (1.8.0.23) with rpmgs script.

* Tue Sep 08 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0.18-alt2
- Built with make.

* Mon Sep 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0.18-alt1
- New version (1.8.0.18) with rpmgs script.

* Mon Aug 24 2020 Leontiy Volodin <lvol@altlinux.org> 1.8.0.9-alt1
- New version (1.8.0.9) with rpmgs script.

* Wed Aug 19 2020 Leontiy Volodin <lvol@altlinux.org> 1.7.0.6-alt1
- New version (1.7.0.6) with rpmgs script.

* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 1.6.4-alt1
- New version (1.6.4) with rpmgs script.

* Wed Apr 15 2020 Leontiy Volodin <lvol@altlinux.org> 0.9.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
