%define _unpackaged_files_terminate_build 1
%define oname ptest

Name: python3-module-%oname
Version: 1.7.4
Release: alt2

Summary: Light testing framework for Python
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/ptest
# https://github.com/KarlGong/ptest.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/60/ba/c8b04e9bb9ca7fe92acf369c2004fa1cf20f3c0c5ece62b8a36abee431e4/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
ptest is a light testing framework for Python. Using decorator to tag
test classes and test cases, executing test cases by command line, and
generating clear report.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.7.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.7.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.git20150813.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150813
- Initial build for Sisyphus

