Name: installer-distro-token-desktop
Version: 0.1.1
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
Requires: installer-feature-token-profile

%description stage2
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution with hardware
token based authentication.

The stage2 part is included into the live installer system.

%package -n installer-feature-token-default
Summary: Auth-token installer step with no profile preselected
License: GPL
Group: System/Configuration/Other
Provides: installer-feature-token-profile = 50

%description -n installer-feature-token-default
Auth-token installer step with no profile preselected

%package -n installer-feature-token-rutokenecp
Summary: Auth-token installer step with RuTokenECP profile preselected
License: GPL
Group: System/Configuration/Other
Provides: installer-feature-token-profile = 40
Requires: pkcs11-profiles-rutokenecp

%description -n installer-feature-token-rutokenecp
Auth-token installer step with RuTokenECPprofile preselected

%package -n installer-feature-token-p11-kit-proxy
Summary: Auth-token installer step with p11-kit-proxy profile preselected
License: GPL
Group: System/Configuration/Other
Provides: installer-feature-token-profile = 40
Requires: pkcs11-profiles-p11-kit-proxy

%description -n installer-feature-token-p11-kit-proxy
Auth-token installer step with p11-kit-proxy profile preselected

%package stage3
Summary: Installer configuration and scripts (desktop, h/w token authentication, stage3 part)
License: GPL
Group: System/Configuration/Other

Requires: alterator-users
Requires: alterator-root
Requires: alterator-auth-token
Requires: alterator-luks
Requires: alterator-net-eth dhcpcd
Requires: alterator-net-general
Requires: installer-feature-powerbutton-stage3

%description stage3
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution with hardware
token based authentication.

The stage3 part is installed onto the new system\'s root
and executed off there during installation process.

%package live
Summary: Installer configuration and scripts (desktop, h/w token authentication, livecd-install part)
License: GPL
Group: System/Configuration/Other

Requires: %name-stage3 = %version-%release
Requires: livecd-install >= 0.9.10
Requires: installer-feature-token-profile

%description live
This package contains installer configuration hopefully suitable
for an ALT Linux based desktop distribution with hardware
token based authentication.

The live part is installed into the live-bootable system
and executed off there by the 'livecd-install' process.

%prep
%setup

%install
%define install2dir %_datadir/install2
mkdir -p %buildroot%install2dir
cp -a alterator-menu %buildroot%install2dir/
cp -a installer-steps %buildroot%install2dir/
cp -a *.d %buildroot%install2dir/

mkdir -p %buildroot%_datadir/alterator
cp -a steps %buildroot%_datadir/alterator/

mkdir -p %buildroot%_sysconfdir/livecd-install
cp -a livecd-installer-steps %buildroot%_sysconfdir/livecd-install/steps.token-desktop
install -m0644 -D steps-livecd-token-desktop \
        %buildroot%_altdir/%name.steps

mkdir -p %buildroot%_datadir/livecd-install
cp -a alterator-menu %buildroot%_datadir/livecd-install/

# Default
install -m0644 -D installer-feature-token-default \
        %buildroot%_altdir/installer-feature-token-default

# RuTokenECP
install -m0644 -D installer-feature-token-rutokenecp \
        %buildroot%_altdir/installer-feature-token-rutokenecp

# PKCS#11 Kit Proxy
install -m0644 -D installer-feature-token-p11-kit-proxy \
        %buildroot%_altdir/installer-feature-token-p11-kit-proxy

%files stage2
%install2dir/alterator-menu
%install2dir/installer-steps
%install2dir/*.d/*

%files stage3

%files live
%_datadir/livecd-install/alterator-menu
%_sysconfdir/livecd-install/steps.token-desktop
%_altdir/%name.steps

%files -n installer-feature-token-default
%_altdir/installer-feature-token-default
%_datadir/alterator/steps/*.default.desktop

%files -n installer-feature-token-rutokenecp
%_altdir/installer-feature-token-rutokenecp
%_datadir/alterator/steps/*.rutokenecp.desktop

%files -n installer-feature-token-p11-kit-proxy
%_altdir/installer-feature-token-p11-kit-proxy
%_datadir/alterator/steps/*.p11-kit-proxy.desktop

%changelog
* Wed Sep 06 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Add 'p11-kit-proxy' profile.

* Thu Aug 17 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Use /etc/alternatives to configure the installer steps.
- Provide installer-feature-token-* packages with various
  pre-configurations for the auth-token installer step.

* Tue Aug 15 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt3
- Make special '-live' subpackage which requires 'livecd-install'.

* Thu Aug 10 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Use special livecd-install set of steps.
- Work-around the conflict with livecd-install.

* Tue Aug 08 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Added "auth-token" step.
