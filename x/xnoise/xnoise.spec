Name: xnoise
Version: 0.2.21
Release: alt1

Summary: XNOISE is a media player for Gtk+ with a slick GUI, great speed and lots of features
Group: Sound
License: GPLv2+
Url: http://www.xnoise-media-player.com/
Source0: https://bitbucket.org/shuerhaaken/xnoise/downloads/xnoise-%version.tar.gz

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildPreReq: desktop-file-utils


BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(libtaginfo_c)

BuildRequires: vala libgtk+3-devel libsqlite3-devel libunique-devel libtag-devel
BuildRequires: gstreamer-devel gst-plugins-devel libgdk-pixbuf-devel
BuildRequires: libsoup-devel libsoup-gnome-devel libxml2-devel libnotify4-devel
BuildRequires: intltool autogen gnome-common chrpath gcc-c++

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

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
desktop-file-validate $RPM_BUILD_ROOT/%_datadir/applications/xnoise.desktop
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
# remove invalid locale file
rm -rf $RPM_BUILD_ROOT/usr/share/locale/default

# Remove RPATHs
chrpath --delete $RPM_BUILD_ROOT%_bindir/xnoise{,_image_extractor_service}
chrpath --delete $RPM_BUILD_ROOT%_libdir/libxnoise.so.0.0.0

# Remove Ubuntu-specific icons
rm -rf $RPM_BUILD_ROOT%_datadir/icons/ubuntu-mono-*

%find_lang %name

%files -f %name.lang
%doc AUTHORS COPYING NEWS README
%_bindir/xnoise
%_bindir/xnoise_image_extractor_service
%_libdir/lib*.so.*
%_libdir/xnoise
%_mandir/man1/xnoise.1*
%_datadir/xnoise
%_datadir/dbus-1/services/org.gtk.xnoise.*.service
%_datadir/applications/xnoise.desktop
%_datadir/icons/hicolor/*/*/xn*

%files devel
%_includedir/xnoise
%_libdir/lib*.so
%_libdir/pkgconfig/xnoise-1.0.pc
# make package own the vala API dir:
# xnoise plugins don't have to be written in vala
#dir %_datadir/vala
#dir %_datadir/vala/vapi
%_datadir/vala/vapi/xnoise-1.0.*

%changelog
* Sun Mar 30 2014 Ilya Mashkin <oddity@altlinux.ru> 0.2.21-alt1
- 0.2.21
- fix url
- sync spec with FC

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

