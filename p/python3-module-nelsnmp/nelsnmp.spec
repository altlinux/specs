%define _unpackaged_files_terminate_build 1
%define oname nelsnmp

Name: python3-module-%oname
Version: 0.2.5
Release: alt2

Summary: A wrapper module for pysnmp
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nelsnmp/
BuildArch: noarch

# https://github.com/networklore/nelsnmp.git
Source0: https://pypi.python.org/packages/f9/3a/1e72673d73d7f89cd6948c47e1234a5fcfb7be5134ddd2fa7460a2212a66/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pysnmp4
BuildRequires: python-tools-2to3

%py3_provides %oname
Requires: python3-module-pysnmp4


%description
A wrapper module for pysnmp.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README.rst HISTORY.rst PKG-INFO
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.5-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.5-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.5-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.git20150315.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Mar 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20150315
- Initial build for Sisyphus

