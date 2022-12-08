%define _unpackaged_files_terminate_build 1
%if "%_vendor" == "alt"
# hack for lib.req: ERROR: /tmp/.private/lav/wine-etersoft-buildroot/usr/lib64/wine/x86_64-unix/ws2_32.so: library ntdll.so not found
%filter_from_requires /^ntdll.so.*/d
%filter_from_requires /^win32u.so.*/d
%global __find_debuginfo_files %nil
%endif

%def_with vanilla
%define gecko_version 2.47.3
%define mono_version 7.4.0
%define winetricks_version 20220617

%define basemajor 7.x
%define major 7.22
%define rel %nil
%define conflictbase wine

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
    %define winepkgname wine-vanilla
%else
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
BuildRequires: libopenal-devel libGLU-devel
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

# Actually for x86_32
Requires: glibc-pthread glibc-nss

Requires: wine-gecko = %gecko_version
Conflicts: wine-mono < %mono_version

# For menu/MIME subsystem
Requires: desktop-file-utils

Requires: %name-common = %EVR

Conflicts: %conflictbase

# FIXME:
# Runtime linked
Requires: libcups
Requires: libXrender libXi libXext libX11 libICE libXcomposite libXcursor libXinerama libXrandr
Requires: libssl libgnutls30
Requires: libXpm libalsa libcups libopenal1 libpulseaudio libudev1 libusb libkrb5

%if_with gtk3
Requires: libcairo libgtk+3
%endif

%if_with vulkan
Requires: libvulkan1
%endif

# Many programs depends on unixODBC
# Requires: libunixODBC2

%if_with pcap
# Recommended
# Requires: libpcap0.8
%endif

Requires: fontconfig libfreetype

# old gl part
Provides: %winepkgname-gl = %EVR
Obsoletes: %winepkgname-gl < %EVR

Conflicts: libwine-vanilla-gl libwine-gl
Conflicts: wine-vanilla-gl wine-gl
Obsoletes: lib%name-gl

# Runtime linked (via dl_open)
Requires: libGL

%if_without vanilla
Requires: libva
Requires: libtxc_dxtn
%endif


# old twain part
Provides: %winepkgname-twain = %EVR
Obsoletes: %winepkgname-twain < %EVR

Conflicts: libwine-vanilla-twain libwine-twain
Conflicts: wine-vanilla-twain wine-twain
Obsoletes: lib%name-twain

# Runtime linked (via dl_open)
Requires: libsane


# Provides/Obsoletes Fedora packages
%define common_provobs wine-filesystem wine-desktop wine-systemd wine-sysvinit
%define base_provobs wine-alsa wine-capi wine-cms wine-ldap wine-openal wine-pulseaudio wine-wow wine-alsa wine-capi wine-cms wine-ldap wine-openal wine-opencl wine-pulseaudio
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
