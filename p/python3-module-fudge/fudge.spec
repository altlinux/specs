%define oname fudge
Name: python3-module-%oname
Version: 1.0.3
Release: alt1.1
Summary: Replace real objects with fakes (mocks, stubs, etc) while testing
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/fudge-je/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python-tools-2to3

%py3_provides %oname

%description
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Fudge is a Python module for using fake objects (mocks and stubs) to
test real ones.

In readable Python code, you declare what methods are available on your
fake and how they should be called. Then you inject that into your
application and start testing. This declarative approach means you don't
have to record and playback actions and you don't have to inspect your
fakes after running code. If the fake object was used incorrectly then
you'll see an informative exception message with a traceback that points
to the culprit.

This package contains tests for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.txt javascript
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus

