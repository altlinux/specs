%define sname couchdb

%def_disable check

Name: python3-module-%sname
Version: 1.2
Release: alt1

Summary: Python library for working with CouchDB. 
License: BSD
Group: Development/Python3
URL: http://code.google.com/p/couchdb-python/
BuildArch: noarch

# https://github.com/djc/couchdb-python.git
Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest python3-module-sphinx
BuildRequires: python-tools-2to3


%description
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

%package tests
Summary: Tests for %sname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A Python library for CouchDB. It provides a convenient high level
interface for the CouchDB server.

This package contains tests for %sname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|sphinx-build|sphinx-build-3|' doc/Makefile

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build

%install
%python3_install

%make -C doc html

%check
%__python3 setup.py test

%files
%doc *.rst doc/build/html
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Dec 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2-alt1
- Version updated to 1.2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0.1-alt1.git20141116.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20141116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.git20141116.1
- NMU: Use buildreq for BR.

* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20141116
- Version 1.0.1
- Extracted tests into separate packages

* Sat Aug 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt2.hg20140707
- Added module for Python 3

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.hg20140707
- New snapshot

* Thu Dec 05 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1
- Version 0.10

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8-alt1.1
- Rebuild with Python-2.7

* Wed Dec 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.8-alt1
- v0.8

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.7-alt1
- v0.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Rebuilt with python 2.6

* Mon Oct 12 2009 Mikhail Pokidko <pma@altlinux.org> 0.6-alt1
- Initial ALT build



