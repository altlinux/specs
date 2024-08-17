%global __find_debuginfo_files %nil

Summary:	set cores based on mednafen multi-emulator
Name:		libretro-mednafen
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

This set of packages adds cores, based on Mednafen multi-emulator.

SNES core of mednafen based on old version of Beetle SNES, what causing a issue with compilation.

%define mednafens mednafen_gba mednafen_lynx mednafen_ngp mednafen_pce mednafen_pce_fast mednafen_pcfx mednafen_supergrafx mednafen_vb mednafen_wswan
%{expand:%(\
    for mednafen in %{mednafens}; do \
        echo -e "%%package $mednafen\n"; \
        echo -e "Summary: $mednafen libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$mednafen\n";\
        echo -e "Obsoletes: libretro-$mednafen\n";\
        echo -e "%description ${mednafen}\n${mednafen} libretro core\n"; \
        echo -e "%files $mednafen\n%_libexecdir/libretro/${mednafen}_libretro.so\n"; \
    done\
)}

%ifnarch %e2k
%define mednafens mednafen_psx mednafen_psx_hw mednafen_saturn mednafen_supafaust
%{expand:%(\
    for mednafen in %{mednafens}; do \
        echo -e "%%package $mednafen\n"; \
        echo -e "Summary: $mednafen libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$mednafen\n";\
        echo -e "Obsoletes: libretro-$mednafen\n";\
        echo -e "%description ${mednafen}\n${mednafen} libretro core\n"; \
        echo -e "%files $mednafen\n%_libexecdir/libretro/${mednafen}_libretro.so\n"; \
    done\
)}
%endif


%prep
%setup -q
%ifarch %e2k
# error: in "goto *expr", expr must have type "void *"
# but "labels as values" are slow with LCC, better to disable it
sed -i '/defined(__ICC)/c #if 0' \
	libretro-mednafen_supergrafx/mednafen/pce_fast/ioread.inc \
	libretro-mednafen_pce_fast/libretro.cpp
sed -i 's/#ifdef _MSC_VER/#if 1/' libretro-mednafen_{vb,pcfx}/mednafen/hw_cpu/v810/v810_oploop.inc
sed -i 's/HAVE_COMPUTED_GOTO/0/' libretro-beetle_psx/mednafen/psx/cpu.cpp
%endif
%build

for core in mednafen_gba mednafen_lynx mednafen_ngp mednafen_pce mednafen_pce_fast mednafen_pcfx mednafen_supergrafx mednafen_vb mednafen_wswan; do
./libretro-build.sh $core
done

%ifnarch %e2k
for core in mednafen_psx mednafen_psx_hw mednafen_saturn mednafen_supafaust; do
./libretro-build.sh $core
done
%endif

%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

# Core info files placed into separate package
rm -f %{buildroot}%{_libexecdir}/%{name}/*.info

%changelog
* Tue Aug 13 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit
