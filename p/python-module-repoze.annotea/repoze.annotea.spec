%define oname repoze.annotea

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt3
Summary: Implement W3C Annotea server in repoze
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.annotea/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg rdflib repoze.bfg.restrequest repoze.catalog
%py_requires repoze.errorlog repoze.folder repoze.retry repoze.tm2
%py_requires repoze.zodbconn

%description
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

%package -n python3-module-%oname
Summary: Implement W3C Annotea server in repoze
Group: Development/Python3
%py3_requires repoze.bfg rdflib repoze.bfg.restrequest repoze.catalog
%py3_requires repoze.errorlog repoze.folder repoze.retry repoze.tm2
%py3_requires repoze.zodbconn

%description -n python3-module-%oname
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.annotea
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

This package contains tests for repoze.annotea.

%package tests
Summary: Tests for repoze.annotea
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.annotea implements the server side of the W3C Annotea
specification for RDF-based annotations on content, using repoze.bfg as
the underlying framework for the application.

This package contains tests for repoze.annotea.

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
%doc *.txt docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

