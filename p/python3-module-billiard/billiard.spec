%define oname billiard

Name: python3-module-%oname
Version: 4.1.0
Release: alt1

Summary: billiard is a fork of the Python 2.7 multiprocessing package

License: GPL
Group: Development/Python3
Url: https://github.com/celery/billiard/

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires: python3(pytest) python3(psutil)

%add_findreq_skiplist %python3_sitelibdir/%oname/popen_spawn_win32.py

%description
billiard is a fork of the Python 2.7 multiprocessing package.
The multiprocessing package itself is a renamed and updated version of
R Oudkerk's pyprocessing package. This standalone variant is intended
to be compatible with Python 2.4 and 2.5, and will draw it's
fixes/improvements from python-trunk.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

%check
%python3_check

%files
%doc LICENSE.txt CHANGES.txt README.rst
%python3_sitelibdir/*

%changelog
* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 4.1.0-alt1
- new version 4.1.0 (with rpmrb script)

* Sat Aug 27 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.2-alt1
- new version 4.0.2 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt1
- new version 4.0.0 (with rpmrb script)

* Wed Jun 29 2022 Grigory Ustinov <grenka@altlinux.org> 3.6.4.0-alt3
- Fixed BuildRequires.

* Mon May 30 2022 Grigory Ustinov <grenka@altlinux.org> 3.6.4.0-alt2
- Fixed BuildRequires.

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 3.6.4.0-alt1
- new version 3.6.4.0 (with rpmrb script)

* Sat Sep 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.6.3.0-alt1
- new version 3.6.3.0 (with rpmrb script)

* Sat Sep 19 2020 Vitaly Lipatov <lav@altlinux.ru> 3.6.0-alt2
- separated python3 build from pypi

* Tue Jun 04 2019 Vitaly Lipatov <lav@altlinux.ru> 3.6.0-alt1
- new version (3.6.0) with rpmgs script

* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0.3-alt2
- Updated build dependencies.

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 3.5.0.3-alt1
- Updated to upstream version 3.5.0.3.
- Enabled tests.
- Merged in python3 build from python3-module-billiard.

* Wed May 31 2017 Lenar Shakirov <snejok@altlinux.ru> 3.3.0.23-alt1
- Version 3.3.0.23

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.20-alt1
- Version 3.3.0.20

* Sat Oct 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0.18-alt1
- Version 3.3.0.18 (ALT #30404)

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt2
- test_multiprocessing.py removed because of the wrong python2.7(test)
  dependency.

* Thu Apr 11 2013 Dmitry Derjavin <dd@altlinux.org> 2.7.3.26-alt1
- Initial ALTLinux build.


