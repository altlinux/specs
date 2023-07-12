Name: lightdm-autologin-greeter
Version: 1.0
Release: alt3
Summary: Autologin greeter using LightDM
License: MIT
URL: https://github.com/spanezz/lightdm-autologin-greeter
Group: Graphical desktop/Other
# Source-url: https://github.com/spanezz/lightdm-autologin-greeter/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar
Source1: %name.README.distro

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
Requires: python3-module-pygobject3
Requires: liblightdm-gobject

# LightDM is required for this to be useful
Requires: dm-tool lightdm lightdm-gir
Requires: /usr/share/design/current

# All LightDM greeters provide this
Provides: lightdm-greeter

BuildArch: noarch

%description
%name is a minimal greeter for LightDM that has
the same autologin behavior as nodm, but being based on LightDM,
it stays on top of modern display manager requirements.

The difference between LightDM's built-in autologin and this greeter,
is the behavior in case of 0-seconds autologin delay. When LightDM
automatically logs in with no delay, upon logout it will show the
login window again. The intent is that if the default user logged out,
they probably intend to log in again as a different user.

In the case of managing a kiosk-like setup, if the X session quits, then
the desired behavior is to just start it again.

LightDM with an autologin timeout of 1 or more seconds would work,
but one sees the login dialog window appear and disappear
on-screen at each system startup.

With this greeter, the X session starts right away, and is restarted
if it quits, without any flicker of a login dialog box.

If one is not setting up a kiosk-like setup, it's very likely that the
default autologin behavior of LightDM is the way to go, and that this
greeter is not needed.

%prep
%setup

# Install Source1 into source tree
cp %SOURCE1 README.distro

%build
# Nothing to build

%install
mkdir -p %buildroot%prefix
cp -a bin %buildroot%prefix
cp -a share %buildroot%prefix

sed -i "s:#!/usr/bin/python:#!%__python3:" %buildroot%_bindir/%name

# Add alternatives for xgreeters
mkdir -p %buildroot/%_altdir
printf '%_datadir/xgreeters/lightdm-default-greeter.desktop\t%_datadir/xgreeters/%name.desktop\t49\n' >%buildroot/%_altdir/%name

%files
%doc README.md README.distro
%_altdir/%name
%_bindir/%name
%_datadir/xgreeters/%name.desktop
%_datadir/lightdm/lightdm.conf.d/60-%name.conf

%changelog
* Thu Mar 23 2023 Anton Midyukov <antohami@altlinux.org> 1.0-alt3
- initial build to Sisyphus
- cleanup spec

* Wed Feb 22 2023 Igor Vlasenko <viy@altlinux.org> 1.0-alt2_17
- update to new release by fcimport
