%define _unpackaged_files_terminate_build 1
%define rname screenpen

Name: screenpen-python
Version: 0.3.3
Release: alt1

Summary: Screen annotation software which allows drawing directly on the screen

License: GPL-3.0-only
Group: Graphics
Url: https://github.com/rsusik/screenpen
VCS: https://github.com/rsusik/screenpen

# Source-url: https://github.com/rsusik/screenpen/archive/504907dd197a2382ff379380c424c84f94a3284a.tar.gz
Source: %name-%version.tar
Source1: %name.desktop
Source2: %name.svg
Source3: %name.sh
Patch: %name-no-pkg_resources.patch

BuildArch: noarch

%add_python3_path %_datadir/%name
%add_findprov_skiplist %_datadir/%name/*

BuildRequires(pre): rpm-build-python3

# PyQt5 is imported inside try/except and so is not detected automatically
Requires: python3-module-PyQt5

%description
ScreenPen is an open source multiplatform alternative to Epic Pen: it
allows drawing lines, rectangles and charts (using matplotlib) directly
on the screen. A transparent background is used when the window system
supports it, otherwise a screenshot is taken and drawn on.

This package is the Python/Qt implementation by Robert Susik. It is
installed as screenpen-python and does not conflict with the C++ screenpen.

%prep
%setup
%patch -p1

%build

%install
mkdir -p %buildroot%_datadir/%name
cp -a %rname %buildroot%_datadir/%name/
install -D -m755 %SOURCE3 %buildroot%_bindir/%name
install -D -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -D -m644 %SOURCE2 %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg

%files
%doc README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.svg

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 0.3.3-alt1
- initial build for Sisyphus

