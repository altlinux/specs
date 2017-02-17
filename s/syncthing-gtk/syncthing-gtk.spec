#%%def_enable mate-file-manager-syncthing-gtk
#%%def_enable nemo-syncthing-gtk
#%%def_enable nautilus-syncthing-gtk

Name: syncthing-gtk
Version: 0.9.2.4
Release: alt2
Summary: Syncthing Gtk-based graphical interface
Summary(ru_RU.UTF-8): Основанный на GTK графический интерфейс для Syncthing
License: GPLv2+
Group: Networking/Other
Url: https://github.com/syncthing/syncthing-gtk
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildPreReq: python-devel python-module-setuptools desktop-file-utils
Requires: syncthing >= 0.14
Requires: librsvg-gir
Requires: icon-theme-hicolor
BuildArch: noarch

%description
Graphical user interface with notification area icon for Syncthing
based on GTK+ and Python.

Supported Syncthing features:
 * Everything what WebUI can display.
 * Adding / editing / deleting nodes.
 * Adding / editing / deleting repositories.
 * Restart / shutdown server.
 * Editing daemon settings.

Additional features:
 * First run wizard for initial configuration.
 * Running Syncthing daemon in background.
 * Half-automatic setup for new nodes and repositories.
 * Filesystem watching and instant synchronization using inotify.
 * Caja, Nautilus, and Nemo file managers integration.
 * Desktop notifications.

%description -l ru_RU.UTF-8
Графический пользовательский интерфейс со значком в области уведомлений для
Syncthing, основанный на GTK и Python.

Основные возможности Syncthing: 
* Всё тоже, что может отображать WebUI
* Добавление / редактирование / удаление узлов
* Добавление / редактирование / удаление репозиториев
* Перезагрузка / выключение сервера
* Параметры демона редактирования.

Дополнительные возможности:
* Первый мастер запуска для начальной конфигурации
* Запуск Syncthing демон в фоновом режиме
* Полу-автоматическая настройка для новых узлов и хранилищ
* Filesystem смотреть и мгновенные синхронизация с помощью Inotify
* Интеграция с файловыми менеджерами Caja, Nautilus и Nemo
* Вывод уведомлений на рабочий стол.

%if_enabled mate-file-manager-syncthing-gtk
%package -n mate-file-manager-syncthing-gtk
Summary: Syncthing-GTK+ client integrated into mate-file-manager
Summary(ru_RU.UTF-8): Интеграция Syncthing-gtk с mate-file-manager
Group: Graphical desktop/GNOME 
Requires: mate-file-manager
Requires: python-module-caja
Requires: syncthing-gtk = %version

%description -n mate-file-manager-syncthing-gtk
Graphical user interface with notification area icon for Syncthing
based on GTK+ and Python.

This package integrates Syncthing-GTK+ seamlessly into mate-file-manager.

%description -n mate-file-manager-syncthing-gtk -l ru_RU.UTF-8
Графический пользовательский интерфейс со значком в области уведомлений для
Syncthing, основанный на GTK и Python.

Это пакет интеграции Syncthing-gtk c mate-file-manager.
%endif

%if_enabled nemo-syncthing-gtk
%package -n nemo-syncthing-gtk
Summary: Syncthing-GTK+ client integrated into Nemo
Summary(ru_RU.UTF-8): Интеграция Syncthing-gtk с Nemo
Group: Graphical desktop/GNOME 
Requires: nemo
Requires: nemo-python
Requires: syncthing-gtk = %version

%description -n nemo-syncthing-gtk
Graphical user interface with notification area icon for Syncthing
based on GTK+ and Python.

This package integrates Syncthing-GTK+ seamlessly into Nemo.

%description -n nemo-syncthing-gtk -l ru_RU.UTF-8
Графический пользовательский интерфейс со значком в области уведомлений для
Syncthing, основанный на GTK и Python.

Это пакет интеграции Syncthing-gtk с файловым менеджером Nemo.
%endif

%if_enabled nautilus-syncthing-gtk
%package -n nautilus-syncthing-gtk
Summary: Syncthing-GTK+ client integrated into Nautilus
Summary(ru_RU.UTF-8): Интеграция Syncthing-gtk с Nautilus
Group: Graphical desktop/GNOME 
Requires: nautilus
Requires: nautilus-python
Requires: syncthing-gtk = %version

%description -n nautilus-syncthing-gtk
Graphical user interface with notification area icon for Syncthing
based on GTK+ and Python.

This package integrates Syncthing-GTK+ seamlessly into Nautilus.

%description -n nautilus-syncthing-gtk -l ru_RU.UTF-8
Графический пользовательский интерфейс со значком в области уведомлений для
Syncthing, основанный на GTK и Python.

Это пакет интеграции Syncthing-gtk с файловым менеджером Nautilus.
%endif

%prep
%setup
%__subst 's/^\(Exec=\).*$/\1%name/' %name.desktop

%build
%python_build

%install
%python_install
rm -rf %buildroot%python_sitelibdir/syncthing_gtk/windows.*

#fix categories desktop file
desktop-file-edit --add-category=FileTransfer %buildroot%_desktopdir/%name.desktop

%if_enabled mate-file-manager-syncthing-gtk
install -Dm 0644 scripts/syncthing-plugin-caja.py \
  %buildroot%_datadir/caja-python/extensions/syncthing-gtk.py
%endif

%if_enabled nemo-syncthing-gtk
install -Dm 0644 scripts/syncthing-plugin-nemo.py \
  %buildroot%_datadir/nemo-python/extensions/syncthing-gtk.py
%endif

%if_enabled nautilus-syncthing-gtk
install -Dm 0644 scripts/syncthing-plugin-nautilus.py \
  %buildroot%_datadir/nautilus-python/extensions/syncthing-gtk.py
%endif
  
# Add execution bit to scripts with shebangs and remove from others.
find %{buildroot} -type f -name "*.py" | while read py; do
    if [[ "$(head -c2 "$py"; echo)" == "#!" ]]; then
        chmod a+x "$py"
    else
        chmod a-x "$py"
    fi
done

%find_lang %name

%files -f %name.lang
%doc LICENSE README.md
%_bindir/%name
%_datadir/%name/
%python_sitelibdir/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/*/*.png
%_pixmapsdir/*.png

%if_enabled mate-file-manager-syncthing-gtk
%files -n mate-file-manager-syncthing-gtk
%dir %_datadir/caja-python/
%dir %_datadir/caja-python/extensions/
%_datadir/caja-python/extensions/syncthing-gtk.py
%endif

%if_enabled nemo-syncthing-gtk
%files -n nemo-syncthing-gtk
%dir %_datadir/nemo-python/
%dir %_datadir/nemo-python/extensions/
%_datadir/nemo-python/extensions/syncthing-gtk.py
%endif

%if_enabled nautilus-syncthing-gtk
%files -n nautilus-syncthing-gtk
%dir %_datadir/nautilus-python/
%dir %_datadir/nautilus-python/extensions/
%_datadir/nautilus-python/extensions/syncthing-gtk.py
%endif

%changelog
* Fri Feb 17 2017 Anton Midyukov <antohami@altlinux.org> 0.9.2.4-alt2
- Added cronbuild options

* Fri Feb 03 2017 Anton Midyukov <antohami@altlinux.org> 0.9.2.4-alt1
- new version 0.9.2.4

* Wed Nov 23 2016 Anton Midyukov <antohami@altlinux.org> 0.9.2.3-alt1
- new version 0.9.2.3

* Sun Oct 09 2016 Anton Midyukov <antohami@altlinux.org> 0.9.2.2-alt1
- new version 0.9.2.2

* Sun Sep 04 2016 Anton Midyukov <antohami@altlinux.org> 0.9.2.1-alt1
- New version 0.9.2.1
- fix categories desktop file
- added cronbuild-update-source

* Mon Aug 22 2016 Anton Midyukov <antohami@altlinux.org> 0.9.1-alt1
- New version

* Fri May 27 2016 Anton Midyukov <antohami@altlinux.org> 0.9.0.2-alt1
- New version
- Added requires on librsvg-gir
- Disable plugin for caja, nemo, nautilus.

* Tue Apr 26 2016 Anton Midyukov <antohami@altlinux.org> 0.8.3-alt1
- Initial build for ALT Linux Sisyphus
- Added russian translation.
