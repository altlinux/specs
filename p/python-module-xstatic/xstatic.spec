%define oname xstatic
%define pypi_name XStatic

%def_with python3

Name: python-module-%oname
Version: 1.0.1
Release: alt2.1
Summary: XStatic base package with minimal support code
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
The goal of XStatic family of packages is to provide static file
packages with minimal overhead - without selling you some dependencies
you don't want.

XStatic has some minimal support code for working with the XStatic-*
packages.

%package -n python3-module-%oname
Summary: XStatic base package with minimal support code
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The goal of XStatic family of packages is to provide static file
packages with minimal overhead - without selling you some dependencies
you don't want.

XStatic has some minimal support code for working with the XStatic-*
packages.

%prep
%setup -n %pypi_name-%version

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
install -p -m644 %oname/__init__.py %buildroot%python_sitelibdir/%oname/
cp -fR %oname/pkg %buildroot%python_sitelibdir/%oname/

%if_with python3
pushd ../python3
%python3_install
install -p -m644 %oname/__init__.py %buildroot%python3_sitelibdir/%oname/
cp -fR %oname/pkg %buildroot%python3_sitelibdir/%oname/
popd
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jun 13 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.1-alt2
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

