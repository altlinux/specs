%define _unpackaged_files_terminate_build 1
%if "%_vendor" == "alt"
# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
%filter_from_requires /^ntdll.so.*/d
%filter_from_requires /^win32u.so.*/d
%global __find_debuginfo_files %nil
%endif

%def_without vanilla
%define gecko_version 2.47.3
%define mono_version 7.4.0
%define winetricks_version 20220617

%define basemajor 7.x
%define major 8.0
%define rel %nil
%define conflictbase wine-vanilla

# build ping subpackage
%def_with set_cap_net_raw

%if_feature llvm 11.0
# build real PE libraries (.dll, not .dll.so), via clang
%def_with mingw
%else
%def_without mingw
%endif

# https://bugs.etersoft.ru/show_bug.cgi?id=15244
%def_with unwind

# keep debugging symbols in PE files (skip strip)
# TODO: check if we need debug info and pack it separately
%def_with debugpe

# use rpm-macros-features
%if_feature vulkan
%def_with vulkan
%endif

# use rpm-macros-features

%if_feature opencl
%def_with opencl
%endif

%if_feature pcap 1.2.1
%def_with pcap
%else
%def_without pcap
%def_without set_cap_net_raw
%endif

%ifarch x86_64 aarch64
    %def_with build64
    %define winearch wine64
    %define winepkgname wine-tkg
%else
    %def_without build64
    %define winearch wine32
    %define winepkgname wine-tkg
%endif

Name: wine-tkg
Version: %major
Release: alt1.rc1
Epoch: 1

Summary: Wine TKG - environment for running Windows applications

License: LGPLv2+
Group: Emulators
Url: https://github.com/Kron4ek/wine-tkg

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/Kron4ek/wine-tkg/archive/refs/heads/master.zip
Source: %name-%version.tar

Source3: %name-%version-desktop.tar
Source4: %name-%version-icons.tar
# multilib wrapper scripts
Source6: %name-%version-bin-scripts.tar

# local patches
#Source10: %name-patches-%version.tar

Patch1: 0011-build-fake-binary-makes-autoreq-happy.patch

AutoReq: yes, noperl, nomingw32

ExclusiveArch: %ix86 x86_64 aarch64

# set compilers
%ifarch aarch64
%def_with clang
# clang-12: error: unsupported argument 'auto' to option 'flto='
%define optflags_lto -flto=thin
%endif

# disable LTO: link error in particular, and unverified in general
#x86_64-alt-linux-gcc -m64 -o loader/wine64-preloader loader/preloader.o loader/preloader_mac.o -static -nostartfiles -nodefaultlibs \
#  -Wl,-Ttext=0x7d400000
#ld: /usr/src/tmp/wine64-preloader.yxZ9KH.ltrans0.ltrans.o: in function `_start':
#<artificial>:(.text+0x12): undefined reference to `thread_data'
#ld: <artificial>:(.text+0x2a): undefined reference to `wld_start'
%define optflags_lto %nil

# TODO: also check build64
# workaround for https://bugzilla.altlinux.org/38130
# notbuild64mingw = without mingw && without build64
%if %{expand:%%{?_without_mingw:1}%%{!?_without_mingw:0}} && %{expand:%%{?_without_build64:1}%%{!?_without_build64:0}}
    %define notbuild64mingw 1
%endif

%define libdir %_libdir
%define libwinedir %libdir/wine
%define winebindir %_libexecdir/wine
%if_with build64
    %define wineserver wineserver64
    %define winepreloader wine64-preloader
%else
    %define wineserver wineserver32
    %define winepreloader wine-preloader
%endif

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
%add_findreq_skiplist %libwinedir/%winepedir/*

#
# /usr/bin/strip: ./usr/lib64/wine/x86_64-windows/stqrTIUz/stPNVRry/dsound.dll: warning: line number count (0x10000) exceeds section size (0x8)
# /usr/bin/strip: ./usr/lib64/wine/x86_64-windows/stbguFIA: file format not recognized
# see also our strip below
%if_with debugpe
%brp_strip_none %libwinedir/%winepedir/*
%endif

# we don't need provide anything
AutoProv:no

# for wine-staging gitapply.sh script
BuildRequires: /proc

# used llvm/clang toolchain if needed
%define llvm_version 11
%define llvm_br clang >= %llvm_version llvm >= %llvm_version lld >= %llvm_version

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
# TODO: osmesa

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

Requires: wine-gecko = %gecko_version
Conflicts: wine-mono < %mono_version

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: %name-common = %EVR

Conflicts: %conflictbase

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

This build uses wine-tkg-staging-fsync configuration
from https://github.com/Kron4ek/wine-tkg/blob/master/wine-tkg-config.txt.

%package test
Summary: WinAPI test for Wine
Summary(ru_RU.UTF-8): Тест WinAPI для Wine
Group: Emulators
Requires: %name = %EVR
Conflicts: %conflictbase-test

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

Conflicts: %conflictbase-full

%description full
Wine meta package. Use it for install all wine subpackages.


%package common
Summary: Common wine files and scripts
Summary(ru_RU.UTF-8): Общие файлы и скрипты Wine
Group: Emulators
BuildArch: noarch
Conflicts: %conflictbase-common
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

Conflicts: %conflictbase-programs

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
Conflicts: %conflictbase-ping

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
Conflicts: %conflictbase-devel-tools
Conflicts: lib%conflictbase-devel
Conflicts: lib%name-devel < %version
%if_without vanilla
Provides: libwine-devel = %EVR
%endif
# we don't need provide anything
AutoProv:no

# due winegcc requires
Requires: gcc gcc-c++ glibc-devel libstdc++-devel


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
Conflicts: lib%conflictbase-devel
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
# Apply local patches
#name-patches/patchapply.sh

%build
%if_with clang
%remove_optflags -frecord-gcc-switches
export CC=clang
%endif
%if_with mingw
export CROSSCC=clang
%endif


%configure --with-x \
%if_with build64
	--enable-win64 \
%endif
	--disable-tests \
	--without-gstreamer \
	--without-oss --with-alsa --with-pulse \
	--with-cups \
	--without-capi \
	%{subst_with opencl} \
	%{subst_with pcap} \
	%{subst_with unwind} \
	%{subst_with mingw} \
	%{subst_with vulkan} \
	--bindir=%winebindir \
	%nil

%__make depend
%make_build


%install
%makeinstall_std

# clean permissions (via find to hide file list)
find %buildroot%libwinedir/%winesodir -type f | xargs chmod 0644
find %buildroot%libwinedir/%winepedir -type f | xargs chmod 0644

%if_with libwine
# keep in libdir for compatibility
mv -v %buildroot%libwinedir/%winesodir/libwine.so.1* %buildroot%libdir
%else
rm -v %buildroot%libwinedir/%winesodir/libwine.so.1*
%endif

# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
%if "%_vendor" == "alt"
cp -v %buildroot%libwinedir/%winesodir/ntdll.so %buildroot%libdir
cp -v %buildroot%libwinedir/%winesodir/win32u.so %buildroot%libdir
%endif

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

# wine64 and wine64-preloader are already built as wine64* on x86_64 only
mv -v %buildroot%winebindir/wineserver %buildroot%winebindir/%wineserver
%if_with build64
[ -s %buildroot%_bindir/wine64 ] || ln -sv --relative %buildroot%winebindir/wine64 %buildroot%_bindir/
%endif


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

%post ping
%_sbindir/wine-cap_net_raw on || :

%preun ping
if [ $1 = 0 ]; then
    %_sbindir/wine-cap_net_raw off || :
fi
%endif

%files
%if "%winebindir" != "%libwinedir"
%dir %winebindir/
%endif
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
%dir %libwinedir/%winepedir/

%if "%_vendor" == "alt"
%exclude %libdir/ntdll.so
%exclude %libdir/win32u.so
%endif

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

%if_without mingw
%{?_without_vanilla:%libwinedir/%winesodir/windows.networking.connectivity.so}
%libwinedir/%winesodir/*.com.so
%libwinedir/%winesodir/*.cpl.so
%libwinedir/%winesodir/*.ocx.so
%libwinedir/%winesodir/*.ax.so
%libwinedir/%winesodir/*.exe.so
%libwinedir/%winesodir/*.acm.so
%libwinedir/%winesodir/*.drv.so
%libwinedir/%winesodir/*.ds.so
%libwinedir/%winesodir/*.sys.so
%libwinedir/%winesodir/*.dll.so
%endif

%if_without build64
%libwinedir/%winepedir/*.dll16
%libwinedir/%winepedir/*.drv16
%libwinedir/%winepedir/*.exe16
%libwinedir/%winepedir/winoldap.mod16
%libwinedir/%winepedir/*.vxd
%endif

%ifdef notbuild64mingw
%libwinedir/%winesodir/*.dll16.so
%libwinedir/%winesodir/*.drv16.so
%libwinedir/%winesodir/*.exe16.so
%libwinedir/%winesodir/winoldap.mod16.so
%libwinedir/%winesodir/*.vxd.so
%endif


%libwinedir/%winepedir/*.com
%libwinedir/%winepedir/*.cpl
%libwinedir/%winepedir/*.drv
%libwinedir/%winepedir/*.dll
%libwinedir/%winepedir/*.acm
%libwinedir/%winepedir/*.ocx
%libwinedir/%winepedir/*.tlb
%libwinedir/%winepedir/*.sys
%libwinedir/%winepedir/*.exe
%libwinedir/%winepedir/*.ax
%libwinedir/%winepedir/*.ds
%if_without vanilla
%libwinedir/%winepedir/windows.networking.connectivity
%endif
%libwinedir/%winepedir/light.msstyles


%files common
%doc ANNOUNCE AUTHORS LICENSE README
%lang(de) %doc documentation/README.de
%lang(es) %doc documentation/README.es
%lang(fr) %doc documentation/README.fr
%lang(hu) %doc documentation/README.hu
%lang(it) %doc documentation/README.it
%lang(ko) %doc documentation/README.ko
%lang(nb) %doc documentation/README.no
%lang(pt) %doc documentation/README.pt
%lang(pt_BR) %doc documentation/README.pt_br
%lang(tr) %doc documentation/README.tr

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
#%_aclocaldir/wine.m4

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
%if_with mingw
%libwinedir/%winepedir/lib*.a
%endif
%libwinedir/%winesodir/lib*.a

%changelog
* Wed Dec 21 2022 Vitaly Lipatov <lav@altlinux.ru> 1:8.0-alt1.rc1
- initial build based on wine-vanilla spec
