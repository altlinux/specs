Group: Engineering
Name:           lego-mindstorms-udev-rules
Version:        0.0.3
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
install -Dp -m755 %name/role-mindstormusers %buildroot%_controldir/role-mindstormusers
install -Dp -m644 %name/lego-mindstorms.role %buildroot%_sysconfdir/role.d/lego-mindstorms.role

%pre
%_sbindir/groupadd -f mindstormusers || :

%files
%_udevrulesdir/%file_name
%_controldir/role-mindstormusers
%config(noreplace) %_sysconfdir/role.d/lego-mindstorms.role


%changelog
* Mon Oct 23 2023 Valery Sinelnikov <greh@altlinux.org> 0.0.3-alt1
- Remove ATTRS{busnum}=="1" from udev rules (closes: 47964)

* Fri Oct 07 2022 Valery Sinelnikov <greh@altlinux.org> 0.0.2-alt1
- Removed localadmins assignments in role management rules
- Rename the control to role-mindstormusers for understanding
- Fixed the control for stability

* Thu Sep 29 2022 Valery Sinelnikov <greh@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux
