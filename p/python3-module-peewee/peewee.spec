%define oname peewee

%def_disable check

Name: python3-module-%oname
Version: 3.15.4
Release: alt1

Summary: A small, expressive orm -- supports postgresql, mysql and sqlite

License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/peewee/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

Obsoletes: python-module-peewee
Provides: python-module-peewee

BuildRequires(pre): rpm-macros-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx python3-module-pytest python3-modules-sqlite3

# Keep noarch: Could not find libsqlite3, SQLite extensions will not be built.
#BuildRequires: libsqlite3-devel

%add_python3_req_skip pysqlcipher

%description
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

* A small, expressive ORM
* Written in python with support for versions 2.6+ and 3.2+.
* built-in support for sqlite, mysql and postgresql
* tons of extensions available in the playhouse
  (postgres hstore/json/arrays, sqlite full-text-search, schema
  migrations, and much more).


%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Peewee is a simple and small ORM. It has few (but expressive) concepts,
making it easy to learn and intuitive to use.

This package contains documentation for %oname.

%prep
%setup

find -type f -name '*.py' -exec \
	sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' '{}' +

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install
%python3_prune

%make -C docs html SPHINXBUILD=sphinx-build-3

%check
python3 setup.py test
python3 runtests.py

%files
%doc *.md *.rst examples
%_bindir/pwiz.py
%python3_sitelibdir/*

%files docs
%doc docs/_build/html/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 3.15.4-alt1
- new version 3.15.4 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 3.15.1-alt1
- new version 3.15.1 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 3.14.10-alt1
- new version 3.14.10 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.14.4-alt1
- new version 3.14.4 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.13.3-alt1
- new version 3.13.3 (with rpmrb script)

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 3.13.2-alt2
- build python3 package separately
- cleanup spec, drop tests packing

* Thu Apr 16 2020 Pavel Vasenkov <pav@altlinux.org> 3.13.2-alt1
- Bump to new version 3.13.2

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.6.0-alt2.git20150421.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.6.0-alt2.git20150421.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.6.0-alt2.git20150421.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 2.6.0-alt2.git20150421
- Rebuild with "def_disable check"
- Cleanup buildreq

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.0-alt1.git20150421
- Version 2.6.0

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.7-alt1.git20150212
- Version 2.4.7

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20150108
- New snapshot
- Added module for Python 3

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.5-alt1.git20141231
- Initial build for Sisyphus

