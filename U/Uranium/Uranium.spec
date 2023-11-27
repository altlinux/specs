# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global with_check 1

%add_python3_compile_include %_libexecdir/uranium

Name:    Uranium
Version: 5.3.1
Release: alt2

Summary:  A Python framework for building Desktop applications.
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/Ultimaker/Uranium

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-devel cmake
BuildRequires:  %_bindir/doxygen
BuildRequires:  %_bindir/msgmerge

# Tests
%if 0%{?with_check}
BuildRequires:  python3-module-Arcus
BuildRequires:  python3-module-numpy
BuildRequires:  python3-module-numpy-testing
BuildRequires:  python3-module-scipy
BuildRequires:  python3-module-PyQt6
BuildRequires:  python3-module-pytest
BuildRequires:  python3-module-pip
BuildRequires:  python3-module-shapely
BuildRequires:  python3-module-twisted-web
BuildRequires:  python3-modules-sqlite3
BuildRequires:  python3-module-pyclipper
%endif

BuildArch: noarch

# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Cmake bits taken from 4.13.1, before upstream went nuts with conan
Source2: mod_bundled_packages_json.py
Source3: UraniumPluginInstall.cmake
Source4: UraniumTests.cmake
Source5: UraniumTranslationTools.cmake
Source6: CMakeLists.txt
Source7: CPackConfig.cmake
Source8: Doxyfile

Patch: Uranium-4.7.1-set-default-languages.patch

# from Fedora
Patch2: Uranium-5.3.0-qt-try-ints-then-bytes-for-gl-mask-functions.patch
Patch3: Uranium-5.3.0-qt-6.5-hack.patch

%description
%summary

%package doc
Summary: Documentation for %name package
Group: Documentation

%description doc
Documentation for Uranium, a Python framework for building 3D printing
related applications.

%prep
%setup
#mkdir cmake
cp -a %SOURCE2 %SOURCE3 %SOURCE4 %SOURCE5 cmake/
rm CMakeLists.txt
cp -a %SOURCE6 %SOURCE7 %SOURCE8 .
 
# fix compile-shaders
sed -i 's|qsb |qsb-qt6 |g' scripts/compile-shaders

%autopatch -p1

%build
# there is no arch specific content, so we set LIB_SUFFIX to nothing
# see https://github.com/Ultimaker/Uranium/commit/862a246bdfd7e25541b04a35406957612c6f4bb7
%cmake -DLIB_SUFFIX:STR=
%cmake_build
%cmake_build -- doc

%install
%cmake_install
mv %buildroot/%_datadir/cmake* %buildroot/%_datadir/cmake

# Sanitize the location of locale files
pushd %buildroot%_datadir
mv uranium/resources/i18n locale
ln -s ../../locale uranium/resources/i18n
rm locale/uranium.pot
rm locale/*/uranium.po
popd

%find_lang uranium

%check
%if 0%{?with_check}
pip3 freeze
# skipping failing tests, see:
# * https://github.com/Ultimaker/Uranium/issues/594
# * https://github.com/Ultimaker/Uranium/issues/603
python3 -m pytest -v -k "not (TestSettingFunction and test_init_bad) and not TestHttpRequestManager"
%endif

%files -f uranium.lang
%doc LICENSE README.md
%python3_sitelibdir/*
%_libexecdir/uranium
%_datadir/uranium
%_datadir/cmake/Modules/*

%files doc
%doc html LICENSE

%changelog
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
