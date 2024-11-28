%define distro virtualization-pve

Name: installer-distro-%distro
Version: 11.0.0
Release: alt0.1

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
Requires: alterator-vm
Requires: alterator-notes

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
Requires: alterator-luks
Requires: alterator-net-ifupdown2
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
* Wed Nov 20 2024 Alexey Shabalin <shaba@altlinux.org> 11.0.0-alt0.1
- Initial build, based on installer-distro-alt-server-v.

