%define _unpackaged_files_terminate_build 1
%if "%_vendor" == "alt"
# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
%filter_from_requires /^ntdll.so.*/d
%filter_from_requires /^win32u.so.*/d
%global __find_debuginfo_files %nil
%endif

%def_without devel
%def_with vanilla
%define gecko_version 2.47.4
%define mono_version 11.1.0
%define winetricks_version 20250102

# https://dl.winehq.org/wine/source/
%define basemajor 11.x
%define major 11.11
%define rel %nil

# the packages will conflict with that
%define conflictlist wine wine-stable wine-tkg wine-proton-tkg wine-etersoft
%define wow64conflict i586-wine i586-wine-stable i586-wine-tkg i586-wine-proton-tkg

%define __add_conflict() \
for mod in %{conflictlist}; do \
    echo -n "$mod-%{*} "; \
done; unset mod;\
%nil

%define add_conflict() \
Conflicts: %(%{expand: %%__add_conflict %{*}}) \
%nil

# build ping subpackage
%def_with set_cap_net_raw

# build wow64 package (both 32/64 PE in the one package)
%def_with wow64

%ifarch aarch64
# old clang have some troubles with .seh on aarch64
# use at least llvm 15
%define min_llvm_ver 15
%else
%define min_llvm_ver 11
%endif

# used _llvm_version from rpm-macros-llvm-common
%if %{defined _llvm_version}
%define llvm_ver %(LANG=C printf %%.0f %{_llvm_version})
%else
%define llvm_ver 0
%endif

%if %llvm_ver < %min_llvm_ver
%global _llvm_version %min_llvm_ver.0
%define llvm_ver %min_llvm_ver
%endif

# use %min_llvm_ver instead of _llvm_version (feature version can be obsoleted)
%if_feature llvm %min_llvm_ver
# build real PE libraries (.dll, not .dll.so), via clang
%def_with mingw
%else
%def_without mingw
# can't build wow64 without PE
%undefine _with_wow64
%endif

%if_with wow64
%undefine _without_mingw
%def_with mingw
%endif

# build all project with clang
%def_without clang

# https://bugs.etersoft.ru/show_bug.cgi?id=15244
%def_with unwind

# keep debugging symbols in PE files (skip strip)
# TODO: check if we need debug info and pack it separately
%def_with debugpe

# use rpm-macros-features
%if_feature vulkan
    %def_with vulkan
%else
    %def_without vulkan
%endif

%if_feature wayland
    %def_with wayland
%else
    %def_without wayland
%endif

%if_feature ffmpeg
    %def_with ffmpeg
%else
    %def_without ffmpeg
%endif

%def_with sdl

%if_feature opencl
    %def_with opencl
%else
    %def_without opencl
%endif

%if_feature pcap 1.10.3
    %def_with pcap
%else
    %def_without pcap
    %def_without set_cap_net_raw
%endif

# default for unsupported arches
%define winepkgname wine-vanilla

%ifarch x86_64 aarch64
    %def_with build64
    %define winearch wine64
    %define winepkgname wine-vanilla
%endif

# workaround for https://bugzilla.altlinux.org/38130
# buildwow64 = _arch = x86_64  && with wow64
%if "%_arch" == "x86_64" && %{expand:%%{?_with_wow64:1}%%{!?_with_wow64:0}}
    %def_with buildwow64
    %undefine _with_build64
    %define winearch wine
%else
    %def_without buildwow64
%endif

%ifarch %ix86
    %def_without build64
    %define winearch wine32
    %define winepkgname wine-vanilla
%endif

Name: wine-vanilla
Version: %major
Release: alt1
Epoch: 1

Summary: Wine - environment for running Windows applications

License: LGPLv2+
Group: Emulators
Url: http://winehq.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://dl.winehq.org/wine/source/%basemajor/wine-%version%rel.tar.xz
Source: %name-%version.tar

Source3: %name-%version-desktop.tar
Source4: %name-%version-icons.tar
# multilib wrapper scripts
Source6: %name-%version-bin-scripts.tar

# local patches
#Source10: %name-patches-%version.tar

Patch1: 0011-build-fake-binary-makes-autoreq-happy.patch
Patch2: 0102-fix-build-on-32-bit-systems-with-llvm-https-bugs.win.patch

AutoReq: yes, noperl, nomingw32, nocpp

# build with clang on aarch64, as for Mac OS
%ifarch aarch64
%undefine _without_clang
%def_with clang
%endif

%if_with clang
# clang-12: error: unsupported argument 'auto' to option 'flto='
%define optflags_lto -flto=thin
%endif

# PE cross-compilation is required for ARM64
%if_with mingw
ExclusiveArch: %ix86 x86_64 aarch64
%else
ExclusiveArch: %ix86 x86_64
%endif

# minimalize memory using
%ifarch %ix86 armh
%define optflags_debug -g0
%define optflags_lto %nil
%endif


# disable LTO: link error in particular, and unverified in general
#x86_64-alt-linux-gcc -m64 -o loader/wine64-preloader loader/preloader.o loader/preloader_mac.o -static -nostartfiles -nodefaultlibs \
#  -Wl,-Ttext=0x7d400000
#ld: /usr/src/tmp/wine64-preloader.yxZ9KH.ltrans0.ltrans.o: in function `_start':
#<artificial>:(.text+0x12): undefined reference to `thread_data'
#ld: <artificial>:(.text+0x2a): undefined reference to `wld_start'
%define optflags_lto %nil

# used in paths
%define wineproduct wine
%define libdir %_libdir
%define libwinedir %libdir/%wineproduct
%define winebindir %_libexecdir/%wineproduct
%if_with build64
    %define wineserver wineserver64
    %define winebin wine64
%endif
%if_with buildwow64
    %define wineserver wineserver64
    %define winebin wine64
%endif
%if_without build64
    %define wineserver wineserver32
    %define winebin wine32
%endif

%define winepedir unsupported-windows
%define winesodir unsupported-unix

%define winepe32dir i386-windows
%define winepe64dir %_arch-windows

# set arch dependent dirs
%ifarch %{ix86}
%define winepedir i386-windows
%define winesodir i386-unix
%endif
%ifarch x86_64
%define winepedir x86_64-windows
%define winesodir x86_64-unix
%define wow64_arches i386,x86_64
%endif
%ifarch %{arm}
%define winepedir arm-windows
%define winesodir arm-unix
%endif
%ifarch aarch64
%define winepedir aarch64-windows
%define winesodir aarch64-unix
%endif


%if_without build64
    # skip -fPIC checking (-fnoPIC need in new wine to skip DECLSPEC_HOTPATCH)
    %add_verify_elf_skiplist %libwinedir/%winesodir/*.so
    # -fPIC is totally disabled for i586
    %add_verify_elf_skiplist %_bindir/*
    %add_verify_elf_skiplist %winebindir/*
%endif

# TODO: remove it for mingw build (when there will no any dll.so files)
%add_verify_elf_skiplist %libwinedir/%winesodir/*.*.so
%add_findreq_skiplist %libwinedir/%winepe32dir/*
%add_findreq_skiplist %libwinedir/%winepe64dir/*

#
# /usr/bin/strip: ./usr/lib64/wine/x86_64-windows/stqrTIUz/stPNVRry/dsound.dll: warning: line number count (0x10000) exceeds section size (0x8)
# /usr/bin/strip: ./usr/lib64/wine/x86_64-windows/stbguFIA: file format not recognized
# see also our strip below
%if_with debugpe
%global __os_install_post %{nil}
%brp_strip_none %libwinedir/%winepe32dir/*
%brp_strip_none %libwinedir/%winepe64dir/*
%endif

# we don't need provide anything
AutoProv:no

# for wine-staging gitapply.sh script
BuildRequires: /proc

# used llvm/clang toolchain if needed
%if "%_vendor" == "alt" && %{defined _llvm_version}
%define llvm_br clang%_llvm_version llvm%_llvm_version lld%_llvm_version
%else
# just use default llvm
%define llvm_br clang llvm lld
%endif

%if_with clang
BuildRequires: %llvm_br
%else
BuildRequires: gcc
%endif

%if_with mingw
BuildRequires: %llvm_br
%endif

# General dependencies
BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires(pre): rpm-macros-features
%if "%_vendor" == "alt"
BuildRequires(pre): rpm-macros-llvm-common
%endif
BuildRequires: util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libattr-devel
BuildRequires: libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libv4l-devel
BuildRequires: libalsa-devel jackit-devel libpulseaudio-devel
BuildRequires: libGLU-devel
%if_with sdl
BuildRequires: libSDL2-devel
%endif
%if_with wayland
BuildRequires: libwayland-client-devel libglvnd-devel libwayland-egl-devel libxkbcommon-devel
%endif
%if_with ffmpeg
BuildRequires: libavutil-devel libavformat-devel libavcodec-devel
%endif

BuildRequires: libusb-devel libieee1284-devel
BuildRequires: libgcrypt-devel libgnutls-devel libsasl2-devel libkrb5-devel
BuildRequires: libunixODBC-devel
%if_with pcap
BuildRequires: libpcap-devel
%endif
BuildRequires: valgrind-devel
%if_with unwind
BuildRequires: libunwind-devel
%endif

# dlls/netapi32
#BuildRequires: libnetapi-devel
BuildRequires: pkgconfig(netapi)

#BuildRequires: gstreamer-devel gst-plugins-devel

# for winscard (libpcsclite.so here)
BuildRequires: libpcsclite-devel

%if_with vulkan
BuildRequires: libvulkan-devel
%endif

%if_with opencl
BuildRequires: ocl-icd-devel opencl-headers
%endif

# Staging part
%if_with gtk3
# GTK3 theme support: staging only
BuildRequires: libgtk+3-devel libcairo-devel
%endif
BuildRequires: libva-devel

# udev needed for udev version detect
BuildRequires: libudev-devel udev libdbus-devel

# all Xorg dependencies
BuildRequires: libxcb-devel
BuildRequires: libICE-devel libSM-devel
BuildRequires: libX11-devel libXau-devel libXaw-devel libXrandr-devel
BuildRequires: libXext-devel libXfixes-devel libXfont-devel libXft-devel libXi-devel
BuildRequires: libXmu-devel libXpm-devel libXrender-devel
BuildRequires: libXres-devel libXScrnSaver-devel libXinerama-devel libXt-devel
BuildRequires: libXxf86dga-devel libXcomposite-devel
BuildRequires: libXxf86vm-devel libfontenc-devel libXdamage-devel
BuildRequires: libXvMC-devel libXcursor-devel libXv-devel

# a long way to get needed perl-XML-LibXML?
BuildRequires: perl-XML-Simple

BuildRequires: desktop-file-utils

#BuildRequires(pre): rpm-macros-wine

# Use it instead proprietary MS Core Fonts
# Requires: fonts-ttf-liberation

# FIXME: Actually for x86_32
Requires: glibc-pthread glibc-nss

#Requires: %name-gecko = %gecko_version

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: %name-common = %EVR

# ALT bug #55444
# wine will ask anyway
Requires: wine-mono = %mono_version
Requires: wine-gecko = %gecko_version

# wine-mono and wine-gecko require these to get removed on version change
Provides: wine-mono-req = %mono_version
Provides: wine-gecko-req = %gecko_version

%if_with buildwow64
Conflicts: %wow64conflict
%endif

Conflicts: %conflictlist

# old gl part
Provides: %winepkgname-gl = %EVR
Obsoletes: %winepkgname-gl < %EVR

Conflicts: libwine-vanilla-gl libwine-gl
Conflicts: wine-vanilla-gl wine-gl
Obsoletes: lib%name-gl < %EVR

# old twain part
Provides: %winepkgname-twain = %EVR
Obsoletes: %winepkgname-twain < %EVR

Conflicts: libwine-vanilla-twain libwine-twain
Conflicts: wine-vanilla-twain wine-twain
Obsoletes: lib%name-twain < %EVR

# Provides/Obsoletes Fedora packages
%define common_provobs wine-filesystem wine-desktop wine-systemd wine-sysvinit
%define base_provobs wine-alsa wine-capi wine-cms wine-ldap wine-openal wine-pulseaudio wine-wow wine-alsa wine-capi wine-cms wine-ldap wine-opencl wine-pulseaudio
%define fonts_provobs wine-fonts wine-arial-fonts wine-courier-fonts wine-fixedsys-fonts wine-marlett-fonts wine-ms-sans-serif-fonts wine-small-fonts wine-symbol-fonts wine-system-fonts wine-tahoma-fonts wine-times-new-roman-fonts wine-wingdings-fonts
#Provides: %common_provobs %base_provobs %fonts_provobs
Obsoletes: %common_provobs %base_provobs %fonts_provobs


#=========================================================================

%description
Wine (originally an acronym for "Wine Is Not an Emulator")
is a compatibility layer capable of running Windows applications.
Instead of simulating internal Windows logic like a virtual machine or emulator,
Wine translates Windows API calls into POSIX calls on-the-fly,
eliminating the performance and memory penalties
of other methods and allowing you to cleanly integrate Windows applications into your desktop.

This build uses only winehq upstream sources without any patches.

%package test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %EVR
%add_conflict test

%description test
WinAPI test for Wine (unneeded for usual work).
Warning: it may kill your X server suddenly.


%package full
Summary: Wine meta package
Summary(ru_RU.UTF-8): Мета пакет Wine
Group: Emulators
# due ExclusiveArch
#BuildArch: noarch
Requires: %name = %EVR
Requires: %name-programs = %EVR

Requires: winetricks >= %winetricks_version

%add_conflict full

%description full
Wine meta package. Use it for install all wine subpackages.


%package common
Summary: Common wine files and scripts
Summary(ru_RU.UTF-8): Общие файлы и скрипты Wine
Group: Emulators
# Cannot be noarch: Requires wine-vanilla which has ExclusiveArch
#BuildArch: noarch
%add_conflict common
# we don't need provide anything
AutoProv:no
Conflicts: libwine <= 6.14.1
Conflicts: i586-libwine <= 6.14.1
Conflicts: wine <= 6.14.1
Conflicts: i586-wine <= 6.14.1

Conflicts: libwine-vanilla <= 6.14.1
Conflicts: i586-libwine-vanilla <= 6.14.1
Conflicts: wine-vanilla <= 6.14.1
Conflicts: i586-wine-vanilla <= 6.14.1

Requires: %name = %EVR

%description common
Common arch independent wine files and scripts.

%description common -l ru_RU.UTF-8
Общие архитектурно-независимые файлы Wine.


%package programs
Summary: Wine programs
Group: Emulators
Requires: %name = %EVR
# due ExclusiveArch
#BuildArch: noarch

%add_conflict programs

%description programs
Wine GUI programs:
 * winefile
 * notepad
 * winemine


%package ping
Summary: Set capability for Wine ping
Group: Emulators
Requires: %name = %EVR
# due ExclusiveArch
#BuildArch: noarch
%add_conflict ping

%if_with set_cap_net_raw
Requires(pre): libcap-utils
%endif


%description ping
Set capability for Wine ping in post install script.

Also you can control in manually:

$ wine-cap_net_raw [on|off]


%package devel-tools
Summary: Development tools for %name-devel
Group: Development/C
Requires: %name-devel = %EVR
%add_conflict devel-tools
Conflicts: lib%name-devel < %version
%if_with devel
Provides: libwine-devel = %EVR
%endif
# we don't need provide anything
AutoProv:no

# winegcc requires
Requires: glibc-devel libstdc++-devel

%if_with clang
Requires: %llvm_br
%else
Requires: gcc gcc-c++
%endif

%if_with mingw
Requires: %llvm_br
%endif

%description devel-tools
%name-devel-tools contains tools needed to
develop programs using %name.

%description devel-tools -l ru_RU.UTF-8
%name-devel содержит файлы для разработки программ,
использующих Wine: заголовочные файлы и утилиты,
предназначенные для компилирования программ с %name.


%package devel
Summary: Headers for %name-devel
Group: Development/C
Requires: %name = %EVR
Obsoletes: lib%name-devel < %version
#Provides: lib%name-devel = %EVR
%add_conflict devel
# we don't need provide anything
AutoProv:no


%description devel
%name-devel contains the header files and some utilities needed to
develop programs using %name.

%description devel -l ru_RU.UTF-8
%name-devel содержит файлы для разработки программ, использующих Wine:
заголовочные файлы и утилиты, предназначенные
для компилирования программ с %name.


%prep
%setup
%patch1 -p1
%patch2 -p1
# Apply local patches
#name-patches/patchapply.sh

%build
%if_with clang
%remove_optflags -frecord-gcc-switches
export CC=clang-%llvm_ver
# not supported
#export CPP=clang-cpp-%llvm_ver
export LD=lld-%llvm_ver
%endif

# disable fortify as it can breaks wine
# http://bugs.winehq.org/show_bug.cgi?id=24606
%remove_optflags -fcf-protection
%remove_optflags -fstack-protector-strong
%remove_optflags -fstack-clash-protection
# drop default FORTIFY_SOURCE here to mute warning when overrides with _FORTIFY_SOURCE=0 (wine disable it)
%remove_optflags -Wp,-D_FORTIFY_SOURCE=2
%remove_optflags -D_FORTIFY_SOURCE=2

%if_without buildwow64
echo "Needed llvm %_llvm_version is not present on the build platform, build without wow64 support."
%endif

%configure --with-x \
	--disable-win16 \
%if_with build64
	--enable-win64 \
%endif
%if_with buildwow64
	--enable-archs=%wow64_arches \
%endif
	--disable-tests \
	--without-gstreamer \
	--without-oss --with-alsa --with-pulse \
	--with-cups \
	--without-capi \
	%{subst_with opencl} \
	%{subst_with pcap} \
%if_with mingw
	--with-mingw=%llvm_bindir/clang \
%endif
	%{subst_with vulkan} \
	%{subst_with sdl} \
	%{subst_with wayland} \
	%{subst_with ffmpeg} \
	--bindir=%winebindir \
	%nil

%__make depend
%make_build


%install
%makeinstall_std

# clean permissions (via find to hide file list)
find %buildroot%libwinedir/%winesodir -type f | xargs chmod 0644
find %buildroot%libwinedir/%winepedir -type f | xargs chmod 0644

# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
cp -v %buildroot%libwinedir/%winesodir/ntdll.so %buildroot%libdir
cp -v %buildroot%libwinedir/%winesodir/win32u.so %buildroot%libdir

mkdir -p %buildroot%_bindir/

mv -v %buildroot%winebindir/wine %buildroot%winebindir/%winebin

# hack: move all programs back to _bindir
find %buildroot%winebindir -mindepth 0 -maxdepth 1 -not -type d | \
    egrep -v '/wine$|/wine32$|/wineserver$|/wineserver32$|/wine64$|/wineserver64|/winegcc|/wineg++|/winecpp|/winebuild$' | \
    xargs mv -v -t %buildroot%_bindir/
[ -s %buildroot%_bindir/wineg++ ] || ln -sv --relative %buildroot%winebindir/wineg++ %buildroot%_bindir/
[ -s %buildroot%_bindir/winecpp ] || ln -sv --relative %buildroot%winebindir/winecpp %buildroot%_bindir/


# FIXME: it is missed on 64 bit (it is supposed to be installed with wine 32)
%if_with build64
install -p -m 0644 tools/wine/wine.man %buildroot%_man1dir/wine.1
%endif

# unpack desktop files
cd %buildroot%_desktopdir/
tar xvf %SOURCE3
mkdir -p %buildroot%_datadir/desktop-directories/
mv *.directory %buildroot%_datadir/desktop-directories/
cd - >/dev/null

# unpack icons files
mkdir -p %buildroot%_iconsdir/
cd %buildroot%_iconsdir/
tar xvf %SOURCE4
cd - >/dev/null

# unpack bin scripts files
mkdir -p %buildroot%_bindir/
tar xvf %SOURCE6
for i in bin-scripts/*.in ; do
    tbin=%buildroot%_bindir/$(basename $i .in)
    sed -e "s:@BINDIR@:%winebindir:g" -e "s:@DATADIR@:%_datadir/%wineproduct:g" -e "s:@LIBDIR@:%_libdir:g" -e "s:@WINELIBDIR@:%_libdir/%wineproduct:g" -e "s:@WINELIB32DIR@:%_lib32dir/%wineproduct:g"    $i > $tbin
    chmod +x $tbin
done

%if "%wineserver" != "wineserver"
mv -v %buildroot%winebindir/wineserver %buildroot%winebindir/%wineserver
cp %buildroot%_bindir/wineserver %buildroot%winebindir/wineserver
%endif

%if_with build64
[ -s %buildroot%_bindir/wine64 ] || ln -sv --relative %buildroot%winebindir/wine64 %buildroot%_bindir/
%endif

chmod a+x %buildroot%libwinedir/%winesodir/{wine,wine-preloader,wine_make_autoreq_happy}

%if_with set_cap_net_raw
# script for %name-ping
mkdir -p %buildroot%_sbindir/
mv %buildroot%_bindir/wine-cap_net_raw %buildroot%_sbindir/
%endif

# Do not pack non english man pages yet
rm -rv %buildroot%_mandir/*.UTF-8

# Do not pack dangerous association to run windows executables
rm -v %buildroot%_desktopdir/wine.desktop

%if_without debugpe
# [aarch64] /usr/bin/strip: /usr/src/tmp/wine-staging-buildroot/usr/lib64/wine/aarch64-windows/xinput1_1.dll: file format not recognized
%ifarch aarch64
# /usr/src/tmp/wine-staging-buildroot/usr/lib64/wine/aarch64-windows/xpssvcs.dll
# [aarch64] llvm-strip: error: unsupported object file format
llvm-strip %buildroot%libwinedir/%winepedir/* || :
%else
strip %buildroot%libwinedir/%winepedir/*
%endif
# fix against old broken strip: restore builtin mark
tools/winebuild/winebuild --builtin %buildroot%libwinedir/%winepedir/*
%endif


%if_with set_cap_net_raw
%files ping
%_sbindir/wine-cap_net_raw
%endif

%files
%if_with build64
%_bindir/wine64
%endif
%winebindir/%winebin
%winebindir/%wineserver

%dir %libwinedir/
%dir %libwinedir/%winesodir/
%if_with buildwow64
%dir %libwinedir/%winepe32dir/
%dir %libwinedir/%winepe64dir/
%else
%dir %libwinedir/%winepedir/
%endif

%exclude %libdir/ntdll.so
%exclude %libdir/win32u.so

%libwinedir/%winesodir/avicap32.so
%libwinedir/%winesodir/ntdll.so
%libwinedir/%winesodir/ctapi32.so
%libwinedir/%winesodir/dnsapi.so
%libwinedir/%winesodir/dwrite.so
%libwinedir/%winesodir/qcap.so
%libwinedir/%winesodir/odbc32.so
%libwinedir/%winesodir/crypt32.so
%libwinedir/%winesodir/kerberos.so
%libwinedir/%winesodir/mountmgr.so
%libwinedir/%winesodir/netapi32.so
%libwinedir/%winesodir/nsiproxy.so
%libwinedir/%winesodir/winspool.so
%libwinedir/%winesodir/msv1_0.so
%libwinedir/%winesodir/win32u.so
%libwinedir/%winesodir/winex11.so
%if_with wayland
%libwinedir/%winesodir/winewayland.so
%endif
%libwinedir/%winesodir/ws2_32.so
%if_with opencl
%libwinedir/%winesodir/opencl.so
%endif
%libwinedir/%winesodir/secur32.so
%libwinedir/%winesodir/gphoto2.so
%libwinedir/%winesodir/sane.so
%libwinedir/%winesodir/winepulse.so
%libwinedir/%winesodir/winealsa.so
%libwinedir/%winesodir/winevulkan.so
%libwinedir/%winesodir/opengl32.so
%if_with pcap
%libwinedir/%winesodir/wpcap.so
%endif
%libwinedir/%winesodir/winebus.so
%libwinedir/%winesodir/winebth.so
%libwinedir/%winesodir/winedmo.so
%libwinedir/%winesodir/wineusb.so
%libwinedir/%winesodir/wineps.so
%libwinedir/%winesodir/localspl.so
%libwinedir/%winesodir/winscard.so

%libwinedir/%winesodir/wine
%libwinedir/%winesodir/wine-preloader
%libwinedir/%winesodir/wine_make_autoreq_happy

# PE executables or PE stubs
%libwinedir/%winepedir/*.??*

%if_without mingw
%libwinedir/%winesodir/*.??*.so
%endif

%if_with buildwow64
%libwinedir/%winepe32dir/*.??*
%endif


%files common
%doc ANNOUNCE.md AUTHORS LICENSE README.md
%lang(de) %doc documentation/README-de.md
%lang(es) %doc documentation/README-es.md
%lang(fr) %doc documentation/README-fr.md
%lang(hu) %doc documentation/README-hu.md
%lang(it) %doc documentation/README-it.md
%lang(ko) %doc documentation/README-ko.md
%lang(nb) %doc documentation/README-no.md
%lang(pt) %doc documentation/README-pt.md
%lang(pt_BR) %doc documentation/README-pt_br.md
%lang(tr) %doc documentation/README-tr.md

#if "%winebindir" != "%libwinedir"
%dir %winebindir/
%if "%wineserver" != "wineserver"
%winebindir/wineserver
%endif

%_bindir/wine
%_bindir/wineserver

%_bindir/wineapploader

%_bindir/regsvr32
%_bindir/winecfg
%_bindir/regedit
%_bindir/msiexec

%_bindir/wineconsole

%_bindir/winedbg
%_bindir/wineboot
%_bindir/winepath

%_bindir/notepad
%_bindir/winefile

%_man1dir/notepad.*
%_man1dir/winefile.*

%_iconsdir/*

%_desktopdir/wine-mime-msi.desktop
%_desktopdir/wine-regedit.desktop
#_desktopdir/wine-serverkill.desktop
%_desktopdir/wine-uninstaller.desktop
%_desktopdir/wine-winecfg.desktop
%_desktopdir/wine-wineconsole.desktop
#_desktopdir/wine-winehelp.desktop

# danger
#_desktopdir/wine.desktop

%_datadir/desktop-directories/*.directory

%_man1dir/wine.*
%_man1dir/msiexec.*
%_man1dir/regedit.*
%_man1dir/regsvr32.*
%_man1dir/wineboot.*
%_man1dir/winecfg.*
%_man1dir/wineconsole.*
%_man1dir/winepath.*
%_man1dir/wineserver.*
%_man1dir/winedbg.*


%dir %_datadir/%wineproduct/
%_datadir/%wineproduct/wine.inf
%_datadir/%wineproduct/nls/
%_datadir/%wineproduct/fonts/
%_datadir/%wineproduct/winmd/

%files full

%files programs
%_bindir/winemine
%_man1dir/winemine.*
%_desktopdir/wine-notepad.desktop
%_desktopdir/wine-winefile.desktop
%_desktopdir/wine-winemine.desktop


%files devel-tools
%doc LICENSE
%_bindir/function_grep.pl
%_bindir/winebuild
%winebindir/winebuild
%_bindir/wmc
%_bindir/wrc
%_bindir/widl
%_bindir/wineg++
%winebindir/wineg++
%_bindir/winegcc
%winebindir/winegcc
%_bindir/winecpp
%winebindir/winecpp
%_bindir/winedump
%_bindir/winemaker
%_bindir/msidb

%_includedir/wine/
#_aclocaldir/wine.m4

%_man1dir/wmc.*
%_man1dir/wrc.*
%_man1dir/widl.*
%_man1dir/winebuild.*
%_man1dir/winedump.*
%_man1dir/wineg++.*
%_man1dir/winegcc.*
%_man1dir/winecpp.*
%_man1dir/winemaker.*


%files devel
%if_with buildwow64
%libwinedir/%winepe32dir/lib*.a
#libwinedir/%winepe64dir/lib*.a
%endif
%if_with mingw
%libwinedir/%winepedir/lib*.a
%endif
# fix for makefiles: Don't build native import libraries for PE-only build.
%if_without clang
%libwinedir/%winesodir/lib*.a
%endif

%changelog
* Wed Jul 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.11-alt1
- new version 11.11

* Wed Jul 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.10-alt1
- new version 11.10

* Wed Jul 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.9-alt1
- new version 11.9

* Wed Jul 01 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.8-alt1
- new version 11.8
- set strict require wine-mono 11.1.0

* Wed Apr 29 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.7-alt1
- new version 11.7

* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.6-alt1
- new version 11.6

* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.5-alt1
- new version 11.5

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.4-alt1
- new version 11.4
- wine-cap_net_raw: add /usr/lib/wine path to 'on' command too (ALT bug 56551)

* Fri Feb 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1:11.3-alt1
- new major version 11
- set strict require wine-mono 11.0.0

* Fri Feb 27 2026 Vitaly Lipatov <lav@altlinux.ru> 1:10.18-alt3
- add Provides: wine-mono-req
- add Provides: wine-gecko-req

* Wed Jan 29 2026 Vitaly Lipatov <lav@altlinux.ru> 1:10.18-alt2
- wine-vanilla-common: remove BuildArch noarch due ExclusiveArch in wine-vanilla

* Fri Nov 07 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.18-alt1
- new version 10.18 (with rpmrb script)

* Mon Oct 27 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.17-alt2
- wine-cap_net_raw: set capability for /usr/lib/wine path too (ALT bug 56551)
- wine.spec: move wine-mono and wine-gecko requires to the main package wine (ALT bug 55444)
- wine.spec: move notepad and winefile commands to the main package wine (ALT bug 55444)
- wine-vanilla-common: add require wine-vanilla
- add patch: configure: Work around install-sh requirement in autoconf <= 2.69

* Thu Oct 23 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.17-alt1
- new version 10.17 (with rpmrb script)
- set strict require wine-mono 10.3.0

* Sun Oct 19 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.16-alt2
- spec: improve llvm version handling

* Sat Oct 04 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.16-alt1
- new version 10.16 (with rpmrb script)

* Tue Sep 16 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.15-alt1
- new version 10.15 (with rpmrb script)

* Thu Sep 11 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.14-alt1
- new version 10.14 (with rpmrb script)
- set strict require wine-mono 10.2.0

* Thu Sep 11 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.13-alt1
- new version 10.13 (with rpmrb script)

* Mon Jul 21 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.12-alt1
- new version 10.12 (with rpmrb script)

* Mon Jul 21 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.11-alt1
- new version 10.11 (with rpmrb script)

* Thu Jun 19 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.10-alt1
- new version 10.10 (with rpmrb script)
- set strict require wine-mono 10.1.0

* Thu Jun 19 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.9-alt1
- new version 10.9 (with rpmrb script)
- disable build with libOSMesa-devel (no longer supported)

* Thu May 22 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.8-alt1
- new version 10.8
- apply patch to fix build on aarch64 with clang

* Thu May 22 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.6-alt2
- use _llvm_version and llvm_bindir from rpm-macros-llvm-common
- use feature_osmesa
- don't build wow64 when clang is missed

* Sun May 04 2025 Vitaly Lipatov <lav@altlinux.ru> 1:10.6-alt1
- new version (10.6) with rpmgs script
- set strict require wine-mono 10.0.0
- don't require clang version
- enable wayland support
- enable ffmpeg support
- require winetricks 20250102

* Mon Feb 12 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.2-alt2
- spec: add wow64 support and enable it (not needs i586-wine-vanilla anymore)
- spec: cleanup PE packing
- spec: skip build on aarch64 if clang is too old
- spec: disable win16 build
- spec: don't require wine-etersoft-gecko from the main package
- spec: add wineserver in winebindir

* Sat Feb 10 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.2-alt1
- new version 9.2 (with rpmrb script)
- set strict require wine-mono 9.0.0
- update winetricks require to 20240105
- don't require wine-gecko from wine-vanilla package

* Sat Jan 27 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.1-alt1
- new version 9.1 (with rpmrb script)

* Wed Jan 17 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt2
- new version 9.0

* Mon Jan 15 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt1.rc5
- new version (9.0-rc5) with rpmgs script
- switch to use conflictlist

* Mon Jan 08 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt1.rc4
- new version (9.0-rc4) with rpmgs script

* Sat Dec 23 2023 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt1.rc3
- new version (9.0-rc3) with rpmgs script

* Sun Dec 17 2023 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt1.rc2
- new version (9.0-rc2) with rpmgs script

* Mon Dec 11 2023 Vitaly Lipatov <lav@altlinux.ru> 1:9.0-alt1.rc1
- new version (9.0-rc1) with rpmgs script

* Sat Nov 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.21-alt1
- new version 8.21 (with rpmrb script)

* Sun Nov 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.20-alt1
- new version 8.20 (with rpmrb script)

* Sun Oct 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.19-alt1
- new version 8.19 (with rpmrb script)
- set strict require wine-mono 8.1.0

* Sun Oct 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.18-alt1
- new version 8.18 (with rpmrb script)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.17-alt1
- new version 8.17 (with rpmrb script)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.16-alt1
- new version 8.16 (with rpmrb script)

* Tue Sep 05 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.15-alt2
- remove post/preun scripts for wine-vanilla-ping

* Sun Sep 03 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.15-alt1
- new version 8.15 (with rpmrb script)

* Sun Aug 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.14-alt1
- new version 8.14 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.13-alt1
- new version 8.13 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.9-alt1
- new version 8.9 (with rpmrb script)
- set strict require wine-mono 8.0.0
- require winetricks 20230505

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.6-alt1
- new version 8.6 (with rpmrb script)
- add BuildRequires: libpcsclite-devel
- disable fortify as it can breaks wine
- set strict require wine-gecko 2.47.4

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.3-alt1
- new version 8.3 (with rpmrb script)
- add BuildRequires: libOSMesa-devel

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.2-alt1
- new version 8.2 (with rpmrb script)
- upgrade libpcap require to 1.10.3 (due pcap_init())
- use -g0 for 32 bit systems (minimize memory)
- fix build on 32 bit systems with llvm

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.1-alt1
- new version 8.1 (with rpmrb script)

* Wed Jan 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0-alt2
- 8.0 release
- .desktop files: update descriptions (see altbug #39800)

* Sat Jan 21 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0-alt1.rc5
- new version (8.0-rc5) with rpmgs script

* Sun Jan 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0-alt1.rc3
- new version (8.0-rc3) with rpmgs script

* Tue Dec 20 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.22-alt2
- drop manual requires in favour of real autoreqs

* Wed Dec 07 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.22-alt1
- new version 7.22 (with rpmrb script)
- drop libldap-devel from build requires (bundled now)

* Tue Dec 06 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.21-alt1
- new version 7.21 (with rpmrb script)

* Sun Nov 06 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.20-alt1
- new version 7.20 (with rpmrb script)
- set strict require wine-mono 7.4.0

* Sun Oct 16 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.19-alt1
- new version 7.19 (with rpmrb script)

* Fri Sep 23 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.18-alt1
- new version 7.18 (with rpmrb script)

* Mon Sep 12 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.17-alt2
- not requires libldap, use autoreq

* Sat Sep 10 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.17-alt1
- new version 7.17 (with rpmrb script)

* Mon Aug 29 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.16-alt1
- new version 7.16 (with rpmrb script)

* Thu Aug 18 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.15-alt2
- add conflicts to old wine-vanilla packages

* Sun Aug 14 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.15-alt1
- new version 7.15 (with rpmrb script)

* Sat Jul 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.14-alt1
- new version 7.14 (with rpmrb script)

* Sat Jul 16 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.13-alt1
- new version 7.13 (with rpmrb script)
- set strict require wine-gecko 2.47.3

* Tue Jul 12 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.12-alt2
- add obsoletes for libwine, wine, i586-libwine, i586-wine < 6.14.1

* Sat Jul 02 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.12-alt1
- new version 7.12 (with rpmrb script)

* Sat Jul 02 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.11-alt1
- new version 7.11 (with rpmrb script)

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.10-alt1
- new version 7.10 (with rpmrb script)
- set strict require wine-mono 7.3.0
- rewrite spec, abolish -gl and -twain subpackages

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.9-alt1
- new version 7.9 (with rpmrb script)

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.8-alt1
- new version 7.8 (with rpmrb script)

* Tue Apr 26 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.7-alt1
- new version 7.7 (with rpmrb script)

* Mon Apr 11 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.6-alt1
- new version 7.6 (with rpmrb script)
- set strict require wine-mono 7.2.0

* Fri Apr 01 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.5-alt1
- new version 7.5 (with rpmrb script)
- drop out unneeded build requires (many libs is embedded now)
- drop out unneeded requires
- set strict require wine-mono 7.1.1

* Thu Mar 31 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.1-alt2
- set version for provided libwine-devel
- skip linking wine64 to bindir if it is already exists
- don't pack libwinecrt0.a twice
- fix checking for build64mingw, fix build
- fix build without PE
- pack lib*.a needed for build with wine

* Wed Feb 09 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.1-alt1
- new version 7.1 (with rpmrb script)
- fix build (add hack with ntdll.so and disable debuginfo subpackages)

* Sat Nov 20 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.22-alt1
- new version 6.22 (with rpmrb script)

* Sat Nov 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.21-alt1
- new version 6.21 (with rpmrb script)

* Sat Nov 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.20-alt1
- new version 6.20 (with rpmrb script)

* Sat Nov 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.19-alt1
- new version 6.19 (with rpmrb script)
- add provides libwine-vanilla-devel (thanks, lakostis@)

* Wed Nov 03 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.18-alt1
- new version 6.18 (with rpmrb script)

* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17-alt2
- use rpm-macros-feature for vkd3d checking

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17-alt1
- biarch build, PE build

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 6.15-alt1
- new version 6.15

* Fri Jul 30 2021 Vitaly Lipatov <lav@altlinux.ru> 6.14-alt1
- new version 6.14
- set strict require wine-mono 6.3.0

* Wed Jul 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.13-alt1
- new version 6.13

* Sat Jul 03 2021 Vitaly Lipatov <lav@altlinux.ru> 6.12-alt1
- new version 6.12

* Fri Jun 25 2021 Vitaly Lipatov <lav@altlinux.ru> 6.11-alt2
- fix packing

* Sat Jun 19 2021 Vitaly Lipatov <lav@altlinux.ru> 6.11-alt1
- new version 6.11
- set strict require wine-mono 6.2.0
- build with opencl and pcap

* Sat May 08 2021 Vitaly Lipatov <lav@altlinux.ru> 6.8-alt1
- new version 6.8

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 6.6-alt1
- new version 6.6

* Sat Mar 27 2021 Vitaly Lipatov <lav@altlinux.ru> 6.5-alt1
- new version 6.5

* Sat Mar 13 2021 Vitaly Lipatov <lav@altlinux.ru> 6.4-alt1
- new version 6.4

* Thu Feb 18 2021 Vitaly Lipatov <lav@altlinux.ru> 6.2-alt1
- new version 6.2
- set strict require wine-mono 6.0.0

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 6.0-alt1
- new version 6.0
- set strict require wine-gecko 2.47.2

* Sun Nov 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.22-alt2
- don't provide libwine.so.1 from libwine-vanilla subpackage

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 5.22-alt1
- new version 5.22

* Mon Nov 16 2020 Vitaly Lipatov <lav@altlinux.ru> 5.21-alt1
- new version 5.21

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 5.20-alt1
- new version 5.20

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 5.19-alt1
- new version 5.19
- add gcc-c++ require to devel package (due winegcc)

* Sun Oct 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.18-alt3
- move additional files to .gear subdir (drop etersoft dir)
- add Source git URL

* Thu Oct 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.18-alt2
- Re-enabled vkd3d support.

* Mon Sep 28 2020 Vitaly Lipatov <lav@altlinux.ru> 5.18-alt1
- new version 5.18
- console no longer requires the curses library
- build with vkd3d disabled (see ALT bug 39002)

* Sat Sep 12 2020 Vitaly Lipatov <lav@altlinux.ru> 5.17-alt1
- new version 5.17
- drop static libs if disabled

* Wed Sep 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt3
- just require libvulkan1 as all other libs
- backport small fixes from future biarch build
- sync Requires/Conflicts with wine staging package

* Wed Sep 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt2
- build vulkan only for p9 and Sisyphus
- disable static package

* Sun Aug 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.16-alt1
- new version 5.16

* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.13-alt2
- Rebuilt with vulkan, vkd3d and faudio support (ALT bug #38810).

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.13-alt1
- new version 5.13

* Sat Jul 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.12-alt1
- new version 5.12
- set strict require wine-mono 5.1.0

* Sat Jun 06 2020 Vitaly Lipatov <lav@altlinux.ru> 5.10-alt1
- new version 5.10

* Sun May 24 2020 Vitaly Lipatov <lav@altlinux.ru> 5.9-alt1
- new version 5.9

* Sat May 09 2020 Vitaly Lipatov <lav@altlinux.ru> 5.8-alt1
- new version 5.8

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7-alt1
- new version 5.7

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 5.5-alt1
- new version 5.5

* Sat Mar 14 2020 Vitaly Lipatov <lav@altlinux.ru> 5.4-alt1
- new version 5.4

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt2
- update requires

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 5.3-alt1
- new version 5.3

* Mon Feb 17 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2-alt1
- new version 5.2

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt1
- new version 5.1

* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt1
- wine 5.0 release

* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 5.0-alt0.rc6
- pre release 5.0-RC6
- wine-gecko 2.47.1

* Sun Nov 17 2019 Vitaly Lipatov <lav@altlinux.ru> 4.20-alt1
- new version 4.20
- strict require wine-mono 4.9.4

* Sat Nov 02 2019 Vitaly Lipatov <lav@altlinux.ru> 4.19-alt1
- new version 4.19

* Fri Oct 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.18-alt1
- new version 4.18

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 4.17-alt1
- new version 4.17

* Sun Sep 15 2019 Vitaly Lipatov <lav@altlinux.ru> 4.16-alt1
- new version 4.16

* Sat Aug 31 2019 Vitaly Lipatov <lav@altlinux.ru> 4.15-alt1
- new version 4.15

* Sat Aug 17 2019 Vitaly Lipatov <lav@altlinux.ru> 4.14-alt1
- new version 4.14

* Sun Aug 04 2019 Vitaly Lipatov <lav@altlinux.ru> 4.13-alt1
- new version 4.13

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 4.12.1-alt1
- new version 4.12.1

* Sat Jul 06 2019 Vitaly Lipatov <lav@altlinux.ru> 4.12-alt1
- new version 4.12, enable ExclusiveArch for x86 and aarch64
- remove BR: prelink

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 4.11-alt1
- new version 4.11
- strict require wine-mono-4.9.0

* Mon Jun 10 2019 Vitaly Lipatov <lav@altlinux.ru> 4.10-alt1
- new version 4.10

* Mon May 27 2019 Vitaly Lipatov <lav@altlinux.ru> 4.9-alt1
- new version 4.9
- strict require wine-mono-4.8.3

* Mon May 20 2019 Vitaly Lipatov <lav@altlinux.ru> 4.8-alt1
- new version 4.8

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6-alt2
- strict require wine-mono-4.8.1

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 4.6-alt1
- new version 4.6

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.4-alt1
- new version 4.4

* Sat Mar 02 2019 Vitaly Lipatov <lav@altlinux.ru> 4.3-alt1
- new version 4.3

* Mon Feb 18 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2-alt1
- new version 4.2

* Sat Feb 09 2019 Vitaly Lipatov <lav@altlinux.ru> 4.1-alt1
- new version 4.1

* Wed Jan 23 2019 Vitaly Lipatov <lav@altlinux.ru> 4.0-alt1
- new version 4.0

* Sat Nov 24 2018 Vitaly Lipatov <lav@altlinux.ru> 3.21-alt1
- new version 3.21

* Sun Nov 11 2018 Vitaly Lipatov <lav@altlinux.ru> 3.20-alt1
- new version 3.20

* Sat Nov 03 2018 Vitaly Lipatov <lav@altlinux.ru> 3.19-alt1
- new version 3.19

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.18-alt1
- new version 3.18
- use external winetricks

* Sun Sep 30 2018 Vitaly Lipatov <lav@altlinux.ru> 3.17-alt1
- new version 3.17

* Fri Sep 14 2018 Vitaly Lipatov <lav@altlinux.ru> 3.16-alt1
- new version 3.16

* Fri Aug 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.15-alt1
- new version 3.15

* Mon Aug 20 2018 Vitaly Lipatov <lav@altlinux.ru> 3.14-alt1
- new version 3.14

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.13-alt1
- new version 3.13

* Tue Jul 10 2018 Vitaly Lipatov <lav@altlinux.ru> 3.12-alt1
- new version 3.12

* Sat Jun 23 2018 Vitaly Lipatov <lav@altlinux.ru> 3.11-alt1
- new version 3.11

* Wed Jun 13 2018 Vitaly Lipatov <lav@altlinux.ru> 3.10-alt1
- new version 3.10
- add runtime linking requires
- use clang on aarch64

* Sat May 26 2018 Vitaly Lipatov <lav@altlinux.ru> 3.9-alt1
- new version 3.9

* Sat May 12 2018 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8

* Sat Apr 28 2018 Vitaly Lipatov <lav@altlinux.ru> 3.7-alt1
- new version 3.7

* Sat Apr 21 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6-alt1
- new version 3.6

* Sat Mar 31 2018 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5

* Mon Mar 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4

* Sat Mar 03 2018 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- new version 3.3

* Mon Feb 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- new version 3.2

* Fri Feb 02 2018 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt1
- new version 3.1

* Fri Jan 19 2018 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- new version 3.0
- update winetricks up to 20171222

* Sat Nov 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt1
- new version 2.22

* Sat Nov 11 2017 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- new version 2.21

* Thu Nov 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.20-alt1
- new version 2.20

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 2.19-alt1
- new version 2.19

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.18-alt1
- new version 2.18

* Fri Sep 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.17-alt1
- new version 2.17
- update winetricks to 20170823

* Sat Sep 02 2017 Vitaly Lipatov <lav@altlinux.ru> 2.16-alt1
- new version 2.16

* Sun Aug 20 2017 Vitaly Lipatov <lav@altlinux.ru> 2.15-alt1
- new version 2.15

* Thu Aug 03 2017 Vitaly Lipatov <lav@altlinux.ru> 2.14-alt1
- new version 2.14

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.13-alt1
- new version 2.13

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.12-alt1
- new version 2.12

* Sun Jun 25 2017 Vitaly Lipatov <lav@altlinux.ru> 2.11-alt1
- new version 2.11

* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 2.10-alt1
- new version 2.10

* Sat May 27 2017 Vitaly Lipatov <lav@altlinux.ru> 2.9-alt1
- new version 2.9
- update winetricks to 20170517-next

* Sat May 13 2017 Vitaly Lipatov <lav@altlinux.ru> 2.8-alt1
- new version 2.8

* Sat Apr 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.7-alt1
- new version 2.7

* Sat Apr 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.6-alt1
- new version 2.6

* Sun Apr 09 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt2
- update winetricks to 20170327
- add default icons (ALT bug 25237)

* Sat Apr 01 2017 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version 2.5

* Fri Mar 17 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4-alt1
- new version 2.4

* Sat Mar 04 2017 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3

* Sun Feb 19 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- new version 2.2

* Thu Jan 26 2017 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- new version 2.0

* Thu Dec 01 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.24-alt1
- new version 1.9.24

* Tue Nov 15 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.23-alt1
- new version 1.9.23

* Sun Oct 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.22-alt1
- new version 1.9.22

* Fri Oct 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt3
- pack desktop files for programs to wine-vanilla-programs
- do not pack wine.desktop for protect from suddenly running from GUI

* Thu Oct 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt2
- split wine-vanilla-programs subpackage (ALT bug #32587)

* Sat Oct 15 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.21-alt1
- new version 1.9.21

* Thu Oct 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.20-alt1
- new version 1.9.20

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.19-alt1
- new version 1.9.19

* Sat Sep 03 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.18-alt1
- new version 1.9.18

* Fri Sep 02 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt2
- add wine and libwine-devel provides

* Sun Aug 21 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.17-alt1
- new version 1.9.17

* Thu Aug 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.16-alt1
- new version 1.9.16 (requires wine-gecko = 2.47 since 1.9.13)
- update winetricks to 20160724

* Thu Jun 16 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.12-alt1
- new version 1.9.12

* Sat May 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.11-alt1
- new version 1.9.11

* Fri May 20 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.10-alt1
- new version 1.9.10

* Tue Apr 05 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- new version 1.9.7

* Fri Mar 18 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.6-alt1
- new version 1.9.6

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt2
- fix packing issues
- make wine-vanilla-full noarch
- add libpulseaudio-devel buildreq

* Wed Feb 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- new version 1.9.4 (requires wine-gecko = 2.44)

* Tue Jan 12 2016 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version 1.9.1

* Sat Dec 12 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc4
- new version 1.8-rc4

* Tue Dec 01 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc2
- new version 1.8-rc2

* Sun Nov 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt0rc1
- new version 1.8-rc1

* Fri Oct 30 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.54-alt1
- new version 1.7.54

* Sat Oct 17 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.53-alt1
- new version 1.7.53, requires wine-gecko = 2.40

* Mon Aug 10 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.49-alt1
- new version 1.7.49

* Wed Jul 22 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.47-alt2
- add requires to wine-mono and wine-gecko to full subpackage (closes: #31149)

* Mon Jul 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.47-alt1
- new version 1.7.47

* Mon Jun 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.45-alt1
- new version 1.7.45

* Thu Jun 04 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.44-alt1
- new version 1.7.44

* Tue May 26 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.43-alt2
- add unixODBC-devel buildreq (closes: #31024)
- add cabextract require (closes: #31024)
- add wine-vanilla-full package (closes: #31024)

* Tue May 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.43-alt1
- new version 1.7.43
- build with liblcms2 (closes: #31006)
- build without gstreamer (closes: #31014)

* Sat May 02 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.42-alt1
- new version 1.7.42

* Sun Apr 05 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.40-alt1
- new version 1.7.40

* Wed Apr 01 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.39.gdbf8bde-alt1
- build against commit dbf8bde14616e54abbcf4caca92d4b708170b0ac

* Fri Mar 27 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.39-alt1
- new version 1.7.39

* Mon Mar 09 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.38-alt1
- new version 1.7.38, requires wine-gecko = 2.36

* Fri Feb 20 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.37-alt1
- new version 1.7.37

* Sun Feb 08 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.36-alt1
- new version 1.7.36

* Fri Feb 06 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.35-alt2
- rebuild with new libgphoto2

* Sat Jan 24 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.35-alt1
- new version 1.7.35

* Wed Jan 14 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7.34-alt1
- new version 1.7.34

* Sat Dec 13 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.33-alt1
- new version 1.7.33, requires wine-gecko = 2.34

* Mon Nov 10 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.30-alt1
- new version 1.7.30

* Tue Oct 21 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.29-alt1
- new version 1.7.29

* Sat Oct 11 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.28-alt2
- update winetricks to 20140302 (ALT bug #30382)

* Mon Oct 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.28-alt1
- new version 1.7.28

* Fri Sep 19 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.27-alt1
- new version 1.7.27

* Sat Sep 06 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.26-alt1
- new version 1.7.26

* Sat Aug 23 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.25-alt1
- new version 1.7.25

* Fri Jul 25 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.23-alt1
- new version 1.7.23

* Mon Jul 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.22-alt1
- new version 1.7.22

* Tue Jul 08 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.21-alt1
- new version 1.7.21

* Sun May 18 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.19-alt1
- new version 1.7.19

* Mon May 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.18-alt1
- new version 1.7.18 (ALT bug #30054)

* Sat Apr 05 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.16-alt1
- new version 1.7.16

* Sat Mar 22 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.15-alt1
- new version 1.7.15

* Fri Mar 14 2014 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- new version 1.7.14

* Sat Oct 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- new version 1.7.5

* Mon Oct 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- new version 1.7.4

* Sat Sep 14 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2

* Fri Aug 02 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- release 1.6
- remove libssl-devel requires

* Sun Jun 30 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.rc4
- new version 1.6-rc4

* Sat Jun 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.rc3
- new version 1.6-rc3, requires wine-gecko 2.21

* Tue Feb 19 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.24-alt1
- new version 1.5.24

* Wed Feb 06 2013 Vitaly Lipatov <lav@altlinux.ru> 1.5.23-alt1
- new version 1.5.23, requires wine-gecko 1.9

* Sat Dec 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.20-alt1
- new version 1.5.20, requires wine-gecko 1.8
- remove libhal-devel buildreq

* Mon Sep 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.13-alt2
- restore missed-in-merge changes

* Sat Sep 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.13-alt1
- new version 1.5.13, cleanup spec
- disable libesd support and requires

* Fri Sep 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.12-alt1
- new version 1.5.12

* Wed Aug 01 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.10-alt1
- new version 1.5.10, requires wine-gecko 1.7

* Sat Jul 14 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.8-alt1
- new version 1.5.8

* Mon May 28 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt2
- fix wine-gecko requires to 1.5

* Sat May 26 2012 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5

* Fri Mar 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- new version 1.4.0
- update winetricks to 20120308
- fix requires

* Sat Jan 14 2012 Vitaly Lipatov <lav@altlinux.ru> 1.3.37-alt1
- new version 1.3.37

* Sat Dec 31 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.36-alt1
- new version 1.3.36

* Sat Dec 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.35-alt1
- new version 1.3.35
- update winetricks to 20111115

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.34-alt1
- new version 1.3.34, use wine-gecko 1.4

* Sat Nov 05 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.32-alt1
- new version 1.3.32

* Tue Nov 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.31-alt1
- new version 1.3.31
- update winetricks to 20110629

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.30-alt1
- new version 1.3.30

* Fri Aug 26 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.27-alt1
- new version 1.3.26, use wine-gecko 1.3

* Mon Aug 22 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.26-alt1
- new version 1.3.26
- drop out winehelp desktop file

* Thu Jun 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.21-alt1
- new version 1.3.21

* Fri Apr 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.19-alt1
- new version 1.3.19

* Sun Apr 17 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.18-alt1
- new version 1.3.18

* Mon Apr 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt2
- fix build requires (add missed libtiff-devel, gstreamer plugin base, libgnutls-devel)

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.17-alt1
- new version 1.3.17
- again winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)
- add libncurses requires

* Wed Mar 30 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt3
- drop xorg-x11-proto-devel buildreqs
- pack all man files

* Tue Mar 29 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt2
- winetricks: update to 20110324
- winetricks: do not use zenity/kdialog via direct run (ALT bug 24838)

* Sat Mar 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.3.16-alt1
- new version 1.3.16
- update winetricks to 20110318
- require wine-gecko 1.2.0
- add some desktop files for menu (ALT bug 25237)

* Thu Dec 30 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt2
- winetricks: use detected MENU instead direct command (ALT bug 24838)

* Mon Dec 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.3.10-alt1
- new version 1.3.10 (ALT bug 24273)

* Fri Jul 16 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc7-alt1
- new version 1.2-rc7

* Mon Jun 14 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc3-alt1
- new version 1.2-rc3

* Mon May 31 2010 Ilya Shpigor <elly@altlinux.org> 1.2_rc2-alt1
- new version 1.2-rc2

* Tue May 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt3
- fix build for x86_64 architecture (try 2)

* Fri May 14 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt2
- fix build for x86_64 architecture

* Tue May 11 2010 Ilya Shpigor <elly@altlinux.org> 1.1.44-alt1
- new version 1.1.44

* Mon Apr 19 2010 Ilya Shpigor <elly@altlinux.org> 1.1.43-alt1
- new version 1.1.43

* Mon Apr 05 2010 Ilya Shpigor <elly@altlinux.org> 1.1.42-alt1
- new version 1.1.42

* Mon Mar 22 2010 Ilya Shpigor <elly@altlinux.org> 1.1.41-alt1
- new version 1.1.41

* Sat Mar 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.40-alt1
- new version 1.1.40

* Sun Feb 21 2010 Ilya Shpigor <elly@altlinux.org> 1.1.39-alt1
- new version 1.1.39

* Mon Feb 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.38-alt1
- new version 1.1.38

* Mon Jan 25 2010 Ilya Shpigor <elly@altlinux.org> 1.1.37-alt1
- new version 1.1.37

* Mon Jan 18 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt2
- add winetricks to wine-vanilla package (fix altbug #22650)

* Sat Jan 16 2010 Ilya Shpigor <elly@altlinux.org> 1.1.36-alt1
- new version 1.1.36

* Fri Jan 08 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt4
- fix conflict libwine-vanilla-devel-static with libwine-devel

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt3
- don't build libwine-vanilla-devel-doc package

* Wed Jan 06 2010 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt2
- build the libwine-vanilla-devel-doc package as the architecture-independent

* Fri Dec 25 2009 Ilya Shpigor <elly@altlinux.org> 1.1.35-alt1
- new version 1.1.35

* Fri Dec 25 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.34-alt2
- enable build for x86_64 (fix altbug #10042)

* Fri Dec 11 2009 Ilya Shpigor <elly@altlinux.org> 1.1.34-alt1
- new version 1.1.34

* Tue Nov 24 2009 Ilya Shpigor <elly@altlinux.org> 1.1.33-alt1
- new version 1.1.33

* Sat Oct 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.32-alt1
- new version 1.1.32

* Sat Aug 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt2
- fix services.exe crash (altbug #20927)

* Fri Jul 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.26-alt1
- new version 1.1.26

* Thu Jul 23 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.25-alt1
- new version 1.1.25

* Tue Jun 30 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.24-alt1
- new version 1.1.24

* Tue May 26 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.22-alt1
- new version 1.1.22

* Sat May 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.21-alt1
- new version 1.1.21

* Sat Mar 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.18-alt1
- new version 1.1.18

* Fri Mar 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.17-alt1
- new version 1.1.17

* Sat Feb 28 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.16-alt1
- new version 1.1.16

* Sun Feb 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.15-alt1
- new version 1.1.15

* Fri Feb 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.14-alt1
- new version 1.1.14

* Sat Jan 17 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.13-alt1
- new version 1.1.13

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.1.12-alt1
- merge with upstream (1.1.12)

* Fri Dec 26 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.11-alt1
- merge with upstream (1.1.11)
- add libhal-devel buildreq

* Fri Nov 21 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt1
- merge with upstream (1.1.9)

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- merge with upstream (1.1.8)

* Sat Nov 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt2
- rebuild configure
- remove autoconf due too old autoconf in ALT 4.0

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- merge with upstream (1.1.7)
- add autoconf -f due strange configure

* Fri Sep 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- merge with upstream (1.1.5)
- revert to original sources from git://source.winehq.org/git/wine.git

* Wed Jul 16 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- merge with upstream (1.1.1)
- cleanup spec, return update_menus
- fix altbug #16230 again (run init functions from linked libs)

* Tue Jul 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt2
- merge with upsteam
- link gdi32 with freetype/fontconfig directly (fix altbug #16230)
- disable RPATH for installed libs (LDRPATH_INSTALL=)

* Wed Jul 02 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- initial build from vanilla source for ALT Linux Sisyphus
