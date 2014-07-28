%define oname repoze.bfg.chameleon_genshi

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt3
Summary: chameleon.genshi template bindings for the repoze.bfg web framework
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.bfg.chameleon_genshi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.bfg chameleon

%description
Bindings for Chameleon Genshi-style templating support under repoze.bfg.

The API for use of repoze.bfg.chameleon_genshi under BFG is identical to
the one used for chameleon.zpt` templates. Only the templating language
itself (Genshi vs. ZPT) and import locations (r.b.chameleon_genshi vs.
r.b.chameleon_zpt) differ.

%package -n python3-module-%oname
Summary: chameleon.genshi template bindings for the repoze.bfg web framework
Group: Development/Python3
%py3_requires repoze.bfg chameleon

%description -n python3-module-%oname
Bindings for Chameleon Genshi-style templating support under repoze.bfg.

The API for use of repoze.bfg.chameleon_genshi under BFG is identical to
the one used for chameleon.zpt` templates. Only the templating language
itself (Genshi vs. ZPT) and import locations (r.b.chameleon_genshi vs.
r.b.chameleon_zpt) differ.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bfg.chameleon_genshi
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Bindings for Chameleon Genshi-style templating support under repoze.bfg.

The API for use of repoze.bfg.chameleon_genshi under BFG is identical to
the one used for chameleon.zpt` templates. Only the templating language
itself (Genshi vs. ZPT) and import locations (r.b.chameleon_genshi vs.
r.b.chameleon_zpt) differ.

This package contains tests for repoze.bfg.chameleon_genshi.

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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

