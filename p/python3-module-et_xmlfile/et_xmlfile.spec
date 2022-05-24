%define _unpackaged_files_terminate_build 1
%define oname et_xmlfile

Name: python3-module-%oname
Version: 1.1.0
Release: alt1

Summary: An implementation of lxml.xmlfile for the standard library

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/et_xmlfile

Source0: %{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml

%py3_provides %oname

%description
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires lxml

%description tests
et_xmlfile is a low memory library for creating large XML files.

It is based upon the xmlfile module from lxml with the aim of allowing
code to be developed that will work with both libraries. It was
developed initially for the openpyxl project but is now a standalone
module.

This package contains tests for %oname.

%prep
%setup -n %{oname}-%{version}

%build
export LC_ALL=en_US.UTF-8
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Mon May 23 2022 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Thu Jul 15 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt3
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

