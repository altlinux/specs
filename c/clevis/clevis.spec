%define _unpackaged_files_terminate_build 1
%define _libexecdir %_usr/libexec
%define dracutmodulesdir  %(pkg-config --variable=dracutmodulesdir --silence-errors dracut 2>/dev/null || echo unknown) 

Name:    clevis
Version: 21
Release: alt2
Summary: Automated Encryption Framework

License: GPL-3.0-or-later
Group:   System/Kernel and hardware
URL:     https://github.com/latchset/clevis
Source:  clevis-%{version}.tar.gz

Requires: tpm2-tools >= 4.0.0
Requires: jose >= 8
Requires: curl
Requires: jq
Requires: clevis-pin-tpm2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: asciidoc-a2x
BuildRequires: bash-completion
BuildRequires: libjose-devel
BuildRequires: libaudit-devel
BuildRequires: libudisks2-devel
BuildRequires: libssl-devel openssl
BuildRequires: tpm2-tools tang >= 6 curl libluksmeta-devel
BuildRequires: dracut
BuildRequires: cryptsetup
BuildRequires: jq
BuildRequires: pcsc-lite opensc
BuildRequires: libsystemd-devel systemd
BuildRequires: cryptsetup

%description
Clevis is a plugable framework for automated decryption.
It can be used to provide automated decryption of data
or even automated unlocking of LUKS volumes.

%package  luks
Summary:  LUKS integration for clevis
Group:    System/Kernel and hardware
Requires: %name = %EVR
Requires: cryptsetup
Requires: luksmeta >= 8
%filter_from_requires /.usr.lib.dracut-lib.sh/d

%description luks
LUKS integration for clevis. This package allows you to bind a LUKS
volume to a clevis unlocking policy. For automated unlocking, an unlocker
will also be required. See, for example, clevis-dracut and clevis-udisks2.

%package  systemd
Summary:  systemd integration for clevis
Group:    System/Kernel and hardware
Requires: %name = %EVR
Requires: systemd >= 236

%description systemd
Automatically unlocks LUKS _netdev block devices from /etc/crypttab.

%package  dracut
Summary:  Dracut integration for clevis
Group:    System/Kernel and hardware
Requires: %name-systemd = %EVR
#Requires: dracut-network

%description dracut
Automatically unlocks LUKS block devices in early boot.

%package  udisks2
Summary:  UDisks2/Storaged integration for clevis
Group:    System/Kernel and hardware
Requires: %name-luks = %EVR

%description udisks2
Automatically unlocks LUKS block devices in desktop environments that
use UDisks2 or storaged (like GNOME).

%package  pin-pkcs11
Summary:  PKCS#11 for clevis
Group:    System/Kernel and hardware
Requires: %name-systemd = %EVR
Requires: %name-luks = %EVR
Requires: %name-dracut = %EVR
Requires: pcsc-lite
Requires: opensc
Requires: socat
Requires: openssl

%description pin-pkcs11
Automatically unlocks LUKS block devices through a PKCS#11 device.

%prep
%setup

%build
export PATH=/usr/sbin:$PATH
%meson
%meson_build

%install
%meson_install

%files
%_bindir/%name
%_bindir/%name-decrypt
%_bindir/%name-decrypt-null
%_bindir/%name-decrypt-sss
%_bindir/%name-decrypt-tang
%_bindir/%name-decrypt-tpm2
%_bindir/%name-encrypt-null
%_bindir/%name-encrypt-sss
%_bindir/%name-encrypt-tang
%_bindir/%name-encrypt-tpm2
%_man1dir/%name-decrypt.1*
%_man1dir/%name-encrypt-sss.1*
%_man1dir/%name-encrypt-tang.1*
%_man1dir/%name-encrypt-tpm2.1*
%_man1dir/%name.1*
%_datadir/bash-completion/completions/%name

%files luks
%_man1dir/%name-luks-*
%_bindir/%name-luks-*

%files systemd
%_libexecdir/%name-luks-askpass
%_libexecdir/%name-luks-unlocker
%_unitdir/%name-luks-askpass.path
%_unitdir/%name-luks-askpass.service
%_man7dir/%name-luks-unlockers.7*

%files dracut
%dracutmodulesdir/60clevis
%dracutmodulesdir/60clevis-pin-null
%dracutmodulesdir/60clevis-pin-sss
%dracutmodulesdir/60clevis-pin-tang
%dracutmodulesdir/60clevis-pin-tpm2

%files udisks2
%_sysconfdir/xdg/autostart/%name-luks-udisks2.desktop
#%attr(4755, root, root) %_libexecdir/%name-luks-udisks2
%_libexecdir/%name-luks-udisks2

%files pin-pkcs11
%_libexecdir/%name-luks-pkcs11-askpass
%_libexecdir/%name-luks-pkcs11-askpin
%_bindir/%name-decrypt-pkcs11
%_bindir/%name-encrypt-pkcs11
%_bindir/%name-pkcs11-afunix-socket-unlock
%_bindir/%name-pkcs11-common
%_unitdir/%name-luks-pkcs11-askpass.service
%_unitdir/%name-luks-pkcs11-askpass.socket
%_man1dir/%name-encrypt-pkcs11.1*
%dracutmodulesdir/60clevis-pin-pkcs11

%changelog
* Fri Aug 22 2025 Alexey Shabalin <shaba@altlinux.org> 21-alt2
- split luks, systemd, dracut, udisks2, pin-pkcs11 packages
- define _libexecdir as /usr/libexec
- cherry-pick commits from upstream master

* Fri Sep 27 2024 Leontiy Volodin <lvol@altlinux.org> 21-alt1
- new version
- apply usrmerge

* Wed Mar 13 2024 Leontiy Volodin <lvol@altlinux.org> 20-alt1
- new version

* Tue Oct 24 2023 Leontiy Volodin <lvol@altlinux.org> 19-alt1.1
- add require

* Tue Sep 12 2023 Leontiy Volodin <lvol@altlinux.org> 19-alt1
- new version
- update url tag

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 11-alt1
- initial build

