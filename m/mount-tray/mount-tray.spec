Name: mount-tray
Version: 1.2.6
Release: alt1

Summary: udisks based removable device mounter
License: GPLv2
Group: System/Kernel and hardware
Url: https://github.com/h4tr3d/mount-tray
Packager: Evgenii Terechkov <evg@altlinux.org>

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch


# Automatically added by buildreq on Thu Dec 15 2022
# optimized out: gcc-c++ glibc-kernheaders-generic glibc-kernheaders-x86 libglvnd-devel libgpg-error libqt5-core libqt5-dbus libqt5-gui libqt5-widgets libstdc++-devel libudev-devel pkg-config python3 python3-base qt5-base-devel qt5-declarative-devel qt5-location-devel qt5-tools qt5-webchannel-devel sh4
BuildRequires: qt5-base-devel qt5-tools-devel

BuildRequires: gcc-c++ libudev-devel

BuildRequires(pre): rpm-macros-qt5


Requires: udisks2

%description
Small Qt-based tray application for mount and unmount removable
devices like USB storage or CD and DVD-ROM. It used udisks for mount
and unmount operations, udev for device detection and DBus for take
information about external mounting and unmounting (for ex from
pcmanfm).

%prep
%setup
%patch0 -p1

echo QMAKE_CXXFLAGS_RELEASE = %optflags >>  mount-tray.pro
echo QMAKE_CFLAGS_RELEASE = %optflags >>  mount-tray.pro

%build
export PATH=$PATH:%_qt5_bindir

%qmake_qt5 QMAKE_CFLAGS_RELEASE="%optflags" \
	QMAKE_CXXFLAGS_RELEASE="%optflags" mount-tray.pro

INSTALL_ROOT=%buildroot %qmake_qt5 mount-tray.pro

lrelease mount-tray.pro

%make_build



%install
INSTALL_ROOT=%buildroot %makeinstall_std

mkdir -p %buildroot%_datadir/%name/translations
cp translations/MountTray*.qm %buildroot%_datadir/%name/translations
install -d -m755 %buildroot%_liconsdir/

install -d -m 755 %buildroot%_bindir/

install -pDm 755 %name %buildroot%_bindir/%name
install -pDm 644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -pDm 644 images/%name.png %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%dir %_datadir/%name
%_datadir/%name/*
%doc COPY

%changelog
* Wed Dec 14 2022 Hihin Ruslan <ruslandh@altlinux.ru> 1.2.6-alt1
- Add russian translate

* Wed Jan 27 2021 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.5-alt7
- Use tray icon in png format (ALT #39566)
- Restore patch
- Remove [Build]Requires no longer needed

* Thu Jan 07 2021 Dmitriy Khanzhin <jinn@altlinux.org> 1.2.5-alt6
- Add application icon
- Add Requires: udisks2
- Remove patch
- Cleanup spec

* Wed Nov 13 2019 Nikita Ermakov <arei@altlinux.org> 1.2.5-alt5
- Enable Qt5 by default and make Qt4 optional.

* Sun Mar 26 2017 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt4
- Change Url: (ALT#33264)

* Tue Nov 17 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt3
- Add requires to libqt[45]-svg (ALT#31502)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt2
- Build with qt4 (qt5 is now optional)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt1
- 1.2.5-4-g8bb9e94
