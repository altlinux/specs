%define oname logilab-database

Name: python3-module-%oname
Version: 1.17.1
Release: alt1

Summary: Provides some classes to make unified access to different RDBMS possible
License: LGPLv2.1+
Group: Development/Python3
URL: http://www.logilab.org/project/logilab-database

BuildArch: noarch

# hg clone http://hg.logilab.org/logilab/database
Source: database-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-logilab-common

%description
logilab-database provides some classes to make unified access to
different RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database,
  index, users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

%prep
%setup

%build
%python3_build

%install
%python3_install

rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*

%files
%doc ChangeLog README
%python3_sitelibdir/*

%changelog
* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.17.1-alt1
- Version updated to 1.17.1
- build for python2 disabled.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt2
- Rebuilt with updated setuptools.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt1
- Updated to upstream version 1.15.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.13.2-alt1.hg20150318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.13.2-alt1.hg20150318.1
- NMU: Use buildreq for BR.

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.2-alt1.hg20150318
- Version 1.13.2

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.1-alt1.hg20150105
- Version 1.13.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt1.hg20140513
- Version 1.12.2

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1.hg20131009
- Version 1.10.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2.hg20130321
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20130321
- Version 1.9.0

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.2-alt1.hg20120210.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.hg20120210
- Initial build for Sisyphus

