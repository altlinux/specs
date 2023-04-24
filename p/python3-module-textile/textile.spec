%define modulename textile

%def_with check

Name: python3-module-%modulename
Version: 4.0.2
Release: alt1

Summary: This is Textile. A Humane Web Text Generator

Group: Development/Python3
License: BSD-3-Clause
URL: https://pypi.org/project/textile/
VCS: https://github.com/textile/python-textile

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-html5lib
%endif

%description
Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc *.txt *.textile
%_bindir/pytextile
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo %modulename}


%changelog
* Mon Apr 24 2023 Anton Vyatkin <toni@altlinux.org> 4.0.2-alt1
- New version 4.0.2.

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.8-alt2
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.8-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.8-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.8-alt1
- Version 2.1.8
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.4-alt1.1
- Rebuild with Python-2.7

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Version 2.1.4

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.10-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0.10-alt1.1
- Rebuilt with python-2.5.

* Thu Apr 28 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.10-alt1
- Initial build for ALT Linux
