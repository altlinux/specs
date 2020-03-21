%define _unpackaged_files_terminate_build 1

Name: kde5-plasma-kwin-effects-yaml
Version: 4.1.1
Release: alt1.git5892d7e
Summary: Yet Another Magic Lamp is a window minimization effect for KWin
License: GPLv2
Group: Graphical desktop/KDE
Url: https://github.com/zzag/kwin-effects-yet-another-magic-lamp
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildRequires(pre): rpm-build-kf5
BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: qt5-base-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: plasma5-kwin-devel

%description
Yet Another Magic Lamp is a window minimization effect for KWin.
Whenever a window is minimized, it'll get sucked down into the
dock/panel. The main difference between this effect and the one
shipped with KWin is that this effect is more "curvy". In addition
to that, this effect works correctly with weird setups (e.g. the
panel is between screens) and has more configuration options.

%prep
%setup

%build
%K5cmake

%install
%K5install

%files
%_K5plug/kwin/effects/configs/kwin_yetanothermagiclamp_config.so
%_K5plug/kwin/effects/plugins/libkwin4_effect_yetanothermagiclamp.so
%doc LICENSE

%changelog
* Sat Mar 21 2020 Alexander Makeenkov <amakeenk@altlinux.org> 4.1.1-alt1.git5892d7e
- Initial build for ALT

