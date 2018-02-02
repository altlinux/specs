%define _unpackaged_files_terminate_build 1
%define oname xmltodict

%def_with python3

Name: python-module-%oname
Version: 0.11.0
Release: alt1.1
Summary: Makes working with XML feel like you are working with JSON
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/xmltodict/

# https://github.com/martinblech/xmltodict.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-nose python-module-coverage
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-nose python3-module-coverage
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%package -n python3-module-%oname
Summary: Makes working with XML feel like you are working with JSON
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
xmltodict is a Python module that makes working with XML feel like you
are working with JSON.

%prep
%setup

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
export PYTHONPATH=$PWD
python setup.py test
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
python3 setup.py test
py.test3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Nov 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.0-alt1
- Updated to upstream version 0.11.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150118
- Version 0.9.1

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20140727
- Initial build for Sisyphus

