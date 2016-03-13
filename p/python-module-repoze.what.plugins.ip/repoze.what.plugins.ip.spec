%define oname repoze.what.plugins.ip

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: ip based restrictions for repoze.what
License: Apache 2.0
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.ip/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze.what.plugins repoze.what

%description
Basic IP based restriction predicate, using googles ipaddr library.

%package -n python3-module-%oname
Summary: ip based restrictions for repoze.what
Group: Development/Python3
%py3_requires repoze.what.plugins repoze.what

%description -n python3-module-%oname
Basic IP based restriction predicate, using googles ipaddr library.

%prep
%setup

%if_with python3
cp -fR . ../python3
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
%doc tests
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc tests
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

