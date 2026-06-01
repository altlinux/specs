Name: razergenie
Version: 1.3.0
Release: alt1

Summary: Standalone Qt application for configuring your Razer devices under GNU/Linux
License: GPLv3
Group: System/Configuration/Hardware
Url: https://github.com/z3ntu/RazerGenie

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake meson
BuildRequires: qt6-base-devel qt6-tools-devel qt6-declarative-devel
BuildRequires: libopenrazer-devel
Requires: openrazer

%description
Standalone Qt application for configuring your Razer devices under GNU/Linux.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc LICENSE.md README.md
%_bindir/%name
%_datadir/%name/*
%_datadir/metainfo/xyz.z3ntu.razergenie.appdata.xml
%_desktopdir/xyz.z3ntu.%name.desktop
%_iconsdir/hicolor/scalable/apps/xyz.z3ntu.%name.svg

%changelog
* Mon Jun 01 2026 Sergey Palcheh <minergenon@altlinux.org> 1.3.0-alt1
- new version 1.3.0

* Mon Jan 13 2025 Sergey Palcheh <minergenon@altlinux.org> 1.2.0-alt1
- initial build for ALT Sisyphus
