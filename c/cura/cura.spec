%define _unpackaged_files_terminate_build 1

%def_with check

%add_python3_path %_libexecdir/cura
%add_findprov_skiplist %_libexecdir/cura/*

Name: cura
Epoch: 1
Version: 5.14.0
Release: alt1

Summary: 3D printer / slicing GUI
License: LGPL-3.0-or-later
Group: Engineering
URL: https://github.com/Ultimaker/Cura
VCS: https://github.com/Ultimaker/Cura

Source: %name-%version.tar
# Additional firmware files, changelogs, new release images etc.
# It's AGPL-3.0-or-later.
Source1: %name-binary-data-%version.tar
Source2: CuraVersion.py.in

Patch: %name-%version-%release.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: Uranium >= %version
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-keyring
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-tests
BuildRequires: python3-module-pynest2d
BuildRequires: python3-module-pySavitar
BuildRequires: python3-module-requests
%endif

Requires: CuraEngine = %epoch:%version
Requires: cura-fdm-materials
Requires: 3dprinter-udev-rules
Requires: qt6-declarative
Requires: qt6-svg
Requires: fonts-ttf-google-noto-sans
Requires: fonts-ttf-google-noto-sans-display

%description
Cura is a state-of-the-art slicer app
to prepare your 3D models for your 3D printer.
With hundreds of settings & community-managed print profiles,
Ultimaker Cura is sure to lead your next project to a success.

%prep
%setup -a1
sed 's/@CURA_VERSION@/%version/g' %SOURCE2 > cura/CuraVersion.py
%autopatch -p1

%python3_fix_shebang cura_app.py
rm resources/conan*
rm -r resources/themes/*/fonts

%build
%cmake \
    -DLIB_SUFFIX= \
    -DCURA_NO_INSTALL_PLUGINS=3DConnexion,SentryLogger
%cmake_build

%install
%cmake_install

install -d %buildroot%_desktopdir
sed packaging/AppImage/%name.desktop.jinja \
    -e 's|Exec=UltiMaker-Cura|Exec=%_bindir/%name|' \
    -e 's|{{ cura_version }}|%version|' \
    > %buildroot%_desktopdir/%name.desktop

install -pD -m644 -t %buildroot%_datadir/metainfo \
    packaging/AppImage/%name.appdata.xml

install -pD -m644 %name.sharedmimeinfo \
    %buildroot%_datadir/mime/packages/%name.xml

install -pD -m644 resources/images/%name-icon.png \
    %buildroot%_iconsdir/hicolor/128x128/apps/%name-icon.png
install -pD -m644 resources/images/%name-icon-32.png \
    %buildroot%_iconsdir/hicolor/32x32/apps/%name-icon.png

%find_lang cura fdmextruder.def.json fdmprinter.def.json --output=%name.lang

%check
%__python3 -m pytest -v

%files -f %name.lang
%doc LICENSE README.md CONTRIBUTING.md
%_bindir/%name
%python3_sitelibdir/%name
%_datadir/%name
%_libexecdir/%name
%_desktopdir/%name.desktop
%_datadir/metainfo/%name.appdata.xml
%_datadir/mime/packages/%name.xml
%_iconsdir/hicolor/*/apps/%name-icon.png

%changelog
* Thu Nov 19 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.14.0-alt1
- New version 5.14.0.
- Update summary and description.
- Switch to build from Gear tags.
- Clean up old BRs and automate Requires.
- Bring back UFPReader and UFPWriter plugins.
- Unbundle the fonts to use system ones.
- Install plugins without test files along with them.
- Don't force QT_QPA_PLATFORM and use XDG Desktop Portal (ALT #61381).
- Drop Cura updates checkbox from preferences page.
- Fixes:
  + Export to 3mf files (ALT #60492).
  + Simulation view crash for numpy 2.0+.

* Wed Sep 02 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt6
- Drop unnecessary python3-module-pip build dep.
- Fix cleaning up plugin metadata files.

* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt5
- Drop 3DConnexion plugin (not designed for Linux).
- Drop references to deleted plugins in metadata files.
- Minor spec cleanup.

* Wed Aug 26 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt4
- Drop build type specification to make Cura use the default style.
- Fix issues with Qt 6.9+ (Closes: 40977, 43368, 51690, 59262).
- Spec:
  + Add python3-module-certifi dep for FirmwareUpdateChecker plugin.
  + Add VCS tag.

* Wed Jul 22 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt3
- Fix numpy 2.3.0+ compatibility.

* Fri Jun 05 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt2
- Fix newlines.

* Thu May 28 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.13.0-alt1
- New version 5.13.0.
- Remove dependencies version from about dialog, because these do not
  necessarily match with ALT ones and thus are hard to maintain.

* Tue Apr 21 2026 Valery Zabrovsky <brow@altlinux.org> 1:5.12.1-alt1
- New version 5.12.1.

* Mon Oct 13 2025 Artyom Bystrov <arbars@altlinux.org> 1:5.4.0-alt4
- NMU: add numpy modules in BuildRequires

* Tue Jun 18 2024 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt3
- add dependency on python3(stl) (Closes: 49331)
- spec: convert License to SPDX format

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt2
- fix build with python 3.12

* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 1:5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Thu Apr 27 2023 Anton Midyukov <antohami@altlinux.org> 1:5.3.1-alt1
- new version (5.3.1) with rpmgs script (Closes: 43069)

* Mon Mar 06 2023 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt3
- add 'BuildRequires: python3(importlib_metadata)' for fix build with check

* Sat Mar 05 2022 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt2
- add requires for plugins

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 1:4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 1:4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 1:4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Tue Apr 20 2021 Anton Midyukov <antohami@altlinux.org> 1:4.8-alt2
- merge with p9

* Wed Apr 14 2021 Anton Midyukov <antohami@altlinux.org> 1:4.7.1-alt1.p9
- Use qt style gtk instead material

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 1:4.8-alt1
- New version 4.8

* Fri Sep 18 2020 Anton Midyukov <antohami@altlinux.org> 1:4.7.1-alt1
- New version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 1:4.6.1-alt1
- New version 4.6.1

* Tue Mar 24 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt2
- Avoid crash caused by KDE qqc2 desktop style

* Sun Jan 26 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1.1
- Fix requires

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 1:4.4.1-alt1
- New version 4.4.1

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 1:3.6.0-alt2.1
- NMU: remove rpm-build-ubt from BR:

* Fri Apr 19 2019 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1.1
- Not rebuild locales files

* Fri Dec 21 2018 Anton Midyukov <antohami@altlinux.org> 1:3.6.0-alt1
- New version 3.6.0

* Wed Oct 31 2018 Anton Midyukov <antohami@altlinux.org> 1:3.5.1-alt1
- New version 3.5.1

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 1:3.4.1-alt1
- New version 3.4.1

* Mon May 07 2018 Anton Midyukov <antohami@altlinux.org> 1:3.3.0-alt1.S1
- New version 3.3.0

* Sat Feb 24 2018 Anton Midyukov <antohami@altlinux.org> 1:3.2.1-alt1.S1
- New version 3.2.1
- Disable tests

* Sat Jan 06 2018 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt2
- Fix fail start with nvidia proprietary driver.

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 1:3.0.3-alt1
- New version 3.0.3

* Wed Dec 13 2017 Anton Midyukov <antohami@altlinux.org> 1:2.4.0-alt1
- New version 2.4.0

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt3
- NMU: sync with fc cura-15.04.4-4

* Thu Mar 17 2016 Andrey Cherepanov <cas@altlinux.org> 15.04.4-alt2
- Initial build in Sisyphus

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 15.04.4-alt1_2
- update to new release by fcimport

* Thu Nov 26 2015 Igor Vlasenko <viy@altlinux.ru> 15.02.1-alt1_4
- new version

