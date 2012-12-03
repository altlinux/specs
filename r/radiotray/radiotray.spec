%define		_giconsdir %_iconsdir/hicolor/128x128/apps

Name:		radiotray
Version:	0.7.3
Release:	alt1
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Summary:	Radio Tray is an online radio streaming player that runs on a Linux system tray
License:	GPLv1
Group:		Sound
URL:		http://radiotray.sourceforge.net/
Source0:	%name-%version.tar.gz

BuildArch: noarch

BuildRequires: /usr/bin/convert python-module-pyxdg python-devel

%description
Radio Tray is an online radio streaming player that runs on a Linux system tray.
Its goal is to have the minimum interface possible, making it very straightforward to use. 
Radio Tray is not a full featured music player, there are plenty of excellent music players already.
However, there was a need for a simple application with minimal interface just to listen to online radios.
And that's the sole purpose of Radio Tray.

Features
- plays most media formats (based on gstreamer libraries)
- drag & drop bookmarks support
- easy to use
- supports PLS playlist format (Shoutcast/Icecast)
- supports M3U playlist format
- supports ASX, WAX and WVX playlist format
- extensible by plugins

%prep
%setup

%build
python setup.py bdist

%install
mkdir %buildroot
tar -xzf dist/%name-*.tar.gz -C %buildroot

# Icons
%__mkdir -p %buildroot/{%_miconsdir,%_niconsdir,%_liconsdir,%_giconsdir}
install -m 0644 data/images/%name.png %buildroot%_giconsdir/%name.png
convert -resize 48x48 data/images/%name.png %buildroot%_liconsdir/%name.png
convert -resize 32x32 data/images/%name.png %buildroot%_niconsdir/%name.png
convert -resize 16x16 data/images/%name.png %buildroot%_miconsdir/%name.png

%find_lang %name

%files -f %name.lang
%doc AUTHORS CONTRIBUTORS COPYING NEWS PKG-INFO README
%_bindir/%name
%_datadir/%name
%_desktopdir/*
%python_sitelibdir/%name
%python_sitelibdir/*-info
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_giconsdir/%name.png

%changelog
* Mon Dec 03 2012 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt1
- build for Sisyphus

* Sun Dec 02 2012 Motsyo Gennadi <drool@altlinux.ru> 0.7.3-alt0.M60T.1
- initial build for t6 (thank to Serg A. Kotlyarov)
