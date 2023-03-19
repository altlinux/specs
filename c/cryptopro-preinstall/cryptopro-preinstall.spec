Name:     cryptopro-preinstall
Version:  4.0.0
Release:  alt10

Summary:  Environment for official CryptoPro CSP packages (with Rutoken S and ECP support)
License:  GPL
Group:    Security/Networking

Url:      http://www.altlinux.org/CryptoPro
Source:   cryptopro-paths.sh
Packager: Andrey Cherepanov <cas@altlinux.org>

ExclusiveArch: %ix86 x86_64 %e2k mipsel

Requires: %name-base = %version-%release

# CryptoPro packages require lsb
Requires: lsb >= 3.0

%description
Provide environment for official CryptoPro CSP packages installation.
See instructions and usage information (in Russian) at
http://www.altlinux.org/CryptoPro

Tested with CryptoPro CSP 4.0.0 Build 9708.

%package base
Summary: Base environment for official CryptoPro CSP packages (with Rutoken S and ECP support)
License: GPL
Group: Security/Networking

# for cprocsp-rdr-gui-gtk
Requires: libgtk+2

# for own CryptoPro install program
Requires: newt52

# for curl
Requires: libidn
Requires: libssh2

# for Rutoken S and ECP support
Requires: opensc
Requires: pcsc-lite
Requires: pcsc-lite-rutokens
Requires: pcsc-lite-ccid
%ifarch %ix86 x86_64
Requires: librtpkcs11ecp
%endif

# Hacks to provide requirements of cprocsp-pki-cades and cprocsp-pki-plugin
%if "%_lib" == "lib64"
%define hacked_lib_suffix ()(64bit)
%else
%define hacked_lib_suffix %nil
%endif
Provides: libcapi10.so.4%hacked_lib_suffix
Provides: libcapi20.so.4%hacked_lib_suffix
Provides: libcpalloc.so.0%hacked_lib_suffix
Provides: librdrsup.so.4%hacked_lib_suffix
Provides: libcpui.so.4%hacked_lib_suffix

Provides: %name-full = %EVR
Obsoletes: %name-full < %EVR

%description base
This package provides base environment for official CryptoPro CSP
without pulling in whole LSB package with some extra dependencies;
install cprocsp-compat-altlinux-64 or cprocsp-compat-altlinux
before the rest of CryptoPro packages to compensate for that.

%install
install -pDm755 %SOURCE0 %buildroot%_sysconfdir/bashrc.d/cryptopro-paths.sh

%files

%files base
%_sysconfdir/bashrc.d/cryptopro-paths.sh

%changelog
* Sun Mar 19 2023 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt10
- Put CryptoPro executables path to the end of $PATH.

* Thu Nov 12 2020 Michael Shigorin <mike@altlinux.org> 4.0.0-alt9
- E2K: drop librtmp (obsolete and deleted from repos)

* Thu Apr 04 2019 Ivan A. Melnikov <iv@altlinux.org> 4.0.0-alt8
- Build on mipsel.

* Tue Apr 02 2019 Michael Shigorin <mike@altlinux.org> 4.0.0-alt7
- Restrict binary Rutoken PKCS11 library to x86.
- Add libidn and libssh2 for cpro's curl.
- E2K: add librtmp and symlink it with desired soname *if* missing.

* Thu Oct 18 2018 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt6
- Add Rutoken PKCS11 library.
- Update requirement for cprocsp-rdr-gui-gtk.
- Obsoletes full subpackage.

* Thu Nov 03 2016 Michael Shigorin <mike@altlinux.org> 4.0.0-alt5
- *fix* requires (revert previous change)
- lsb-less "base" subpackage provided separately
- "full" subpackage with a few more extras (see wiki)
- minor spec cleanup

* Wed Nov 02 2016 Sergey V Turchin <zerg@altlinux.org> 4.0.0-alt4
- fix requires

* Wed Jul 20 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt3
- Add provides for fix unmet requirements for cprocsp-pki-cades and
  cprocsp-pki-plugin

* Sat Jul 02 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt2
- Fix path add if CryproPro is not installed
- Add Rutoken ECP support

* Tue Jun 28 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
