%define oname pyjnius

%def_with check

Name: python3-module-pyjnius
Version: 1.6.1
Release: alt1

Summary: A Python module to access Java classes as Python classes using JNI

Group: Development/Python3
License: MIT
Url: https://pypi.org/project/pyjnius
Vcs: https://github.com/kivy/pyjnius

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
BuildRequires: /usr/bin/javac
BuildRequires: ant
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
A Python module to access Java classes as Python classes
using the Java Native Interface (JNI).

%prep
%setup

%build
%pyproject_build
ant jar test-compile
mv build/test-classes tests

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/setup_sdist.py
rm -rf %buildroot%python3_sitelibdir/__pycache__/setup_sdist.*

%check
mv jnius jnius.hide
export CLASSPATH=${PWD}/tests/test-classes:${PWD}/jnius.hide/src
export PYTHONPATH=%buildroot%python3_sitelibdir
%ifnarch x86_64 i586 aarch64
py.test-3 -v -k 'not test_jvm_options'
%else
py.test-3 -v
%endif

%files
%doc README.md
%python3_sitelibdir/jnius/
%python3_sitelibdir/%{pyproject_distinfo %oname}
%python3_sitelibdir/jnius_config.py
%python3_sitelibdir/__pycache__/jnius_config.cpython-311.*

%changelog
* Wed Dec 13 2023 Anton Vyatkin <toni@altlinux.org> 1.6.1-alt1
- new version 1.6.1

* Thu Apr 22 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.0.0-alt2
- initial build for ALT Sisyphus

* Mon Apr 19 2021 Pablo Soldatoff <soldatoff@etersoft.ru> 1.3.0.0-alt1
- new version (1.3.0.0) with rpmgs script

