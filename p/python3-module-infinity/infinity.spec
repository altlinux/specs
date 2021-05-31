%define _unpackaged_files_terminate_build 1
%define oname infinity

Name: python3-module-%oname
Version: 1.4
Release: alt4
Summary: All-in-one infinity value for Python. Can be compared to any object
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/infinity/

# https://github.com/kvesteri/infinity.git
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-Pygments python3-module-six
BuildPreReq: python3-module-pytest

%description
All-in-one infinity value for Python. Can be compared to any object.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
py.test3

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1.4-alt4
- Drop python2 support.

* Mon Jun 10 2019 Stanislav Levin <slev@altlinux.org> 1.4-alt3
- Added missing dep on Pytest.

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

