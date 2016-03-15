%define oname subunit

%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1.1
Summary: Python implementation of subunit test streaming protocol
License: Apache or BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/python-subunit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-testtools python-module-mimeparse
BuildPreReq: python-module-testscenarios
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-testtools python-tools-2to3
BuildPreReq: python3-module-mimeparse
BuildPreReq: python3-module-testscenarios
%endif

Provides: python-module-python-%oname = %EVR
Obsoletes: python-module-python-%oname < %EVR

%description
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 implementation of subunit test streaming protocol
Group: Development/Python3
Provides: python3-module-python-%oname = %EVR
Obsoletes: python3-module-python-%oname < %EVR
%add_python3_req_skip gtk pynotify

%description -n python3-module-%oname
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

%package -n python3-module-%oname-tests
Summary: Tests for python-subunit (Python 3)
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
Provides: python3-module-python-%oname-tests = %EVR
Obsoletes: python3-module-python-%oname-tests < %EVR

%description -n python3-module-%oname-tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.
%endif

%package tests
Summary: Tests for python-subunit
Group: Development/Python
Requires: %name = %version-%release
Provides: python-module-python-%oname-tests = %EVR
Obsoletes: python-module-python-%oname-tests < %EVR

%description tests
Subunit is a streaming protocol for test results. The protocol is human
readable and easily generated and parsed. By design all the components
of the protocol conceptually fit into the xUnit TestCase->TestResult
interaction.

Subunit comes with command line filters to process a subunit stream and
language bindings for python, C, C++ and shell. Bindings are easy to
write for other languages.

This package contains tests for python-subunit.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i py3_$i
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc NEWS README
%_bindir/*
%exclude %_bindir/py3_*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc NEWS README
%_bindir/py3_*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/__pycache__/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/__pycache__/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Version 1.1.0

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt3
- Added necessary obsoletes

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt2
- Renamed python-module-python-subunit -> python-module-subunit

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.18-alt1
- Version 0.0.18

* Thu Sep 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.15-alt1
- Version 0.0.15

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1
- Version 0.0.10

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.0.7-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.7-alt1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1
- Initial build for Sisyphus

