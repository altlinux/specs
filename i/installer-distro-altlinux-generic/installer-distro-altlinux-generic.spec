Name: installer-distro-altlinux-generic
Version: 6.0
Release: alt1

Summary: Installer configuration (generic)
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

Packager: Michael Shigorin <mike@altlinux.org>

%description
This package contains installer configuration hopefully suitable
for a generic ALT Linux based distribution.

It is derived from installer-distro-server-light by Anton Farygin.

%package stage2
Summary: Installer configuration and scripts (stage2 part)
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
# modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-vm-altlinux-generic-stage2
Requires: x-cursor-theme-jimmac

%description stage2
This package contains installer configuration hopefully suitable
for a generic ALT Linux based distribution.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPL
Group: System/Configuration/Other
Provides: installer-altlinux-generic-stage3 = %name-%version
#Requires: installer-stage3
# modules
# FIXME: grub/lilo
Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
#Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for a generic ALT Linux based distribution.

The stage3 part is installed onto the new system's root
and executed off there during installation process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/*.d/*

%files stage3

%changelog
* Sat Jul 16 2011 Michael Shigorin <mike@altlinux.org> 6.0-alt1
- initial release based on installer-distro-server-light 6.0-alt3
- dropped unconditional X11 stuff removal just before the finish
  (this should only happen for known temporarily installed packages)
- dropped services reconfiguration (should be done based on service
  lists coming from the distro profile)
- enhanced descriptions
