Group: Engineering
Name:           lego-mindstorms-udev-rules
Version:        0.0.1
Release:        alt1
Summary:        Rules for udev to allow normal users access to work with lego mindstorms controllers
License:        GPLv3+
Source0:        %name-%version.tar
BuildArch:      noarch

# For the %%_udevrulesdir macro
BuildRequires:  libsystemd-devel libudev-devel systemd systemd-analyze systemd-coredump systemd-networkd systemd-portable systemd-services systemd-stateless systemd-sysvinit systemd-utils

# For the directory
Requires:        udev

%global file_name 96-lego-mindstorms-udev.rules

%description
Rules for udev to allow normal users access to work with lego mindstorms controllers

%prep
%setup -q

%install

install -Dp -m644 %name/%file_name %buildroot%_udevrulesdir/%file_name
install -Dp -m755 %name/mindstorms-role %buildroot%_controldir/mindstorms-role
install -Dp -m644 %name/lego-mindstorms.role %buildroot%_sysconfdir/role.d/lego-mindstorms.role

%pre
%_sbindir/groupadd -f mindstormusers || :

%files
%_udevrulesdir/%file_name
%_controldir/mindstorms-role
%config(noreplace) %_sysconfdir/role.d/lego-mindstorms.role


%changelog
* Thu Sep 29 2022 Valery Sinelnikov <greh@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux
