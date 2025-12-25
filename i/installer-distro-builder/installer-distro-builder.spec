%define distro builder
Name: installer-distro-%distro
Version: 11.0
Release: alt1

Summary: Installer files for alt-platform-builder
License: GPL-2.0-only
Group: System/Configuration/Other

Source: %name-%version.tar

%description
%summary

%package stage2
Summary: alt-platform-builder installer stage2
Group: System/Configuration/Other
Provides: installer-%distro-stage2 = %version
Requires: installer-stage2
#modules
Requires: alterator-sysconfig
Requires: alterator-datetime
Requires: installer-alterator-pkg
Requires: alterator-vm
Requires: alterator-notes
Requires: x-cursor-theme-jimmac

%description stage2
alt-platform-builder installer stage2.

%package stage3
Summary: alt-platform-builder installer stage3
Group: System/Configuration/Other
Provides: installer-%distro-stage3 = %version
Requires: installer-stage3
#modules
Requires: alterator-users >= 10.14-alt1
Requires: alterator-root
Requires: alterator-net-eth
Requires: alterator-net-general
Requires: alterator-net-bond alterator-net-bridge
Requires: installer-feature-nfs-server-stage3
%ifarch %ix86 x86_64 aarch64 ppc64le
Requires: installer-feature-powerbutton-stage3
Requires: alterator-grub
%endif
Requires: alterator-luks

%description stage3
alt-platform-builder installer stage3.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a * %buildroot%install2dir/

# Don't expand groups lists
mkdir -p %buildroot%_sysconfdir/alterator
echo "expand-description=no" >%buildroot%_sysconfdir/alterator/pkg-groups.conf

%files stage2
%_sysconfdir/alterator/pkg-groups.conf
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/*.d/*
%files stage3
%changelog
* Thu Oct 02 2025 Andrey Cherepanov <cas@altlinux.org> 11.0-alt1
- Initial build for Sisyphus.
