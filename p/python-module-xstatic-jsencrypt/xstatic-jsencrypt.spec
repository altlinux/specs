%define mname xstatic
%define oname %mname-jsencrypt
%define pypi_name XStatic-JSEncrypt

%def_with python3

Name: python-module-%oname
Version: 2.3.1.1
Release: alt1.1
Summary: JSEncrypt (XStatic packaging standard)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-%mname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-%mname
%endif

%py_provides %mname.pkg.jsencrypt
%py_requires %mname.pkg

%description
JSEncrypt JavaScript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by **any** project that needs these
files.

%package -n python3-module-%oname
Summary: JSEncrypt (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.jsencrypt
%py3_requires %mname.pkg

%description -n python3-module-%oname
JSEncrypt JavaScript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by **any** project that needs these
files.

%prep
%setup -n %pypi_name-%version

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
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
%python_sitelibdir/%mname/pkg/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*.pth

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3.1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 2.3.1.1-alt1
- 2.3.1.1
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0.2-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.0.0.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Nov 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0.2-alt1
- Initial build for Sisyphus

