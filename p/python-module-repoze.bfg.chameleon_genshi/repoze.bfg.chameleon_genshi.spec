%define oname repoze.bfg.chameleon_genshi
Name: python-module-%oname
Version: 0.3
Release: alt2.1
Summary: chameleon.genshi template bindings for the repoze.bfg web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.chameleon_genshi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.bfg chameleon

%description
Bindings for Chameleon Genshi-style templating support under repoze.bfg.

The API for use of repoze.bfg.chameleon_genshi under BFG is identical to
the one used for chameleon.zpt` templates. Only the templating language
itself (Genshi vs. ZPT) and import locations (r.b.chameleon_genshi vs.
r.b.chameleon_zpt) differ.

%package tests
Summary: Tests for repoze.bfg.chameleon_genshi
Group: Development/Python
Requires: %name = %version-%release

%description tests
Bindings for Chameleon Genshi-style templating support under repoze.bfg.

The API for use of repoze.bfg.chameleon_genshi under BFG is identical to
the one used for chameleon.zpt` templates. Only the templating language
itself (Genshi vs. ZPT) and import locations (r.b.chameleon_genshi vs.
r.b.chameleon_zpt) differ.

This package contains tests for repoze.bfg.chameleon_genshi.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

