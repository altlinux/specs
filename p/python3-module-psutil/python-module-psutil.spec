%define oname psutil

# can't check not on a real system
%def_disable check

Name: python3-module-%oname
Version: 5.9.4
Release: alt1

Summary: A process utilities module for Python

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/psutil/

# Source-url: %__pypi_url %oname
Source: %oname-%version.tar

%add_python3_req_skip _psutil_bsd _psutil_mswindows _psutil_osx pywintypes win32com
%add_python3_req_skip _psutil_sunos _psutil_windows

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_enabled check
BuildRequires: python3-module-pytest
BuildRequires: /proc /sys
%endif

%description
psutil is a module providing an interface for retrieving information on running
processes and system utilization (CPU, memory) in a portable way by using
Python, implementing many functionalities offered by tools like ps, top and
Windows task manager.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
%python3_prune

%check
%if_enabled check
python3 setup.py build_ext -i
export PYTHONPATH=$PWD
py.test-3 -vv
%endif

%files
%doc CREDITS *.rst LICENSE docs/*.rst
%python3_sitelibdir/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 5.9.4-alt1
- new version 5.9.4 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 5.9.1-alt1
- new version 5.9.1 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 5.9.0-alt1
- new version 5.9.0 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 5.8.0-alt1
- new version 5.8.0 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.3-alt1
- new version 5.7.3 (with rpmrb script)

* Sun Nov 08 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt2
- build python3 package separately

* Sun Apr 12 2020 Vitaly Lipatov <lav@altlinux.ru> 5.7.0-alt1
- new version 5.7.0 (with rpmrb script) (ALT bug 38347)
- CVE-2019-18874

* Sun Jul 07 2019 Vitaly Lipatov <lav@altlinux.ru> 5.6.3-alt1
- new version 5.6.3 (with rpmrb script)

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 5.6.1-alt1
- new version 5.6.1 (with rpmrb script)

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 5.5.1-alt1
- new version 5.5.1 (with rpmrb script)

* Sun Nov 04 2018 Vitaly Lipatov <lav@altlinux.ru> 5.4.7-alt1
- new version 5.4.7 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 5.4.3-alt1
- new version 5.4.3 (with rpmrb script)

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.3.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Vitaly Lipatov <lav@altlinux.ru> 5.3.1-alt1
- new version 5.3.1 (with rpmrb script)

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.1.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.1.1-alt1.1
- NMU: Use buildreq for BR.

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Version 3.1.1

* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.3-alt1
- Version 2.1.3
- Added module for Python 3

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Sat Feb 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Version 0.6.1 (ALT #28561)

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Jan 23 2012 Alexey Morsov <swi@altlinux.ru> 0.4.1-alt1
- new version

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- initial build for ALT Linux Sisyphus
