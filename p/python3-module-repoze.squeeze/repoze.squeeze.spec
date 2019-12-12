%define oname repoze.squeeze

Name: python3-module-%oname
Version: 0.4.4
Release: alt3

Summary: WSGI middleware component which "squeezes" HTML documents by merging browser resources
License: BSD
Group: Development/Python3
Url: https://github.com/repoze/repoze.squeeze

# https://github.com/repoze/repoze.squeeze.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%py3_requires repoze lxml webob repoze.xmliter


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
Group: Development/Python3
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

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.4-alt3
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.4.4-alt2.git20090622.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.4-alt2.git20090622.1.1
- (AUTO) subst_x86_64.

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

