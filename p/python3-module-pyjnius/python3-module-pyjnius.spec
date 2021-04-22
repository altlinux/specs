%define oname pyjnius

Name: python3-module-pyjnius
Version: 1.3.0.0
Release: alt2

Summary: A Python module to access Java classes as Python classes using JNI

Group: Development/Python3
License: MIT License
Url: https://github.com/kivy/pyjnius

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires: /usr/bin/javac
BuildRequires: python3-module-Cython

%description
A Python module to access Java classes as Python classes
using the Java Native Interface (JNI).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%files
%doc README.md
%python3_sitelibdir/jnius/
%python3_sitelibdir/%oname-*.egg-info/
%python3_sitelibdir/jnius_config.py
%python3_sitelibdir/setup_sdist.py
#python3_sitelibdir/__pycache__/

%changelog
* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0.0-alt2
- initial build for ALT Sisyphus

* Mon Apr 19 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 1.3.0.0-alt1
- new version (1.3.0.0) with rpmgs script

