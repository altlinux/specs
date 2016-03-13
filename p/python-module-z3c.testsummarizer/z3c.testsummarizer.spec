%define oname z3c.testsummarizer

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt3.1
Summary: Checks a pipermail archive for recent messages and creates a summary
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testsummarizer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

%package -n python3-module-%oname
Summary: Checks a pipermail archive for recent messages and creates a summary
Group: Development/Python3

%description -n python3-module-%oname
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

%package -n python3-module-%oname-tests
Summary: Tests for z3c.testsummarizer
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

This package contains tests for z3c.testsummarizer.

%package tests
Summary: Tests for z3c.testsummarizer
Group: Development/Python
Requires: %name = %version-%release

%description tests
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

This package contains tests for z3c.testsummarizer.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec sed -i 's|rfc822|rfc822py3|g' '{}' +
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

