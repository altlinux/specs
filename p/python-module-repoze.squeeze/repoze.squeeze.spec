%define oname repoze.squeeze

%def_with python3

Name: python-module-%oname
Version: 0.4.4
Release: alt2.git20090622.1
Summary: WSGI middleware component which "squeezes" HTML documents by merging browser resources
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.squeeze
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.squeeze.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze lxml webob repoze.xmliter

%description
This package provides a WSGI middleware component which "squeezes"
HTML documents by merging browser resources (javascript
and stylesheets).

It uses statistical analysis to determine the optimal bundles based on
the HTML documents that pass through it. Vary-headers are observed, as
are resource expiration dates.

Documents that are not squeezed are given the 'no-cache' pragma in an
expectation that we will be able to squeeze it after sufficient
burn-in. Squeezed documents are served with expiration dates no later
than the expiration dates of the squeezed resources which it
references.

%package -n python3-module-%oname
Summary: WSGI middleware component which "squeezes" HTML documents by merging browser resources
Group: Development/Python3
%py3_requires repoze lxml webob repoze.xmliter

%description -n python3-module-%oname
This package provides a WSGI middleware component which "squeezes"
HTML documents by merging browser resources (javascript
and stylesheets).

It uses statistical analysis to determine the optimal bundles based on
the HTML documents that pass through it. Vary-headers are observed, as
are resource expiration dates.

Documents that are not squeezed are given the 'no-cache' pragma in an
expectation that we will be able to squeeze it after sufficient
burn-in. Squeezed documents are served with expiration dates no later
than the expiration dates of the squeezed resources which it
references.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.squeeze
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a WSGI middleware component which "squeezes"
HTML documents by merging browser resources (javascript
and stylesheets).

It uses statistical analysis to determine the optimal bundles based on
the HTML documents that pass through it. Vary-headers are observed, as
are resource expiration dates.

Documents that are not squeezed are given the 'no-cache' pragma in an
expectation that we will be able to squeeze it after sufficient
burn-in. Squeezed documents are served with expiration dates no later
than the expiration dates of the squeezed resources which it
references.

This package contains tests for repoze.squeeze.

%package tests
Summary: Tests for repoze.squeeze
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a WSGI middleware component which "squeezes"
HTML documents by merging browser resources (javascript
and stylesheets).

It uses statistical analysis to determine the optimal bundles based on
the HTML documents that pass through it. Vary-headers are observed, as
are resource expiration dates.

Documents that are not squeezed are given the 'no-cache' pragma in an
expectation that we will be able to squeeze it after sufficient
burn-in. Squeezed documents are served with expiration dates no later
than the expiration dates of the squeezed resources which it
references.

This package contains tests for repoze.squeeze.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt2.git20090622.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt2.git20090622
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.4-alt1.git20090622.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20090622.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20090622
- Initial build for Sisyphus

