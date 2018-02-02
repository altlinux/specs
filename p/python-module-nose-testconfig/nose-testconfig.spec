%define _unpackaged_files_terminate_build 1
%define oname nose-testconfig

%def_with python3

Name: python-module-%oname
Version: 0.10
Release: alt1.1
Summary: Test Configuration plugin for nosetests
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/nose-testconfig/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/singingwolfboy/nose-testconfig.git
Source0: https://pypi.python.org/packages/a0/1a/9bb934f1274715083cfe8139d7af6fa78ca5437707781a1dcc39a21697b4/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-nose python-module-yaml
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-nose python3-module-yaml
%endif

%py_provides testconfig

%description
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration
data to the tests being executed.

%package -n python3-module-%oname
Summary: Test Configuration plugin for nosetests
Group: Development/Python3
%py3_provides testconfig

%description -n python3-module-%oname
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration
data to the tests being executed.

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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc ACKS TODO docs/* examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ACKS TODO docs/* examples
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.git20130419.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130419
- Initial build for Sisyphus

