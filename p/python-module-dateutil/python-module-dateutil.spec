Name: python-module-dateutil
Version: 2.3
Release: alt1

Summary: Extensions to the standard datetime module

License: PSF
Group: Development/Python
Url: https://pypi.python.org/pypi/python-dateutil/2.2

Packager: Vitaly Lipatov <lav@altlinux.ru>

%setup_python_module dateutil
%add_python_req_skip _winreg winreg

Source: python-dateutil-%version.tar

BuildArch: noarch

BuildRequires: python-devel python-modules-encodings
BuildPreReq: python-module-setuptools-tests python-module-six
BuildPreReq: pytz-zoneinfo
# texlive-base-bin

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

%prep
%setup -n python-dateutil-%version

%build
%python_build

%install
%python_install
#NOTE: Not sure, but seems zoneinfo is needed under windows only
rm -f %buildroot%python_sitelibdir/dateutil/zoneinfo/*.tar.gz

ln -s %_datadir/pytz/zoneinfo.tar.gz \
	%buildroot%python_sitelibdir/dateutil/zoneinfo/

%check
python setup.py test

%files
%doc LICENSE NEWS README*
%dir %python_sitelibdir/dateutil/
%python_sitelibdir/*egg-info/
%python_sitelibdir/dateutil
#%%dir %python_sitelibdir/dateutil/zoneinfo
#%%{py_sitescriptdir}/dateutil/zoneinfo/*.py[co]


%changelog
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

