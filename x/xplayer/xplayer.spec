%define gst_api_ver 1.0
%define _libexecdir %_prefix/libexec

Name: xplayer
Version: 2.2.5
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
Requires: dconf gnome-icon-theme
Requires: gstreamer%gst_api_ver
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver
Requires: gst-plugins-ugly%gst_api_ver
Requires: gst-libav
Requires: iso-codes

BuildRequires(pre): rpm-build-licenses
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
Requires: %name = %version-%release
Requires: libxplayer-plparser-gir grilo-plugins
%ifnarch aarch64
Requires: dleyna-server
%endif

%description plugins
A default plugins for Xplayer:
	skipto
	pythonconsole
	opensubtitles
	im-status
	apple-trailers
	autoload-subtitles
	recent
	vimeo
	chapters
	grilo

%package plugins-lirc
Summary: LIRC (Infrared remote) plugin for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins-lirc
A plugin to add LIRC (Infrared remote) support to Xplayer.

%package plugins-rotation
Summary: Rotation plugin for Xplayer
Group: Video
Requires: %name = %version-%release

%description plugins-rotation
A plugin to allow videos to be rotated if they're in the wrong orientation.

%package plugins-zeitgeist
Summary: Zeitgeist plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Requires: zeitgeist

%description plugins-zeitgeist
A plugin sending events to Zeitgeist

%package plugins-gromit
Summary: Gromit Annotations plugin for xplayer
Group: Video
Requires: %name = %version-%release
Requires: gromit

%description plugins-gromit
This package contains presentation helper to make annotations on screen via Gromit

%package plugins-brasero
Summary: Video disc recorder plugin for Xplayer
Group: Video
Requires: %name = %version-%release
Requires: brasero

%description plugins-brasero
This package contains plugin that allow record (S)VCDs or video DVDs
with Brasero

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
%_libdir/%name/plugins/screenshot
%_libdir/%name/plugins/media-player-keys
%_libdir/%name/plugins/properties
%_libdir/%name/plugins/ontop
%_libdir/%name/plugins/screensaver
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
%ifnarch aarch64
%_libdir/%name/plugins/dbus
%endif
%_libdir/%name/plugins/skipto
%_libdir/%name/plugins/pythonconsole
%_libdir/%name/plugins/opensubtitles
%_libdir/%name/plugins/im-status
%_libdir/%name/plugins/apple-trailers
%_libdir/%name/plugins/autoload-subtitles
%_libdir/%name/plugins/recent
%_libdir/%name/plugins/vimeo
%_libdir/%name/plugins/chapters
%_libdir/%name/plugins/grilo
%_datadir/glib-2.0/schemas/org.x.player.plugins.opensubtitles.gschema.xml
%_datadir/glib-2.0/schemas/org.x.player.plugins.pythonconsole.gschema.xml

%files plugins-lirc
%_libdir/%name/plugins/lirc

%files plugins-rotation
%_libdir/%name/plugins/rotation

%files plugins-zeitgeist
%_libdir/%name/plugins/zeitgeist-dp

%files plugins-gromit
%_libdir/%name/plugins/gromit

%files plugins-brasero
%_libdir/%name/plugins/brasero-disc-recorder

%files video-thumbnailer
%_bindir/%name-video-thumbnailer
%_datadir/thumbnailers/%name.thumbnailer
%_man1dir/%name-video-thumbnailer.1.*

%changelog
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
