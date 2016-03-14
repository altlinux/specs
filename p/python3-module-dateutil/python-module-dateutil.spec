%define oname dateutil

%def_disable check

Name: python3-module-%oname
Version: 2.4.2
Release: alt1.git20150728.1.1

Summary: Extensions to the standard datetime module (Python 3)

License: PSF
Group: Development/Python3
Url: http://labix.org/python-dateutil

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

%add_python3_req_skip _winreg winreg

# https://github.com/dateutil/dateutil.git
Source: python-dateutil-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools
BuildRequires: python3-module-pytest rpm-build-python3

#BuildRequires: python3-devel python3-module-setuptools-tests
#BuildPreReq: pytz-zoneinfo python3-module-six
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

%check
python3 setup.py test
python3 dateutil/test/test.py

%files
%doc LICENSE NEWS README*
%python3_sitelibdir/*egg-info
%python3_sitelibdir/%oname


%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.2-alt1.git20150728.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.4.2-alt1.git20150728.1
- NMU: Use buildreq for BR.

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.git20150728
- Version 2.4.2

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt2.git20141203
- Don't delete dateutil-zoneinfo.tar.gz

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.git20141203
- Version 2.3

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt4.bzr20131101
- Rebuilt with new pytz

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt3.bzr20131101
- Rebuilt with new pytz

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt2.bzr20131101
- Don't delete zoneinfo

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2-alt1.bzr20131101
- Version 2.2

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 2.0-alt1.1
- Rebuild with Python-3.3

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

