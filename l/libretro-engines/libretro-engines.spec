%global __find_debuginfo_files %nil

Summary:	An interface for emulator and game ports
Name:		libretro-engines
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


%define engines boom3 cannonball dinothawr ecwolf jumpnbump lutro mrboom numero nxengine prboom reminiscence superbroswar tyrquake vitaquake2 xrick
%{expand:%(\
    for engine in %{engines}; do \
        echo -e "%%package ${engine}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "%%description $engine\n%%summary\n";\
        echo -e "%%files $engine\n%%_libexecdir/libretro/${engine}_libretro.so\n";\
    done\
)}

%ifnarch %e2k
%define engines chailove
%{expand:%(\
    for engine in %{engines}; do \
        echo -e "%%package ${engine}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "%%description $engine\n%%summary\n";\
        echo -e "%%files $engine\n%%_libexecdir/libretro/${engine}_libretro.so\n";\
    done\
)}
%endif

%ifnarch %ix86
%define engines vitaquake3 
%{expand:%(\
    for engine in %{engines}; do \
        echo -e "%%package ${engine}\n";\
        echo -e "Summary: libretro core\nGroup: Emulators\n";\
        echo -e "%%description $engine\n%%summary\n";\
        echo -e "%%files $engine\n%%_libexecdir/libretro/${engine}_libretro.so\n";\
    done\
)}
%endif

%prep
%setup -q

%build

for core in boom3 cannonball chailove dinothawr ecwolf jumpnbump lutro mrboom numero nxengine prboom reminiscence superbroswar tyrquake vitaquake2 xrick; do
./libretro-build.sh $core
done

%ifnarch %e2k
for core in chailove; do
./libretro-build.sh $core
done
%endif

%ifnarch %ix86
for core in vitaquake3 ; do
./libretro-build.sh $core
done
%endif

%install
mkdir -p %{buildroot}%{_libexecdir}/libretro
install -m 0644 ./dist/unix/*.so %{buildroot}%{_libexecdir}/libretro/

%changelog
* Sun Jul  7 2024 Artyom Bystrov <arbars@altlinux.org> 20240628-alt1
- Initial commit for Sisyphus
