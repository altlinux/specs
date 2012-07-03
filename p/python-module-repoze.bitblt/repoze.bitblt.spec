%define oname repoze.bitblt
Name: python-module-%oname
Version: 0.8
Release: alt1.git20110324.1.1
Summary: Image transforming WSGI middleware
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.bitblt
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.bitblt.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze PIL webob

%description
This package provides a WSGI middleware component which automatically
scales images according to the ``width`` and ``height`` property in
the <img> tag.

%package tests
Summary: Tests for repoze.bitblt
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a WSGI middleware component which automatically
scales images according to the ``width`` and ``height`` property in
the <img> tag.

This package contains tests for repoze.bitblt.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.git20110324.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20110324.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20110324
- Initial build for Sisyphus

