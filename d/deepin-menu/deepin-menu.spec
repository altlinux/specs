Name: deepin-menu
Version: 5.0.1
Release: alt4
Summary: Deepin menu service
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/linuxdeepin/deepin-menu
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz
Patch: deepin-menu-5.0.1-alt-dtk-5_6_22.patch

BuildRequires(pre): desktop-file-utils rpm-macros-dqt5
BuildRequires: libdtkwidget-devel deepin-qt-dbus-factory-devel dqt5-base-devel dqt5-multimedia-devel dqt5-x11extras-devel

%description
Deepin menu service for building beautiful menus.

%prep
%setup
%patch -p2

# Modify lib path to reflect the platform
sed -i 's|/usr/bin|/usr/libexec|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

%build
%qmake_dqt5 \
  CONFIG+=nostrip \
  DEFINES+=QT_NO_DEBUG_OUTPUT \
  QMAKE_RPATHDIR=%_dqt5_libdir
%make_build

%install
%makeinstall INSTALL_ROOT=%buildroot

%files
%doc README.md
%doc LICENSE
%_prefix/libexec/%name
%_datadir/dbus-1/services/com.deepin.menu.service

%changelog
* Mon May 27 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt4
- Built via separate qt5 instead system (ALT #48138).

* Thu Jan 18 2024 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt3
- Fixed build on dtk 5.6.22.

* Mon Oct 12 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt2
- Enabled debuginfo.
- Fixed path location.

* Tue Jul 21 2020 Leontiy Volodin <lvol@altlinux.org> 5.0.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
