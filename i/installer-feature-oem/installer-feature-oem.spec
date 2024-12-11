Name: installer-feature-oem
Version: 0.2
Release: alt4

Summary: OEM mode support for installer
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: https://www.altlinux.org/Installer/OEM

Source: %name-%version.tar
BuildArch: noarch

%description
%summary.

%package stage2
Summary: OEM mode support for installer
Group: System/Configuration/Other
Requires: installer-common-stage2

%description stage2
%summary.

%prep
%setup

%install
%makeinstall

%files stage2
%_datadir/install2/initinstall.d/*
%_datadir/install2/preinstall.d/*
%_datadir/install2/postinstall.d/*

%changelog
* Wed Dec 11 2024 Anton Midyukov <antohami@altlinux.org> 0.2-alt4
- replace 40-oem-step.sh from preinstall.d/ to postinstall.d/

* Fri Dec 06 2024 Anton Midyukov <antohami@altlinux.org> 0.2-alt3
- initinstall.d/98-oem.sh: install alterator-net-eth, when needs
- preinstall.d/40-oem-step.sh: add net-eth step only when available

* Wed Jul 17 2024 Dmitry Terekhin <jqt4@altlinux.org> 0.2-alt2
- Add alterator-net-eth to the installed system

* Sun Sep 24 2023 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- create large initrd for OEM
- add parameters: OEM_NET, OEM_ROOT, OEM_USER in cmdline kernel
- update Url

* Thu Sep 21 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial release
