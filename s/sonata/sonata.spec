Name: sonata
Version: 1.6.2.1
Release: alt2.1

Summary: Sonata is an elegant GTK+ music client for the Music Player Daemon (MPD).
Summary(ru_RU.UTF8): Sonata - элегантный клиент для Music Player Daemon (MPD), написаный на GTK+
License: GPL3+
Group: Sound
Url: http://sonata.berlios.de

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar
Source1: %{name}_16.png
Source2: %{name}_32.png
Source3: %{name}_48.png

BuildPreReq: desktop-file-utils
BuildRequires: python-devel >= 2.4 python-module-tagpy python-module-pygtk-devel >= 2.10.0 
BuildRequires: python-module-pygobject-devel
BuildRequires: python-module-dbus-devel
BuildRequires: libX11-devel gcc4.1-c++ libgtk+2-devel

Requires: python-module-tagpy python-module-elementtree python-module-ZSI python-module-python-mpd
Requires: python-module-dbus
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

%prep
%setup -q
subst "s|'share/sonata'|'share/doc/%name-%version'|g" setup.py

%build
python setup.py build

%install
python setup.py install --root=$RPM_BUILD_ROOT --optimize=2 --record=INSTALLED_FILES
%find_lang %name

# set up icons for 'not the only and mighty Gnome and KDE'
mkdir -p %buildroot%_niconsdir %buildroot%_liconsdir %buildroot%_miconsdir
install -m 644 %SOURCE1 %buildroot%_miconsdir/%name.png
install -m 644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -m 644 %SOURCE3 %buildroot%_liconsdir/%name.png

%files -f %name.lang
%doc README TODO TRANSLATORS CHANGELOG
%_bindir/*
%_desktopdir/*
%_datadir/locale/*/*/%name.mo
%_man1dir/*
%_pixmapsdir/%{name}*
%_defaultdocdir/%name-%version
%python_sitelibdir/*
%_niconsdir/%name.png
%_liconsdir/%name.png
%_miconsdir/%name.png


%changelog
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

