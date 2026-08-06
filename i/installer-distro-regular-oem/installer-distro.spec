Name: installer-distro-regular-oem
Version: 0.5
Release: alt1

Summary: Installer configuration for ALT Regular
License: GPL-2.0-or-later
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

%description
This package contains OEM installer configuration for
ALT Regular (Starterkits).

It is derived from installer-distro-regular.

%package stage2
Summary: Installer configuration for ALT Regular (stage2 part)
Group: System/Configuration/Other
# modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: installer-alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: x-cursor-theme-jimmac

%description stage2
This package contains installer configuration for
ALT Regular (Starterkits).

The stage2 part is included into live installer system.

%package stage3
Summary: Installer configuration for ALT Regular (stage3 part)
License: GPL-2.0+
Group: System/Configuration/Other
#Requires: installer-stage3
# modules
Requires: alterator-luks
Requires: alterator-notes

%description stage3
This package contains installer configuration for
ALT Regular (Starterkits).

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
%ghost %install2dir/services-*
%ghost %install2dir/systemd-*

%files stage3

%changelog
* Thu Aug 06 2026 Anton Midyukov <antohami@altlinux.org> 0.5-alt1
- Initial build from installer-distro-regular.
