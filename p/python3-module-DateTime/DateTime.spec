%define _unpackaged_files_terminate_build 1

%define oname DateTime

%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 5.1
Release: alt1

Summary: This package provides a DateTime data type, as known from Zope
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/DateTime/
VCS: https://github.com/zopefoundation/DateTime.git

Source0: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-zope.interface
BuildRequires: python3-module-pytz
%endif

%description
This package provides a DateTime data type, as known from Zope. Unless you need
to communicate with Zope APIs, you're probably better off using Python's
built-in datetime module.

%package tests
Summary: Tests for DateTime
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package provides a DateTime data type, as known from Zope. Unless you need
to communicate with Zope APIs, you're probably better off using Python's
built-in datetime module.

This package contains tests for DateTime.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3

%files
%doc *.txt *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/%oname/tests

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Wed Mar 22 2023 Anton Vyatkin <toni@altlinux.org> 1:5.1-alt1
- New version 5.1.

* Tue Mar 14 2023 Anton Vyatkin <toni@altlinux.org> 1:5.0-alt1
- New version 5.0.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1:4.1.1-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.1.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.0.2-alt1.dev.git20150614.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:4.0.2-alt1.dev.git20150614.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.2-alt1.dev.git20150614
- New snapshot

* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.2-alt1.dev.git20140324
- Version 4.0.2dev

* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.1-alt1
- Version 4.0.1

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0-alt1
- Version 4.0

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:3.0.3-alt1.1
- Rebuild with Python-3.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.3-alt1
- Version 3.0.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt2
- Added module for Python 3

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0rel-alt1
- Version 3.0 (release)

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b3-alt1
- Version 3.0b3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0b1-alt1.1
- Rebuild with Python-2.7

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0b1-alt1
- Initial build for Sisyphus

