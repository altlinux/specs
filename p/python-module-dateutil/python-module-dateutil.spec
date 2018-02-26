Name: python-module-dateutil
Version: 1.5
Release: alt1.1

Summary: Extensions to the standard datetime module

License: PSF
Group: Development/Python
Url: http://labix.org/python-dateutil

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module dateutil
%add_python_req_skip _winreg

Source: http://labix.org/download/python-dateutil/python-dateutil-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-modules-encodings python-module-setuptools
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
%setup -n python-dateutil-%version

%build
%python_build

%install
%python_install
#NOTE: Not sure, but seems zoneinfo is needed under windows only
rm -rf %buildroot%python_sitelibdir/dateutil/zoneinfo

%files
%doc LICENSE NEWS README
%dir %python_sitelibdir/dateutil/
%python_sitelibdir/*egg-info/
%python_sitelibdir/dateutil/*.py*
#%%dir %python_sitelibdir/dateutil/zoneinfo
#%%{py_sitescriptdir}/dateutil/zoneinfo/*.py[co]


%changelog
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

