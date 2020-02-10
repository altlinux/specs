%define _unpackaged_files_terminate_build 1

%define oname nose-testconfig

Name: python3-module-%oname
Version: 0.10
Release: alt2

Summary: Test Configuration plugin for nosetests
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose-testconfig/
BuildArch: noarch

# https://github.com/singingwolfboy/nose-testconfig.git
Source0: https://pypi.python.org/packages/a0/1a/9bb934f1274715083cfe8139d7af6fa78ca5437707781a1dcc39a21697b4/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-yaml

%py3_provides testconfig


%description
nose-testconfig is a plugin to the nose test framework which provides a
faculty for passing test-specific (or test-run specific) configuration
data to the tests being executed.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3

%files
%doc ACKS TODO docs/* examples
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.10-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.git20130419.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1.git20130419
- Initial build for Sisyphus

