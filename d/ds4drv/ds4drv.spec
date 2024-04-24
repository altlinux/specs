%define git_commit be7327fc3f5abb8717815f2a1a2ad3d335535d8a

Name: ds4drv
Version: 0.5.1
Release: alt3.gitbe7327f

Summary: A Sony DualShock 4 userspace driver for Linux
License: MIT
Group: Other

Url: https://github.com/chrippa/%name
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

# https://github.com/chrippa/%name/archive/%git_commit/%name-%git_commit.tar.gz
Source: %name-%git_commit.tar

Patch0: %name-python-3.12.patch

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
%setup -n %name-%git_commit
%patch0 -p1

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
* Wed Apr 24 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt3.gitbe7327f
- Update to git be7327f
- Fix double setting in conf (ALT #50015)

* Fri Apr 05 2024 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt2
- Fix run with python 3.12 (ALT #45143)

* Sun Dec 20 2020 Nazarov Denis <nenderus@altlinux.org> 0.5.1-alt1
- Initial build for ALT Linux
