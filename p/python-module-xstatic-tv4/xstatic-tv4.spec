%define mname xstatic
%define oname %mname-tv4
%define pypi_name XStatic-tv4

%def_with python3

Name: python-module-%oname
Version: 1.2.7.0
Release: alt2.1
Summary: Tiny Validator for v4 JSON Schema (XStatic packaging standard)
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

%py_provides %mname.pkg.tv4
%py_requires %mname.pkg

%description
Use json-schema draft v4 to validate simple values and complex objects using a rich validation vocabulary.

%package -n python3-module-%oname
Summary: Tiny Validator for v4 JSON Schema (XStatic packaging standard)
Group: Development/Python3
%py3_provides %mname.pkg.tv4
%py3_requires %mname.pkg

%description -n python3-module-%oname
Use json-schema draft v4 to validate simple values and complex objects using a rich validation vocabulary.

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.7.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.7.0-alt2
- build as noarch

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.7.0-alt1
- Initial build for Sisyphus
