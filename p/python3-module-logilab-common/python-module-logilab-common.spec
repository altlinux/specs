%define _unpackaged_files_terminate_build 1
%define oname logilab-common

%def_with check

Name: python3-module-%oname
Version: 1.9.8
Release: alt1

Summary: Useful miscellaneous modules used by Logilab projects
License: LGPLv2.1+
Group: Development/Python3
Url: https://pypi.org/project/logilab-common

BuildArch: noarch

Source: %oname-%version.tar
Patch0: alt-urllib2-fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-mypy_extensions
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-typing_extensions
BuildRequires: python3-module-pytz
%endif

%py3_provides logilab

%description
logilab-common is a collection of low-level Python packages and modules,
designed to ease:
  * handling command line options and configuration files
  * writing interactive command line tools
  * manipulation files and character strings
  * interfacing to OmniORB (removed by packager)
  * generating of SQL queries
  * running unit tests
  * manipulating tree structures
  * accessing RDBMS (currently postgreSQL, mysql and sqlite)
  * generating text and HTML reports
  * logging

%prep
%setup -q -n %oname-%version
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject -- -k 'not test_deprecation'

%files
%doc ChangeLog README.rst COPYING
%_bindir/*
%python3_sitelibdir/logilab
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/*-nspkg.pth

%changelog
* Wed Mar 08 2023 Anton Vyatkin <toni@altlinux.org> 1.9.8-alt1
- new version 1.9.8

* Wed Apr 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5.2-alt1
- Version updated to 1.5.2
- build for python2 disabled.

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt3
- Rebuilt with python-3.6.

* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt2
- Rebuilt with updated setuptools.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.1-alt1
- Updated to upstream version 1.4.1.

* Thu Jan 26 2017 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt2.hg20150708
- Rename /usr/bin/pytest{,3} to avoid collision with pytest{,3}-3.0.5
  (ALT#33028).
- Package *.pth files for modifying the Python path for the
  namespace pkg.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.2-alt1.hg20150708.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.2-alt1.hg20150708.1
- NMU: Use buildreq for BR.

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.hg20150708
- Version 1.0.2

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.63.2-alt1.hg20141130
- Version 0.63.2

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.63.0-alt1.hg20141105
- Version 0.63.0

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.62.0-alt1.hg20140716
- Version 0.62.0

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 0.61.0-alt1.hg20140211
- Version 0.61.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.59.0-alt2.hg20130215
- Use 'find... -exec...' instead of 'for ... $(find...'

* Thu Feb 28 2013 Aleksey Avdeev <solo@altlinux.ru> 0.59.0-alt1.hg20130215
- Version 0.59.0

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.0-alt2.hg20120417
- Added module for Python 3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.58.0-alt1.hg20120417
- Version 0.58.0

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.57.1-alt1
- Version 0.57.1

* Sun Oct 23 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.52.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.52.0-alt1
- 0.52.0
- skip test_knownValues_is_standard_module_4 test because
  logilab.common.modutils.is_standard_module is fundamentally broken on
  our x86_64 (see #24144)

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.51.1-alt1
- 0.51.1

* Sat Aug 28 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.51.0-alt1
- 0.51.0
- run tests

* Sun Jun 13 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.3-alt1
- 0.50.3

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.1-alt2
- build from hg

* Mon May 03 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.50.1-alt1
- 0.50.1

* Fri Mar 19 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.49.0-alt1
- 0.49.0

* Fri Feb 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.48.0-alt1
- 0.48.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.45.2-alt1
- 0.45.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.45.0-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.45.0-alt1
- 0.45.0

* Thu Aug 20 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.44.0-alt1
- 0.44.0

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.39.0-alt1
- 0.39.0

* Fri Mar 06 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.1-alt1
- 0.38.1

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.0-alt2
- use %%python_{build,install}

* Wed Jan 28 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.38.0-alt1
- 0.38.0

* Sat Dec 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.37.0-alt1
- 0.37.0

* Sat Nov 15 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.36.1-alt1
- 0.36.1

* Sun Nov 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.36.0-alt1
- 0.36.0

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.35.2-alt1
- 0.35.2
- spec cleanup
- package logilab/__init__.py, fixing imports and automatic dependency
  search (closes: #17532)
- don't package tests

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.21.0-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.21.0-alt1
- Initial build for ALT Linux
