%define _unpackaged_files_terminate_build 1

Name: ayatana-settings
Version: 26.6.13
Release: alt1

Summary: Ayatana Indicators Settings
License: GPLv3
Group: Graphical desktop/Other
Url: https://github.com/AyatanaIndicators/ayatana-settings

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake

BuildRequires: ayatana-cmake-modules
BuildRequires: cmake
BuildRequires: intltool
BuildRequires: hicolor-icon-theme
BuildRequires: libgtk4-devel
BuildRequires: mate-themes

%description
Ayatana Settings allows you to configure all your Ayatana system
indicators.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

# these translations are ignored by %%find_lang
rm -fv %buildroot%_datadir/locale/it_CARES/LC_MESSAGES/%name.mo
rm -fv %buildroot%_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/%name.mo

%find_lang %name

%files -f %name.lang
%doc COPYING AUTHORS ChangeLog README.md
%_bindir/ayatana-settings
%_iconsdir/ContrastHigh/scalable/apps/%name.*
%_iconsdir/ContrastHigh/scalable/categories/%name-*
%_iconsdir/hicolor/scalable/apps/%name.*
%_iconsdir/hicolor/scalable/categories/%name-*
%_iconsdir/HighContrast/scalable/apps/%name.*
%_iconsdir/HighContrast/scalable/categories/%name-*

%_desktopdir/ayatana-settings.desktop
%_man8dir/ayatana-settings.8*

%changelog
* Sun Jun 14 2026 Nikolay Strelkov <snk@altlinux.org> 26.6.13-alt1
- New version 26.6.13.

* Sat Nov 23 2024 Nikolay Strelkov <snk@altlinux.org> 24.10.1-alt1
- New version 24.10.1.

* Sun Jan 28 2024 Nikolay Strelkov <snk@altlinux.org> 21.1.28-alt3
- Handle review issues:
  + removed obsolete Packager tag
  + break Requires to multiple lines
  + do not own icons dirs (thanks to @antohami)

* Mon Aug 07 2023 Nikolay Strelkov <snk@altlinux.org> 21.1.28-alt2
- Removed translation which is ignored by %%find_lang
- Language specific files are declared

* Mon Nov 07 2022 Nikolay Strelkov <snk@altlinux.org> 21.1.28-alt1
- Initial build for Sisyphus
