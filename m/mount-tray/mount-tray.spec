%def_enable qt4
%def_disable qt5

Summary: udisks based removable device mounter
Name: mount-tray
License: GPLv2
Version: 1.2.5
Release: alt4
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
Packager: Evgenii Terechkov <evg@altlinux.org>
Group: System/Kernel and hardware
Url: https://github.com/h4tr3d/mount-tray

BuildRequires: gcc-c++ libudev-devel
%if_enabled qt5
Requires: libqt5-svg
BuildRequires: qt5-base-devel
%endif
%if_enabled qt4
BuildRequires: libqt4-devel
Requires: libqt4-svg
%endif

%description
Small Qt-based tray application for mount and unmount removable
devices like USB storage or CD and DVD-ROM. It used udisks for mount
and unmount operations, udev for device detection and DBus for take
information about external mounting and unmounting (for ex from
pcmanfm).

%prep
%setup
%patch0 -p1

%build
%if_enabled qt5
%qmake_qt5
%endif
%if_enabled qt4
%qmake_qt4
%endif
%make_build STRIP=touch

%install
install -pDm 755 %name %buildroot%_bindir/%name
install -pDm 644 %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%_bindir/%name
%_desktopdir/%name.desktop
%doc COPY

%changelog
* Sun Mar 26 2017 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt4
- Change Url: (ALT#33264)

* Tue Nov 17 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt3
- Add requires to libqt[45]-svg (ALT#31502)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt2
- Build with qt4 (qt5 is now optional)

* Fri Jul  3 2015 Terechkov Evgenii <evg@altlinux.org> 1.2.5-alt1
- 1.2.5-4-g8bb9e94
