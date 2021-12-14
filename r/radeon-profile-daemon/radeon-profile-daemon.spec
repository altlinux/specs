Name: radeon-profile-daemon
Version: 20190603
Release: alt1

Summary: Daemon for radeon-profile GUI
Summary(ru_RU.UTF-8): Демон для графического интерфейса radeon-profile
License: GPL-2.0
Group: System/Kernel and hardware
Url: https://github.com/marazmista/radeon-profile
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://github.com/marazmista/radeon-profile-daemon/archive/refs/tags/%version.tar.gz
Patch: 20190603-fixed-systemd-path.patch

Requires: radeon-profile

BuildRequires(pre): rpm-macros-qt5
BuildRequires: qt5-charts-devel
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel

%description
System daemon for reading info about Radeon GPU clocks and volts as well as
control card power profiles so the GUI radeon-profile application can be run
as normal user.
Supports opensource xf86-video-ati and xf86-video-amdgpu drivers.

%description -l ru_RU.UTF-8
Системная служба мониторинга тактовой частоты и напряжения графического
процессора Radeon, а также считывания профилей питания управляющих карт.
Позволяет графическому интерфейсу radeon-profile работать от обычного
пользователя.
Поддерживает драйверы xf86-video-ati и xf86-video-amdgpu с открытым исходным
кодом.

%prep
%setup
%patch -p1

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%post
SYSTEMCTL=systemctl
%post_service radeon-profile-daemon
if [ $1 = 1 ] && sd_booted && "$SYSTEMCTL" --version >/dev/null 2>&1; then
    "$SYSTEMCTL" enable radeon-profile-daemon.service >/dev/null 2>&1 || :
fi

%preun
%preun_service radeon-profile-daemon

%files
%doc README.md LICENSE
%_bindir/%name
%_unitdir/%name.service

%changelog
* Sun Nov 07 2021 Evgeny Chuck <koi@altlinux.org> 20190603-alt1
- initial build for ALT Linux Sisyphus
