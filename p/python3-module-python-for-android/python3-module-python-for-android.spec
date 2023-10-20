%define oname python-for-android

%def_with check

Name: python3-module-python-for-android
Version: 2023.9.16
Release: alt1

Summary: Turn your Python application into an Android APK

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/python-for-android

BuildArch: noarch

Source: %name-%version.tar
Patch: drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sh
BuildRequires: python3-module-colorama
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-toml
BuildRequires: python3-module-build
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-pip
BuildRequires: unzip
BuildRequires: /proc
BuildRequires: /dev/pts
%endif

%add_python3_req_skip android._android android._android_sound android.config

%description
python-for-android is an open source build tool to let you package Python code
into standalone android APKs.

%prep
%setup
%patch -p2

subst "s|python|python3|" pythonforandroid/tools/*
rm -v pythonforandroid/tools/liblink

sed -i 's/from backports import tempfile/import tempfile/' tests/test_recipe.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -v -k "\
not test_get_dep_names_of_package \
and not test_get_package_dependencies \
and not test_venv \
and not test_get_package_as_folder \
and not test_extract_metainfo_files_from_package \
and not test__extract_info_from_package \
and not test_get_package_name"

%files
%doc README.md
%_bindir/p4a
%_bindir/python-for-android
%python3_sitelibdir/pythonforandroid/
%python3_sitelibdir/python_for_android-%version.dist-info
%python3_sitelibdir/ci/

%changelog
* Sat Oct 14 2023 Anton Vyatkin <toni@altlinux.org> 2023.9.16-alt1
- new version 2023.9.16

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 2020.6.2-alt3
- Fixed FTBFS (setuptools 66).

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 2020.6.2-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 2020.6.2-alt1
- new version (2020.6.2) with rpmgs script
