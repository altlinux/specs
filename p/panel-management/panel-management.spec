%define commit 2a7ad208f56ac2dee23ad6c1bc217bcb8e29dbb2

Name: panel-management
Version: 2.3
Release: alt1

Summary: Interactive panel management tool (Promethean, NexTouch)
Summary(ru_RU.UTF-8): Управление интерактивной панелью

License: GPL-3.0-only
Group: System/Configuration/Other
Url: https://hub.mos.ru/mos/src/panel-management

BuildArch: noarch

# Source-url: https://hub.mos.ru/mos/src/panel-management/-/archive/%commit/panel-management-%commit.tar.gz
Source: %name-%version.tar
Patch0: %name-2.3-alt-mos_pyqt_dialogs-name.patch
Patch1: %name-2.3-alt-use-ipaddress.patch

BuildRequires: rpm-build-python3

# commands used at runtime
Requires: /usr/bin/nc
Requires: /usr/bin/nmcli
Requires: /usr/bin/pkexec

%description
GUI and command line tool to control an interactive panel (Promethean AP5,
NexTouch): power, volume, input source (HDMI, OPS, Android).

%description -l ru_RU.UTF-8
Графический интерфейс и утилита командной строки для управления интерактивной
панелью (Promethean AP5, NexTouch): питание, громкость, источник сигнала
(HDMI, OPS, Android).

%prep
%setup
%autopatch -p1

%install
mkdir -p %buildroot%_datadir/%name
install -m755 %name.py %buildroot%_datadir/%name/
install -m644 *_commands %buildroot%_datadir/%name/
cp -a panel_management_modules %buildroot%_datadir/%name/
rm -rv %buildroot%_datadir/%name/panel_management_modules/__pycache__ ||:

mkdir -p %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF2'
#!/bin/sh
# the command lists are read from the current directory
cd %_datadir/%name
exec ./%name.py "$@"
EOF2
chmod 755 %buildroot%_bindir/%name

install -Dm644 %name.desktop %buildroot%_desktopdir/%name.desktop
install -Dm644 %name.1 %buildroot%_man1dir/%name.1
install -Dm644 %name.1.ru %buildroot%_mandir/ru/man1/%name.1
install -Dm644 %name.complete %buildroot%_datadir/bash-completion/completions/%name
install -Dm644 %name.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
for s in 16 22 24; do
    install -Dm644 icons/%name-tray-symbolic_$s.svg \
        %buildroot%_iconsdir/hicolor/${s}x$s/status/%name-tray-symbolic.svg
done

%add_python3_path %_datadir/%name

%files
%doc README.md
%_bindir/%name
%_datadir/%name/
%_desktopdir/%name.desktop
%_man1dir/%name.1*
%_mandir/ru/man1/%name.1*
%_datadir/bash-completion/completions/%name
%_iconsdir/hicolor/scalable/apps/%name.svg
%_iconsdir/hicolor/*/status/%name-tray-symbolic.svg

%changelog
* Tue Oct 20 2026 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- initial build for Sisyphus
