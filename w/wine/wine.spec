%define _unpackaged_files_terminate_build 1
%if "%_vendor" == "alt"
# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
%filter_from_requires /^ntdll.so.*/d
%filter_from_requires /^win32u.so.*/d
%global __find_debuginfo_files %nil
%endif

%def_with devel
%def_without vanilla
%define gecko_version 2.47.4
%define mono_version 8.1.0
%define winetricks_version 20240105

# https://dl.winehq.org/wine/source/
%define basemajor 9.0
%define major 9.0
%define rel %nil
%define stagingrel %rel
# the packages will conflict with that
%define conflictlist wine-vanilla wine-stable wine-tkg wine-proton-tkg wine-etersoft
%define wow64conflict i586-%name

%define __add_conflict() \
for mod in %{conflictlist}; do \
    echo -n "$mod-%{*} "; \
done; unset mod;\
%nil

%define add_conflict() \
Conflicts: %(%{expand: %%__add_conflict %{*}}) \
%nil

# used in wine staging only
%def_with gtk3

# build ping subpackage
%def_with set_cap_net_raw

# build wow64 package (both 32/64 PE in the one package)
%def_without wow64

%ifarch aarch64
# old clang have some troubles with .seh on aarch64
%define llvm_version 15
%else
%define llvm_version 11
%endif

%if_feature llvm %llvm_version
# build real PE libraries (.dll, not .dll.so), via clang
%def_with mingw
%else
%def_without mingw
%endif

%if_with wow64
%undefine _without_mingw
%def_with mingw
%endif

# TODO: clang: error: unsupported option '-mabi=' for target 'x86_64-unknown-linux-gnu'
#def_with clang

# https://bugs.etersoft.ru/show_bug.cgi?id=15244
%def_with unwind

# keep debugging symbols in PE files (skip strip)
# TODO: check if we need debug info and pack it separately
%def_with debugpe

# use rpm-macros-features
%if_feature vulkan
%def_with vulkan
%endif

%def_without wayland

# use rpm-macros-features

%if_feature opencl
    %def_with opencl
%endif

%if_feature pcap 1.10.3
    %def_with pcap
%else
    %def_without pcap
    %def_without set_cap_net_raw
%endif

# default for unsupported arches
%define winepkgname wine

%ifarch x86_64 aarch64
    %def_with build64
    %define winearch wine64
    %define winepkgname wine
%endif

# workaround for https://bugzilla.altlinux.org/38130
# buildwow64 = _arch = x86_64  && with wow64
%if "%_arch" == "x86_64" && %{expand:%%{?_with_wow64:1}%%{!?_with_wow64:0}}
    %def_with buildwow64
    %undefine _with_build64
    %define winearch wine
%endif

%ifarch %ix86
    %def_without build64
    %define winearch wine32
    %define winepkgname wine
%endif

Name: wine
Version: %major.10
Release: alt1
Epoch: 1

Summary: Wine - environment for running Windows applications

License: LGPLv2+
Group: Emulators
Url: https://www.altlinux.org/Wine

Packager: Vitaly Lipatov <lav@altlinux.ru>

# TODO: major in gear

# Source-url: https://dl.winehq.org/wine/source/%basemajor/wine-%major%rel.tar.xz
Source: %name-%version.tar
# Source1-url: https://github.com/wine-staging/wine-staging/archive/v%major%stagingrel.tar.gz
Source1: %name-staging-%version.tar

Source3: %name-%version-desktop.tar
Source4: %name-%version-icons.tar
# multilib wrapper scripts
Source6: %name-%version-bin-scripts.tar

# local patches
Source10: %name-patches-%version.tar

AutoReq: yes, noperl, nomingw32

# set compilers
%ifarch aarch64
%def_with clang
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

%define libdir %_libdir
%define libwinedir %libdir/wine
%define winebindir %_libexecdir/wine
%if_with build64
    %define wineserver wineserver64
    %define winepreloader wine64-preloader
%endif
%if_with buildwow64
    %define wineserver wineserver
    %define winepreloader wine-preloader
%endif
%if_without build64
    %define wineserver wineserver32
    %define winepreloader wine-preloader
%endif

%define winepe32dir i386-windows
%define winepe64dir %_arch-windows

%define winepedir unsupported-windows
%define winesodir unsupported-unix

# set arch dependent dirs
%ifarch %{ix86}
%define winepedir i386-windows
%define winesodir i386-unix
%endif
%ifarch x86_64
%define winepedir x86_64-windows
%define winesodir x86_64-unix
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
%define llvm_br clang >= %llvm_version llvm >= %llvm_version lld >= %llvm_version

%if_with clang
BuildRequires: %llvm_br
%else
BuildRequires: gcc
%endif

%if_with mingw
BuildRequires: %llvm_br
%endif

# hack against broken patch in wine-staging
# Failed to apply patch eventfd_synchronization/0011-server-Add-an-object-operation-to-grab-the-esync-fil.patch
BuildRequires: git-core

# General dependencies
BuildRequires(pre): rpm-build-intro >= 2.1.14
BuildRequires(pre): rpm-macros-features
BuildRequires: util-linux flex bison
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libattr-devel
BuildRequires: libgphoto2-devel libsane-devel libcups-devel
BuildRequires: libv4l-devel
BuildRequires: libalsa-devel jackit-devel libpulseaudio-devel
BuildRequires: libGLU-devel
BuildRequires: libSDL2-devel
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
BuildRequires: libnetapi-devel
#BuildRequires: gstreamer-devel gst-plugins-devel

# for winscard (libpcsclite.so here)
BuildRequires: libpcsclite-devel

# can be missed on old systems
BuildRequires: libOSMesa-devel

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

#Requires: wine-gecko = %gecko_version

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: %name-common = %EVR

%if_with buildwow64
Conflicts: %wow64conflict
%endif

Conflicts: %conflictlist

# old gl part
Provides: %winepkgname-gl = %EVR
Obsoletes: %winepkgname-gl < %EVR

Conflicts: libwine-vanilla-gl libwine-gl
Conflicts: wine-vanilla-gl wine-gl
Obsoletes: lib%name-gl

# old twain part
Provides: %winepkgname-twain = %EVR
Obsoletes: %winepkgname-twain < %EVR

Conflicts: libwine-vanilla-twain libwine-twain
Conflicts: wine-vanilla-twain wine-twain
Obsoletes: lib%name-twain

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

This build based on wine source with wine-staging project patches
and ALT in progress patches.

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

Requires: wine-mono = %mono_version
Requires: wine-gecko = %gecko_version
Requires: winetricks >= %winetricks_version

%add_conflict full

%description full
Wine meta package. Use it for install all wine subpackages.


%package common
Summary: Common wine files and scripts
Summary(ru_RU.UTF-8): Общие файлы и скрипты Wine
Group: Emulators
BuildArch: noarch
%add_conflict common
# we don't need provide anything
AutoProv:no
Conflicts: libwine <= 6.14.1
Conflicts: i586-libwine <= 6.14.1
Conflicts: wine <= 6.14.1
Conflicts: i586-wine <= 6.14.1

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
%setup -a 1 -a 10
# Apply wine-staging patches
%name-staging/staging/patchinstall.py DESTDIR=$(pwd) --all --backend=patch

# disable rpath using for executable
#__subst "s|^\(LDRPATH_INSTALL =\).*|\1|" Makefile.in

# Apply local patches
%name-patches/patchapply.sh

%build
%if_with clang
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif
%if_with mingw
export CROSSCC=clang
%endif

# disable fortify as it can breaks wine
# http://bugs.winehq.org/show_bug.cgi?id=24606
%remove_optflags -fcf-protection
%remove_optflags -fstack-protector-strong
%remove_optflags -fstack-clash-protection
# drop default FORTIFY_SOURCE here to mute warning when overrides with _FORTIFY_SOURCE=0 (wine disable it)
%remove_optflags -Wp,-D_FORTIFY_SOURCE=2
%remove_optflags -D_FORTIFY_SOURCE=2


%configure --with-x \
	--disable-win16 \
%if_with build64
	--enable-win64 \
%endif
%if_with buildwow64
	--enable-archs=i386,x86_64 \
%endif
	--disable-tests \
	--without-gstreamer \
	--without-oss --with-alsa --with-pulse \
	--with-cups \
	--without-capi \
	%{subst_with opencl} \
	%{subst_with pcap} \
	%{subst_with mingw} \
	%{subst_with vulkan} \
	%{subst_with wayland} \
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

# return wine64 and wine64-preloader (half revert of upstream 5884e98fbec966b0ad9f3babcbec7d8fe25dbc1d)
%ifarch aarch64
mv -v %buildroot%winebindir/wine %buildroot%winebindir/wine64
mv -v %buildroot%winebindir/wine-preloader %buildroot%winebindir/wine64-preloader
mv -v %buildroot%winebindir/wine_make_autoreq_happy %buildroot%_bindir/wine64_make_autoreq_happy
%endif

# hack: move all programs back to _bindir
find %buildroot%winebindir -mindepth 0 -maxdepth 1 -not -type d | \
    egrep -v '/wine$|/wine-preloader$|/wineserver$|/wine64$|/wine64-preloader$|/wineserver64|/winegcc|/wineg++|/winecpp|/winebuild$' | \
    xargs mv -v -t %buildroot%_bindir/
[ -s %buildroot%_bindir/wineg++ ] || ln -sv --relative %buildroot%winebindir/wineg++ %buildroot%_bindir/
[ -s %buildroot%_bindir/winecpp ] || ln -sv --relative %buildroot%winebindir/winecpp %buildroot%_bindir/


# FIXME: it is missed on 64 bit (it is supposed to be installed with wine 32)
%if_with build64
install -p -m 0644 loader/wine.man %buildroot%_man1dir/wine.1
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
    sed -e "s:@BINDIR@:%winebindir:g" $i > $tbin
    chmod +x $tbin
done

# wine64 and wine64-preloader are already built as wine64* on x86_64 only
%if "%wineserver" != "wineserver"
mv -v %buildroot%winebindir/wineserver %buildroot%winebindir/%wineserver
# some systems requires wineserver in winebindir
[ -s %buildroot%winebindir/wineserver ] || cp %buildroot%_bindir/wineserver %buildroot%winebindir/wineserver
%endif
%if_with build64
[ -s %buildroot%_bindir/wine64 ] || ln -sv --relative %buildroot%winebindir/wine64 %buildroot%_bindir/
%endif

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
%winebindir/wine64
%_bindir/wine64
%else
%winebindir/wine
%endif
%winebindir/%wineserver
%winebindir/%winepreloader

# eterbug #14676
%if_with build64
%_bindir/wine64_make_autoreq_happy
%else
%_bindir/wine_make_autoreq_happy
%endif

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
%libwinedir/%winesodir/bcrypt.so
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
%libwinedir/%winesodir/wineusb.so
%libwinedir/%winesodir/wineps.so
%libwinedir/%winesodir/localspl.so
%libwinedir/%winesodir/winscard.so

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
%_bindir/wine-preloader

%_bindir/wineapploader

%_bindir/regsvr32
%_bindir/winecfg
%_bindir/regedit
%_bindir/msiexec

%_bindir/wineconsole

%_bindir/winedbg
%_bindir/wineboot
%_bindir/winepath

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


%dir %_datadir/wine/
%_datadir/wine/wine.inf
%_datadir/wine/nls/
%_datadir/wine/fonts/



%files full

%files programs
%_bindir/notepad
%_bindir/winefile
%_bindir/winemine
%_man1dir/notepad.*
%_man1dir/winefile.*
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
%ifarch %{ix86} x86_64
%libwinedir/%winesodir/lib*.a
%endif

%changelog
* Mon Aug 19 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.10-alt1
- update patches to staging wine-9.0
  + partially revert 46c8a637525d0f1cf67830295fb460c819b800b6. (eterbug #17552)

* Fri Mar 01 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.9-alt1
- update patches to staging wine-9.0
  + compstui: Add more string resources. (eterbug #17016)
  + revert "prntvpt: Prefer builtin. (eterbug #14957)"

* Mon Feb 26 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.8-alt1
- update patches to staging wine-9.0
  - wineps.drv: Return default resolution if PPD doesn't provide the list of supported resolutions. (eterbug #17039)

* Tue Feb 20 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.7-alt1
- update patches to staging wine-9.0
  + windowscodecs: Implement IWICBitmapFlipRotator(WICBitmapTransformRotate90) for bitmaps with bpp >= 8. (eterbug #17003)
  + windowscodecs/tests: Add a test for IWICBitmapFlipRotator(WICBitmapTransformRotate90). (eterbug #17003)
- require winetricks 20240105

* Thu Feb 08 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.6-alt2
- spec: cleanup PE packing
- spec: force PE compilation for aarch64
- spec: skip build on aarch64 if clang is too old
- spec: disable win16 build
- spec: add wow64 support
- spec: don't require wine-etersoft-gecko from the main package
- spec: add wineserver in winebindir

* Mon Feb 05 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.6-alt1
- update patches to staging wine-9.0:
  + prntvpt: Add version resource. (eterbug #16463)
- spec: need lvvm 15.0 on aarch64

* Tue Jan 30 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.5-alt1
- disable clang using for aarch64
- update patches to staging wine-9.0
  + prntvpt: Also initialize dmDefaultSource field. (eterbug #14957)
  + prntvpt: Forward BindPTProviderThunk to PTOpenProviderEx. (eterbug #14957)
  + prntvpt: Forward UnbindPTProviderThunk to PTCloseProvider. (eterbug #14957)
  + prntvpt: Implement ConvertDevModeToPrintTicketThunk2. (eterbug #14957)
  + prntvpt: Implement ConvertPrintTicketToDevModeThunk2. (eterbug #14957)
  + prntvpt: Implement GetPrintCapabilitiesThunk2. (eterbug #14957)
  + prntvpt: Prefer builtin. (eterbug #14957)

* Wed Jan 17 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.4-alt1
- build 9.0 release

* Mon Jan 15 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.3-alt1
- build 9.0-rc5

* Mon Jan 08 2024 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.2-alt1
- build 9.0-rc4
- switch to use conflictlist

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:9.0.1-alt1
- build 9.0-rc3

* Sat Nov 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.21.1-alt1
- new version 8.21.1 (with rpmrb script)
- set strict require wine-mono 8.1.0 (needed since 8.19)

* Sun Nov 12 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.20.1-alt1
- new version 8.20.1 (with rpmrb script)

* Sun Nov 05 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.19.1-alt1
- new version 8.19.1 (with rpmrb script)

* Wed Nov 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.18.1-alt1
- new version 8.18.1 (with rpmrb script)
- add clang requires for devel-tools for mingw build (ALT bug 47472)

* Mon Oct 30 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.17.1-alt1
- new version 8.17.1 (with rpmrb script)
- fix clang/gcc requires for devel-tools (winegcc)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.16.1-alt1
- new version 8.16.1 (with rpmrb script)

* Mon Sep 04 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.15.1-alt1
- new version 8.15.1 (with rpmrb script)

* Thu Aug 31 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.14.1-alt2
- remove post/preun scripts for wine-ping

* Mon Aug 21 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.14.1-alt1
- new version (8.14.1) with rpmgs script

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.13-alt1
- new version 8.13 (with rpmrb script)

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.9.2-alt1
- new version (8.9.2) with rpmgs script
- update wine staging patches to 8.9.1

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.9.1-alt1
- new version 8.9.1 (with rpmrb script)
- set strict require wine-mono 8.0.0
- require winetricks 20230505

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.6.1-alt1
- new version 8.6.1 (with rpmrb script)
- add BuildRequires: libpcsclite-devel
- set strict require wine-gecko 2.47.4

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.2.1-alt1
- new version 8.2 (with rpmrb script)
- upgrade libpcap require to 1.10.3 (due pcap_init())
- add BuildRequires: libOSMesa-devel
- update patches to staging wine-8.2
  + fix build on 32 bit systems with llvm (https://bugs.winehq.org/show_bug.cgi?id=54889)
  + msv1_0: disable annoying message about missed ntlm_auth

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.1-alt1
- new version 8.1 (with rpmrb script)

* Wed Jan 25 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0.4-alt1
- 8.0 release
- .desktop: update descriptions (ALT bug 39800)

* Sun Jan 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0.3-alt1.rc5
- new version (8.0-rc4) with rpmgs script

* Sat Jan 21 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0.2-alt1.rc4
- new version (8.0-rc4) with rpmgs script

* Sun Jan 08 2023 Vitaly Lipatov <lav@altlinux.ru> 1:8.0.1-alt1.rc3
- new version (8.0-rc3) with rpmgs script

* Tue Dec 20 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.22.1-alt1
- new version 7.22.1 (with rpmrb script)
- update patches to staging wine-7.22
 - msv1_0: disable annoying message about missed ntlm_auth
 + build fake binary makes autoreq happy
- drop manual requires in favour of real autoreqs

* Sun Nov 06 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.20.1-alt1
- new version 7.20.1 (with rpmrb script)
- set strict require wine-mono 7.4.0

* Wed Oct 19 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.19.1-alt1
- new version 7.19.1 (with rpmrb script)

* Sat Sep 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.18.1-alt1
- new version 7.18.1 (with rpmrb script)
- restore libwine.so.1 packing for compatibility reasons

* Mon Sep 12 2022 Alexey Shabalin <shaba@altlinux.org> 1:7.17.1-alt2
- not requires libldap, use autoreq

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.17.1-alt1
- new version 7.17.1 (with rpmrb script)

* Tue Sep 06 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.16.1-alt2
- build with opencl

* Mon Aug 29 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.16.1-alt1
- new version 7.16.1 (with rpmrb script)

* Sun Aug 14 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.15.1-alt1
- new version 7.15.1 (with rpmrb script)

* Sat Jul 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.14.1-alt1
- new version 7.14.1 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.13.1-alt1
- new version 7.13.1 (with rpmrb script)
- add obsoletes for libwine, wine, i586-libwine, i586-wine < 6.14.1
- set strict require wine-gecko 2.47.3

* Sat Jul 02 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.11.1-alt1
- new version 7.11.1 (with rpmrb script)

* Sat Jul 02 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.10.1-alt1
- new version 7.10.1 (with rpmrb script)

* Fri Jun 24 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.7.1-alt1
- new version 7.7.1 (with rpmrb script)

* Wed Jun 15 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.6.1-alt2
- drop Requires: webclient
- add conflicts for wine-common
- fix build without PE

* Mon Apr 11 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.6.1-alt1
- new version 7.6.1 (with rpmrb script)
- set strict require wine-mono 7.2.0

* Fri Apr 01 2022 Vitaly Lipatov <lav@altlinux.ru> 1:7.5.1-alt1
- new version 7.5
- drop out unneeded build requires (many libs is embedded now)
- drop out unneeded requires
- set strict require wine-mono 7.1.1

* Thu Mar 31 2022 Vitaly Lipatov <lav@altlinux.ru> 1:6.23.1-alt2
- set version for provided libwine-devel
- skip linking wine64 to bindir if it is already exists
- don't pack libwinecrt0.a twice
- fix checking for build64mingw, fix build
- fix build without PE
- pack lib*.a needed for build with wine

* Fri Mar 04 2022 Vitaly Lipatov <lav@altlinux.ru> 1:6.23.1-alt1
- new version (6.23.1) with rpmgs script
- fix build (add hack with ntdll.so and disable debuginfo subpackages)

* Sat Nov 27 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.22.1-alt1
- new version (6.22.1) with rpmgs script
- add check for libpcap and llvm versions

* Sun Nov 07 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.21-alt1
- new version 6.21 (with rpmrb script)

* Thu Sep 30 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17.1-alt4
- use rpm-macros-feature for vkd3d checking
- return to wine package name

* Fri Sep 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17.1-alt3
- improve package conflicts, make spec wine-vanilla compatible

* Tue Sep 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17.1-alt2
- disable strip PE modules

* Sat Sep 11 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.17.1-alt1
- new version 6.17.1 (with rpmrb script)

* Fri Sep 10 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.16.2-alt1
- update patchset: eterbugs #15185, 15271, 15286
- strip debug info from PE modules

* Mon Aug 30 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.16.1-alt2
- skip strip all PE files from winepedir (we need debug info)
- add script wine-cap_net_raw in wine-ping package (eterbug #15254)
- rewrite clang build requires to p9 compatibility

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.16.1-alt1
- new version 6.16.1 (with rpmrb script)

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.2-alt3
- enable PE dlls build (via clang)
- add workaround for altbug #38130 (avoid nested if)

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.2-alt2.2
- enable build with libunwind
- rearrange BR: add libattr, libxjr, add libSDL2, libgcrypt, libsasl2, valgrind
- disable build with opencl if build PE
- allow enable PE dlls build (via clang)
- add subpackage wine-ping to allow ping via setcap cap_net_raw=ep in post script

* Sun Aug 29 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.2-alt2.1
- disable LTO (test it later)
- move secondary definitions below, drop alt only section
- wine-devel now requires base wine package
- fix clang requires (basically, for p9)
- provide and obsolete libname if we don't pack libname
- small cleanup

* Mon Aug 23 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.2-alt1
- update patches to staging wine-6.15

* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.1-alt2
- enable wine biarch based on changes by @lav@ and @darktemplar (ALT bug #37035)
- add wine-common noarch package
- add wine-devel-tools package (with toolchain)
- rename libwine-devel to wine-devel and make it noarch
- rename libwine-gl to wine-gl
- rename libwine-twain to wine-twain
- move all files exclude libwine.so.1 from libwine to main package wine

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.15.1-alt1
- new version 6.15.1 (with rpmrb script)

* Sat Jul 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.14.1-alt1
- new version 6.14.1 (with rpmrb script)
- set strict require wine-mono 6.3.0

* Thu Jul 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.13.1-alt1
- new version 6.13.1 (with rpmrb script)

* Sat Jul 03 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.12.1-alt1
- new version 6.12.1 (with rpmrb script)

* Fri Jun 25 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.11.1-alt2
- fix packing

* Tue Jun 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.11.1-alt1
- new version 6.11.1 (with rpmrb script)
- set strict require wine-mono 6.2.0

* Sun Apr 25 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.7.1-alt1
- new version 6.7.1 (with rpmrb script)

* Fri Apr 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.6.1-alt1
- new version 6.6.1 (with rpmrb script)
- set strict require wine-mono 6.1.1

* Tue Apr 13 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.5.1-alt1
- new version 6.5.1 (with rpmrb script)

* Thu Apr 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.5.2-alt1
- update patches to staging wine-6.5
 + fix dotnet 4.5 install (https://bugs.winehq.org/show_bug.cgi?id=49897)

* Wed Mar 31 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.5.1-alt1
- new version 6.5.1 (with rpmrb script)

* Wed Mar 17 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.4.1-alt1
- new version 6.4.1 (with rpmrb script)

* Fri Feb 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.2.1-alt1
- new version 6.2.1 (with rpmrb script)
- set strict require wine-mono 6.0.0

* Thu Jan 21 2021 Vitaly Lipatov <lav@altlinux.ru> 1:6.0.1-alt1
- new version 6.0.1 (with rpmrb script)
- set strict require wine-gecko 2.47.2

* Sat Nov 21 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.22.1-alt1
- new version 5.22.1 (with rpmrb script)

* Mon Nov 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.21.1-alt1
- new version 5.21.1 (with rpmrb script)

* Sat Oct 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.20.0.1-alt1
- new version 5.20.0.1 (with rpmrb script)

* Sat Oct 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.19.1-alt1
- new version 5.19.1 (with rpmrb script)
- add gcc-c++ require to devel package (due winegcc)
- update Basealt patches to staging wine-5.19

* Thu Oct 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.5-alt1
- update Basealt patches to staging wine-5.18

* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.4-alt1
- add scripts/wine_setup (check and install all needed packages)
- revert "add reg files for initial file open integration"
- update patches to staging wine-5.18:
 + wine.inf.in: disable decorated window for maincontroller.exe (eterbug #14662)
 + add Office and media file associations (eterbug #14583)

* Sun Oct 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.3-alt1
- update patches to staging wine-5.18
- add reg files for initial file open integration
- drop Requires: glibc-pthread (we already have auto reqs for it)
- update summary and description (ALT bug 34281)

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.2-alt1
- update Basealt patches

* Thu Oct 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.18.1-alt3
- Re-enabled vkd3d.

* Thu Oct 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.1-alt2
- crypt32: fix CertGetCertificateContextProperty for CERT_KEY_PROV_INFO_PROP_ID property

* Mon Sep 28 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.18.1-alt1
- new version 5.18.1 (with rpmrb script)
- console no longer requires the curses library
- build with vkd3d disabled (see ALT bug 39002)

* Tue Sep 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.17.1-alt1
- new version 5.17.1 (with rpmrb script)
- add fix for dotnet install issue (eterbug #11790)

* Wed Sep 09 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.16.1-alt3
- just require libvulkan1 as all other libs
- backport small fixes from future biarch build

* Tue Sep 08 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.16.1-alt2
- build vulkan only for p9 and Sisyphus

* Sun Aug 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.16.1-alt1
- new version 5.16.1 (with rpmrb script)

* Fri Aug 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.12.1-alt2
- Rebuilt with vulkan, vkd3d and faudio support (ALT bug #38810).

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.12.1-alt1
- new version 5.12.1 (with rpmrb script)
- set strict require wine-mono 5.1.0

* Thu Jul 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.10.1-alt1
- new version 5.10.1 (with rpmrb script)

* Tue May 26 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.9.1-alt1
- new version 5.9.1 (with rpmrb script)

* Sun May 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.8.1-alt1
- new version 5.8.1 (with rpmrb script)

* Tue May 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.7.1-alt1
- new version 5.7.1 (with rpmrb script)
- update wine-mono require to 5.0.0

* Mon Mar 30 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.5.1-alt1
- new version 5.5.1 (with rpmrb script)

* Mon Mar 16 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.4.1-alt1
- new version 5.4.1 (with rpmrb script)

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.3.1-alt2
- add BR: libnetapi-devel
- add requires for detected libraries

* Sun Mar 01 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.3.1-alt1
- new version 5.3.1 (with rpmrb script)

* Mon Feb 17 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.2.1-alt1
- new version 5.2.1 (with rpmrb script)

* Tue Feb 04 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.1.2-alt1
- new version 5.1.2 (with rpmrb script)

* Wed Jan 22 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.0.2-alt1
- new version 5.0.2 (with rpmrb script)
- wine 5.0 release

* Sun Jan 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1:5.0.1-alt1
- new version (5.0.1) with rpmgs script
- based on wine 5.0-rc6
- update wine-gecko require to 2.47.1

* Mon Nov 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.20.1-alt1
- new version (4.20.1) with rpmgs script
- update patch set
- update wine-mono require to 4.9.4

* Sun Nov 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.19.2-alt1
- improve patchapply.sh, update patches

* Sat Nov 02 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.19.1-alt1
- new version 4.19.1 (with rpmrb script)
- make GetDriveType() always return DRIVE_FIXED for C: (eterbug #14223)

* Sat Oct 19 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.18.1-alt1
- new version 4.18.1 (with rpmrb script)

* Sat Sep 28 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.17.1-alt1
- new version 4.17.1 (with rpmrb script)
- update wine-mono require to 4.9.3

* Sun Sep 15 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.16.1-alt1
- new version 4.16.1 (with rpmrb script)
- wine/debug.h: Make wine_dbgstr_wn use UTF-8 for output (eterbug #14134)
- reapply ntoskrnl.exe: Ignore CProCtrl initialization failure (eterbug #13466)

* Sun Sep 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.15.1-alt1
- new version 4.15.1 (with rpmrb script)

* Sun Aug 04 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.13.1-alt1
- new version 4.13.1 (with rpmrb script)
- use EVR instead of version-release

* Wed Jul 17 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1.2-alt1
- add patch with cryptext: Implement CryptExtOpenCER

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1.1-alt1
- new version (4.12.1.1) with rpmgs script
- fixe 64 bit build

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.12.1-alt1
- new version 4.12.1 (with rpmrb script)
- enable ExclusiveArch for x86 and aarch64
- remove BR: prelink

* Sat Jun 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.11.1-alt1
- new version 4.11.1 (with rpmrb script)
- strict require wine-mono-4.9.0

* Tue Jun 11 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.10.1-alt1
- new version 4.10.1 (with rpmrb script)

* Wed May 29 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.9.1-alt1
- new version 4.9.1 (with rpmrb script)
- strict require wine-mono-4.8.3

* Wed May 22 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.8.1-alt1
- new version 4.8.1 (with rpmrb script)

* Fri Apr 19 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.6.1-alt1
- new version 4.6.1 (with rpmrb script)
- strict require wine-mono-4.8.1

* Mon Mar 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.4.1-alt1
- new version 4.4.1 (with rpmrb script)
- fix segfault when run wine in a directory with nonlatin letters in their name (ALT bug 36268)

* Tue Mar 05 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.3.1-alt1
- new version (4.3.1) with rpmgs script

* Mon Feb 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Thu Feb 14 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.1.1-alt1
- new version 4.1.1 (with rpmrb script)
- disable file open associations by default (eterbug #13662)

* Wed Jan 23 2019 Vitaly Lipatov <lav@altlinux.ru> 1:4.0.1-alt1
- new version 4.0.1 (with rpmrb script)

* Fri Dec 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.21.2-alt1
- ntoskrnl.exe: Ignore CProCtrl initialization failure (eterbug #13466)
- remove "-firstrundlg" parameter from command line for CryptoPro 5.0 installer (eterbug #13466)
- drop version from internal subdirs

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.21.1-alt1
- new version 3.21.1 (with rpmrb script)

* Fri Nov 09 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.19.1-alt1
- new version 3.19.1 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.18.1-alt1
- new version 3.18.1 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.17.1-alt1
- new version 3.17.1 (with rpmrb script)
- use external winetricks

* Wed Aug 15 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.3-alt1
- ntdll: Don't allow blocking on a critical section during (eterbug #12662)

* Tue Jul 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.2-alt1
- add patch kernel32: Set environment variable PUBLIC on the process (eterbug #13054)

* Sat Jul 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.13.1-alt1
- new version 3.13.1 (with rpmrb script)

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.12.1-alt1
- new version 3.12.1 (with rpmrb script)

* Fri Jun 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.11.1-alt1
- new version (3.11.1) with rpmgs script
- drop -fno-omit-frame-pointer

* Wed Jun 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.10.1-alt1
- new version 3.10.1 (with rpmrb script)
- use clang on aarch64

* Tue May 29 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.9.1-alt1
- new version 3.9.1 (with rpmrb script)

* Fri May 18 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.8.1-alt1
- new version 3.8.1 (with rpmrb script)

* Sat May 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.7.1-alt1
- new version 3.7.1 (with rpmrb script)

* Wed Apr 25 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.6.1-alt1
- new version 3.6.1 (with rpmrb script)
- fix missed wined3d-csmt.dll (ALT bug 34777)

* Sat Mar 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.5.0-alt1
- new version 3.5.0 (with rpmrb script)

* Thu Mar 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.4.1-alt1
- new version 3.4.1 (with rpmrb script)

* Mon Mar 05 2018 Vitaly Lipatov <lav@altlinux.ru> 1:3.3.1-alt1
- new version (3.3)
- build with winehq 3.3 incorporated Kerberos related code only

* Tue Jan 16 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.3-alt1
- update winetricks up to 20171222
- wine.inf: Add the Kerberos SSP/AP registration

* Thu Jan 11 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.1-alt2
- add the font replacement for Microsoft Sans Serif as Tahoma
- update and rewrite Kerberos related patches

* Thu Nov 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.1-alt1
- update winetricks up to 20171018-next
- remove obsoleted patches
- use separated patch list and apply script
- add local_build.sh script

* Fri Nov 24 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.21.0-alt1
- new version (2.21) with rpmgs script
- update Kerberos patches against wine staging 2.21

* Wed Nov 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.20.2-alt1
- add server APC patches (eterbug #12054, redmine #356)

* Mon Nov 06 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.20.1-alt1
- new version (2.20.1) with rpmgs script
- update Kerberos patches against wine staging 2.20

* Wed Oct 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.18.0-alt1
- new version (2.18.0) with rpmgs script
- update Kerberos patches (eterbug #11982)

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.17.1-alt1
- add Kerberos SSPI (via GSSIAPI support)

* Fri Sep 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.17.0-alt1
- new version (2.17.0) with rpmgs script

* Mon Sep 11 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.16.0-alt1
- new version (2.16.0) with rpmgs script
- update winetricks up to 20170823-next
- add dotnet47 support in winetricks

* Sun Aug 27 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.15.0-alt1
- new version (2.15.0) with rpmgs script

* Tue Aug 08 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.14.0-alt1
- new version (2.14.0) with rpmgs script
- enable font smoothing by default
- add libpng16, libjpeg requires

* Sun Jul 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.13.0-alt1
- new version (2.13.0) with rpmgs script
- add fix debug output patches

* Wed Jul 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.12.0-alt1
- new version 2.12.0 (with rpmrb script)

* Thu Jun 29 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.11.0-alt1
- new version (2.11.0) with rpmgs script

* Thu Jun 15 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.10.1-alt1
- new version (2.10.1) with rpmgs script
- replace RegQueryValueEx HKEY_PERFORMANCE hack with wine-staging one

* Tue May 30 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.9.1-alt1
- new version (2.9.1) with rpmgs script

* Fri May 26 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.8.1-alt1
- new version 2.8.1 (with rpmrb script)
- update winetricks to 20170517-next

* Fri May 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.7.1-alt1
- new version (2.7.1) with rpmgs script

* Sun Apr 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.4.1-alt2
- set Epoche:1 for compatibility
- fix build requires
- add if_enabled static
- add Obsoletes for Fedora packages, fix conflicts with wine-vanilla

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
- patches moving:
 + enable linking with freetype and fontconfig
 + add PERF_DATA_BLOCK struct definition
 + add fast hack for RegQueryValueEx-HKEY_PERFORMANCE_DATA_BLOCK
 + make OleLoadPicture load DIBs using WIC decoder

* Sat Apr 08 2017 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- initial build wine-staging for ALT Sisyphus
