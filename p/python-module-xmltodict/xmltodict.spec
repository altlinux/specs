%define _unpackaged_files_terminate_build 1
%define oname xmltodict

%def_with python3

Name: python-module-%oname
Version: 0.10.2
Release: alt1
Summary: Makes working with XML feel like you are working with JSON
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/xmltodict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/martinblech/xmltodict.git
Source0: https://pypi.python.org/packages/4a/5e/cd36c16c9eca47162fbbea9aa723b9ab3010f9ae9d4be5c9f6cb2bc147ab/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose python3-module-coverage
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
%setup -q -n %{oname}-%{version}

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
py.test-%_python3_version
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150118
- Version 0.9.1

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.0-alt1.git20140727
- Initial build for Sisyphus

