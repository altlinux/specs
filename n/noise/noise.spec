%define ver_major 0.4
%define gst_api_ver 1.0

Name: noise
%define xdg_name org.pantheon.%name
Version: %ver_major.2
Release: alt1

Summary: The official elementary music player
Group: Sound
License: GPLv3
Url: https://launchpad.net/noise

#VCS: https://github.com/elementary/music.git
Source: https://launchpad.net/%name/%{ver_major}.x/%version/+download/%name-%version.tar.xz

Requires: elementary-icon-theme
# gstreamer
Requires: gst-plugins-base%gst_api_ver
Requires: gst-plugins-good%gst_api_ver
Requires: gst-plugins-bad%gst_api_ver

# sync 0.4 uses sqlite via libgda
Requires: libgda5-sqlite

BuildRequires: intltool libappstream-glib-devel
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
# fix libdir
find ./ -name "CMakeLists.txt" -print0 | xargs -r0 subst 's|lib\/|${LIB_DESTINATION}/|g' --

%build
%cmake -DCMAKE_BUILD_TYPE:STRING="Release"
%cmake_build

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/plugins
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/icons/hicolor/*/apps/multimedia-audio-player.svg
%_datadir/metainfo/%xdg_name.appdata.xml

%files -n lib%name-core
%_libdir/lib%name-core.so.*

%files -n lib%name-core-devel
%_includedir/%name-core/
%_libdir/lib%name-core.so
%_pkgconfigdir/%name-core.pc

# TODO:
#    /usr/share/vala/vapi/%name-core.deps
#    /usr/share/vala/vapi/%name-core.vapi

%changelog
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

