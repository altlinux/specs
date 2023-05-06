Name: paintown
Version: 3.6.0
Release: alt2.1
Summary: 2D Fighting Game
License: GPL-2.0+
Group: Games/Arcade
Url: http://paintown.sourceforge.net/
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: http://downloads.sourceforge.net/%name/%name-%version.tar.bz2
Source1: %name.desktop.in
Source2: %name.sh

Patch0: paintown-noreturnnonvoid-fix.patch

Patch1: paintown-find-freetype.patch

Patch2: paintown-no-strict-aliasing.patch

Patch3: Fix_E2K_build.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: cmake
%ifarch %e2k
BuildRequires: gcc-c++
%else
%set_gcc_version 10
BuildRequires: gcc10-c++
%endif
BuildRequires: glibc-devel
BuildRequires: liballegro5.2-devel
BuildRequires: libogg-devel
BuildRequires: libpng-devel
BuildRequires: libtool
BuildRequires: libvorbis-devel
BuildRequires: make
BuildRequires: pkg-config
BuildRequires: python-dev
BuildRequires: zlib-devel
BuildRequires: libfreetype-devel
BuildRequires: libSDL-devel
Requires: %name-data = %version

%description
Paintown is a 2D fighting game in the same style as Double Dragon and TMNT.
Paintown is very extensible and comes with editors to help design new levels
and animations.

%package data
Summary: 2D Fighting Game (Data Files)
Group: Games/Arcade
Requires: %name = %version
BuildArch: noarch

%description data
Paintown is a 2D fighting game in the same style as Double Dragon and TMNT.
Paintown is very extensible and comes with editors to help design new levels
and animations.

This package contains the data files.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%ifarch %e2k
%patch3 -p1
%endif

find data/ -type f -exec chmod 0644 {} \;

%build

export CFLAGS="%optflags -Wall"
export CXXFLAGS="$CFLAGS"
mkdir build
pushd build
cmake \
    -DCMAKE_INSTALL_PREFIX="%prefix" \
    -DCMAKE_VERBOSE_MAKEFILE=TRUE \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_C_FLAGS_RELEASE:STRING="%optflags -DNDEBUG" \
    -DCMAKE_CXX_FLAGS_RELEASE:STRING="%optflags -DNDEBUG" \
    -DCMAKE_SKIP_RPATH=TRUE \
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=FALSE \
    -DCMAKE_STRIP="%_bindir/touch" \
    -DDEBUG=OFF \
    -DUSE_SDL=ON \
    ..

%make_build
popd #build

%install
install -D -m0755 ./build/bin/%name %buildroot%_bindir/%name-bin
install -d "%buildroot%_datadir"
install -d "%buildroot%_bindir"
cp -a data "%buildroot%_datadir/%name-%version"
install -D -m0644 misc/icon.png "%buildroot%_pixmapsdir/%name.png"
install -D -m0644 "%SOURCE1" "%buildroot%_desktopdir/%name.desktop"
install -D -m0755 %SOURCE2 %buildroot%_bindir/%name

%files
%doc LEGAL LICENSE README TODO scripting.txt
%_bindir/%name
%_bindir/%name-bin
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%files data
%_datadir/%name-%version

%changelog
* Fri May 5 2023 Artyom Bystrov <arbars@altlinux.org> 3.6.0-alt2.1
- fix macros of E2K arch

* Mon May 01 2023 Artyom Bystrov <arbars@altlinux.org> 3.6.0-alt2
- add e2k support

* Mon May 01 2023 Artyom Bystrov <arbars@altlinux.org> 3.6.0-alt1
- initial build for ALT Sisyphus

