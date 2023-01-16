%define pypi_name apsw
%define sqlite_ver 3.40.0
%def_enable check

Name: python3-module-%pypi_name
Version: 3.40.1.0
Release: alt1

Summary: Another Python SQLite Wrapper
#doc/_sources/copyright.rst.txt
License: Zlib
Group: Development/Python3
Url: https://pypi.org/project/%pypi_name

Vcs: https://rogerbinns.github.io/apsw.git
Source: https://github.com/rogerbinns/%pypi_name/releases/download/%version/%pypi_name-%version.zip

BuildRequires(pre): rpm-build-python3
BuildRequires: unzip libsqlite3-devel >= %sqlite_ver
BuildRequires: python3-devel

%description
APSW is a Python 3 wrapper for the SQLite embedded relational database
engine. In contrast to other wrappers such as pysqlite it focuses on
being a minimal layer over SQLite attempting just to translate the
complete SQLite API into Python.

%prep
%setup -n %pypi_name-%version
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

%build
%define opts --enable=load_extension
%python3_build %opts

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
gcc %optflags %optflags_shared -shared -o ./testextension.sqlext -I. -Isqlite3 src/testextension.c
%__python3 -m %pypi_name.tests
#tracer:
#%__python3 -m %pypi_name.trace
#speed tester:
#%__python3 -m %pypi_name.speedtest

%files
%python3_sitelibdir/*
%doc doc/*

%changelog
* Mon Jan 16 2023 Yuri N. Sedunov <aris@altlinux.org> 3.40.1.0-alt1
- 3.40.1.0

* Mon Nov 28 2022 Yuri N. Sedunov <aris@altlinux.org> 3.40.0.0-alt1
- 3.40.0.0

* Mon Oct 10 2022 Yuri N. Sedunov <aris@altlinux.org> 3.39.4.0-alt1
- 3.39.4.0

* Mon Sep 12 2022 Yuri N. Sedunov <aris@altlinux.org> 3.39.3.0-alt1
- 3.39.3.0

* Mon Aug 01 2022 Yuri N. Sedunov <aris@altlinux.org> 3.39.2.0-alt1
- 3.39.2.0

* Mon Jun 06 2022 Yuri N. Sedunov <aris@altlinux.org> 3.38.5-alt1
- 3.38.5

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Fri Mar 18 2022 Yuri N. Sedunov <aris@altlinux.org> 3.37.0-alt1
- 3.37.0

* Mon Aug 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Thu Jul 22 2021 Yuri N. Sedunov <aris@altlinux.org> 3.35.4-alt3
- python3-only build

* Tue Jul 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.35.4-alt2.r1
- enabled SQLite loadable extensions (ALT # 40472)

* Wed Apr 14 2021 Yuri N. Sedunov <aris@altlinux.org> 3.35.4-alt1.r1
- 3.35.4

* Tue Dec 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1.r1
- 3.34.0
- enabled %%check

* Tue Sep 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.33.0-alt1.r1
- 3.33.0

* Thu Jun 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1.r1
- 3.32.2

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 3.31.1-alt1.r1
- 3.31.1

* Wed Nov 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1.r1
- 3.30.1

* Wed Oct 02 2019 Yuri N. Sedunov <aris@altlinux.org> 3.29.0-alt1.r1
- 3.29.0

* Wed Jun 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1.r1
- 3.28.0

* Thu Mar 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.27.2-alt1.r1
- 3.27.2

* Sat Jan 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1.r1
- 3.26.0

* Mon Nov 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.25.2-alt1.r1
- 3.25.2

* Fri Sep 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1.r1
- 3.24.0

* Tue Apr 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.22.0-alt1.r1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Mar 26 2018 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1.r1
- 3.22.0

* Sat Nov 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.21.0-alt1.r1
- 3.21.0

* Tue Aug 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1.r1
- 3.20.1

* Fri Jul 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.19.3-alt1.r1
- 3.19.3

* Mon May 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1.r1
- 3.18.0

* Mon Apr 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.17.0-alt1.r1
- 3.17.0-r1

* Thu Jan 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1.r1
- 3.16.2

* Sun Jan 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.15.2-alt1.r1
- 3.15.2

* Wed Nov 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.15.0-alt1.r1
- 3.15.0-r1

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.8.3.1-alt1.r1.1.1
 - (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
   (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.8.3.1-alt1.r1.1
- NMU: Use buildreq for BR.

* Wed Jul 09 2014 Alexey Shabalin <shaba@altlinux.ru> 3.8.3.1-alt1.r1
- 3.8.3.1
- add python3 package

* Thu May 23 2013 Alexey Shabalin <shaba@altlinux.ru> 3.7.15.2-alt1.r1
- 3.7.15.2-r1

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt1.r1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.4-alt1.r1.1
- Rebuild with Python-2.7

* Mon Mar 14 2011 Alexey Shabalin <shaba@altlinux.ru> 3.7.4-alt1.r1
- 3.7.4-r1

* Fri Oct 15 2010 Alexey Shabalin <shaba@altlinux.ru> 3.7.2-alt1.r1
- 3.7.2-r1

* Mon Mar 15 2010 Alexey Shabalin <shaba@altlinux.ru> 3.6.22-alt1.r1
- 3.6.22-r1

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.19-alt1.r1.1
- Rebuilt with python 2.6

* Fri Oct 23 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.19-alt1.r1
- 3.6.19

* Thu Aug 27 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.17-alt1.r1
- 3.6.17
- build with system libsqlite

* Thu Jun 04 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.14.2-alt1.r1
- 3.6.14.2
- build statically against libsqlite from sqlite-amalgamation-3.6.14.2

* Sun Apr 19 2009 Alexey Shabalin <shaba@altlinux.ru> 3.6.11-alt1.r1
- 3.6.11
- build statically against libsqlite from sqlite-amalgamation-3.6.13

* Mon Nov 03 2008 Alexey Shabalin <shaba@altlinux.ru> 3.6.3-alt1.r1
- first build for Sisyphus
- thx to aris@ for spec 
- build statically against libsqlite from sqlite-amalgamation-3.6.4

