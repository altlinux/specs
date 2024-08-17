%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-computers
Version:	20240628
Release:	alt1
# Actually, various for each core but mostly GPLv2
License:	GPL2
Group:		Emulators
Url:		http://www.libretro.com
# fetched via libretro-fetch.sh from git and re-packed
Source0:	%{name}-%{version}.tar
BuildRequires:	nasm gcc gcc-c++ cmake ninja-build meson
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
# for dosbox_core
BuildRequires: pkgconfig(ogg)
BuildRequires: libopusurl-devel
BuildRequires: libSDL_net-devel
BuildRequires: libalsa-devel
BuildRequires: pkgconfig(vorbis)
BuildRequires: libmpg123-devel
BuildRequires: pkgconfig(sndfile)

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

%define computers 81 atari800 bk bluemsx dosbox dosbox_core dosbox_pure dosbox_svn fmsx fuse hatari minivmac nekop2 np2kai oberon puae puae2021 quasi88 theodore tic80 uzem vaporspec vemulator x1
%{expand:%(\
    for computer in %{computers}; do \
        echo -e "%%package ${computer}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$computer\n";\
        echo -e "Obsoletes: libretro-$computer\n";\
        echo -e "%%description $computer\n%%summary\n";\
        echo -e "%%files $computer\n%%_libexecdir/libretro/${computer}_libretro.so\n";\
    done\
)}

%ifnarch %e2k
%define computers px68k
%{expand:%(\
    for computer in %{computers}; do \
        echo -e "%%package ${computer}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "Conflicts: libretro-$computer\n";\
        echo -e "Obsoletes: libretro-$computer\n";\
        echo -e "%%description $computer\n%%summary\n";\
        echo -e "%%files $computer\n%%_libexecdir/libretro/${computer}_libretro.so\n";\
    done\
)}
%endif

%prep
%setup -q

%build

%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

for core in 81 atari800 bk bluemsx fmsx fuse hatari minivmac nekop2 np2kai oberon puae puae2021 px68k quasi88 theodore tic80 uzem vaporspec vemulator x1; do
./libretro-build.sh $core
done

%ifnarch %e2k
for core in px68k; do
./libretro-build.sh $core
done
%endif

for core in dosbox_svn dosbox_pure; do
./libretro-build.sh $core
done

for core in dosbox; do
export CXXFLAGS="${CXXFLAGS} -std=gnu++11"
./libretro-build.sh $core
done


for core in dosbox_core; do
  cd libretro-$core/libretro;
  make -j`nproc` platform=unix BUNDLED_AUDIO_CODECS=0 BUNDLED_LIBSNDFILE=0 BUNDLED_SDL=0 WITH_BASSMIDI=0 WITH_FLUIDSYNTH=0 -f Makefile.libretro;
  cp ${core}_libretro.so ../../dist/unix/
done

%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Tue Aug 13 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit for Sisyphus after split of libretro into number of packages
