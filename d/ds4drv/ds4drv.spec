Name: ds4drv
Version: 0.5.1
Release: alt1

Summary: A Sony DualShock 4 userspace driver for Linux
License: MIT
Group: Other

Url: https://github.com/chrippa/%name
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

# https://github.com/chrippa/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: python3-module-setuptools

%description
%name is a Sony DualShock 4 userspace driver for Linux.

Features:
        Option to emulate the Xbox 360 controller for compatibility with Steam games
        Setting the LED color
        Reminding you about low battery by flashing the LED
        Using the trackpad as a mouse
        Custom mappings, map buttons and sticks to whatever mouse, key or joystick action you want
        Settings profiles that can be cycled through with a button binding

%prep
%setup

%build
%python3_build

%install
%python3_install
%__install -Dp -m0644 %name.conf %buildroot%_sysconfdir/%name.conf
%__install -Dp -m0644 udev/50-%name.rules %buildroot%_udevrulesdir/50-%name.rules
%__install -Dp -m0644 systemd/%name.service %buildroot%_unitdir/%name.service

%files
%doc LICENSE
%_bindir/%name
%python3_sitelibdir/%{name}*
%config %_sysconfdir/%name.conf
%_udevrulesdir/50-%name.rules
%_unitdir/%name.service

%changelog
* Sun Dec 20 2020 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux
