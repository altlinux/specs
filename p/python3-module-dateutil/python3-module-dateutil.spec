%define _unpackaged_files_terminate_build 1

%def_without check

%define oname dateutil

Name: python3-module-%oname
Version: 2.8.2
Release: alt1

Summary: Extensions to the standard datetime module

License: PSF
Group: Development/Python
Url: https://pypi.python.org/pypi/python-dateutil/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

%add_python3_req_skip _winreg winreg

# Source-url: %__pypi_url python-dateutil
Source: %name-%version.tar

Patch1: %oname-2.7.3-alt-tests.patch

BuildRequires: tzdata

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(setuptools_scm)
%if_with check
BuildRequires: python3(pytest) python3(hypothesis) python3(freezegun)
BuildRequires: python3-module-pytest-cov
%endif

BuildRequires(pre): rpm-build-intro

Requires: tzdata

%description
The dateutil module provides powerful extensions to the standard
datetime module, available in Python 2.3+. Allows:
- computing of relative deltas (next month, next year, next monday,
  last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a
  superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.

%prep
%setup
%patch1 -p1
# FIXME: Make sure a unicode string can be passed to TZ (GH #802)
%__subst "s|test_gettz_badzone_unicode|disabled_test_gettz_badzone_unicode|" dateutil/test/test_tz.py

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

%if_with check
%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
py.test3
%endif

%files
%doc LICENSE NEWS README*
%python3_sitelibdir/*egg-info/
%python3_sitelibdir/dateutil

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.2-alt1
- new version 2.8.2 (with rpmrb script)

* Tue Apr 06 2021 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt3
- disable check (see https://bugzilla.altlinux.org/show_bug.cgi?id=39164)

* Tue Sep 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt2
- build standalone python3 module

* Sun Mar 22 2020 Vitaly Lipatov <lav@altlinux.ru> 2.8.1-alt1
- new version (2.8.1) with rpmgs script (ALT bug 37303)
- move files against in to subdirectory

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7.3-alt1
- Updated to upstream version 2.7.3.
- Rebuilt module for python-3.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 2.6.0-alt1
- new version 2.6.0 (with rpmrb script)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt2
- Don't delete dateutil-zoneinfo.tar.gz

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1
- Version 2.3

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1
- Version 2.2

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.3
- Rebuilt with new pytz

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.2
- Don't delete zoneinfo

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt1.1
- Rebuild with Python-2.7

* Tue Mar 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1
- Version 1.5

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- new version 1.4.1 (with rpmrb script)

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt0.2.1.1
- Rebuilt with python 2.6

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt0.2.1
- Rebuilt with python-2.5.

* Fri Feb 01 2008 Grigory Batalov <bga@altlinux.ru> 1.1-alt0.2
- Build as noarch.

* Sun Nov 12 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt0.1
- initial build for ALT Linux Sisyphus
- spec from PLD (thanks!)

