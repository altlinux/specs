%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-arcades
Version:	20240628
Release:	alt1
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar

Patch1: libretro-arcades-20240813-alt1-Fix_build_mame2010.patch
Patch2: libretro-arcades-20240813-alt1-Fix_build_mame2015.patch 

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
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
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

THs set contains cores for arcade machines emulation (except FBNeo - this is multi-system emulator)

%define arcades daphne fbalpha2012 fbalpha2012_cps1 fbalpha2012_cps2 fbalpha2012_cps3 fbalpha2012_neogeo fbneo galaksija mame2000 mame2003 mame2003_midway mame2003_plus
%{expand:%(\
    for arcade in %{arcades}; do \
        echo -e "%%package $arcade\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$arcade\n";\
        echo -e "Obsoletes: libretro-$arcade\n";\
        echo -e "%%description $arcade\n%%summary\n";\
        echo -e "%%files $arcade\n%%_libexecdir/libretro/${arcade}_libretro.so\n";\
    done\
)}

%ifarch %ix86 x86_64
%define arcades mame2010 mame2015
%{expand:%(\
    for arcade in %{arcades}; do \
        echo -e "%%package $arcade\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$arcade\n";\
        echo -e "Obsoletes: libretro-$arcade\n";\
        echo -e "%%description $arcade\n%%summary\n";\
        echo -e "%%files $arcade\n%%_libexecdir/libretro/${arcade}_libretro.so\n";\
    done\
)}
%endif

%ifarch aarch64
%define arcades mame2015
%{expand:%(\
    for arcade in %{arcades}; do \
        echo -e "%%package $arcade\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$arcade\n";\
        echo -e "Obsoletes: libretro-$arcade\n";\
        echo -e "%%description $arcade\n%%summary\n";\
        echo -e "%%files $arcade\n%%_libexecdir/libretro/${arcade}_libretro.so\n";\
    done\
)}
%endif


%prep
%setup -q

%patch1 -p1
%patch2 -p1

%build

for core in daphne fbalpha2012 fbalpha2012_cps1 fbalpha2012_cps2 fbalpha2012_cps3 fbalpha2012_neogeo fbneo galaxy mame2000 mame2003 mame2003_midway mame2003_plus; do
./libretro-build.sh $core
done

%ifarch %ix86 x86_64 aarch64
for core in mame2015; do
./libretro-build.sh $core
done
%endif

%ifarch %ix86 x86_64
for core in mame2010; do
./libretro-build.sh $core
done
%endif

%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Thu Aug 15 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit for Sisyphus after split of libretro into number of packages