Name: installer-feature-oem
Version: 0.2
Release: alt2

Summary: OEM mode support for installer
License: GPLv2+
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

%changelog
* Wed Jul 17 2024 Dmitry Terekhin <jqt4@altlinux.org> 0.2-alt2
- Add alterator-net-eth to the installed system

* Sun Sep 24 2023 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- create large initrd for OEM
- add parameters: OEM_NET, OEM_ROOT, OEM_USER in cmdline kernel
- update Url

* Thu Sep 21 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial release
