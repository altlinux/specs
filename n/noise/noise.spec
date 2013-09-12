Name: noise
Version: 0.2.4
Release: alt2

Summary: Simple, fast, and good looking music player
Group: Sound
License: GPLv3

Url: https://launchpad.net/noise

Source0: %name-%version.tgz

Packager: Igor Zubkov <icesik@altlinux.org>

BuildRequires: cmake libsqlheavy-devel libsqlite3-devel libgee-devel
BuildRequires: libgpod-devel libxml2-devel libgtk+3-devel libpeas-devel
BuildRequires: libgranite-devel gstreamer-devel gst-plugins-devel
BuildRequires: libsoup-devel libjson-glib-devel libpixman-devel libtag-devel
BuildRequires: libXdmcp-devel libnotify-devel libpng-devel gcc-c++
BuildRequires: libXdamage-devel libgranite-vala libXxf86vm-devel
BuildRequires: libharfbuzz-devel libXinerama-devel libXi-devel libXrandr-devel
BuildRequires: libXcursor-devel libXcomposite-devel libxkbcommon-devel
BuildRequires: libwayland-cursor-devel at-spi2-atk-devel

%description
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

%package -n libnoise-core
Summary: Simple, fast, and good looking music player (core library)
Group: System/Libraries

%description -n libnoise-core
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

This package contains the shared library.

%package -n libnoise-core-devel
Summary: Simple, fast, and good looking music player (development files)
Group: Development/C

Requires: libnoise-core = %version-%release

%description -n libnoise-core-devel
Noise is an easy to use, stable, fast and good looking music library
organizer written in vala.

It has many modern features including Last.FM integration to download
artwork, information, and scrobble your music, playlists and smart playlists,
find music similar to the currently playing song, simple UI, fast searching
for music, queue system, mass song editing and more...

This package contains the development files.

%prep
%setup -q

%build
%cmake_insource
%make_build

%install
%make_install DESTDIR=%buildroot install

%ifarch x86_64
mkdir -p %buildroot%_libdir/
mv %buildroot/usr/lib/* %buildroot%_libdir/
%endif

%find_lang %name

%files -f %name.lang
%_bindir/*
%_libdir/noise/plugins
%_datadir/applications/noise.desktop
%_datadir/glib-2.0/schemas/org.pantheon.noise.gschema.xml
%_datadir/glib-2.0/schemas/org.pantheon.noise.lastfm.gschema.xml
%_datadir/icons/hicolor/*/apps/multimedia-audio-player.svg
%_datadir/noise


%files -n libnoise-core
%_libdir/libnoise-core.so.*

%files -n libnoise-core-devel
%_includedir/noise-core/noise-core.h
%_libdir/libnoise-core.so
%_pkgconfigdir/noise-core.pc

# TODO:
#    /usr/share/vala/vapi/noise-core.deps
#    /usr/share/vala/vapi/noise-core.vapi

%changelog
* Fri Sep 13 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt2
- fix build on x86_64

* Thu Sep 12 2013 Igor Zubkov <icesik@altlinux.org> 0.2.4-alt1
- build for Sisyphus

