%define oname rdflib

Name: python3-module-%oname
Version: 6.2.0
Release: alt1

Summary: RDFLib is a Python library for working with RDF

License: See License
Group: Development/Python3
Url: http://rdflib.net/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

Conflicts: python-module-%oname

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

BuildArch: noarch

BuildRequires: python3-module-setuptools python3-module-distribute


%description
RDFLib is a Python library for working with RDF, a simple yet powerful
language for representing information.  The library contains parsers
and serializers for RDF/XML, N3, NTriples, Turtle, TriX and RDFa. The
library presents a Graph interface which can be backed by any one of
a number of store implementations, including, memory, MySQL, Redland,
SQLite, Sleepycat, ZODB and SQLObject.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%_bindir/*
%python3_sitelibdir/*

%changelog
* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 6.2.0-alt1
- new version 6.2.0 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 6.1.1-alt1
- new version 6.1.1 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 5.0.0-alt1
- new version 5.0.0 (with rpmrb script)

* Sat Jul 10 2021 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt4
- build python3 module separately, build from a tarball

* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.2.2-alt3
- Fixed build requires.

* Thu Apr 25 2019 Vitaly Lipatov <lav@altlinux.ru> 4.2.2-alt2
- drop unneeded python-module-BeautifulSoup req

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1.qa1
- NMU: applied repocop patch

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.2-alt1
- Updated to upstream version 4.2.2.

* Fri Feb 10 2017 Vitaly Lipatov <lav@altlinux.ru> 4.2.1-alt1
- new version 4.2.1 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.2-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.1.2-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.2-alt1
- Version 4.1.2

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 4.0.1-alt1
- new version 4.0.1 (with rpmrb script)

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-3.3

* Tue May 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0
- Added module for Python 3

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt3.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.4.0-alt3.1
- Rebuild with Python-2.7

* Tue Mar 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt3
- Rebuilt for debuginfo

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt2
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 2.4.0-alt1.1
- Rebuilt with python-2.5.

* Tue Sep 18 2007 Vitaly Lipatov <lav@altlinux.ru> 2.4.0-alt1
- initial build for ALT Linux Sisyphus
