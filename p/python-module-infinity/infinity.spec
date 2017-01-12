%define _unpackaged_files_terminate_build 1
%define oname infinity

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1
Summary: All-in-one infinity value for Python. Can be compared to any object
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/infinity/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kvesteri/infinity.git
Source0: https://pypi.python.org/packages/6d/cf/9d301cb8963e5e391da214ee2cedf20cfa7c958e76ea3e577fc77f3eaae0/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Pygments python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Pygments python3-module-six
%endif

%py_provides %oname

%description
All-in-one infinity value for Python. Can be compared to any object.

%package -n python3-module-%oname
Summary: All-in-one infinity value for Python. Can be compared to any object
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
All-in-one infinity value for Python. Can be compared to any object.

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
python setup.py test
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20141021.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141021
- Initial build for Sisyphus

