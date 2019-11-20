%define oname odict

Name: python3-module-%oname
Version: 1.6.0
Release: alt2

Summary: Ordered dictionary
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/odict/
# https://github.com/bluedynamics/odict.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires: python3-module-interlude python3-module-pytest
BuildRequires: python-tools-2to3


%description
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Dictionary in which the insertion order of items is preserved (using an
internal double linked list). In this implementation replacing an
existing item keeps it at its original position.

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
%__python3 setup.py test
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Wed Nov 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.6.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.6.0-alt1.dev0.git20150103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.6.0-alt1.dev0.git20150103.1
- NMU: Use buildreq for BR.

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.0-alt1.dev0.git20150103
- Version 1.6.0.dev0
- Added module for Python 3

* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20140501
- Initial build for Sisyphus

