Name: installer-distro-token-desktop
Version: 0.1.0
Release: alt2

Summary: Installer configuration (desktop, h/w token authentication)
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer
Source: %name-%version.tar
BuildArch: noarch

Packager: Paul Wolneykien <manowar@altlinux.org>

%description
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution with hardware
token based authentication.

It is derived from installer-distro-altlinux-desktop.

%package stage2
Summary: Installer configuration and scripts (desktop, h/w token authentication, stage2 part)
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
for an ALT Linux based desktop distribution with hardware
token based authentication.

The stage2 part is included into the live installer system.

%package stage3
Summary: Installer configuration and scripts (desktop, h/w token authentication, stage3 part)
License: GPL
Group: System/Configuration/Other
Provides: installer-altlinux-generic-stage3 = %name-%version
#Requires: installer-stage3
# modules
# FIXME: grub/lilo
#Requires: alterator-grub
Requires: alterator-users
Requires: alterator-root
Requires: alterator-auth-token
Requires: alterator-luks
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
#Requires: installer-feature-nfs-server-stage3
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution with hardware
token based authentication.

The stage3 part is installed onto the new system\'s root
and executed off there during installation process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a alterator-menu %buildroot%install2dir/
cp -a installer-steps %buildroot%install2dir/
cp -a *.d %buildroot%install2dir/
cp -a steps %buildroot%install2dir/

mkdir -p %buildroot%_datadir/alterator
cp -a steps %buildroot%_datadir/alterator/

# Conflicts with livecd-install
mkdir -p %buildroot%_sysconfdir/livecd-install
cp -a livecd-installer-steps %buildroot%_sysconfdir/livecd-install/steps.token-desktop

mkdir -p %buildroot%_datadir/livecd-install
cp -a alterator-menu %buildroot%_datadir/livecd-install/

%post stage3
# Work-around the conflict with livecd-install
mkdir -p %_sysconfdir/livecd-install
if [ ! -e %_sysconfdir/livecd-install/steps.livecd-install ]; then \
    mv %_sysconfdir/livecd-install/steps %_sysconfdir/livecd-install/steps.livecd-install; \
fi
rm -f %_sysconfdir/livecd-install/steps
ln -s steps.token-desktop %_sysconfdir/livecd-install/steps

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/steps/*.desktop
%install2dir/*.d/*

%files stage3
%_datadir/livecd-install/alterator-menu
# Conflicts with livecd-install
%_sysconfdir/livecd-install/steps.token-desktop
%_datadir/alterator/steps/*.desktop

%changelog
* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Use special livecd-install set of steps.
- Work-around the conflict with livecd-install.

* Tue Aug 08 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Added "auth-token" step.
