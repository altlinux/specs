%define distro virtualization-pve

Name: installer-distro-%distro
Version: 11.1.0
Release: alt3

Summary: Installer configuration (Virtualization PVE)
License: GPLv2
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

It is derived from installer-distro-altlinux-generic.

%package stage2
Summary: Installer configuration and scripts (stage2 part)
License: GPLv2
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %version
Requires: installer-stage2
# modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-blivet
Requires: alterator-notes
Requires: installer-feature-efi-removable

%description stage2
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPLv2
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %version
# modules
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-ifupdown2
Requires: alterator-notes
Requires: installer-feature-online-repo
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for an ALT Linux based server distribution.

The stage3 part is installed onto the new system's root
and executed off there during installation process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/*.d/*
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/steps

%files stage3

%changelog
* Tue Apr 07 2026 Sergey Konev <darisishe@altlinux.org> 11.1.0-alt3
- Do not skip alterator-grub step for EFI
- Add Requires: installer-feature-efi-removable

* Mon Mar 23 2026 Sergey Konev <darisishe@altlinux.org> 11.1.0-alt2
- Add proper l10n for Grub autoinstall

* Sat Mar 21 2026 Sergey Konev <darisishe@altlinux.org> 11.1.0-alt1
- Skip alterator-grub step, autoinstall grub in removable mode

* Mon Jun 30 2025 Sergey Konev <darisishe@altlinux.org> 11.0.0-alt0.4
- Removed setup-dhcp-ifupdown2 script
  (now setup-dhcp from general installer does that)

* Thu Apr 17 2025 Sergey Konev <darisishe@altlinux.org> 11.0.0-alt0.3
- initinstall script to assemble MD RAIDs
  (required for Volume Managment step)
- Removed redundant LUKS installer step
  alterator-blivet can't create LUKS devices for now
  (Encryption can be provided by Ceph)
- Fixed 85-create-pve-cluster-fs failure
- Fixed empty Release Notes page in the end of installation
- Restored setup-dhcp script

* Wed Jan 29 2025 Sergey Konev <darisishe@altlinux.org> 11.0.0-alt0.2
- Usage of 'tuned' daemon for better system settings fitting
- New volume managment module
- preinstall script for PVE cluster FS creation

* Wed Nov 20 2024 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt0.1
- Initial build, based on installer-distro-alt-server-v.

