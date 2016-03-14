%define oname zope.httpform

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt3.1
Summary: HTTP Form Data Parser
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.httpform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.interface

%description
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

%package -n python3-module-%oname
Summary: HTTP Form Data Parser
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

%package -n python3-module-%oname-tests
Summary: Tests for HTTP Form Data Parser
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

This package contains tests for HTTP Form Data Parser.

%package tests
Summary: Tests for HTTP Form Data Parser
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
zope.httpform is a library that, given a WSGI or CGI environment
dictionary, will return a dictionary back containing converted
form/query string elements. The form and query string elements contained
in the environment are converted into simple Python types when the form
element names are decorated with special suffixes.

This package contains tests for HTTP Form Data Parser.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

