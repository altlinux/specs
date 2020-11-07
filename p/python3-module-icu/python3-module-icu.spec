%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define modulename icu
%define srcname PyICU
%define icu_ver 6.7.1

Name: python3-module-%modulename
# python3 setup.py -V|tail -1
Version: 2.6
Release: alt1

Summary: Python extension wrapping the ICU C++ API
Group: Development/Python3
License: MIT
Url: https://pyicu.osafoundation.org/

%if_disabled snapshot
Source: https://pypi.python.org/packages/source/P/PyICU/%srcname-%version.tar.gz
%else
Vcs: https://github.com/ovalhub/pyicu.git
Source: %srcname-%version.tar
%endif

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ libicu-devel >= %icu_ver
BuildRequires: python3-devel python3-module-setuptools

%description
PyICU - Python 3 extension wrapping the ICU C++ API.

%prep
%setup -n %srcname-%version

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc CREDITS README* CHANGES samples/


%changelog
* Sat Nov 07 2020 Yuri N. Sedunov <aris@altlinux.org> 2.6-alt1
- 2.6 (Python 3 only)

* Sat May 30 2020 Yuri N. Sedunov <aris@altlinux.org> 2.5.0-alt1
- 2.5.0

* Sat Mar 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.4.3-alt1
- 2.4.3

* Fri Dec 27 2019 Yuri N. Sedunov <aris@altlinux.org> 2.4.2-alt1
- 2.4.2
- made python2 build optional
- fixed License tag

* Sun Oct 13 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt2
- updated to v2.3.1-30-g5fb711a (compatible with icu-65.1)

* Sat May 04 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 2.3-alt1
- 2.3 (compatible with icu-64.1)

* Tue Sep 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt2
- Rebuilt with new icu.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.0.2-alt1
- Updated to upstream version 2.0.2.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.2-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Feb 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.9.2-alt1
- 1.9.2
- switched build from tarballs to upstream git

* Sun Aug 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1
- Version 1.8
- Added module for Python 3

* Mon Dec 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Version 1.4

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt1.1
- Rebuild with Python-2.7

* Thu Sep 15 2011 Kirill Maslinsky <kirill@altlinux.org> 1.2-alt1
- 1.2

* Tue May 31 2011 Kirill Maslinsky <kirill@altlinux.org> 1.1-alt1
- 1.1

* Fri Dec 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.0.1-alt1
- Updated to post-1.0.1 snapshot r166 to fix build with fresh ICU.

* Wed Aug 25 2010 Kirill Maslinsky <kirill@altlinux.org> 1.0-alt1
- Initial build for Sisyphus

