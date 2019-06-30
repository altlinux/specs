%define modulename progressbar

%def_with python3

Name: python-module-progressbar
Version: 2.5
Release: alt1

Summary: Text progressbar library for python

Group: Development/Python
License: LGPLv2+
Url: https://github.com/niltonvolpato/python-progressbar

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

# Source-url: https://pypi.io/packages/source/p/%modulename/%modulename-%version.tar.gz
Source: %name-%version.tar

%setup_python_module %modulename

BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python-tools-2to3
%endif

%description
This library provides a text mode progress bar. This is typically used to
display the progress of a long running operation, providing a visual clue that
processing is under way.

The progressbar module is very easy to use, yet very powerful. And
automatically supports features like auto-resizing when available.

%package -n python3-module-progressbar
Summary: Text progressbar library for python
Group: Development/Python3
%py3_provides progressbar

%description -n python3-module-progressbar
This library provides a text mode progress bar. This is typically used to
display the progress of a long running operation, providing a visual clue that
processing is under way.

The progressbar module is very easy to use, yet very powerful. And
automatically supports features like auto-resizing when available.

%prep
%setup

%if_with python3
cp -fR . ../python3
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc README.txt LICENSE.txt examples.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-progressbar
%doc README.txt LICENSE.txt examples.py
%python3_sitelibdir/*
%endif

%changelog
* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version 2.5 (with rpmrb script)

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.4-alt1.dev.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4-alt1.dev.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.dev
- Version 2.4dev
- Added module for Python 3

* Fri Dec 28 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.3-alt1
- New version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2-alt1.1
- Rebuild with Python-2.7

* Thu Mar 11 2010 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Linux Sisyphus
