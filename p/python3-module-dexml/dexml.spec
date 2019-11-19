%define oname dexml

Name: python3-module-%oname
Version: 0.5.1
Release: alt2

Summary: A dead-simple Object-XML mapper for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dexml/
# https://github.com/rfk/dexml.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
The dexml module takes the obvious mapping between XML tags and Python
objects and lets you capture that as cleanly as possible. Loosely
inspired by Django's ORM, you write simple class definitions to define
the expected structure of your XML document.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*


%changelog
* Tue Nov 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.1-alt1.git20150420.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20150420.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20150420
- New snapshot

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20121026
- Initial build for Sisyphus

