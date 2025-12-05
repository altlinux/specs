# TODO:
%define optflags_lto %nil
Name: wine-cpcsp_proxy
Version: 0.7.7
Release: alt1

Summary: Proxy for using Linux CryptoPro in Windows applications with Wine

License: LGPLv2
Group: Emulators
URL: https://github.com/Etersoft/wine-cpcsp_proxy

# Source-git: https://github.com/Etersoft/wine-cpcsp_proxy.git
Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

%define libwinedir %_libdir/wine

# TODO: use mingw detection from wine or just wait for total PE using
%def_with pebuild

# check if we need wow64 build also
%if "%(test -d %libwinedir/i386-windows && echo 1)" == "1"
%def_with wow64
%endif

# default for unsupported arches
%define winepkgname wine-cpcsp_proxy
%define winedevpkgname wine-devel-tools

%ifarch x86_64 aarch64
    %def_with build64
    %define winearch wine64
    %define winepkgname wine-cpcsp_proxy
    %define winedevpkgname wine-devel-tools
%endif

# workaround for https://bugzilla.altlinux.org/38130
# buildwow64 = _arch = x86_64  && with wow64
%if "%_arch" == "x86_64" && %{expand:%%{?_with_wow64:1}%%{!?_with_wow64:0}}
    %def_with buildwow64
    %undefine _with_build64
%endif

%ifarch %ix86
    %def_without build64
    %define winepkgname wine-cpcsp_proxy
    %define winedevpkgname wine-devel-tools
%endif

BuildRequires: %winedevpkgname >= 9

# lib.req: ERROR: /tmp/.private/lav/wine-cpcsp_proxy-buildroot/usr/lib64/wine/x86_64-unix/cpcsp_proxy.so: library ntdll.so not found
AutoReq: no

# TODO: move to rpm-macros-wine
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
%define winepe32dir i386-windows

%add_verify_elf_skiplist %libwinedir/%winesodir/cpcsp_proxy.so
%add_verify_elf_skiplist %libwinedir/%winesodir/cpcsp_proxy.dll.so

%ifarch x86_64
%define capilitepkg lsb-cprocsp-capilite-64
%else
%define capilitepkg lsb-cprocsp-capilite
%endif

#Conflicts: wine-p11csp

%description
Proxy for using Linux CryptoPro in Windows applications with wine.

* Use with CryptoPro:
 install %capilitepkg package before
* Use with cprocsp_compat (CRYPTO@Etersoft):
 install cprocsp_compat before


%if "%winepkgname" != "%name"
%package -n %winepkgname
Group: Emulators
Summary: Proxy for using Linux CryptoPro in Windows applications with Wine

# lib.req: ERROR: /tmp/.private/lav/wine-etersoft-cpcsp_proxy-buildroot/usr/lib/wine-etersoft/i386-unix/cpcsp_proxy.so: library ntdll.so not found
AutoReq: no

%description -n %winepkgname
Proxy for using Linux CryptoPro in Windows applications with wine.

* Using with CryptoPro:
 install %capilitepkg package
* Using with cprocsp_compat (CRYPTO@Etersoft):
 install cprocsp_compat

%endif


%prep
%setup
%if_with buildwow64
cp -a cpcsp_proxy cpcsp_proxy_wow64
%endif

%build
%make_build -C cpcsp_proxy \
    LIBDIR=%_libdir \
%if_with pebuild
    TARGETDLL=cpcsp_proxy.dll \
%else
    TARGETDLL="cpcsp_proxy.dll cpcsp_proxy.dll.so" \
%endif
    %nil

%if_with buildwow64
%make_build -C cpcsp_proxy_wow64 \
    LIBDIR=%_libdir \
    WOW64BUILD=yes \
    TARGETDLL=cpcsp_proxy.dll \
    cpcsp_proxy.dll
    %nil
%endif

%install
mkdir -p %buildroot%libwinedir/{%winesodir,%winepedir}

cp cpcsp_proxy/cpcsp_proxy.so %buildroot%libwinedir/%winesodir
cp cpcsp_proxy/cpcsp_proxy.dll %buildroot%libwinedir/%winepedir
%if_with buildwow64
mkdir -p %buildroot%libwinedir/%winepe32dir
cp cpcsp_proxy_wow64/cpcsp_proxy.dll %buildroot%libwinedir/%winepe32dir
%endif

%if_without pebuild
cp cpcsp_proxy/cpcsp_proxy.dll.so %buildroot%libwinedir/%winesodir
%endif

mkdir -p %buildroot/%_bindir/
install -D cpcsp_proxy_setup/cpcsp_proxy_setup %buildroot/%_bindir/cpcsp_proxy_setup

%files -n %winepkgname
%libwinedir/%winesodir/cpcsp_proxy.so
%libwinedir/%winepedir/cpcsp_proxy.dll
%if_with buildwow64
%libwinedir/%winepe32dir/cpcsp_proxy.dll
%endif
%if_without pebuild
%libwinedir/%winesodir/cpcsp_proxy.dll.so
%endif
%_bindir/cpcsp_proxy_setup

%changelog
* Fri Nov 28 2025 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt1
- enable PE build, add build wow64 (ALT bug 56873)
- update sources to 11.09.2025

* Fri Jul 12 2024 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- update the code to the new unixcall mode

* Sat Jan 13 2024 Vitaly Lipatov <lav@altlinux.ru> 0.6.1-alt1
- README.md: fix typos
- cpcsp_proxy/api_hook.h: remove DECLSPEC_HIDDEN

* Sat Apr 09 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt3
- build and install wine stubs

* Thu Apr 07 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt2
- update README.md
- fix Makefile to build package

* Tue Feb 22 2022 Vitaly Lipatov <lav@altlinux.ru> 0.6.0-alt1
- update for wine-6.21
- further adaptation for wine-6.21 build system
- add .dll.so -> .dll link
- update build for wine-7.2

* Tue Oct 06 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.2-alt1
- add traces to public info converters, verify parameters from the backend
- print information about being saved certificate (eterbug #14660)
- also import CA store from host

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5.1-alt1
- change debug channel to cpcsp_proxy
- move propid_to_name() to print_id_name.h

* Sat Oct 03 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt2
- add README.md
- update description

* Thu Oct 01 2020 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- cpcsp_proxy_setup: Add explicit __cdecl to main() for 64-bit compatibility
- cpcsp_proxy_setup: allow loading both libcapi10 and libcapi20
- cpcsp_proxy_setup.c: load CryptEnumProvidersA from libcapi10

* Sat Sep 12 2020 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- rewrite spec
- cleanup makefiles
- replace wine_dl* with dl*
- drop strip binary

* Tue Jul 14 2020 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt2
- x86_64 build

* Mon Sep 16 2019 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- cpcsp_proxy_setup: Also add the "Provider Types" key for a being added provider

* Fri Jul 19 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt2
- add Conflicts: wine-p11csp

* Thu Jun 27 2019 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- cpcsp_proxy_setup: Various fixes
- cpcsp_proxy: Fix calling convention for CryptoPro provided APIs
- cpcsp_proxy: Pass cpcsp_proxy.spec to winegcc in order to build correct PE exports
- cpcsp_proxy_setup: Add support for certificates with strings in cp1251

* Mon May 20 2019 Konstantin Kondratyuk <kondratyuk@altlinux.ru> 0.1-alt1
- initial build for ALT Sisyphus
