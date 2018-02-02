%define _unpackaged_files_terminate_build 1
%define oname infinity

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt2.1
Summary: All-in-one infinity value for Python. Can be compared to any object
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/infinity/

# https://github.com/kvesteri/infinity.git
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-Pygments python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-Pygments python3-module-six
%endif

%description
All-in-one infinity value for Python. Can be compared to any object.

%package -n python3-module-%oname
Summary: All-in-one infinity value for Python. Can be compared to any object
Group: Development/Python3

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
py.test3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20141021.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20141021
- Initial build for Sisyphus

