%define _unpackaged_files_terminate_build 1
%define oname nosexcover

Name: python3-module-%oname
Version: 1.0.11
Release: alt2
Summary: Extends nose.plugins.cover to add Cobertura-style XML reports
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/nosexcover/

# https://github.com/cmheisel/nose-xcover.git
Source0: https://pypi.python.org/packages/11/b3/2b9e812eb9cb7e60bbfff0a1f581bf411d5b55156e211a4e3580560c8902/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-nose python3-module-coverage

%py3_provides %oname

%description
A companion to the built-in nose.plugins.cover, this plugin will write
out an XML coverage report to a file named coverage.xml.

It will honor all the options you pass to the Nose coverage plugin,
especially --cover-package.

%prep
%setup -n %{oname}-%{version}

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test
nosetests3

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.11-alt2
- Drop python2 support.

* Thu Apr 30 2020 Stanislav Levin <slev@altlinux.org> 1.0.11-alt1.1.1
- Fixed FTBFS.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.11-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.10-alt1.git20140325.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.10-alt1.git20140325
- Initial build for Sisyphus

