# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%global with_check 1

%add_python3_compile_include %_libexecdir/uranium

Name:    Uranium
Version: 4.13.0
Release: alt1

Summary:  A Python framework for building Desktop applications.
License: LGPL-3.0
Group:   Development/Python3
URL:     https://github.com/Ultimaker/Uranium

Packager: Anton Midyukov <antohami@altlinux.org>

BuildRequires(pre): rpm-build-python3 rpm-macros-cmake
BuildRequires: python3-devel cmake
BuildRequires:  %_bindir/doxygen
BuildRequires:  %_bindir/msgmerge

# Tests
%if 0%{?with_check}
BuildRequires:  python3-module-Arcus = %version
BuildRequires:  python3-module-numpy
BuildRequires:  python3-module-numpy-testing
BuildRequires:  python3-module-scipy
BuildRequires:  python3-module-PyQt5
BuildRequires:  python3-module-pytest
BuildRequires:  python3-module-pip
BuildRequires:  python3-module-shapely
BuildRequires:  python3-module-twisted-web
BuildRequires:  python3-modules-sqlite3
%endif

BuildArch: noarch

Source: %name-%version.tar
# Source-url: https://github.com/Ultimaker/%name/archive/refs/tags/%version.tar.gz
Patch: Uranium-4.7.1-set-default-languages.patch

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
%autopatch -p1

%build
# there is no arch specific content, so we set LIB_SUFFIX to nothing
# see https://github.com/Ultimaker/Uranium/commit/862a246bdfd7e25541b04a35406957612c6f4bb7
%cmake -DLIB_SUFFIX:STR=
%cmake_build
%cmake_build --target doc

%install
%cmake_install
mv %buildroot/%_datadir/cmake-* %buildroot/%_datadir/cmake

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
python3 -m pytest -v
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
