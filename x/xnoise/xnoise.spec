Name: xnoise
Version: 0.2.1
Release: alt1

Summary: XNOISE is a media player for Gtk+ with a slick GUI, great speed and lots of features.
Group: Sound
License: GPLv2
Url: http://code.google.com/p/xnoise/
Packager: Alexey Morsov <swi@altlinux.ru>

Source: %name-%version.tar 

BuildPreReq: desktop-file-utils
BuildRequires: vala libgtk+3-devel libsqlite3-devel libunique-devel libtag-devel
BuildRequires: gstreamer-devel gst-plugins-devel libgdk-pixbuf-devel
BuildRequires: libsoup-devel libsoup-gnome-devel libxml2-devel libnotify4-devel
BuildRequires: intltool autogen gnome-common

%description
XNOISE is a media player for Gtk+ with a slick GUI, great speed and lots
of features.

Unlike Rhythmbox, Banshee or itunes, Xnoise uses a tracklist centric
design. The tracklist is a list of video or music tracks that are played
one by one without being removed (right side of window). This gives you
the possibility to queue any track in any order, regardless if they are
on the same album. Tracks or groups of tracks can be reordered at any
time via drag and drop.

The media browser (left side of the window) contains all available media
in a hierarchical tree structure of the available metadata. It is easy
to find a single track, artist or album by using this tree structure or
by just entering a search term. From the media browser, single or
multiple tracks, streams, albums, artists or videos can be dragged into
the tracklist to every position.

%prep
%setup -q

%build
#sed -i 's|2.67|2.65|' configure.ac
#./autogen.sh
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/*
#_includedir/%name/
#_pkgconfigdir/*
%_libdir/%name/
%_datadir/%name/
%_datadir/locale/*/LC_MESSAGES/*.mo
%_desktopdir/%name.desktop
%_liconsdir/*
%_niconsdir/*
%_datadir/icons/hicolor/256x256/apps/*
%_datadir/icons/hicolor/scalable/apps/*
%_datadir/icons/hicolor/scalable/status/*
%_man1dir/*

%changelog
* Sat Apr 28 2012 Alexey Morsov <swi@altlinux.ru> 0.2.1-alt1
- new version

* Fri Apr 06 2012 Alexey Morsov <swi@altlinux.ru> 0.2.0-alt1
- new version

* Wed Feb 22 2012 Alexey Morsov <swi@altlinux.ru> 0.1.31.990-alt1
- new version (pre-release)

* Mon Feb 20 2012 Alexey Morsov <swi@altlinux.ru> 0.1.31-alt1
- new version

* Tue May 31 2011 Alexey Morsov <swi@altlinux.ru> 0.1.23-alt2.hg793
- hg r793

* Fri May 27 2011 Alexey Morsov <swi@altlinux.ru> 0.1.23-alt2
- update russian translation

* Fri May 27 2011 Alexey Morsov <swi@altlinux.ru> 0.1.23-alt1
- initial build for sisyphus


