%define oname repoze.monty

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3.1
Summary: A form field marshaller for WSGI (stolen from Zope)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.monty/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze

%description
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

%package -n python3-module-%oname
Summary: A form field marshaller for WSGI (stolen from Zope)
Group: Development/Python3
%py3_requires repoze

%description -n python3-module-%oname
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.monty
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

This package contains tests for repoze.monty.

%package tests
Summary: Tests for repoze.monty
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.monty is a library that, given a WSGI environment dictionary (and
a wsgi.input file pointer if the request is a POST request), will return
a dictionary back containing "converted" form/query string elements. The
form and query string elements contained in the request are converted
into simple Python types when the form element names are decorated with
special suffixes.

This package contains tests for repoze.monty.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

