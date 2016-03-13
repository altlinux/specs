%define oname chameleon

%def_with python3

Name: python-module-%oname.genshi
Version: 1.0.b4
Release: alt2.bzr20090728.1
Summary: Genshi template engine based on Chameleon
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:chameleon.genshi
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

%package -n python3-module-%oname.genshi
Summary: Genshi template engine based on Chameleon
Group: Development/Python3

%description -n python3-module-%oname.genshi
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

%package -n python3-module-%oname.genshi-tests
Summary: Tests for Genshi template engine based on Chameleon
Group: Development/Python3
Requires: python3-module-%oname.genshi = %version-%release

%description -n python3-module-%oname.genshi-tests
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

This package contains tests for Genshi template engine based on
Chameleon.

%package tests
Summary: Tests for Genshi template engine based on Chameleon
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a fast Genshi template implementation based on
the Chameleon template compiler. It's largely compatible with
``genshi.template``.

This package contains tests for Genshi template engine based on
Chameleon.

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

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*/tests

%files tests
%python_sitelibdir/%oname/*/tests

%if_with python3
%files -n python3-module-%oname.genshi
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/*/tests

%files -n python3-module-%oname.genshi-tests
%python3_sitelibdir/%oname/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.b4-alt2.bzr20090728.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt2.bzr20090728
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.b4-alt1.bzr20090728.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt1.bzr20090728
- Initial build for Sisyphus

