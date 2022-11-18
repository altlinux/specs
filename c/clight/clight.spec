Name: clight
Version: 4.9
Release: alt1

Summary: Monitor brightness control daemon
Summary(ru_RU.UTF-8): Демон управления яркостью монитора

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://github.com/FedeDP/Clight/wiki

Requires: clightd

# Source-url: https://github.com/FedeDP/Clight/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

Patch1: %name-4.9-alt-desktop.patch
Patch2: %name-4.9-alt-desktop_translation.patch

BuildRequires: cmake
BuildRequires: libpopt-devel
BuildRequires: geoclue2-devel
BuildRequires: libgsl-devel
BuildRequires: libconfig-devel
BuildRequires: libmodule-devel
BuildRequires: libsystemd-devel
BuildRequires: libdbus-devel
BuildRequires: libupower-devel
BuildRequires: bash-completion

BuildRequires(pre): rpm-macros-cmake

%description
Clight allows you to match the backlight level to the brightness of
the environment, calculated by capturing frames from a webcam or ambient
light sensors. It also supports setting up external monitors and keyboard
backlighting. What's more, it can control the temperature of the screen.
Finally, it can dim the screen after timeout and control the DPMS screen.
Suitable for automatic brightness adjustment on a PC without light sensors.
Requires Clightd to work. Only systemd support.

%description -l ru_RU.UTF-8
Clight позволяет сопоставить уровень подсветки с яркостью окружающей среды,
вычисленной путем захвата кадров с веб-камеры или датчиков внешней
освещенности. Он также поддерживает настройку внешних мониторов и подсветку
клавиатуры. Более того, он может контролировать температуру экрана. Наконец,
он может затемнить экран после тайм-аута и управлять экраном DPMS. Подходит
для автоматической регулировки яркости на ПК без датчиков освещенности.
Требуется Clightd для работы. Поддержка только systemd.


%package devel
Summary: Module development package for Clight
Summary(ru_RU.UTF-8): Пакет разработки модулей для Clight
Group: Development/Other
BuildArch: noarch
Requires: %name = %EVR

%description devel
This package contains header files for creating modules for Clight.

%description devel -l ru_RU.UTF-8
Этот пакет содержит заголовочные файлы для создания модулей к Clight.


%prep
%setup
%autopatch -p2

%build
%cmake
%cmake_build

%install
%cmake_install

%preun
killall clight >/dev/null 2>&1 ||:

%files
%doc README.md
%_sysconfdir/default/%name.conf
%_sysconfdir/xdg/autostart/%name.desktop
%_bindir/%name
%_desktopdir/%{name}c.desktop
%_datadir/%name
%_datadir/dbus-1/services/org.%name.%name.service
%_iconsdir/hicolor/scalable/apps/%name.svg
%_man1dir/%name.1.xz
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%files devel
%_includedir/%name/*.h

%changelog
* Fri Nov 18 2022 Evgeny Chuck <koi@altlinux.org> 4.9-alt1
- new version (4.9) with rpmgs script
- Fixed patches of the old version v4.8 under the new v4.9

* Thu Sep 15 2022 Evgeny Chuck <koi@altlinux.org> 4.8-alt1
- new version (4.8) with rpmgs script
- Fixed desktop category
- initial build for ALT Linux Sisyphus

