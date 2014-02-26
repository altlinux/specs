Name: installer-distro-altlinux-generic
Version: 7.0.3
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
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: installer-feature-vm-altlinux-generic-stage2

%description stage2
This package contains installer configuration hopefully suitable
for a generic ALT Linux based distribution.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPL
Group: System/Configuration/Other
Provides: installer-altlinux-generic-stage3 = %name-%version
# modules
Requires: alterator-root

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

%files stage3

%changelog
* Wed Feb 26 2014 Michael Shigorin <mike@altlinux.org> 7.0.3-alt1
- reverted the change in 7.0.1 along with further purge:
  do not require alterator-{luks,net-*,users} and dhcpcd explicitly
  so as to minimize the footprint for JeOS case; maybe this warrants
  yet another flavour but there are altlinux-{desktop,server} for
  the more involved distros already

* Thu Dec 20 2012 Michael Shigorin <mike@altlinux.org> 7.0.1-alt1
- added luks step (autoskips if no LUKS containers are created)

* Thu Dec 20 2012 Michael Shigorin <mike@altlinux.org> 7.0-alt1
- dropped postinstall script superceded by m-p's use/cleanup/installer

* Fri Jul 22 2011 Michael Shigorin <mike@altlinux.org> 6.0-alt2
- don't require alterator-grub (prepare for grub/lilo support
  in mkimage-profiles.git)

* Sat Jul 16 2011 Michael Shigorin <mike@altlinux.org> 6.0-alt1
- initial release based on installer-distro-server-light 6.0-alt3
- dropped unconditional X11 stuff removal just before the finish
  (this should only happen for known temporarily installed packages)
- dropped services reconfiguration (should be done based on service
  lists coming from the distro profile)
- enhanced descriptions
