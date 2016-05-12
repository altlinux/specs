Name: gnome-mplayer
Version: 1.0.9
Release: alt1.r2476.1

Summary: is a simple GUI for MPlayer
License: GPL
Group: Video

Url: http://kdekorte.googlepages.com/gnomemplayer
Source: %name-%version.tar

Requires: mplayer

BuildPreReq: rpm-build-gnome gnome-common

BuildRequires: intltool libGConf-devel libgtk+3-devel libgmlib-devel libgmtk-devel libgio-devel libdbus-glib-devel libXScrnSaver-devel libdconf-devel libalsa-devel libpulseaudio-devel libnotify-devel libgpod-devel libnautilus-devel libmusicbrainz3-devel libcurl-devel libnemo-devel mate-file-manager-devel

%description
A GTK3 interface to MPlayer. The power of MPlayer combined with a
friendly interface for your desktop; You can play all your multimedia
(audio, video, CD, DVDs, and VCDs, streams etc.), organize, sort and
create playlists, take screenshots while playing videos, be notified
about media changes. Full DVD and MKV chapter support, when supported
by Mplayer. Subtitle support with the ability to specify preferred audio
and subtitle languages if the media supports it. Support for cover art
retrieval from Amazon.com for audio media files with artist and/or album
information contained in the file.

The player can be used to play media on websites from your browser when
used with Gecko Mediaplayer and is the modern replacement for the
mplayerplug-in application.

Gnome MPlayer has a rich API that is exposed via DBus. Using DBus you
can control a single or multiple instances of GNOME MPlayer from a
single command.

Gnome MPlayer is not dependent on any Gnome libraries. However. the look
and feel of the application is based on the Gnome HIG. The main
dependencies are on GTK3, GLIB2 and DBUS.

%package -n nautilus-%name-properties-page
Summary: extension for nautilus
Group: Graphical desktop/GNOME
Requires: %name = %version-%release

%description -n nautilus-%name-properties-page
%summary

%package -n nemo-%name-properties-page
Summary: extension for nemo
Group: Graphical desktop/Other
Requires: %name = %version-%release

%description -n nemo-%name-properties-page
%summary

%package -n caja-%name-properties-page
Summary: extension for caja
Group: Graphical desktop/MATE
Requires: %name = %version-%release

%description -n caja-%name-properties-page
%summary

%prep
%setup -q
echo "NotShowIn=KDE;"  >>gnome-mplayer.desktop

%build
%autoreconf
%configure --enable-nautilus --enable-nemo --enable-caja
%make_build

%install
%makeinstall_std
rm -rf %buildroot%_docdir/%name

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/gnome-control-center/default-apps/%name.xml
%_datadir/glib-2.0/schemas/*.xml
%doc COPYING ChangeLog README DOCS/tech/dbus.txt DOCS/tech/plugin-interaction.txt DOCS/keyboard_shortcuts.txt

%files -n nautilus-%name-properties-page
%_libdir/nautilus/extensions-3.0/lib%name-properties-page.so*

%files -n nemo-%name-properties-page
%_libdir/nemo/extensions-3.0/lib%name-nemo-properties-page.so*

%files -n caja-%name-properties-page
%_libdir/caja/extensions-2.0/lib%name-caja-properties-page.so*

%changelog
* Thu May 12 2016 Sergey V Turchin <zerg@altlinux.org> 1.0.9-alt1.r2476.1
- NMU: hide menu item from KDE

* Sun Nov 01 2015 Vladimir Lettiev <crux@altlinux.ru> 1.0.9-alt1.r2476
- svn checkout r2476
- build nemo/caja extensions (Closes: #31418)

* Mon May 06 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.8-alt1
- New version 1.0.8

* Thu Nov 08 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.7-alt1
- New version 1.0.7

* Thu Jun 14 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.6-alt1
- New version 1.0.6
- Switched to Gtk3
- New dependencies: libpulseaudio, libgmtk, libgio, libdconf
- Updated description

* Wed Aug 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0.4-alt1
- New version 1.0.4

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0.2-alt1
- New version 1.0.2

* Tue Jan 11 2011 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt2
- Added russian translation to desktop file (Closes: #24890)

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt1
- New version 1.0.0

* Thu Mar 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.9.2-alt1
- New version 0.9.9.2
- russian translation merged upstream

* Tue Feb 09 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.9-alt1
- New version 0.9.9 (Closes: #22916)
- updated russian translation by Denis Koryavov <dkoryavov@>

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.8-alt1
- new version
- patch1 moved to upstream
- updated russian translation by Denis Koryavov <dkoryavov@> (Closes: #21773)

* Sun Jun 14 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.6-alt1
- new version
- fix build with --as-needed flag (gnome-mplayer issue #193)

* Tue Apr 07 2009 Vladimir Lettiev <crux@altlinux.ru> 0.9.5-alt1
- new version
- building of nautilus's plugin in a separate package

* Tue Sep 23 2008 Vladimir Lettiev <crux@altlinux.ru> 0.7.0-alt1
- Initial build for Sisyphus

