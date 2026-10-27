%define modulename indicator_sound_switcher
%define app_id com.yktoo.IndicatorSoundSwitcher

Name:    indicator-sound-switcher
Version: 2.4.0.0
Release: alt1

Summary: Sound input/output selector indicator for Linux
License: GPL-3.0-only
Group:   Development/Python3
URL:     https://github.com/yktoo/indicator-sound-switcher
VCS:     https://github.com/yktoo/indicator-sound-switcher.git

BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-build-gir
BuildRequires: rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
%add_typelib_req_skiplist typelib(AppIndicator3)

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-%release.patch

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

mv %buildroot%python3_sitelibdir%_sysconfdir %buildroot

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/%name
%_desktopdir/%app_id.desktop
%_iconsdir/hicolor/*/*/*.svg
%_iconsdir/hicolor/*/*/*.png
%_man1dir/%name.1.*
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%_sysconfdir/xdg/autostart/%app_id.desktop

%changelog
* Tue Oct 27 2026 Anton Midyukov <antohami@altlinux.org> 2.4.0.0-alt1
- New version 2.4.0.0.

* Thu Aug 22 2024 Anton Midyukov <antohami@altlinux.org> 2.3.10.1-alt1
- New version 2.3.10.1.

* Mon Feb 13 2023 Anton Midyukov <antohami@altlinux.org> 2.3.9-alt1
- new version 2.3.9
- require typelib(AyatanaAppIndicator3) instead typelib(AppIndicator3)

* Mon Jun 20 2022 Anton Midyukov <antohami@altlinux.org> 2.3.8-alt1
- new version 2.3.8

* Tue Jul 21 2020 Anton Midyukov <antohami@altlinux.org> 2.3.4-alt1
- Initial build for Sisyphus
