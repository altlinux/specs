%define _unpackaged_files_terminate_build 1
%define oname ipaddress

%def_with python3

Name: python-module-%oname
Version: 1.0.18
Release: alt1.1
Summary: IPv4/IPv6 manipulation library
License: Python
Group: Development/Python
Url: https://pypi.python.org/pypi/ipaddress/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/phihag/ipaddress.git
Source0: https://pypi.python.org/packages/4e/13/774faf38b445d0b3a844b65747175b2e0500164b7c28d78e34987a5bfe06/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
Port of the 3.3+ ipaddress module to 2.6 and 2.7.

%package -n python3-module-%oname
Summary: IPv4/IPv6 manipulation library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Port of the 3.3+ ipaddress module to 2.6 and 2.7.

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
python test_ipaddress.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 test_ipaddress.py
popd
%endif

%files
%doc README*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.18-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.18-alt1
- automated PyPI update

* Fri May 6 2016 Vladimir Didenko <cow@altlinux.org> 1.0.16-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.6-alt1.git20140914.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1.git20140914
- Initial build for Sisyphus
