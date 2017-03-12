Name: kazam
Summary: A screen-casting program created with design in mind
Version: 1.4.5
Release: alt2
Group: Video
License: GPLv3
Url: https://launchpad.net/kazam
Packager: Anton Midyukov <antohami@altlinux.org>
Source: https://launchpad.net/kazam/unstable/%version/+download/%name-%version.tar.gz
Patch0:	kazam-1.4.5-force-gtk-csd.patch
Patch1: kazam-1.4.5-configparser_api_changes.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-gir
BuildRequires: python3-devel python3-module-distutils-extra intltool

%description
Kazam is a simple screen recording program that will capture
the content of your screen and record a video file that can be played
by any video player that supports VP8/WebM video format.

Optionally you can record sound from any sound input device
that is supported and visible by PulseAudio.

%prep
%setup
%patch0 -p1
%patch1 -p1
sed -i s,"DISTRO='Ubuntu'","DISTRO='%vendor'",g kazam/version.py

%build
%python3_build

%install
%python3_install
cp -r build/share/applications %buildroot/%_datadir
mkdir -p %buildroot/%_iconsdir/hicolor
cp -r data/icons/*x* %buildroot/%_iconsdir/hicolor
mkdir -p %buildroot/%_datadir/locale
cp -r build/mo/* %buildroot/%_datadir/locale
%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING COPYING.LGPL README
%_bindir/%name
%python3_sitelibdir/%name
%python3_sitelibdir/*.egg-info
%_datadir/%name
%_iconsdir/gnome/scalable/apps/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*

%changelog
* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 1.4.5-alt2
- Added buildrequires rpm-build-gir.

* Wed Aug 24 2016 Anton Midyukov <antohami@altlinux.org> 1.4.5-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32413).
