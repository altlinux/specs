%define oname repoze.urispace

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt3.1
Summary: Library / middleware for URI-based assertions
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.urispace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze paste zope.interface elementtree

%description
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

Once asserted, such metadata can be used to guide the application in
serving the resource, with possible applciations including:

* Setting cache control headers.
* Selecting externally applied themes, e.g. in Deliverance.
* Restricting access, e.g. to emulate Zope's "placeful security."

%package -n python3-module-%oname
Summary: Library / middleware for URI-based assertions
Group: Development/Python3
%py3_requires repoze paste zope.interface elementtree

%description -n python3-module-%oname
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

Once asserted, such metadata can be used to guide the application in
serving the resource, with possible applciations including:

* Setting cache control headers.
* Selecting externally applied themes, e.g. in Deliverance.
* Restricting access, e.g. to emulate Zope's "placeful security."

%package -n python3-module-%oname-tests
Summary: Tests for repoze.urispace
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

This package contains tests for repoze.urispace.

%package tests
Summary: Tests for repoze.urispace
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.urispace implements the URISpace 1.0 spec, as proposed to the W3C
by Akamai. Its aim is to provide an implementation of that language as a
vehicle for asserting declarative metadata about a resource based on
pattern matching against its URI.

This package contains tests for repoze.urispace.

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
%doc *.txt docs/*.rst docs/examples
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
%doc *.txt docs/*.rst docs/examples
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

