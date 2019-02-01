# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%set_verify_elf_method relaxed

Name: screengrab
Version: 1.100
Release: alt1
Summary: ScreenGrab is a tool for geting screenshots
License: GPLv2
Source0: %name-%version.tar
Url: https://github.com/lxqt/screengrab
Group: Graphics

BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: /usr/bin/convert
BuildRequires: cmake
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Xdg)
BuildRequires: kf5-kwindowsystem-devel

Patch0: screengrab-1.99-CMakeLists.patch
Patch1: core-cli-upload-option.patch
Patch2: disable-cli-upload-option.patch

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

find . -type f | xargs chmod 644

# fix docs directories
sed -i 's|${CMAKE_INSTALL_FULL_DOCDIR}|${CMAKE_INSTALL_FULL_DOCDIR}-%version|g' CMakeLists.txt

%build
%cmake -DSG_GLOBALSHORTCUTS=OFF \
       -DUPDATE_TRANSLATIONS=ON

%cmake_build

%install
%cmakeinstall_std

# remove unneeded devel files
find %buildroot -name '*.so' -delete

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_liconsdir}
convert -resize 48x48 img/%name.png %buildroot%_liconsdir/%name.png
convert -resize 16x16 img/%name.png %buildroot%_miconsdir/%name.png

%files
%_bindir/%name
%_libdir/*.so.*
%_desktopdir/%name.desktop
%_docdir/%name-%version/
%_datadir/%name/
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
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
