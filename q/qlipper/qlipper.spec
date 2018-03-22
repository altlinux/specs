Name: qlipper
Version: 5.1.1
Release: alt2%ubt
License: GPLv3+
Summary: Lightweight clipboard history
Group: Graphical desktop/Other
Url: https://github.com/pvanek/qlipper
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
Source1: qlipper_ru.ts
Source2: qlipper-startup.desktop
Patch: qlipper-5.1.1-cmake-ru.patch
Patch1: qlipper-5.1.1-desktop-ru.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: qt5-tools-devel

%description
Lightweight clipboard history applet.

%prep
%setup
%patch -p1
%patch1 -p1

cp %SOURCE1 ts

%build
%cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=OFF -DUSE_SYSTEM_QTSA=ON ..
%cmake_build

%install
%cmakeinstall_std
desktop-file-validate %buildroot/%_desktopdir/%name.desktop
%find_lang %name --with-qt --without-mo

mkdir -p %buildroot%_sysconfdir/xdg/autostart
install -m 644 %SOURCE2 %buildroot%_sysconfdir/xdg/autostart/

%files -f %name.lang
%doc COPYING
%doc README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/128x128/apps/qlipper.png
%_sysconfdir/xdg/autostart/qlipper-startup.desktop

%changelog
* Thu Mar 22 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt2%ubt
- Added autostart

* Tue Mar 06 2018 Anton Midyukov <antohami@altlinux.org> 5.1.1-alt1%ubt
- Initial build for ALT (thanks Rosa Team for russian translation)
