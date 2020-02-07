%define _unpackaged_files_terminate_build 1
%define oname ipaddress

Name: python3-module-%oname
Version: 1.0.18
Release: alt2

Summary: IPv4/IPv6 manipulation library
License: Python
Group: Development/Python3
Url: https://pypi.python.org/pypi/ipaddress/
BuildArch: noarch

# https://github.com/phihag/ipaddress.git
Source0: https://pypi.python.org/packages/4e/13/774faf38b445d0b3a844b65747175b2e0500164b7c28d78e34987a5bfe06/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Port of the 3.3+ ipaddress module to 2.6 and 2.7.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
%__python3 test_ipaddress.py

%files
%doc README*
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.18-alt2
- Build for python2 disabled.

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
