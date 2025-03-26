%define app_id io.github.SokolovValy.MobileAuth

Name: mobile-auth
Version: 1.1
Release: alt1

Summary: Alt Mobile domain input tool.
License: GPL-3.0-or-later
Group: System/Configuration/Other
Url: https://github.com/SokolovValy/alt-mobile-auth
VCS: https://github.com/SokolovValy/alt-mobile-auth
BuildArch: noarch

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-python3
BuildRequires: meson
BuildRequires: rpm-build-python3
BuildRequires: rpm-macros-alterator
BuildRequires: libgtk4-devel
BuildRequires: libadwaita-devel
BuildRequires: %_bindir/appstreamcli desktop-file-utils blueprint-compiler
Requires: alterator-auth
Requires: alterator-manager
Requires: alterator-module-executor

Source0: %name-%version.tar

%description
Alt Mobile domain input tool.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/metainfo/%app_id.metainfo.xml
%_alterator_datadir/backends/system/mobile-auth.backend
%_datadir/polkit-1/actions/org.altlinux.alterator.mobile-auth1.policy
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/locale/*/LC_MESSAGES/%name.mo
%python3_sitelibdir/mobileauth
%_datadir/%app_id/%app_id.gresource


%changelog
* Fri Mar 07 2025 Valentin Sokolov <sova@altlinux.org> 1.1-alt1
- Added additional sections to .desktop file
- Improver translation file

* Mon Feb 10 2025 Valentin Sokolov <sova@altlinux.org> 1.0-alt1
- Renamed interface and .policy file names (ru.basealt -> org.altlinux)
- Renamed authentication metod (In_domain -> Join)
- Changed .backend file format (ini -> toml)
- Added Readme

* Wed Sep 04 2024 Valentin Sokolov <sova@altlinux.org> 0.1.1-alt1
- Added desktop icon

* Wed Sep 04 2024 Valentin Sokolov <sova@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
