%define distro virtualization-one

Name: installer-distro-%distro
Version: 11.0.0
Release: alt0.3

Summary: Installer configuration (Virtualization ONE)
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
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-bond alterator-net-bridge
Requires: alterator-net-general
Requires: alterator-notes
Requires: installer-feature-online-repo
Requires: installer-feature-powerbutton-stage3
Requires: installer-feature-systemd-resolved-link-stage3

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
* Fri Oct 24 2025 Alexander Burmatov <thatman@altlinux.org> 11.0.0-alt0.3
- Fix last step (ALT #55975).

* Wed Jul 09 2025 Sergey Konev <darisishe@altlinux.org> 11.0.0-alt0.2
- Add requires to systemd-resolved symlink installer feature,
  so now /etc/resolv.conf will be managed by systemd-resolved
  in installed system

* Tue Jun 24 2025 Alexander Burmatov <thatman@altlinux.org> 11.0.0-alt0.1
- Initial build, based on installer-distro-alt-server-v.
