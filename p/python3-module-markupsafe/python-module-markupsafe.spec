%define oname markupsafe

Name: python3-module-%oname
Version: 2.1.2
Release: alt1
Epoch: 1
Summary: Implements a XML/HTML/XHTML Markup safe string for Python

Group: Development/Python3
License: BSD-3-Clause
Url: http://pypi.python.org/pypi/MarkupSafe

Source: %oname-%version.tar
Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.

%package tests
Summary: Tests for MarkupSafe
Group: Development/Python3
Requires: %name = %version-%release

%description tests
%summary

This package contains tests for MarkupSafe.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Wed Jan 18 2023 Andrey Cherepanov <cas@altlinux.org> 1:2.1.2-alt1
- New version.

* Thu Mar 17 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.1.1-alt1
- New version.

* Fri Feb 18 2022 Andrey Cherepanov <cas@altlinux.org> 1:2.1.0-alt1
- New version.

* Tue May 25 2021 Andrey Cherepanov <cas@altlinux.org> 1:2.0.1-alt2
- Return new version due sphinx fix.

* Mon May 24 2021 Andrey Cherepanov <cas@altlinux.org> 1:1.1.1-alt2
- Build old version.

* Thu May 20 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt1
- New version.
- Build only for Python3.

* Wed May 12 2021 Andrey Cherepanov <cas@altlinux.org> 2.0.0-alt1
- New version.

* Tue Mar 24 2020 Andrey Cherepanov <cas@altlinux.org> 1.1.1-alt1
- New version.
- Fix License tag according upstream and SPDX.
- Build from upstream tag.
- Do not package tests.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.23-alt1.2.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23-alt1.2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.23-alt1.2
- rebuild with rpm-build-python3-0.1.9
  (to conform to the new Python3 deps and location "policy")

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.23-alt1.1
- NMU: Use buildreq for BR.

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1
- Version 0.23

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.15-alt1.1
- Rebuild with Python-3.3

* Mon May 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.15-alt1
- Version 0.15
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12-alt1.1
- Rebuild with Python-2.7

* Tue Mar 01 2011 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- New version 0.12

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Tue Aug 17 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.3-alt1
- New version 0.9.3

* Tue Jul 27 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9.2-alt1
- initial build

