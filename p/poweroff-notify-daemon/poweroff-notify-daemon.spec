Name: poweroff-notify-daemon
Version: 1.0.1
Release: alt2

Summary: Daemon for scheduled PC shutdown with GUI notifications
Summary(ru_RU.UTF-8): Демон запланированного выключения ПК с GUI-уведомлениями

License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/x09/poweroff-notify-daemon

Source: %name-%version.tar

BuildArch: noarch

# Зависимости времени сборки
BuildRequires(pre): rpm-build-python3

# Зависимости времени выполнения
Requires: python3
Requires: python3-module-pygobject3
Requires: libayatana-appindicator3-gir
Requires: libnotify-gir
Requires: systemd
Requires: polkit

%description
Poweroff Notify Daemon provides scheduled PC shutdown functionality
with system tray indicator, countdown timer, and interactive notifications.

Features:
- System tray icon with countdown timer
- User notifications with ability to extend shutdown time
- Per-user configuration via INI file
- Two-level protection: XDG autostart + optional system timer
- Compatible with GNOME 48+, KDE, MATE (via AppIndicator3)
- Centralized management via GPO/Samba AD

%description -l ru_RU.UTF-8
Poweroff Notify Daemon обеспечивает функциональность запланированного
выключения ПК с индикатором в системном трее, таймером обратного отсчёта
и интерактивными уведомлениями.

Возможности:
- Иконка в системном трее с таймером обратного отсчёта
- Уведомления пользователю с возможностью продлить время выключения
- Персональная конфигурация для каждого пользователя через INI-файл
- Двухуровневая защита: XDG autostart + опциональный system timer
- Совместимость с GNOME 48+, KDE, MATE (через AppIndicator3)
- Централизованное управление через GPO/Samba AD

%prep
%setup

%install
# Основные исполняемые файлы
install -Dm755 poweroff-daemon.py %buildroot%_bindir/poweroff-daemon.py
install -Dm755 sync-timer.py %buildroot%_bindir/sync-timer.py

# Systemd system timer и service
install -Dm644 poweroff-schedule.timer %buildroot%_unitdir/poweroff-schedule.timer
install -Dm644 poweroff-schedule.service %buildroot%_unitdir/poweroff-schedule.service

# Конфигурационный файл (example)
install -Dm644 poweroff.time.example %buildroot%_sysconfdir/poweroff.time

# Desktop file для XDG autostart (запуск при логине)
install -Dm644 poweroff-daemon.desktop %buildroot%_sysconfdir/xdg/autostart/poweroff-daemon.desktop

# Иконки
install -Dm644 icons/poweroff-daemon.svg %buildroot%_iconsdir/hicolor/scalable/apps/poweroff-daemon.svg
install -Dm644 icons/poweroff-daemon-warning.svg %buildroot%_iconsdir/hicolor/scalable/apps/poweroff-daemon-warning.svg

for i in 16 24 32 48 64 128 256; do
install -Dm644 icons/poweroff-daemon-${i}.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/poweroff-daemon.png
install -Dm644 icons/poweroff-daemon-warning-${i}.png %buildroot%_iconsdir/hicolor/${i}x${i}/apps/poweroff-daemon-warning.png
done

# Symlink для pixmaps (для старых приложений)
install -dm755 %buildroot%_pixmapsdir
ln -s %_iconsdir/hicolor/48x48/apps/poweroff-daemon.png %buildroot%_pixmapsdir/poweroff-daemon.png

# Документация
install -Dm644 README.md %buildroot%_docdir/%name/README.md
install -Dm644 OVERVIEW.md %buildroot%_docdir/%name/OVERVIEW.md
install -Dm644 LICENSE %buildroot%_docdir/%name/LICENSE

%post
# Информируем администратора о необходимости настройки
cat <<EOF
=================================================================
Poweroff Notify Daemon установлен.

GUI-демон запустится автоматически при следующем входе пользователя.

ВАЖНО: System timer НЕ включен автоматически.
Для активации резервного таймера выполните:
  1. Настройте /etc/poweroff.time
  2. /usr/bin/sync-timer.py
  3. systemctl enable --now poweroff-schedule.timer

Документация: %_docdir/%name/
=================================================================
EOF

%preun
# Если это полное удаление (не обновление)
if [ $1 -eq 0 ]; then
    # Останавливаем и отключаем system timer
    systemctl disable --now poweroff-schedule.timer 2>/dev/null ||:
fi

%files
%doc %_docdir/%name/README.md
%doc %_docdir/%name/OVERVIEW.md
%doc %_docdir/%name/LICENSE

# Исполняемые файлы
%_bindir/poweroff-daemon.py
%_bindir/sync-timer.py

# Systemd system timer (резервное выключение)
%_unitdir/poweroff-schedule.timer
%_unitdir/poweroff-schedule.service

# Конфигурация
%config(noreplace) %_sysconfdir/poweroff.time
%_sysconfdir/xdg/autostart/poweroff-daemon.desktop

# Иконки
%_iconsdir/hicolor/scalable/apps/poweroff-daemon.svg
%_iconsdir/hicolor/scalable/apps/poweroff-daemon-warning.svg
%_iconsdir/hicolor/16x16/apps/poweroff-daemon.png
%_iconsdir/hicolor/16x16/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/24x24/apps/poweroff-daemon.png
%_iconsdir/hicolor/24x24/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/32x32/apps/poweroff-daemon.png
%_iconsdir/hicolor/32x32/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/48x48/apps/poweroff-daemon.png
%_iconsdir/hicolor/48x48/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/64x64/apps/poweroff-daemon.png
%_iconsdir/hicolor/64x64/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/128x128/apps/poweroff-daemon.png
%_iconsdir/hicolor/128x128/apps/poweroff-daemon-warning.png
%_iconsdir/hicolor/256x256/apps/poweroff-daemon.png
%_iconsdir/hicolor/256x256/apps/poweroff-daemon-warning.png
%_pixmapsdir/poweroff-daemon.png

%changelog
* Mon Oct 12 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt2
- Build for Sisyphus.
- Remove gtk-update-icon-cache, as this is handled by a filetrigger.

* Mon Oct 12 2026 Anton Shevtsov <shevtsov.anton@gmail.com> 1.0.1-alt1
- Fix wrong icons
- Add GROUP support
 * [group:name] — domain group rules (override default)
 
* Thu Oct 08 2026 Anton Shevtsov <shevtsov.anton@gmail.com> 1.0.0-alt1
- Initial release
- Implemented GUI daemon with AyatanaAppIndicator3 support
- Added XDG autostart for automatic launch on user login
- Added optional system timer for fallback shutdown
- INI-based configuration with flexible rule system:
  * [default] — base settings
  * [user:name] — personal settings (override default)
- Priority-based configuration merging (default < group < user)
- Compatible with GNOME 48+, KDE, MATE
- Case-insensitive username and group name matching
- Custom project icons (SVG + multiple PNG sizes)
- Dual-level protection against user disabling
- Support for 'shutdown_time = none' to disable shutdown for specific users/groups
- Dynamic tray icons (normal blue / warning red)
- Days of week support for scheduled shutdown
- CRITICAL FIX: Changed group detection from 'groups' to 'id -Gn'
  for proper domain user support (Samba AD)
- CRITICAL FIX: Persistent=false in timer to prevent immediate shutdown on enable
- Enhanced sync-timer.py with proper OnCalendar generation for weekdays

