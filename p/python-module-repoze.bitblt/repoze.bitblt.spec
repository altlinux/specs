%define oname repoze.bitblt

%def_with python3

Name: python-module-%oname
Version: 0.9
Release: alt2.git20121130.1
Summary: Image transforming WSGI middleware
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.bitblt
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.bitblt.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze PIL webob

%description
This package provides a WSGI middleware component which automatically
scales images according to the ``width`` and ``height`` property in
the <img> tag.

%package -n python3-module-%oname
Summary: Image transforming WSGI middleware
Group: Development/Python3
%py3_requires repoze PIL webob

%description -n python3-module-%oname
This package provides a WSGI middleware component which automatically
scales images according to the ``width`` and ``height`` property in
the <img> tag.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.bitblt
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package provides a WSGI middleware component which automatically
scales images according to the ``width`` and ``height`` property in
the <img> tag.

This package contains tests for repoze.bitblt.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt2.git20121130.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt2.git20121130
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20121130
- Version 0.9

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.git20110324.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20110324.1
- Added necessary requirements
- Excluded *.pth

* Thu Jun 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20110324
- Initial build for Sisyphus

