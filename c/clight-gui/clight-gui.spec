Name: clight-gui
Version: 20220515
Release: alt1

Summary: Qt GUI for clight
Summary(ru_RU.UTF-8): Графический интерфейс Qt для Clight

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://github.com/nullobsi/clight-gui

Requires: libqt5-svg
Requires: clight

# Source-url: https://github.com/nullobsi/clight-gui/archive/refs/heads/main.zip
Source: %name-%version.tar
Source1: %{name}_ru.ts
Source2: %name.desktop

Patch1: %name-20220515-alt-translation.patch

BuildRequires: cmake
BuildRequires: qt5-base-devel
BuildRequires: qt5-charts-devel
BuildRequires: qt5-tools-devel

BuildRequires(pre): rpm-macros-cmake

%description
Customize all aspects of Clight with a beautiful GUI! Tray applet with quick
access to settings.
Clight allows you to match the backlight level to the brightness of the
environment, calculated by capturing frames from a webcam. This allows you to
automatically control screen brightness if your device does not have a light
sensor. At the first start, the program creates configuration files and
analyzes the hardware, this may take some time.

%description -l ru_RU.UTF-8
Настройте все аспекты Clight с помощью красивого графического интерфейса!
Апплет в трее с быстрым доступом к настройкам.
Clight позволяет сопоставить уровень подсветки с яркостью окружающей среды,
рассчитанной путем захвата кадров с веб-камеры. Это позволяет автоматически
управлять яркостью экрана, если на вашем устройстве нет датчика освещенности.
При первом запуске программа создает конфигурационные файлы и анализирует
железо, на это может уйти 10-15 секунд. При первом запуске программа создает
конфигурационные файлы и анализирует железо, это может занять некоторое время.

%prep
%setup
%autopatch -p2

# copy the translation into russian
cp %SOURCE1 src/localization

%build
pushd src
%cmake \
    -DGENERATE_TRANSLATIONS="on"

%cmake_build
popd

%install
pushd src
%cmake_install
popd

# install desktop file
install -Dm 644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

%files
%doc README.md
%_bindir/%name
%_iconsdir/hicolor/scalable/status/*.svg
%_desktopdir/%name.desktop

%changelog
* Tue Sep 20 2022 Evgeny Chuck <koi@altlinux.org> 20220515-alt1
- new version (20220515) with rpmgs script
- Add Russian translation
- Added desktop file
- initial build for ALT Linux Sisyphus

