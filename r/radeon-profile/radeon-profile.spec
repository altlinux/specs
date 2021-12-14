Name: radeon-profile
Version: 20200824
Release: alt1

Summary: Application for monitoring equipment of ATi Radeon cards
Summary(ru_RU.UTF-8): Приложение для мониторинга оборудования карт ATi Radeon
License: GPL-2.0
Group: System/Kernel and hardware
Url: https://github.com/marazmista/radeon-profile
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://github.com/marazmista/radeon-profile/archive/refs/tags/%version.tar.gz

Requires: glxinfo
Requires: xrandr
Requires: xdriinfo
Requires: icon-theme-hicolor
Requires: radeon-profile-daemon

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: qt5-charts-devel
BuildRequires: qt5-base-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-tools
BuildRequires: libXrandr-devel
BuildRequires: libdrm-devel

%description
Monitoring of basic GPU parameters (frequencies, voltages, usage, temperature,
fan speed)
DPM profiles and power levels
Fan control (HD 7000+), definition of multiple custom curves or fixed speed
Overclocking (amdgpu) (Wattman, Overdrive, PowerPlay etc)
Per app profiles/Event definitions (i.e. change fan profile when temp above
defined or set DPM to high when selected binary executed)
Define binaries to run with set of environment variablees
(i.e. GALLIUM_HUD, MESA, LIBGL etc)

%description -l ru_RU.UTF-8
Мониторинг основных параметров графического процессора (частоты, напряжения,
использование, температура, скорость вращения вентилятора)
Профили DPM и уровни мощности
Управление вентилятором (HD 7000+), определение нескольких пользовательских
кривых или фиксированная скорость
Разгон (amdgpu) (Wattman, Overdrive, PowerPlay и т. Д.)
Для профилей приложений/определений событий (например, изменение
профиля вентилятора, когда температура выше определенной, или установка
высокого уровня DPM при выполнении выбранного двоичного файла)
Определите двоичные файлы для запуска с набором переменных среды
(например, GALLIUM_HUD, MESA, LIBGL и т. Д.)

%prep
%setup

%build
lrelease-qt5 %name.pro

%qmake_qt5 %name.pro
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

pushd translations
find . -name '*.qm' -exec install -Dpm644 '{}' -t '%buildroot%_datadir/%name/' \;
popd

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sat Nov 06 2021 Evgeny Chuck <koi@altlinux.org> 20200824-alt1
- initial build for ALT Linux Sisyphus
