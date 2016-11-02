Name:     cryptopro-preinstall
Version:  4.0.0
Release:  alt4
Summary:  Prepare environment for install official CryptoPro SCP packages (with Rutoken S and ECP support)
License:  GPL
Group:    Security/Networking
URL:      https://www.altlinux.org/CryptoPro

Packager: Andrey Cherepanov <cas@altlinux.org>

Source1:  cryptopro-paths.sh

# CryptoPro packages requires lsb themself
# Requires: lsb >= 3.0

# Need for cprocsp-rdr-gui-gtk
Requires: libpangox-compat

# Need for Rutoken S and ECP support
Requires: opensc
Requires: pcsc-lite
Requires: pcsc-lite-rutokens
Requires: pcsc-lite-ccid

# Hacks for provide unmet requirements for cprocsp-pki-cades and cprocsp-pki-plugin
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

%description
Prepare environment for install official CryptoPro SCP packages.
See install instrictions and usage information at
https://www.altlinux.org/CryptoPro

Tested with CryptoPro CSP 4.0.0. Build 9708.

%install
install -Dm0755 %SOURCE1 %buildroot%_sysconfdir/bashrc.d/cryptopro-paths.sh

%files
%attr(0755,root,root) %_sysconfdir/bashrc.d/cryptopro-paths.sh

%changelog
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
