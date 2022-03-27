%def_enable snapshot
%define ver_major 5.1
%define gst_api_ver 1.0
# [ lastfm', 'audioplayer', 'cdrom', 'ipod' ]
%define plugins [ 'audioplayer', 'cdrom', 'ipod' ]
%define handy_api_ver 1

Name: noise
%define _name music
%define xdg_name org.pantheon.%name
%define rdn_name io.elementary.%_name
Version: %ver_major.1
Release: alt2

Summary: The official elementary music player
Group: Sound
License: GPL-3.0
Url: https://launchpad.net/noise

%if_disabled snapshot
Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz
%else
#VCS: https://github.com/elementary/music.git
Source: %_name-%version.tar
%endif

Provides: %rdn_name = %version-%release

Requires: elementary-icon-theme
# gstreamer
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver

# sync 0.4 uses sqlite via libgda
Requires: libgda5-sqlite

BuildRequires(pre): meson
BuildRequires: libappstream-glib-devel
BuildRequires: vala-tools libsqlite3-devel libgee0.8-devel
BuildRequires: libxml2-devel libgtk+3-devel libpeas-devel
BuildRequires: libgranite-devel gst-plugins%gst_api_ver-devel
BuildRequires: pkgconfig(libhandy-%handy_api_ver)
BuildRequires: libsoup-devel libjson-glib-devel libpixman-devel libtag-devel
BuildRequires: libnotify-devel libgranite-vala libharfbuzz-devel
BuildRequires: libzeitgeist2.0-devel libgpod-devel libusbmuxd-devel
BuildRequires: gobject-introspection-devel
# for MPRIS plugin
#BuildRequires: libdbusmenu-devel libindicator-devel (pkgconfig(indicate-0.7))
# sync 0.4
BuildRequires: libgda5-devel
# for lastfm plugin
#BuildRequires: libaccounts-glib-devel libgsignon-glib-devel

%description
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

%package -n lib%name-core
Summary: Simple, fast, and good looking music player (core library)
Group: System/Libraries

%description -n lib%name-core
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

This package contains the shared library.

%package -n lib%name-core-devel
Summary: Simple, fast, and good looking music player (development files)
Group: Development/C
Requires: lib%name-core = %version-%release

%description -n lib%name-core-devel
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

This package contains the development files.

%prep
%setup -n %_name-%version

%build
%meson -Dplugins="%plugins"
%meson_build

%install
%meson_install

%find_lang --output=%name.lang %rdn_name

%files -f %name.lang
%_bindir/%rdn_name
%_libdir/%rdn_name/plugins/
%_desktopdir/%rdn_name.desktop
#%_datadir/%rdn_name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%rdn_name.svg
%_datadir/metainfo/%rdn_name.appdata.xml

%files -n lib%name-core
%_libdir/lib%rdn_name-core.so.*

%files -n lib%name-core-devel
%_includedir/%rdn_name-core.h
%_libdir/lib%rdn_name-core.so
%_pkgconfigdir/%rdn_name-core.pc
%_vapidir/%rdn_name-core.deps
%_vapidir/%rdn_name-core.vapi

%changelog
* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 5.1.1-alt2
- updated to 5.1.1-148-g4d974d7f (fixed build with meson >= 0.61)

* Mon Jul 19 2021 Yuri N. Sedunov <aris@altlinux.org> 5.1.1-alt1
- updated to 5.1.1-16-g7667b8e5

* Sun Mar 28 2021 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt3
- updated to 5.0.5-105-g645684a5
- built against libgranite.so.6

* Sat Oct 31 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt2
- updated to 5.0.5-63-g6a112438

* Tue Mar 31 2020 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt1
- updated to 5.0.5-7-gc2e1c535

* Thu Apr 25 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.4-alt1
- updated to 5.0.4-4-gb759f4ba

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.3-alt1
- updated to 5.0.3-12-g80bcdfda

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 5.0.2-alt1
- updated to 5.0.2-5-gc49dd991

* Mon Jun 25 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt3
- updated to 0.4.2-439-g64bccda
- built against libgranite.so.5

* Thu May 24 2018 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt2
- updated to 0.4.2-382-g7a90c49

* Thu Nov 30 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

* Wed Aug 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- 0.4.1

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.3-alt1
- 0.4.0.3

* Tue Jan 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.4.0.2-alt1
- 0.4.0.2

* Wed Sep 09 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt2
- fix build on x86_64

* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt1
- build for Sisyphus

