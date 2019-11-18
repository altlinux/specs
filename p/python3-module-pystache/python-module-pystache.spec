%define sname pystache

Name: python3-module-%sname
Version: 0.5.4
Release: alt3

Summary: Mustache in Python 
License: BSD
Group: Development/Python3
URL: https://github.com/defunkt/pystache
BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

%package tests
Summary: Tests for %sname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.
Pystache is a Python implementation of Mustache.

This package contains tests for %sname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

rm -rf tests

%build
%python3_build

%install
%python3_install

%files
%doc LICENSE *.md
%_bindir/%sname
%python3_sitelibdir/%sname
%python3_sitelibdir/%sname-%version-py*.egg-info
%exclude %python3_sitelibdir/%sname/*/test.py
%exclude %python3_sitelibdir/%sname/*/*/test.*
%exclude %python3_sitelibdir/%sname/tests

%files tests
%_bindir/%sname-test
%python3_sitelibdir/%sname/*/test.py
%python3_sitelibdir/%sname/*/*/test.*
%python3_sitelibdir/%sname/tests


%changelog
* Mon Nov 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.4-alt3
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.4-alt1.git20121103.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.4-alt1.git20121103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.4-alt1.git20121103.1
- NMU: Use buildreq for BR.

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.4-alt1.git20121103
- Version 0.5.4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.3.1-alt1
- initial build



