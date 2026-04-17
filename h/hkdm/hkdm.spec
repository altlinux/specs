Name: hkdm
Version: 0.3.2
Release: alt1
Summary: HotKey Daemon (for) Mobile
License: GPLv3
Group: Accessibility
Url: https://gitlab.com/postmarketOS/hkdm
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.xz

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust pkgconfig(libevdev)

%description
HKDM is a simple hotkey daemon, it runs in the background and reacts to
particular key events / combinations of events by running arbitrary commands.

%prep
%setup -q

%build
%rust_build

%install
install -Dm 755 target/release/%name %buildroot%_sbindir/%name
mkdir -p %buildroot%_sysconfdir/%name/config.d
install -pD -m644 %name.service %buildroot%systemd_unitdir/%name.service

%files
%doc README.md
%_sysconfdir/%name
%systemd_unitdir/%name.service
%_sbindir/%name

%changelog
* Fri Apr 17 2026 Valery Inozemtsev <shrek@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Mon Sep 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

