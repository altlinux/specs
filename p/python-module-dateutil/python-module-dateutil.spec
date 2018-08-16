%define _unpackaged_files_terminate_build 1

%def_with python3
%def_with check

%define oname dateutil

Name: python-module-%oname
Version: 2.7.3
Release: alt1
Summary: Extensions to the standard datetime module
License: PSF
Group: Development/Python
Url: https://pypi.python.org/pypi/python-dateutil/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

%add_python_req_skip _winreg winreg

# https://github.com/dateutil/dateutil.git
Source: %name-%version.tar

Patch1: %oname-%version-alt-tests.patch

BuildRequires: python-devel python-modules-encodings
BuildRequires: python-module-setuptools python-module-six
BuildRequires: pytz-zoneinfo
BuildRequires: python2.7(setuptools_scm)
%if_with check
BuildRequires: python2.7(pytest) python2.7(hypothesis) python2.7(freezegun)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(setuptools_scm)
%if_with check
BuildRequires: python3(pytest) python3(hypothesis) python3(freezegun)
%endif
%endif

Requires: pytz-zoneinfo

%description
The dateutil module provides powerful extensions to the standard
datetime module, available in Python 2.3+. Allows:
- computing of relative deltas (next month, next year, next monday,
  last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a
  superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.

%if_with python3
%package -n python3-module-%oname
Summary: Extensions to the standard datetime module
Group: Development/Python3
Requires: pytz-zoneinfo
%add_python3_req_skip _winreg winreg

%description -n python3-module-%oname
The dateutil module provides powerful extensions to the standard
datetime module, available in Python 2.3+. Allows:
- computing of relative deltas (next month, next year, next monday,
  last week of month, etc),
- computing of dates based on very flexible recurrence rules, using a
  superset of the [WWW] iCalendar specification,
- parsing of RFC strings,
- peneric parsing of dates in almost any string format.
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
export SETUPTOOLS_SCM_PRETEND_VERSION=%version

py.test

%if_with python3
pushd ../python3
py.test3
popd
%endif

%files
%doc LICENSE NEWS README*
%python_sitelibdir/*egg-info/
%python_sitelibdir/dateutil

%files -n python3-module-%oname
%doc LICENSE NEWS README*
%python3_sitelibdir/*egg-info/
%python3_sitelibdir/dateutil

%changelog
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

