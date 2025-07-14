Name: winehelper
Version: 0.5.0
Release: alt1

Summary: Program for easy installation of Windows applications.

License: LGPLv2+
Group: Emulators
Url: https://git.linux-gaming.ru/CastroFidel/winehelper

Source: %name-%version.tar

Requires: wine
Requires: ca-certificates
Requires: p7zip

%add_findreq_skiplist %_datadir/%name/winetricks_*
%add_findreq_skiplist %_datadir/%name/autoinstall/*
%add_findreq_skiplist %_datadir/%name/manualinstall/*
%add_findreq_skiplist %_datadir/%name/database/*

ExclusiveArch: x86_64

%description
Program for easy installation of Windows applications with the possibility
of automatic prefix tuning.

%prep
%setup

%build
%install
install -Dm755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name/{autoinstall,manualinstall,database,image}
install -m755 dependencies.sh %buildroot%_datadir/%name/
install -m755 winetricks_* %buildroot%_datadir/%name/
install -m644 sha256sum.list %buildroot%_datadir/%name/
install -m644 manualinstall/* %buildroot%_datadir/%name/manualinstall/
install -m644 autoinstall/*  %buildroot%_datadir/%name/autoinstall/
install -m644 database/* %buildroot%_datadir/%name/database/
install -m644 image/* %buildroot%_datadir/%name/image/

install -Dm644 auto_completion/bash_completion/%name %buildroot%_sysconfdir/bash_completion.d/%name
install -Dm644 auto_completion/zsh_completion/_%name %buildroot%_datadir/zsh/Completion/Linux/_%name

%files
%doc LICENSE CHANGELOG COPYING THIRD-PARTY
%_bindir/%name
%_datadir/%name/
%_sysconfdir/bash_completion.d/%name
%_datadir/zsh/Completion/Linux/_%name

%changelog
* Mon Jul 14 2025 Mikhail Tergoev <fidel@altlinux.org> 0.5.0-alt1
- 0.5.0
- removed requires: cups-pdf (ALT bug: 55212
- removed check requires libOSMesa from scripts (ALT bug: 55211)

* Fri Jul 04 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.9-alt1
- 0.4.9

* Tue Jul 01 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.7-alt1
- 0.4.7
- updated scripts and prefix for ved-* and ctm-* (ALT bug: 54921 54922)

* Thu Jun 26 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.6-alt1
- 0.4.6

* Thu Jun 19 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.5-alt1
- 0.4.5

* Wed Jun 18 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.3-alt1
- 0.4.3
- removed requires: fonts-ttf-ms (ALT bug: 54833)

* Fri May 30 2025 Mikhail Tergoev <fidel@altlinux.org> 0.4.0-alt1
- 0.4.0

* Tue May 27 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.9-alt1
- 0.3.9

* Mon May 26 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.8-alt1
- 0.3.8
- removed command: update-menus (ALT bug: 54274)

* Tue May 06 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.7-alt2
- added new manualinstall path

* Tue May 06 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.7-alt1
- updated to version 0.3.7
- updated check: noexec only for /home (ALT bug: 54095)

* Wed Mar 12 2025 Mikhail Tergoev <fidel@altlinux.org> 0.3.2-alt1
- initial build for ALT Sisyphus
