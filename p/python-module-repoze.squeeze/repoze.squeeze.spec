%define oname repoze.squeeze
Name: python-module-%oname
Version: 0.4.4
Release: alt1.git20090622.1.1
Summary: WSGI middleware component which "squeezes" HTML documents by merging browser resources
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.squeeze
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.squeeze.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze lxml webob

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

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.4-alt1.git20090622.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20090622.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20090622
- Initial build for Sisyphus

