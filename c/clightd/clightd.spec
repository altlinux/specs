Name: clightd
Version: 5.7
Release: alt1

Summary: Linux DBUS interface for the Clight daemon
Summary(ru_RU.UTF-8): Интерфейс DBUS Linux для демона Clight

License: GPL-3.0-only
Group: System/Configuration/Hardware
Url: https://github.com/FedeDP/Clightd/wiki

# Source-url: https://github.com/FedeDP/Clightd/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: libddcutil-devel
BuildRequires: libjpeg-devel
BuildRequires: libpolkit-devel
BuildRequires: libXrandr-devel
BuildRequires: libX11-devel
BuildRequires: libwayland-client-devel
BuildRequires: libdrm-devel
BuildRequires: libXext-devel
BuildRequires: libusb-devel
BuildRequires: wayland-devel
BuildRequires: libmodule-devel
BuildRequires: libudev-devel
BuildRequires: libsystemd-devel
BuildRequires: libdbus-devel
BuildRequires: pipewire-libs-devel

BuildRequires(pre): rpm-macros-cmake

%description
Clightd is a tire interface that allows you to easily configure the brightness
of the screen, gamma-temperature and get the brightness of the environment by
capturing frames from webcams. Als sensors are also supported. Clightd uses
Clight as a server part. Clightd comes with the Systemd service. Only systemd
support.

%description -l ru_RU.UTF-8
Clightd - это DBUS интерфейс, который позволяет легко настраивать яркость
экрана, гамма-температуру и получать яркость окружающей среды с помощью
захвата кадров с веб-камеры. Также поддерживаются датчики Als. Clightd
использует Clight как серверную часть. Clightd поставляется с сервисом
Systemd. Поддержка только systemd.

%prep
%setup

%build
%cmake \
    -DENABLE_GAMMA=1 \
    -DENABLE_DDC=1 \
    -DENABLE_DPMS=1 \
    -DENABLE_SCREEN=1 \
    -DENABLE_YOCTOLIGHT=1

%cmake_build

%install
%cmake_install

%preun
%preun_service clightd >/dev/null 2>&1 ||:

%files
%doc README.md
%_sysconfdir/dbus-1/system.d/org.%name.%name.conf
%_modulesloaddir/i2c_%name.conf
%_unitdir/%name.service
%_prefix/libexec/%name
%_datadir/dbus-1/system-services/org.%name.%name.service
%_datadir/polkit-1/actions/org.%name.%name.policy

%changelog
* Fri Nov 18 2022 Evgeny Chuck <koi@altlinux.org> 5.7-alt1
- new version (5.7) with rpmgs script

* Mon Sep 19 2022 Evgeny Chuck <koi@altlinux.org> 5.6-alt1
- new version (5.6) with rpmgs script
- initial build for ALT Linux Sisyphus

