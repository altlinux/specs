Name: hkdm
Version: 0.1.1
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
%rust_install %name
mkdir -p %buildroot%_sysconfdir/%name/config.d

mkdir -p %buildroot%systemd_unitdir
cat << __EOF__ > %buildroot%systemd_unitdir/%name.service
[Unit]
Description=hotkey daemon
After=local-fs.target

[Service]
ExecStart=/usr/bin/hkdm

[Install]
WantedBy=multi-user.target
__EOF__

%files
%doc README.md
%_sysconfdir/%name
%systemd_unitdir/%name.service
%_bindir/%name

%changelog
* Mon Sep 11 2023 Valery Inozemtsev <shrek@altlinux.ru> 0.1.1-alt1
- initial release

