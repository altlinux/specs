%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-consoles
Version:	20240628
Release:	alt1
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar
Patch1: libretro-consoles-20240813-alt1-Fix-build-blastem-on-ALT.patch

BuildRequires:	nasm gcc gcc-c++ cmake
# /usr/bin/xxd is needed for libretro-fuse build
BuildRequires:	build-essential
BuildRequires:	libstdc++-devel
BuildRequires:	vim-common
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sdl2)
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

This is set of cores of game consoles emulators.

%define consoles a5200 cap32 chimerasnes ep128emu_core fceumm fixnes freechaf freeintv gearcoleco gearsystem genesis_plus_gx genesis_plus_gx_wide lowresnx mesen mesens meteor mu neocd nestopia o2em opera pcsx1 picodrive prosystem quicknes retro8 smsplus stella stella2014 tgbdual uw8 vecx virtualjaguar
%{expand:%(\
    for console in %{consoles}; do \
        echo -e "%%package $console\n"; \
        echo -e "Summary: $console libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$console\n";\
        echo -e "Obsoletes: libretro-$console\n";\
        echo -e "%description ${console}\n${console} libretro core\n"; \
        echo -e "%files $console\n%_libexecdir/libretro/${console}_libretro.so\n"; \
    done\
)}

%ifnarch aarch64
%define consoles kronos parallel_n64 yabasanshiro yabause
%{expand:%(\
    for console in %{consoles}; do \
        echo -e "%%package $console\n"; \
        echo -e "Summary: $console libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$console\n";\
        echo -e "Obsoletes: libretro-$console\n";\
        echo -e "%description ${console}\n${console} libretro core\n"; \
        echo -e "%files $console\n%_libexecdir/libretro/${console}_libretro.so\n"; \
    done\
)}
%endif

%ifarch %ix86 x86_64
%define consoles blastem
%{expand:%(\
    for console in %{consoles}; do \
        echo -e "%%package $console\n"; \
        echo -e "Summary: $console libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$console\n";\
        echo -e "Obsoletes: libretro-$console\n";\
        echo -e "%description ${console}\n${console} libretro core\n"; \
        echo -e "%files $console\n%_libexecdir/libretro/${console}_libretro.so\n"; \
    done\
)}
%endif

%ifnarch %e2k
%define consoles mupen64plus_next pcsx_rearmed
%{expand:%(\
    for console in %{consoles}; do \
        echo -e "%%package $console\n"; \
        echo -e "Summary: $console libretro core\nGroup: Emulators\n"; \
        echo -e "Conflicts: libretro-$console\n";\
        echo -e "Obsoletes: libretro-$console\n";\
        echo -e "%description ${console}\n${console} libretro core\n"; \
        echo -e "%files $console\n%_libexecdir/libretro/${console}_libretro.so\n"; \
    done\
)}
%endif

%prep
%setup -q
%patch1 -p1

%build

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

for core in a5200 cap32 chimerasnes ep128emu_core fceumm fixnes freechaf freeintv gearcoleco gearsystem genesis_plus_gx genesis_plus_gx_wide lowresnx mesen mesens meteor mu neocd nestopia o2em opera pcsx1 pcsx_rearmed picodrive prosystem quicknes retro8 smsplus stella stella2014 tgbdual uw8 vecx virtualjaguar yabasanshiro yabause; do
./libretro-build.sh $core
done

%ifnarch aarch64
for core in kronos parallel_n64 yabasanshiro yabause; do
./libretro-build.sh $core
done
%endif

%ifnarch %e2k
for core in mupen64plus_next; do
./libretro-build.sh $core
done
%endif

%ifarch %ix86 x86_64
for core in blastem; do
./libretro-build.sh $core
done
%endif

%install
# ProSystem system files path
mkdir -p %{buildroot}%{_libexecdir}/%{name}/prosystem/

mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Thu Aug 15 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit for Sisyphus after split of libretro into number of packages