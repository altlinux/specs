%define _unpackaged_files_terminate_build 1

%define oname manuel

%def_with check

Name: python3-module-%oname
Version: 1.12.4
Release: alt1

Summary: Manuel lets you mix and match traditional doctests with custom test syntax
License: Apache-2.0
Group: Development/Python3
Url: http://pypi.python.org/pypi/manuel/

VCS: https://github.com/benji-york/manuel
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-six
BuildRequires: python3-module-zope
BuildRequires: python3-module-zope.testing
%endif

%description
%summary.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
%summary.

This package contains tests for Manuel.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info
%exclude %python3_sitelibdir/%oname/test*

%files tests
%python3_sitelibdir/%oname/test*
%doc *.rst

%changelog
* Mon Feb 20 2023 Anton Vyatkin <toni@altlinux.org> 1.12.4-alt1
- new version 1.12.4

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.10.1-alt2
- Build for python2 disabled.

* Tue Apr 23 2019 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.10.1-alt1
- update to 1.10.1 to fix build

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.8.0-alt1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.2-alt1
- Version 1.7.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.5.0-alt2.1
- Rebuild with Python-3.3

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5.0-alt1.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus

