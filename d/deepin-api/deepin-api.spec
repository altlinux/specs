%define _unpackaged_files_terminate_build 1
%define goipath github.com/linuxdeepin/dde-api
%define forgeurl https://github.com/linuxdeepin/dde-api

# Run tests in check section
# disable for bootstrapping
%def_without check

Name: deepin-api
Version: 5.5.32
Release: alt1
Summary: Golang bingding for dde-daemon
License: GPL-3.0+
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/dde-api

Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/dde-api-%version.tar.gz
Source1: vendor.tar

BuildRequires(pre): rpm-build-golang rpm-build-python3
BuildRequires: libalsa-devel libcairo-devel libgio-devel libgtk+3-devel libgdk-pixbuf-devel libgudev-devel libcanberra-devel libpulseaudio-devel librsvg-devel libpoppler-glib-devel libpolkitqt5-qt5-devel libsystemd-devel libXfixes-devel libXcursor-devel libX11-devel libXi-devel deepin-gettext-tools libgdk-pixbuf-xlib-devel
Requires: deepin-desktop-base rfkill
Requires(pre): shadow-utils dbus-tools

%description
%summary.

%package -n golang-%name-devel
Summary: %summary
Group: Graphical desktop/Other
# BuildArch: noarch

%description -n golang-%name-devel
%summary.

This package contains library source intended for
building other packages which use import path with
%goipath prefix.

%prep
%setup -n dde-api-%version
#patch -p1
# Remove debian build files.
rm -rf debian/
# Fix unmets.
sed -i 's|/usr/bin/true|/bin/true|' \
    misc/systemd/system/deepin-shutdown-sound.service
# Fixed build for i586.
sed -i 's|gobuild|.build|' Makefile
# Fixed paths.
sed -i 's|/etc/default/locale|%_datadir/locale|' \
    adjust-grub-theme/util.go \
    locale-helper/ifc.go
# Unpacked vendor/ into the source (used .gear/tags).
tar -xf %SOURCE1
# Fixed paths in vendor/.
sed -i 's|/usr/share/locale/locale.alias|/usr/share/X11/locale/locale.alias|' \
    vendor/src/github.com/linuxdeepin/go-lib/locale/locale.go
sed -i 's|/usr/share/icons/deepin/|/usr/share/icons/bloom/|' \
    vendor/src/github.com/linuxdeepin/go-x11-client/util/cursor/cursor_test.go

%build
export GOPATH="$(pwd)/vendor"
export GOFLAGS="-mod=vendor"

%make

%install
export GOPATH="%go_path"

%makeinstall_std SYSTEMD_SERVICE_DIR="%_unitdir" -i

# HOME directory for user deepin-sound-player
mkdir -p %buildroot%_sharedstatedir/deepin-sound-player
install -Dm644 archlinux/deepin-api.sysusers %buildroot/lib/sysusers.d/deepin-api.conf
# Pack golang modules.
mkdir -p %buildroot%go_path/src/%goipath/vendor/src/
cp -a vendor/src/* %buildroot%go_path/src/%goipath/vendor/src/

%files
%doc README.md LICENSE
%_bindir/*
%_libexecdir/deepin-api/*
%_iconsdir/hicolor/??x??/actions/*
%_iconsdir/hicolor/???x???/actions/*
%_iconsdir/hicolor/scalable/actions/*
%_datadir/dbus-1/*
%_datadir/polkit-1/*
%_unitdir/*.service
%_var/lib/polkit-1/*
%_datadir/dde-api/data/*
/lib/sysusers.d/deepin-api.conf

%files -n golang-%name-devel
%go_path/src/%goipath

%changelog
* Thu Nov 03 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.32-alt1
- New version (5.5.32).
- Upstream:
  + fix: Repair the dde-open analysis part of url cannot get
  the scheme problem.

* Tue Sep 13 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.31-alt1
- New version (5.5.31).
- Packaged new golang modules for deepin-daemon.
- Updated internal golang modules.

* Thu Sep 01 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.30-alt3
- Packaged golang modules for deepin-daemon.

* Tue Aug 30 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.30-alt2
- Updated internal golang modules.

* Wed Aug 24 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.30-alt1
- New version (5.5.30).

* Mon Apr 11 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.12-alt1
- New version (5.5.12).

* Wed Feb 16 2022 Leontiy Volodin <lvol@altlinux.org> 5.5.5-alt1
- New version (5.5.5).

* Wed Feb 02 2022 Leontiy Volodin <lvol@altlinux.org> 5.4.32-alt1
- New version (5.4.32).
- Built with internal golang submodules.

* Tue May 18 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.6-alt1
- New version (5.4.6) with rpmgs script.

* Tue Apr 27 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.5-alt1
- New version (5.4.5) with rpmgs script.

* Thu Mar 04 2021 Leontiy Volodin <lvol@altlinux.org> 5.4.2-alt1
- New version (5.4.2) with rpmgs script.
- Fixed build with golang 1.16.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 5.3.2-alt1
- New version (5.3.2) with rpmgs script.

* Thu Dec 10 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.14-alt1
- New version (5.3.0.14) with rpmgs script.

* Mon Nov 30 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.13-alt1
- New version (5.3.0.13) with rpmgs script.

* Thu Nov 19 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.12-alt2
- Fixed BuildRequires.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.12-alt1
- New version (5.3.0.12) with rpmgs script.

* Fri Sep 11 2020 Leontiy Volodin <lvol@altlinux.org> 5.3.0.11-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
