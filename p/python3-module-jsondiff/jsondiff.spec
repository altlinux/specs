%define oname jsondiff

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Diff JSON and JSON-like structures in Python

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/jsondiff

# Source-url: https://pypi.io/packages/source/j/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-nose-random

%description
Diff JSON and JSON-like structures in Python.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%_bindir/jsondiff
%_bindir/jdiff
%python3_sitelibdir/*

%changelog
* Mon Jan 27 2020 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- initial build for ALT Sisyphus
