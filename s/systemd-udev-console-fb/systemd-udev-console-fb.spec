%define sname udev-console

Name: systemd-udev-console-fb
Version: 1.00
Release: alt1

Group: System/Configuration/Boot and Init
Summary: Udev rules to load console fonts systemd in framebuffer
Summary(ru_RU.UTF-8): Правила udev для загрузки консольных фонтов в фреймбуфер
Url: http://altlinux.org/
License: GPLv2+

BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%version.tar
Source1: Readme
Source2: Readme_rus

%description
Udev rules to load console fonts systemd system
in framebuffer according to the locale specified
in the /etc/sysconfig/i18n.

%description -l ru_RU.UTF8
Правила udev для загрузки консольных фонтов в фреймбуфер
при использованиии системой инициализации systemd
в соответствии локалью, заданной в  /etc/sysconfig/i18n.

Requires: udev-rules

%prep
%setup -n %sname-%version
install -m 644 %SOURCE1 .
install -m 644 %SOURCE2 .

%install
install -d -m 755 %buildroot%_udevrulesdir/
install -m 755 all-vcs-set %buildroot/lib/udev/
install -m 644 991-fb-systemd.rules %buildroot%_udevrulesdir/
install -d -m 755 %buildroot%_docdir/%name-%version

%files
%docdir %_docdir/%name-%version
%doc Readme Readme_rus

/lib/udev/all-vcs-set
%_udevrulesdir/991-fb-systemd.rules

%changelog
* Sat Apr 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 1.00-alt1
- initial build for ALT Linux Sisyphus
