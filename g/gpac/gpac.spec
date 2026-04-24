%def_with doc

%global descr GPAC is an open-source multimedia framework focused on modularity and\
standards compliance. GPAC provides tools to process, inspect, package,\
stream, playback and interact with media content. Such content can be any\
combination of audio, video, subtitles, metadata, scalable graphics, encrypted\
media, 2D/3D graphics and ECMAScript. GPAC is best-known for its wide\
MP4/ISOBMFF capabilities and is popular among video enthusiasts, academic\
researchers, standardization bodies, and professional broadcasters.

Name: gpac
Version: 26.02.0
Release: alt1
Epoch: 1

Summary: GPAC is an open-source multimedia framework
License: LGPL-2.0-or-later
Group: Video
Url: https://gpac.io
Vcs: https://github.com/gpac/gpac.git

Source: %name-%version.tar
Patch: fix-gpac-FEDORA-Makefile-norpath.patch

BuildRequires: gcc-c++
BuildRequires: liba52-devel
BuildRequires: libavcodec-devel libavdevice-devel libavfilter-devel libavformat-devel libavutil-devel
BuildRequires: libcaca-devel
BuildRequires: libcurl-devel
BuildRequires: libfaad-devel
BuildRequires: libfreetype-devel
BuildRequires: libGLU-devel
BuildRequires: libjpeg-devel
BuildRequires: libmad-devel
BuildRequires: libnghttp2-devel
BuildRequires: libnghttp3-devel
BuildRequires: libogg-devel
BuildRequires: libopenjpeg2.0-devel
BuildRequires: libpng-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libSDL2-devel
BuildRequires: libssl-devel
BuildRequires: libtheora-devel
BuildRequires: libvorbis-devel
BuildRequires: libxml2-devel
BuildRequires: libxmlrpc-devel
BuildRequires: libXpm-devel
BuildRequires: libXt-devel
BuildRequires: libXv-devel
BuildRequires: pipewire-jack-libs-devel
BuildRequires: zlib-devel
%if_with doc
BuildRequires: doxygen
BuildRequires: graphviz
%endif

Conflicts: mp4box
Conflicts: gpac <= 1:1.0.1

%description
%descr

%package -n lib%name
Summary: Library for %name
Group: System/Libraries

%description -n lib%name
%summary.
%descr

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name

%description -n lib%name-devel
%summary.
%descr

%if_with doc
%package doc
Summary: Documentation for %name
Group: Development/Documentation

%description doc
%summary
%descr
%endif

%prep
%setup
%autopatch -p1
rm -rv extra_lib

%build
%configure CFLAGS="%optflags %optflags_shared"\
	--extra-ldflags="$(pkg-config --libs jack)" \
	--enable-pic \
	--enable-jack \
	--verbose \
%nil
sed -ie 's/DEBUGBUILD=no/DEBUGBUILD=yes/' config.mak
#Avoid mess with setup.h
cp -p config.h include/gpac

%make_build all

%if_with doc
pushd share/doc
doxygen -u
doxygen
popd
%endif

%install
%makeinstall_std

#Fix doxygen timestamp
touch -r Changelog share/doc/html-libgpac/*

#config.h like but not only
sed -i -e '/GPAC_CONFIGURATION/d' %buildroot%_includedir/%name/configuration.h
touch -r Changelog %buildroot%_includedir/%name/*.h
touch -r Changelog %buildroot%_includedir/%name/internal/*.h
touch -r Changelog %buildroot%_includedir/%name/modules/*.h
rm %buildroot%_includedir/%name/config.h
# do not include in gpac, only here to create doxygen group for doc ordering
rm %buildroot%_includedir/%name/00_doxy.h

%files
%doc Changelog README.md
%_bindir/MP4Box
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_man1dir/*.1.xz
%_iconsdir/hicolor/128x128/apps/%name.png

%files -n lib%name
%_libdir/%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%if_with doc
%files doc
%doc share/doc/html-libgpac/*
%endif

%changelog
* Tue Apr 21 2026 Ulysses Apokin <ulysses@altlinux.org> 1:26.02.0-alt1
- Return the package to Sisyphus (ALT #58007).
