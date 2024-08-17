%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-bsnes
Version:	20240628
Release:	alt1
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar.xz
BuildRequires:	nasm gcc gcc-c++ cmake
# /usr/bin/xxd is needed for libretro-fuse build
BuildRequires:	build-essential
BuildRequires:	libstdc++-devel
BuildRequires:	vim-common
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	libstdc++-devel-static

Conflicts: libretro
Obsoletes: libretro

ExcludeArch: ppc64le

%description
For each emulator 'core', RetroArch makes use of a library API that we like
to call 'libretro'.

Think of libretro as an interface for emulator and game ports. You can make
a libretro port once and expect the same code to run on all the platforms
that RetroArch supports. It's designed with simplicity and ease of use in
mind so that the porter can worry about the port at hand instead of having
to wrestle with an obfuscatory API.

The purpose of the project is to help ease the work of the emulator/game
porter by giving him an API that allows him to target multiple platforms
at once without having to redo any code. He doesn't have to worry about
writing input/video/audio drivers - all of that is supplied to him by
RetroArch. All he has to do is to have the emulator port hook into the
libretro API and that's it - we take care of the rest.

This set of cores based on Beetle SNES emulator

%define bsnesX bsnes2014_accuracy bsnes2014_balanced bsnes2014_performance bsnes_cplusplus98 bsnes_mercury_accuracy bsnes_mercury_balanced bsnes_mercury_performance
%{expand:%(\
    for bsnes in %{bsnesX}; do \
        echo -e "%%package $bsnes\n"; \
        echo -e "Summary: $bsnes libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$bsnes\n";\
        echo -e "Obsoletes: libretro-$bsnes\n";\
        echo -e "%description ${bsnes}\n${bsnes} libretro core\n"; \
        echo -e "%files $bsnes\n%_libexecdir/libretro/${bsnes}_libretro.so\n"; \
    done\
)}

%prep
%setup -q

%build

./libretro-build.sh

%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Tue Aug 13 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit for Sisyphus
