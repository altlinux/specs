%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-handhelds
Version:	20240628
Release:	alt1
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar
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

%define handhelds crocods fixgb gambatte gearboy gpsp gw handy melonds mgba pocketcdg pokemini potator sameboy sameduck vbam vba_next
%{expand:%(\
    for handheld in %{handhelds}; do \
        echo -e "%%package ${handheld}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$handheld\n";\
        echo -e "Obsoletes: libretro-$handheld\n";\
        echo -e "%%description $handheld\n%%summary\n";\
        echo -e "%%files $handheld\n%%_libexecdir/libretro/${handheld}_libretro.so\n";\
    done\
)}

%ifnarch %e2k
%define handhelds desmume desmume2015 swanstation
%{expand:%(\
    for handheld in %{handhelds}; do \
        echo -e "%%package ${handheld}\n";\
        echo -e "ExcludeArch: %e2k\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$handheld\n";\
        echo -e "Obsoletes: libretro-$handheld\n";\
        echo -e "%%description $handheld\n%%summary\n";\
        echo -e "%%files $handheld\n%%_libexecdir/libretro/${handheld}_libretro.so\n";\
    done\
)}
%endif


%prep
%setup -q

%build

%ifarch aarch64
for src in ./libretro-desmume2015/desmume/ ./libretro-desmume/desmume/src/frontend/libretro/; do
pushd $src
make -j`nproc` -f Makefile.libretro platform="unix aarch64 hardfloat" DESMUME_JIT=0;
popd
done
%else
./libretro-build.sh $core
%endif

for core in crocods fixgb gambatte gearboy gpsp gw handy melonds mgba pocketcdg pokemini potator sameboy sameduck swanstation vbam vba_next; do
./libretro-build.sh $core
done


%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
%ifarch aarch64
for src in ./libretro-desmume2015/desmume/ ./libretro-desmume/desmume/src/frontend/libretro/; do
pushd $src;
install -m 0644 *.so %{buildroot}%{_libexecdir}/libretro/;
popd;
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/
done
%endif

install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Tue Aug 13 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
Initial commit for Sisyphus after split of libretro into number of packages