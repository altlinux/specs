%define oname repoze.browserid

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt2.git20121206.1
Summary: Browser id middleware for WSGI
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.browserid
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.browserid.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze paste

%description
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

%package -n python3-module-%oname
Summary: Browser id middleware for WSGI
Group: Development/Python3
%py3_requires repoze paste

%description -n python3-module-%oname
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.browserid
Group: Development/Python3
Requires: python3-module-%oname = %version

%description -n python3-module-%oname-tests
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

This package contains tests for repoze.browserid.

%package tests
Summary: Tests for repoze.browserid
Group: Development/Python
Requires: %name = %version

%description tests
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

This package contains tests for repoze.browserid.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3-alt2.git20121206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2.git20121206
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20121206
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110222
- Initial build for Sisyphus

