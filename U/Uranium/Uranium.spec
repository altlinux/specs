%define _unpackaged_files_terminate_build 1

%def_with check

%add_python3_path %_libexecdir/uranium
%add_findprov_skiplist %_libexecdir/uranium/*

Name: Uranium
Version: 5.14.0
Release: alt2

Summary: A Python framework for building 3D printing desktop applications
License: LGPL-3.0-or-later
Group: Development/Python3
URL: https://github.com/Ultimaker/Uranium
VCS: https://github.com/Ultimaker/Uranium

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: rpm-build-python3
BuildRequires: cmake
BuildRequires: %_bindir/msgmerge
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-pyArcus
BuildRequires: python3-module-pyclipper
BuildRequires: python3-module-PyQt6
BuildRequires: python3-module-pyUvula
BuildRequires: python3-module-scipy
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-twisted-web
%endif

BuildArch: noarch

%description
%summary.

%prep
%setup
%autopatch -p1

# fix compile-shaders
sed -i 's|qsb |qsb-qt6 |g' scripts/compile-shaders

%build
%cmake \
    -DLIB_SUFFIX= \
    -DUM_NO_INSTALL_PLUGINS=UpdateChecker
%cmake_build

%install
%cmake_install

%find_lang uranium

%check
%__python3 -m pytest -v

%files -f uranium.lang
%doc LICENSE README.md
%python3_sitelibdir/*
%_libexecdir/uranium
%_datadir/uranium
%_datadir/cmake/Modules/*

%pretrans -p <lua>
path = "%_datadir/uranium/resources/i18n"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%changelog
* Tue Nov 24 2026 Valery Zabrovsky <brow@altlinux.org> 5.14.0-alt2
- Add pretrans script for Uranium locale dir (ALT #61587).

* Wed Nov 18 2026 Valery Zabrovsky <brow@altlinux.org> 5.14.0-alt1
- New version 5.14.0.
- Switch to build from Gear tags.
- Drop doc package (unmaintained upstream).
- Move locale files back to Uranium dir.
- Install plugins without test files along with them.
- Don't use parentheses in STL mime types (ALT #43363).
- Enable checks on i586.

* Wed Sep 02 2026 Valery Zabrovsky <brow@altlinux.org> 5.13.0-alt5
- Drop unnecessary python3-module-pip build dep.
- Fix cleaning up plugin metadata files.

* Mon Aug 31 2026 Valery Zabrovsky <brow@altlinux.org> 5.13.0-alt4
- Fix python3-module-pyArcus build dep.

* Wed Aug 26 2026 Valery Zabrovsky <brow@altlinux.org> 5.13.0-alt3
- Remove UpdateChecker plugin.
- Fix issues with Qt 6.9+.
- Spec: add VCS tag.

* Wed Jul 22 2026 Valery Zabrovsky <brow@altlinux.org> 5.13.0-alt2
- Fix FTBFS with python3.14.
- Fix numpy 2.3.0+ compatibility.

* Wed May 27 2026 Valery Zabrovsky <brow@altlinux.org> 5.13.0-alt1
- New version 5.13.0.

* Thu Apr 16 2026 Valery Zabrovsky <brow@altlinux.org> 5.12.1-alt1
- New version 5.12.1.

* Tue Feb 24 2026 Stanislav Levin <slev@altlinux.org> 5.4.0-alt6
- NMU: fixed FTBFS (pytest 9).

* Mon Feb 09 2026 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt5
- Disable check on %%ix86.

* Tue Oct 29 2024 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt4
- upstream-Replace-deprecated-imp.patch

* Mon Feb 26 2024 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt3
- Disable failed tests

* Sun Jan 28 2024 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt2
- Fix build with python 3.12

* Mon Dec 18 2023 Anton Midyukov <antohami@altlinux.org> 5.4.0-alt1
- new version (5.4.0) with rpmgs script

* Mon Nov 27 2023 Anton Midyukov <antohami@altlinux.org> 5.3.1-alt2
- Add patches for qt6.6 support

* Tue Apr 25 2023 Anton Midyukov <antohami@altlinux.org> 5.3.1-alt1
- new version (5.3.1) with rpmgs script

* Wed Jan 26 2022 Anton Midyukov <antohami@altlinux.org> 4.13.0-alt1
- new version (4.13.0) with rpmgs script

* Mon Dec 13 2021 Anton Midyukov <antohami@altlinux.org> 4.12.1-alt1
- new version (4.12.1) with rpmgs script

* Sat Sep 11 2021 Anton Midyukov <antohami@altlinux.org> 4.11.0-alt1
- new version (4.11.0) with rpmgs script

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 4.8-alt2.1
- NMU: spec: adapted to new cmake macros.

* Tue Apr 20 2021 Anton Midyukov <antohami@altlinux.org> 4.8-alt2
- merge with p9

* Thu Apr 15 2021 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt1.p9
- Fix setup default language

* Sun Nov 15 2020 Anton Midyukov <antohami@altlinux.org> 4.8-alt1
- New version 4.8

* Thu Nov 12 2020 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt2
- Fix buildrequires

* Thu Sep 17 2020 Anton Midyukov <antohami@altlinux.org> 4.7.1-alt1
- New version 4.7.1

* Thu May 07 2020 Anton Midyukov <antohami@altlinux.org> 4.6.1-alt1
- New version 4.6.1

* Sat Jan 25 2020 Anton Midyukov <antohami@altlinux.org> 4.4.1-alt1
- New version 4.4.1

* Thu Oct 03 2019 Stanislav Levin <slev@altlinux.org> 3.6.0-alt4
- Fixed testing.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 3.6.0-alt3
- NMU: remove rpm-build-ubt from BR:

* Tue Jun 04 2019 Stanislav Levin <slev@altlinux.org> 3.6.0-alt2
- Fixed Pytest4.x compatibility errors.

* Fri Feb 01 2019 Anton Midyukov <antohami@altlinux.org> 3.6.0-alt1
- New version 3.6.0

* Wed Jan 30 2019 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1.1
- Fix BuildRequires

* Mon Sep 03 2018 Anton Midyukov <antohami@altlinux.org> 3.4.1-alt1
- New version 3.4.1

* Sun May 06 2018 Anton Midyukov <antohami@altlinux.org> 3.3.0-alt1.S1
- New version 3.3.0

* Fri Feb 23 2018 Anton Midyukov <antohami@altlinux.org> 3.2.1-alt1.S1
- New version 3.2.1

* Sun Dec 31 2017 Anton Midyukov <antohami@altlinux.org> 3.0.3-alt1
- New version 3.0.3

* Wed Nov 22 2017 Anton Midyukov <antohami@altlinux.org> 2.4.0-alt1
- Initial build for Sisyphus
