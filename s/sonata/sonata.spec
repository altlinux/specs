Name: sonata
Version: 1.7
Release: alt1.a2.git20140903.1

Summary: Sonata is an elegant GTK+ music client for the Music Player Daemon (MPD).
Summary(ru_RU.UTF8): Sonata - элегантный клиент для Music Player Daemon (MPD), написаный на GTK+
License: GPL3+
Group: Sound
Url: https://github.com/multani/sonata

Source: %name-%version.tar
BuildArch: noarch
Source1: %{name}_16.png
Source2: %{name}_32.png
Source3: %{name}_48.png

BuildRequires(pre): rpm-build-python3
BuildPreReq: desktop-file-utils python3-module-setuptools
BuildRequires: python3-devel python3-module-tagpy
BuildRequires: python3-module-pygobject-devel
BuildRequires: python3-module-dbus-devel
BuildRequires: libX11-devel gcc-c++ libgtk+3-devel

#Requires: python-module-tagpy python-module-elementtree python-module-ZSI python-module-python-mpd
#Requires: python-module-dbus
Requires: python3-module-%name = %EVR
Requires: dbus-tools-gui
Requires(post,postun): desktop-file-utils

%description
Sonata is an elegant GTK+ music client for the Music Player Daemon
(MPD).
- Expanded and collapsed views
- Automatic remote and local album art
- User-configurable columns
- Automatic fetching of lyrics
- Playlist and stream support
- Support for editing song tags
- Popup notification
- Playlist queue support
- Library and playlist searching
- Audioscrobbler (last.fm) support
- Multiple MPD profiles
- Keyboard friendly
- Support for multimedia keys
- Commandline control

%package -n python3-module-%name
Summary: Python module for %name
Group: Development/Python3
BuildArch: noarch
Conflicts: %name < %EVR

%description -n python3-module-%name
Sonata is an elegant GTK+ music client for the Music Player Daemon
(MPD).
- Expanded and collapsed views
- Automatic remote and local album art
- User-configurable columns
- Automatic fetching of lyrics
- Playlist and stream support
- Support for editing song tags
- Popup notification
- Playlist queue support
- Library and playlist searching
- Audioscrobbler (last.fm) support
- Multiple MPD profiles
- Keyboard friendly
- Support for multimedia keys
- Commandline control

This package contains Python module of Sonata.

%prep
%setup
subst "s|'share/sonata'|'share/doc/%name-%version'|g" setup.py

%build
%python3_build

%install
%python3_install
%find_lang %name

# set up icons for 'not the only and mighty Gnome and KDE'
mkdir -p %buildroot%_niconsdir %buildroot%_liconsdir %buildroot%_miconsdir
install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files -f %name.lang
%doc *.rst TODO TRANSLATORS CHANGELOG
%_bindir/*
%_desktopdir/*
%_datadir/locale/*/*/%name.mo
%_man1dir/*
#_pixmapsdir/%{name}*
%_defaultdocdir/%name-%version
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png

%files -n python3-module-%name
%python3_sitelibdir_noarch/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.7-alt1.a2.git20140903.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.a2.git20140903
- Version 1.7a2

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.2.1-alt2.1
- Rebuild with Python-2.7

* Thu Oct 14 2010 Alexey Morsov <swi@altlinux.ru> 1.6.2.1-alt2
- fix requires (Closes: 23885)

* Thu Sep 24 2009 Alexey Morsov <swi@altlinux.ru> 1.6.2.1-alt1
- new version

* Tue Apr 14 2009 Alexey Morsov <swi@altlinux.ru> 1.6.2-alt1
- new version

* Wed Apr 01 2009 Alexey Morsov <swi@altlinux.ru> 1.6.0-alt1
- new version
- clean spec (remove deprecated macros)

* Fri Sep 26 2008 Alexey Morsov <swi@altlinux.ru> 1.5.3-alt1
- new version

* Sat Jun 07 2008 Alexey Morsov <swi@altlinux.ru> 1.5.2-alt1
- new version

* Sat May 17 2008 Alexey Morsov <swi@altlinux.ru> 1.5.1-alt1
- new version
- fix iconsdir (add 16,32,48 sized icons) to correspond 
  with policy
- fix menus to correspond with policy
- enable dbus support

* Wed Apr 30 2008 Alexey Morsov <swi@altlinux.ru> 1.5-alt1
- 1.5
- Replace album view with genre view for library
- Display covers for albums in artist/genre views
- Allow setting artwork for streams
- Speed up mpd-related commandline arguments
- etc.

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 1.4-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 16 2008 Alexey Morsov <swi@altlinux.ru> 1.4-alt1
- Initial build for Sisyphus
- Integrate info window into main player
- Update to audioscrobbler protocol 1.2 and scrobbling bug fixes
- Implemented caching of scrobbles across client restarts

