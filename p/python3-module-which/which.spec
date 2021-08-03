%define oname which

Name: python3-module-%oname
Version: 1.1.0
Release: alt2
Summary: A portable GNU which replacement implemented in Python
License: MIT
Group: Development/Python3
Url: http://code.google.com/p/which/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%description
which.py is a small GNU-which replacement. It has the following
features:

* it is portable (Windows, Linux, Mac OS X, Un*x);
* it understands PATHEXT and "App Paths" registration on Windows (i.e.
  it will find everything that start does from the command shell);
* it can print all matches on the PATH;
* it can note "near misses" on the PATH (e.g. files that match but may
  not, say, have execute permissions); and
* it can be used as a Python module.

%prep
%setup

%build
find -type f -name '*.py' -exec 2to3 -w '{}' +
sed -i 's|#!/usr/bin/env python|#!/usr/bin/python3|' which.py
%python3_build

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*

%changelog
* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

