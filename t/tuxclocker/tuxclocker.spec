%define libname libtuxclocker
%global __find_debuginfo_files %nil

Name:    tuxclocker
Version: 1.5.1
Release: alt1

Summary: Qt overclocking tool for GNU/Linux
License: GPL-3.0
Group:   System/Configuration/Hardware
Url:     https://github.com/Lurkki14/tuxclocker
VCS:     https://github.com/Lurkki14/tuxclocker.git

Source: %name-%version.tar
Source1: submodules-%name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: gcc-c++ cmake meson git
BuildRequires: libssl-devel boost-devel libdrm-devel hwdata-devel
BuildRequires: python3-module-hwdata python3-dev libnvidia-ml libXext-devel
BuildRequires: libxnvctrl-devel qt5-base-devel qt5-tools qt5-charts-devel
BuildRequires: boost-filesystem-devel boost-signals-devel
Requires: libqt5-charts
Requires: libnvidia-ml
Requires: dbus
Requires: icon-theme-hicolor

ExclusiveArch: x86_64

%description
TuxClocker is a hardware controlling and monitoring program.
TuxClocker consists of a DBus daemon and a Qt GUI that uses the daemon.

%prep
%setup -a1

%build
%meson \
    -Dplugins=true \
    -Ddaemon=true \
    -Drequire-nvidia=true \
    -Drequire-amd=true \
    -Drequire-python-hwdata=true
%meson_build

%install
%meson_install

%find_lang %name

%files -f %name.lang
%doc LICENSE README.md
%_bindir/tuxclocker-qt
%_bindir/tuxclockerd
%dir %_libdir/tuxclocker
%dir %_libdir/tuxclocker/plugins
%_libdir/tuxclocker/plugins/*.so
%_libdir/libtuxclocker.so
%_datadir/applications/%name.desktop
%_datadir/dbus-1/system-services/org.tuxclocker.service
%_datadir/dbus-1/system.d/org.tuxclocker.conf
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Wed Feb 26 2025 Sergey Palcheh <minergenon@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus

