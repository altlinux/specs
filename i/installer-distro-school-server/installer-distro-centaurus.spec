%define distro school-server
Name: installer-distro-%distro
Version: 7.0
Release: alt8

Summary: Installer files for Centaurus distro 
License: GPL
Group: System/Configuration/Other
BuildArch: noarch

Source: %name-%version.tar

%description
Installer files for School Server distro.

%package stage2
Summary: School Server installer stage2
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %name-%version
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: x-cursor-theme-jimmac

%description stage2
School Server installer stage2.

%package stage3
Summary: School Server installer stage3
License: GPL
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %name-%version
Requires: installer-stage3
#modules
Requires: alterator-users
Requires: alterator-root
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3
Requires: alterator-grub
Requires: alterator-luks

%description stage3
School Server installer stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/services-*
%install2dir/systemd-*
%install2dir/*.d/*

%files stage3

%changelog
* Wed Dec 25 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt8
- Add bacula-local-backup to expert list

* Fri Dec 06 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt7
- Turn off Rujel and Clamav services by default

* Mon Dec 02 2013 Andrey Cherepanov <cas@altlinux.org> 7.0-alt6
- Initial build installer-distro-school-server in Sisyphus
