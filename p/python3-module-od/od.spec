%define oname od

Name: python3-module-%oname
Version: 1.0
Release: alt1

Summary: Shorthand syntax for building OrderedDicts

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/od/

# Source-url: https://pypi.io/packages/source/o/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools


%description
Shorthand syntax for building OrderedDicts.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
rm -f %buildroot%python3_sitelibdir/test_od.py

# TODO: add repeated_test module
#check
#python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- initial build for ALT Sisyphus
