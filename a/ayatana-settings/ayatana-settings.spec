%define _unpackaged_files_terminate_build 1

Name: ayatana-settings
Version: 21.1.28
Release: alt1

Summary: Ayatana Indicators Settings
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-settings

Packager: Nikolay Strelkov <snk@altlinux.org>
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

BuildRequires: hicolor-icon-theme
BuildRequires: python3-module-polib
BuildRequires: python3-module-psutil
BuildRequires: python3-module-setuptools

Requires: typelib(Gtk) = 3.0
Requires: python3-module-polib python3-module-psutil

%description
Ayatana Settings allows you to configure all your Ayatana system
indicators.

%prep
%setup

# Remove hashbangs on scripts installed into sitelib.
find 'ayatanasettings' -type 'f' -iname '*.py' -exec sed -i -e '0,/^\s*#!\s*\/.*$/d' '{}' '+'

# Also remove executable flags.
find 'ayatanasettings' -type 'f' -iname '*.py' -exec chmod -x '{}' '+'

%build
%python3_build

%install
%python3_install

%files
%doc COPYING AUTHORS ChangeLog README.md
%_bindir/ayatana-settings
%_man1dir/ayatana-settings.1.*
%python3_sitelibdir/ayatanasettings
%python3_sitelibdir/ayatana_settings-%{version}*-info
%dir %_iconsdir/hicolor/scalable
%dir %_iconsdir/hicolor/scalable/apps
%_iconsdir/hicolor/scalable/apps/%name.*
%_desktopdir/ayatana-settings.desktop
%_datadir/ayatana-settings/
%_datadir/locale/*/LC_MESSAGES/*.mo

%changelog
* Mon Nov 07 2022 Nikolay Strelkov <snk@altlinux.org> 21.1.28-alt1
- Initial build for Sisyphus
