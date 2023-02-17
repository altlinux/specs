%define oname python-for-android

Name: python3-module-python-for-android
Version: 2020.6.2
Release: alt3

Summary: Turn your Python application into an Android APK

Group: Development/Python3
License: MIT
Url: https://github.com/kivy/python-for-android/

BuildArch: noarch

# Source-url: %__pypi_url %oname
Source: %name-%version.tar
Patch0: pencil2-setup.py-Fix-dependency-syntax-2354.patch

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

%add_python3_req_skip android._android android._android_sound android.config

%description
python-for-android is an open source build tool to let you package Python code into standalone android APKs.

%prep
%setup
%autopatch -p1
subst "s|python|python3|" pythonforandroid/tools/*
rm -v pythonforandroid/tools/liblink

%build
%python3_build

%install
%python3_install
%python3_prune


%files
%doc README.md
%_bindir/p4a
%_bindir/python-for-android
%python3_sitelibdir/pythonforandroid/
%python3_sitelibdir/python_for_android*.egg-info/
%python3_sitelibdir/ci/

%changelog
* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 2020.6.2-alt3
- Fixed FTBFS (setuptools 66).

* Fri Apr 23 2021 Vitaly Lipatov <lav@altlinux.ru> 2020.6.2-alt2
- initial build for ALT Sisyphus

* Tue Apr 20 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 2020.6.2-alt1
- new version (2020.6.2) with rpmgs script
