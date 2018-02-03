%define _unpackaged_files_terminate_build 1
%define oname nelsnmp

%def_with python3

Name: python-module-%oname
Version: 0.2.5
Release: alt1.1
Summary: A wrapper module for pysnmp
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nelsnmp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/networklore/nelsnmp.git
Source0: https://pypi.python.org/packages/f9/3a/1e72673d73d7f89cd6948c47e1234a5fcfb7be5134ddd2fa7460a2212a66/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-pysnmp4
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-pysnmp4
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: python-module-pysnmp4

%description
A wrapper module for pysnmp.

%if_with python3
%package -n python3-module-%oname
Summary: A wrapper module for pysnmp
Group: Development/Python3
%py3_provides %oname
Requires: python3-module-pysnmp4

%description -n python3-module-%oname
A wrapper module for pysnmp.
%endif

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc README.rst HISTORY.rst PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.rst HISTORY.rst PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150315.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150315
- Initial build for Sisyphus

