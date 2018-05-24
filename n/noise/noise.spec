%def_enable snapshot
%define ver_major 0.4
%define gst_api_ver 1.0
# [ lastfm', 'audioplayer', 'cdrom', 'ipod' ]
%define plugins [ 'audioplayer', 'cdrom', 'ipod' ]

Name: noise
%define xdg_name org.pantheon.%name
%define rdnn_name io.elementary.music
Version: %ver_major.2
Release: alt2

Summary: The official elementary music player
Group: Sound
License: GPLv3
Url: https://launchpad.net/noise

%if_disabled snapshot
Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz
%else
#VCS: https://github.com/elementary/music.git
Source: %name-%version.tar
%endif

Requires: elementary-icon-theme
# gstreamer
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver

# sync 0.4 uses sqlite via libgda
Requires: libgda5-sqlite

BuildRequires(pre): meson
BuildRequires: libappstream-glib-devel
BuildRequires: cmake gcc-c++ vala-tools libsqlheavy-devel libsqlite3-devel libgee0.8-devel
BuildRequires: libxml2-devel libgtk+3-devel libpeas-devel
BuildRequires: libgranite-devel gst-plugins%gst_api_ver-devel
BuildRequires: libsoup-devel libjson-glib-devel libpixman-devel libtag-devel
BuildRequires: libXdmcp-devel libnotify-devel libpng-devel
BuildRequires: libXdamage-devel libgranite-vala libXxf86vm-devel
BuildRequires: libharfbuzz-devel libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libXcomposite-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel at-spi2-atk-devel
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
%setup

%build
%meson -Dplugins="%plugins"
%meson_build

%install
%meson_install

%find_lang --output=%name.lang %rdnn_name

%files -f %name.lang
%_bindir/%rdnn_name
%_libdir/%rdnn_name/plugins/
%_desktopdir/%rdnn_name.desktop
#%_datadir/%rdnn_name/
%_datadir/glib-2.0/schemas/%rdnn_name.gschema.xml
%_datadir/icons/hicolor/*/apps/multimedia-audio-player.svg
%_datadir/metainfo/%rdnn_name.appdata.xml

%files -n lib%name-core
%_libdir/lib%rdnn_name-core.so.*

%files -n lib%name-core-devel
%_includedir/%rdnn_name-core.h
%_libdir/lib%rdnn_name-core.so
%_pkgconfigdir/%rdnn_name-core.pc
%_vapidir/%rdnn_name-core.deps
%_vapidir/%rdnn_name-core.vapi

%changelog
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

