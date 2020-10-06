Name: wine-cpcsp_proxy
Version: 0.5.2
Release: alt1

Summary: Proxy for using Linux CryptoPro in Windows applications with wine

License: LGPLv2
Group: Emulators
URL: https://github.com/Etersoft/wine-cpcsp_proxy

Source: %name-%version.tar

ExclusiveArch: %ix86 x86_64

BuildRequires: libwine-devel >= 5.16
# for wineapploader
BuildRequires: wine

# FIXME: winegcc: Could not find g++
BuildRequires: gcc-c++

#Conflicts: wine-p11csp

%define winelibdir %_libdir/wine

%add_verify_elf_skiplist %winelibdir/cpcsp_proxy.dll.so
%add_verify_elf_skiplist %winelibdir/cpcsp_proxy_setup.exe.so

%ifarch x86_64
%define capilitepkg lsb-cprocsp-capilite-64
%else
%define capilitepkg lsb-cprocsp-capilite
%endif

%description
Proxy for using Linux CryptoPro in Windows applications with wine.

* Use with CryptoPro:
 install %capilitepkg package
* Use with cprocsp_compat (CRYPTO@Etersoft):
 install cprocsp_compat

%prep
%setup

%build
%make_build -C cpcsp_proxy
%make_build -C cpcsp_proxy_setup

%install
mkdir -p %buildroot%winelibdir/
cp cpcsp_proxy/cpcsp_proxy.dll.so %buildroot%winelibdir
cp cpcsp_proxy_setup/cpcsp_proxy_setup.exe.so %buildroot%winelibdir
mkdir -p %buildroot/%_bindir/
cp %_bindir/wineapploader %buildroot/%_bindir/cpcsp_proxy_setup

%files
%winelibdir/cpcsp_proxy_setup.exe.so
%winelibdir/cpcsp_proxy.dll.so
%_bindir/cpcsp_proxy_setup

%changelog
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
