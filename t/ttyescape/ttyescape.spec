Name: ttyescape
Version: 1.0.2
Release: alt1
Summary: because mobile users can be hackers too
License: GPLv2
Group: Accessibility
Url: https://gitlab.com/postmarketOS/ttyescape/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz

BuildArch: noarch
Requires: hkdm buffyboard fonts-console-terminus

%description
TTYescape is a collection of config files and a shell script enabling mobile
users to escape the mortal limitations of "Desktop Environments" and "hardware
acceleration", ascending to the one TRUE form of computer usage - the TTY.

%prep
%setup -q

%build

%install
install -pD -m0755 togglevt.sh %buildroot%_bindir/togglevt.sh
install -pD -m0644 ttyescape-hkdm.toml %buildroot%_sysconfdir/%name/config.d/ttyescape.toml

mkdir -p %buildroot%_sysconfdir/sysconfig
touch %buildroot%_sysconfdir/sysconfig/ttyescape.conf

%files
%doc README.md
%ghost %_sysconfdir/sysconfig/ttyescape.conf
%_sysconfdir/%name/config.d/ttyescape.toml
%_bindir/togglevt.sh

%changelog
* Mon Sep 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- initial release

