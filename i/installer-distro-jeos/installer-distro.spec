Name: installer-distro-jeos
Version: 0.1
Release: alt1

Summary: Installer configuration for JeOS
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains installer configuration
for minimalistic image JeOS.

It is derived from installer-distro-altlinux-generic.

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

%description stage2
This package contains installer configuration
for minimalistic image JeOS.

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration and scripts (stage3 part)
License: GPL
Group: System/Configuration/Other
Provides: installer-altlinux-generic-stage3 = %name-%version
# modules
Requires: alterator-root

%description stage3
This package contains installer configuration
for minimalistic image JeOS.

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
* Wed Sep 20 2023 Anton Midyukov <antohami@altlinux.org> 0.1-alt1
- Initial build
