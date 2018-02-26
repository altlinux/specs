%define oname dateutil
Name: python3-module-%oname
Version: 2.0
Release: alt1

Summary: Extensions to the standard datetime module (Python 3)

License: PSF
Group: Development/Python3
Url: http://labix.org/python-dateutil

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%add_python3_req_skip _winreg winreg

Source: http://labix.org/download/python-dateutil/python-dateutil-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
# texlive-base-bin


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
%setup -n python-%oname-%version

%build
%python3_build

%install
%python3_install
#NOTE: Not sure, but seems zoneinfo is needed under windows only
rm -rf %buildroot%python_sitelibdir/%oname/zoneinfo

%files
%doc LICENSE NEWS README
%dir %python3_sitelibdir/%oname/
%python3_sitelibdir/*egg-info/
%python3_sitelibdir/%oname/*.py*
%python3_sitelibdir/%oname/__pycache__
#%%dir %python_sitelibdir/%oname/zoneinfo
#%%{py_sitescriptdir}/%oname/zoneinfo/*.py[co]


%changelog
* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Built for Python 3

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

