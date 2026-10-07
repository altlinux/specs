Name: livecd-cmdline-mount
Version: 1.0
Release: alt3

Summary: Fetching mount settings from /proc/cmdline
Summary(ru_RU.UTF-8): Извлекает настройки монтирования из /proc/cmdline
License: GPL-3.0-or-later
Group: System/Configuration/Other
URL: https://www.altlinux.org/LiveCD

BuildArch: noarch

Source: %name-%version.tar

%description
This package installs two files for systemd service.
You can use it to automount net filesystem or disk by uuid or label.
It parses the contents of the mount variable in the /proc/cmdline file.

%description -l ru_RU.UTF-8
Этот пакет устанавливает два файла для systemd сервиса.
Его можно использовать для автомонтирования сетевых файловых систем или дисков
по их uuid или label.
Он парсит содержимое переменной mount файла /proc/cmdline.

%prep
%setup

%install
install -pD -m755 livecd-cmdline-mount %buildroot%_bindir/livecd-cmdline-mount
install -pD -m644 livecd-cmdline-mount.service \
	%buildroot%systemd_unitdir/livecd-cmdline-mount.service

%files
%_bindir/livecd-cmdline-mount
%systemd_unitdir/livecd-cmdline-mount.service
%doc README.practicum.md

%preun
%preun_service %name

%changelog
* Thu Aug 20 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt3
- Add README and spec description.

* Thu Aug 20 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt2
- Add LABEL and UUID variables.

* Fri Jul 17 2026 Artyom Osipchuk <artos@altlinux.org> 1.0-alt1
- Initial build.
