Name:    clevis
Version: 19
Release: alt1
Summary: Automated Encryption Framework

License: GPL-3.0-or-later
Group:   System/Libraries
URL:     https://github.com/latchset/clevis
Source:  clevis-%{version}.tar.gz
Patch: clevis-19-alt-fix-requires-detection.patch

Requires: clevis-pin-tpm2
BuildRequires: libjose-devel meson cmake bash-completion libpwquality-devel libcryptsetup-devel cryptsetup libjq-devel jq libluksmeta-devel libsystemd-devel systemd asciidoc-a2x libaudit-devel libudisks2-devel libgio-devel keyutils curl tpm2-tools dracut tang socat

%description
Clevis is a plugable framework for automated decryption.
It can be used to provide automated decryption of data
or even automated unlocking of LUKS volumes.

%prep
%setup
%patch -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%_bindir/clevis
%_bindir/clevis-decrypt
%_bindir/clevis-decrypt-null
%_bindir/clevis-decrypt-sss
%_bindir/clevis-decrypt-tang
%_bindir/clevis-decrypt-tpm2
%_bindir/clevis-encrypt-null
%_bindir/clevis-encrypt-sss
%_bindir/clevis-encrypt-tang
%_bindir/clevis-encrypt-tpm2
%_bindir/clevis-luks-bind
%_bindir/clevis-luks-common-functions
%_bindir/clevis-luks-edit
%_bindir/clevis-luks-list
%_bindir/clevis-luks-pass
%_bindir/clevis-luks-regen
%_bindir/clevis-luks-report
%_bindir/clevis-luks-unbind
%_bindir/clevis-luks-unlock
%_sysconfdir/xdg/autostart/clevis-luks-udisks2.desktop
%_datadir/bash-completion/completions/clevis
%_libexecdir/clevis-luks-udisks2
%_libexecdir/clevis-luks-askpass
%_unitdir/clevis-luks-askpass.path
%_unitdir/clevis-luks-askpass.service
%dir %_libexecdir/dracut/modules.d/60clevis-pin-null/
%_libexecdir/dracut/modules.d/60clevis-pin-null/module-setup.sh
%dir %_libexecdir/dracut/modules.d/60clevis-pin-sss/
%_libexecdir/dracut/modules.d/60clevis-pin-sss/module-setup.sh
%dir %_libexecdir/dracut/modules.d/60clevis-pin-tang/
%_libexecdir/dracut/modules.d/60clevis-pin-tang/module-setup.sh
%dir %_libexecdir/dracut/modules.d/60clevis-pin-tpm2/
%_libexecdir/dracut/modules.d/60clevis-pin-tpm2/module-setup.sh
%dir %_libexecdir/dracut/modules.d/60clevis/
%_libexecdir/dracut/modules.d/60clevis/clevis-hook.sh
%_libexecdir/dracut/modules.d/60clevis/module-setup.sh
%_man1dir/clevis-decrypt.1*
%_man1dir/clevis-encrypt-sss.1*
%_man1dir/clevis-encrypt-tang.1*
%_man1dir/clevis-encrypt-tpm2.1*
%_man1dir/clevis-luks-bind.1*
%_man1dir/clevis-luks-edit.1*
%_man1dir/clevis-luks-list.1*
%_man1dir/clevis-luks-pass.1*
%_man1dir/clevis-luks-report.1*
%_man1dir/clevis-luks-unbind.1*
%_man1dir/clevis-luks-unlock.1*
%_man1dir/clevis-luks-regen.1*
%_man1dir/clevis.1*
%_man7dir/clevis-luks-unlockers.7*

%changelog
* Tue Sep 12 2023 Leontiy Volodin <lvol@altlinux.org> 19-alt1
- new version
- update url tag

* Mon Oct 01 2018 Oleg Solovyov <mcpain@altlinux.org> 11-alt1
- initial build

