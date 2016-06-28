Name:     cryptopro-preinstall
Version:  4.0.0
Release:  alt1
Summary:  Prepare environment for install official CryptoPro SCP packages (with Rutoken support)
License:  GPL
Group:    Security/Networking
URL:      https://www.altlinux.org/CryptoPro

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source1:  cryptopro-paths.sh

# Need for base CryptoPro packages
Requires: lsb >= 3.0

# Need for cprocsp-rdr-gui-gtk
Requires: libpangox-compat

# Need for Rutoken support
Requires: opensc
Requires: pcsc-lite
Requires: pcsc-lite-rutokens

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
* Tue Jun 28 2016 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus
