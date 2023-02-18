# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

#set_verify_elf_method relaxed

Name: screengrab
Version: 2.5.0
Release: alt1

Summary: ScreenGrab is a tool for geting screenshots
License: GPLv2
Group: Graphics

Url: https://github.com/lxqt/screengrab
Source: %name-%version.tar
Patch0: screengrab-link.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: libqtxdg-devel
# To generate screengrab.desktop
BuildRequires: perl-YAML-LibYAML-API

%description
ScreenGrab -- program getting screenshots working in Linux and Windows.
The program uses Qt5 and is independent from any desktop environment.
Main features:
    * grab screenshot of desktop
    * working on Window and Linux operating systems
    * save screenshots in PNG and JPEG format
    * grab screenshot with delay (1 - 90 sec)
    * hide its window
    * minimize to system tray and work from at (tray menu)

%prep
%setup
%autopatch -p1

find -type f -print0 | xargs -r0 chmod 644 --

# fix docs directories
sed -i 's|${CMAKE_INSTALL_FULL_DOCDIR}|${CMAKE_INSTALL_FULL_DOCDIR}-%version|g' CMakeLists.txt

%ifarch %e2k
%add_optflags -std=c++11
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_docdir/%name-%version/
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/screengrab.svg
%_datadir/metainfo/screengrab.metainfo.xml

%changelog
* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 2.5.0-alt1
- new version 2.5.0

* Mon Apr 18 2022 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- new version 2.4.0

* Sat Nov 06 2021 Anton Midyukov <antohami@altlinux.org> 2.3.0-alt1
- new version 2.3.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Mon Mar 23 2020 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- new version 2.0.0

* Thu Jun 06 2019 Michael Shigorin <mike@altlinux.org> 1.101-alt1.1
- E2K: explicit -std=c++11
- minor spec cleanup/fixup

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 1.101-alt1
- new version 1.101

* Sun Jan 27 2019 Anton Midyukov <antohami@altlinux.org> 1.100-alt1
- new version 1.100

* Thu Jul 26 2018 Anton Midyukov <antohami@altlinux.org> 1.99-alt2
- Fix update conflict
- Update buildrequires
- Fix library location

* Sun Jul 22 2018 Motsyo Gennadi <drool@altlinux.ru> 1.99-alt1
- 1.99 (#altbug 35169)

* Sun Jan 12 2014 Motsyo Gennadi <drool@altlinux.ru> 1.0-alt1
- 1.0

* Thu Jun 14 2012 Motsyo Gennadi <drool@altlinux.ru> 0.9.92-alt1.20120505
- git snapshot 20120505

* Tue Jul 05 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.81-alt1
- 0.9.81

* Sun Jan 23 2011 Motsyo Gennadi <drool@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Nov 15 2010 Motsyo Gennadi <drool@altlinux.ru> 0.9-alt1
- 0.9

* Fri May 14 2010 Motsyo Gennadi <drool@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Sat Mar 27 2010 Motsyo Gennadi <drool@altlinux.ru> 0.8-alt1
- 0.8

* Thu Mar 25 2010 Motsyo Gennadi <drool@altlinux.ru> 0.6.2-alt1
- initial build for ALT Linux
