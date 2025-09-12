Name: wg-obfuscator
Version: 1.4
Release: alt1

Summary: WireGuard Obfuscator is a tool designed to make WireGuard traffic look like random data.
License: GPL-3.0
Group: Security/Networking

Url: https://github.com/ClusterM/wg-obfuscator
VCS: https://github.com/ClusterM/wg-obfuscator.git
Source: %name-%version.tar.gz

Packager: Alexei Mezin <alexvm@altlinux.org>

Summary(ru_RU.UTF8): Инструмент для маскировки траффика WireGuard

BuildRequires(pre): gcc
##BuildRequires: lowdown


%description
WireGuard Obfuscator is a tool designed to make WireGuard traffic look like random data, making it significantly harder to detect by DPI (Deep Packet Inspection) systems.

%description -l ru_RU.UTF8
WireGuard Obfuscator это сетевой прокси-сервер, который маскирует пакеты протокола WireGuard, что сбивает с толку системы DPI (Deep Packet Inspection).

%prep
%setup

%build
%make_build

%install
install -D -m 0755 %name $RPM_BUILD_ROOT/%_bindir/%name
install -D -m 0644 %name.service $RPM_BUILD_ROOT/%_unitdir/%name.service
install -D -m 0644 %name.conf $RPM_BUILD_ROOT/%_sysconfdir/%name.conf


%files
%doc README.md
%_bindir/*
%_unitdir/*
%_sysconfdir/*


%changelog
* Sat Sep 13 2025 Alexei Mezin <alexvm@altlinux.org> 1.4-alt1
- New version

* Sat Aug 23 2025 Alexei Mezin <alexvm@altlinux.org> 1.3-alt1
- New version

* Mon Jul 07 2025 Alexei Mezin <alexvm@altlinux.org> 1.1-alt1
- Initial build

