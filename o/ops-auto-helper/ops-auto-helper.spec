Name: ops-auto-helper
Version: 1
Release: alt1

Summary: Automation for interactive panels with OPS modules

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://hub.mos.ru/mos/pkgs/ops-auto-helper

BuildArch: noarch

Source: ops-poweroff.sh

BuildRequires(pre): rpm-macros-systemd

# the script uses these commands, they are not found automatically
Requires: /usr/bin/ip
Requires: /usr/bin/jq
Requires: /usr/bin/nc

%description
Automation for interactive panels (boards) with OPS modules.
Helps to fully power off Promethean AP5: the embedded Android is switched
off when the board is powered off (systemd system-shutdown hook).

%description -l ru_RU.UTF-8
Автоматизация для интерактивных панелей (досок) с модулями OPS.
Помогает полностью выключить доску Promethean AP5: встроенный Android
выключается при выключении системы (скрипт system-shutdown systemd).

%prep

%install
install -D -m755 %SOURCE0 %buildroot%_systemd_util_dir/system-shutdown/ops-poweroff.sh

%files
%_systemd_util_dir/system-shutdown/ops-poweroff.sh

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1-alt1
- initial build for Sisyphus.

