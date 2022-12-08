%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: xplayer
Version: 2.4.4
Release: alt1
Summary: Xplayer is a generic media player.
Group: Video
License: %gpl2only
URL: https://github.com/linuxmint/xplayer

Source: %name-%version.tar
Patch: %name-%version.patch

Provides: %name-backend = %version %name-backend-gstreamer = %version %name-backend-xine = %version

Requires: lib%name = %version-%release
Requires: %name-video-thumbnailer = %version-%release
Requires: dconf gnome-icon-theme gstreamer%gst_api_ver

BuildRequires(pre): rpm-build-licenses rpm-build-python3
BuildRequires: gcc-c++ gnome-common gsettings-desktop-schemas-devel gst-plugins-bad1.0 gst-plugins-base1.0
BuildRequires: gst-plugins-good1.0 gstreamer1.0-utils gtk-doc intltool itstool libSM-devel
BuildRequires: libclutter-gst3.0-devel libclutter-gtk3-devel libgrilo-devel libgtk+3-gir-devel
BuildRequires: liblirc-devel libpeas-devel libxapps-devel libxplayer-plparser-devel
BuildRequires: libxplayer-plparser-gir-devel libzeitgeist2.0-devel python3-dev
BuildRequires: python3-module-pygobject3-devel yelp-tools

%description
Xplayer is a generic media player. It features a simple playlist, a full-screen
mode, seek and volume controls, as well as a pretty complete keyboard navigation.

%package -n lib%name
Summary: Xplayer Library
License: LGPLv2+
Group: System/Libraries

%description -n lib%name
This package provides shared library for Xplayer movie player.

%package -n lib%name-devel
Summary: Development files for Xplayer Library
License: LGPLv2+
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides files required to develop programs that use
Xplayer library.

%package -n lib%name-gir
Summary: GObject introspection data for the Xplayer library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the Xplayer library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the Xplayer library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the Xplayer library

%package plugins
Summary: default plugins for Xplayer
Group: Video
BuildArch: noarch
Requires: %name = %version-%release %name-plugin-gromit = %version-%release %name-plugin-ontop = %version-%release %name-plugin-screensaver = %version-%release
Requires: %name-plugin-skipto = %version-%release %name-plugin-properties = %version-%release %name-plugin-media-player-keys = %version-%release
Requires: %name-plugin-python-console = %version-%release %name-plugin-opensubtitles = %version-%release %name-plugin-grilo = %version-%release

%description plugins
A default plugins for Xplayer:
	gromit
	ontop
	screensaver
	skipto
	properties
	media-player-keys
	pythonconsole
	opensubtitles
	grilo

%package plugin-apple-trailers
Summary: Apple Trailers
Group: Video
Requires: %name = %version-%release

%description plugin-apple-trailers
Sets the user agent for the Apple Trailers site

%package plugin-autoload-subtitles
Summary: Autoload Subtitles
Group: Video
Requires: %name = %version-%release

%description plugin-autoload-subtitles
Autoloads text subtitles

%package plugin-chapters
Summary: Chapters
Group: Video
Requires: %name = %version-%release

%description plugin-chapters
Support chapter markers in movies

%package plugin-im-status
Summary: Instant Messenger Status
Group: Video
Requires: %name = %version-%release

%description plugin-im-status
Set your Instant Messenger status to away when a movie is playing

%package plugin-media-player-keys
Summary: Media Player Keys
Group: Video
Requires: %name = %version-%release

%description plugin-media-player-keys
Support additional media player keys

%package plugin-opensubtitles
Summary: Subtitle Downloader
Group: Video
Requires: %name = %version-%release libxplayer-plparser-gir

%description plugin-opensubtitles
Look for subtitles for the currently playing movie

%package plugin-properties
Summary: Movie Properties
Group: Video
Requires: %name = %version-%release

%description plugin-properties
Adds movie properties to the sidebar

%package plugin-recent
Summary: Recent files
Group: Video
Requires: %name = %version-%release

%description plugin-recent
Adds files that have been played to recent files

%package plugin-screensaver
Summary: Screen Saver
Group: Video
Requires: %name = %version-%release

%description plugin-screensaver
Deactivates the screen saver when a movie is playing

%package plugin-screenshot
Summary: Screenshot
Group: Video
Requires: %name = %version-%release

%description plugin-screenshot
Allows screenshots and galleries to be taken of videos

%package plugin-skipto
Summary: Skip To
Group: Video
Requires: %name = %version-%release

%description plugin-skipto
Provides the "Skip to" dialog

%package plugin-vimeo
Summary: Vimeo
Group: Video
Requires: %name = %version-%release

%description plugin-vimeo
Sets the user agent for the Vimeo site

%package plugin-ontop
Summary: Always On Top
Group: Video
Requires: %name = %version-%release

%description plugin-ontop
Keep the main window on top when playing a movie

%package plugin-mpris
Summary: MPRIS Support
Group: Video
Requires: %name = %version-%release dleyna-server libxplayer-plparser-gir

%description plugin-mpris
This plugin enables MPRIS support over DBUS

%package plugin-grilo
Summary: Grilo Browser
Group: Video
Requires: %name = %version-%release grilo-plugins

%description plugin-grilo
A plugin to let you browse media content from various sources

%package plugin-python-console
Summary: Python Console
Group: Video
Requires: %name = %version-%release libxplayer-plparser-gir

%description plugin-python-console
Interactive Python console

%package plugin-lirc
Summary: LIRC (Infrared remote) plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Obsoletes: %name-plugins-lirc < %version-%release

%description plugin-lirc
A plugin to add LIRC (Infrared remote) support to Xplayer.

%package plugin-rotation
Summary: Rotation plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Obsoletes: %name-plugins-rotation < %version-%release

%description plugin-rotation
A plugin to allow videos to be rotated if they're in the wrong orientation.

%package plugin-zeitgeist
Summary: Zeitgeist plugin for Xplayer
Group: Video
Requires: %name = %version-%release zeitgeist
Obsoletes: %name-plugins-zeitgeist < %version-%release

%description plugin-zeitgeist
A plugin sending events to Zeitgeist

%package plugin-gromit
Summary: Gromit Annotations plugin for xplayer
Group: Video
Requires: %name = %version-%release gromit
Obsoletes: %name-plugins-gromit < %version-%release

%description plugin-gromit
This package contains presentation helper to make annotations on screen via Gromit

%package plugin-brasero
Summary: Video disc recorder plugin for Xplayer
Group: Video
Requires: %name = %version-%release brasero
Obsoletes: %name-plugins-brasero < %version-%release

%description plugin-brasero
This package contains plugin that allow record (S)VCDs or video DVDs with Brasero

%package video-thumbnailer
Summary: Xplayer video thumbnailer
Group: Video
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: iso-codes

%description video-thumbnailer
This package provides a video thumbnailer from Xplayer package that can be
used by other applications like filemanagers.

%add_python3_path %_libdir/%name/plugins

%prep
%setup -q
%patch -p1

%build
export ac_cv_path_PYLINT=%_bindir/pylint.py3
%autoreconf
%configure \
	--disable-schemas-compile \
	--enable-python \
	--enable-vala \
	--disable-static \
	--disable-Werror \
	--enable-introspection

%make_build

%install
%make DESTDIR=%buildroot install
find %buildroot%_libdir -name \*.la -delete

%find_lang --with-gnome %name

%files -f %name.lang
%doc AUTHORS NEWS README TODO
%_bindir/*
%exclude %_bindir/%name-video-thumbnailer
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libexecdir/%name/%name-bugreport.py
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.png
%_iconsdir/hicolor/*/*/*.svg
%_datadir/%name
%_man1dir/*.1*
%exclude %_man1dir/%name-video-thumbnailer.1*
%_datadir/glib-2.0/schemas/org.x.player.gschema.xml
%_datadir/glib-2.0/schemas/org.x.player.enums.xml

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%files plugins

%files plugin-screenshot
%_libdir/%name/plugins/screenshot

%files plugin-media-player-keys
%_libdir/%name/plugins/media-player-keys

%files plugin-properties
%_libdir/%name/plugins/properties

%files plugin-screensaver
%_libdir/%name/plugins/screensaver

%files plugin-skipto
%_libdir/%name/plugins/skipto

%files plugin-im-status
%_libdir/%name/plugins/im-status

%files plugin-apple-trailers
%_libdir/%name/plugins/apple-trailers

%files plugin-autoload-subtitles
%_libdir/%name/plugins/autoload-subtitles

%files plugin-recent
%_libdir/%name/plugins/recent

%files plugin-vimeo
%_libdir/%name/plugins/vimeo

%files plugin-chapters
%_libdir/%name/plugins/chapters

%files plugin-opensubtitles
%_libdir/%name/plugins/opensubtitles
%_datadir/glib-2.0/schemas/org.x.player.plugins.opensubtitles.gschema.xml

%files plugin-ontop
%_libdir/%name/plugins/ontop

%files plugin-python-console
%_libdir/%name/plugins/pythonconsole
%_datadir/glib-2.0/schemas/org.x.player.plugins.pythonconsole.gschema.xml

%ifnarch aarch64
%files plugin-mpris
%_libdir/%name/plugins/dbus
%endif

%files plugin-grilo
%_libdir/%name/plugins/grilo

%files plugin-lirc
%_libdir/%name/plugins/lirc

%files plugin-rotation
%_libdir/%name/plugins/rotation

%files plugin-zeitgeist
%_libdir/%name/plugins/zeitgeist-dp

%files plugin-gromit
%_libdir/%name/plugins/gromit

%files plugin-brasero
%_libdir/%name/plugins/brasero-disc-recorder

%files video-thumbnailer
%_bindir/%name-video-thumbnailer
%_datadir/thumbnailers/%name.thumbnailer
%_man1dir/%name-video-thumbnailer.1.*

%changelog
* Thu Dec 08 2022 Valery Inozemtsev <shrek@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Sun May 30 2021 Valery Inozemtsev <shrek@altlinux.ru> 2.4.0-alt1
- 2.4.0 (closes: #40103)

* Thu Feb 27 2020 Valery Inozemtsev <shrek@altlinux.ru> 2.2.5-alt2
- split plugins

* Wed Feb 19 2020 Valery Inozemtsev <shrek@altlinux.ru> 2.2.5-alt1
- 2.2.5

* Wed Jul 31 2019 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Wed Jun 26 2019 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- fix build on beekeeper machines

* Mon Jan 28 2019 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1.1
- fix build on beekeeper machines

* Wed Dec 26 2018 Vladimir Didenko <cow@altlinux.org> 2.0.2-alt1
- 2.0.2

* Wed Dec 5 2018 Vladimir Didenko <cow@altlinux.org> 2.0.1-alt1
- 2.0.1

* Wed Nov 21 2018 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Jul 4 2018 Vladimir Didenko <cow@altlinux.org> 1.8.3-alt1
- 1.8.3

* Wed Jun 13 2018 Vladimir Didenko <cow@altlinux.org> 1.8.1-alt1
- 1.8.1

* Mon May 7 2018 Vladimir Didenko <cow@altlinux.org> 1.8.0-alt1
- 1.8.0

* Thu Nov 23 2017 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Jul 4 2017 Vladimir Didenko <cow@altlinux.org> 1.4.3-alt1
- 1.4.3

* Mon Jun 5 2017 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri May 19 2017 Vladimir Didenko <cow@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Dec 14 2016 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Sun Nov 13 2016 Vladimir Didenko <cow@altlinux.org> 1.2.1-alt1
- 1.2.1-1-gbf68bda

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.7-alt1
- 1.0.7-4-g772ae2e

* Thu Jun 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.6-alt1
- New version

* Thu May 26 2016 Vladimir Didenko <cow@altlinux.org> 1.0.5-alt1
- New version

* Tue May 17 2016 Vladimir Didenko <cow@altlinux.org> 1.0.4-alt1
- New version

* Wed Mar 2 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus
