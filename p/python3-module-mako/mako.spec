%define _unpackaged_files_terminate_build 1
%define modname mako

%def_with check

Name: python3-module-%modname
Version: 1.2.4
Release: alt1

Summary: template library written in Python

Group: Development/Python3
License: MIT
Url: http://www.makotemplates.org

# Source-url: http://pypi.io/packages/source/M/Mako/Mako-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

# Fix #23203
Requires: python3-module-beaker

Conflicts: python-module-mako < %EVR
Obsoletes: python-module-mako < %EVR

BuildRequires(pre): rpm-build-intro >= 2.2.5
BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires:
BuildRequires: python3(markupsafe)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
BuildRequires: python3(tox_no_deps)
%endif

# conditional import, but unconditionally required
%py3_requires markupsafe

%description
Mako is a template library written in Python. It provides a familiar,
non-XML syntax which compiles into Python modules for maximum
performance. Mako's syntax and API borrows from the best ideas of many
others, including Django templates, Cheetah, Myghty, and Genshi.
Conceptually, Mako is an embedded Python (i.e. Python Server Page)
language, which refines the familiar ideas of componentized layout and
inheritance to produce one of the most straightforward and flexible
models available, while also maintaining close ties to Python calling
and scoping semantics.

%prep
%setup

%build
%python3_build

%install
%python3_install
%python3_prune

%check
py.test-3 -v

%files
%doc CHANGES LICENSE README*
%_bindir/mako-render
%python3_sitelibdir/mako/
%python3_sitelibdir/Mako-%{version}*.egg-info

%changelog
* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.4-alt1
- Automatically updated to 1.2.4.

* Sat Sep 24 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.3-alt1
- Automatically updated to 1.2.3.

* Mon Sep 12 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Automatically updated to 1.2.2.

* Thu Jul 28 2022 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Mon Oct 11 2021 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- 1.1.4 -> 1.1.5.

* Thu May 13 2021 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1
- Build new version.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 1.1.3-alt1
- Build new version.

* Thu Nov 05 2020 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- NMU: new version 1.1.2 (with rpmrb script)
- NMU: cleanup spec, drop test files packing

* Tue Sep 01 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.9-alt2
- Transfer on python3.

* Fri Apr 26 2019 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.1-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Version 1.0.0

* Wed Apr 17 2013 Fr. Br. George <george@altlinux.ru> 0.7.3-alt1.1
- Fix build with 2to3

* Wed Feb 20 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.3-alt1
- Version 0.7.3

* Thu May 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.0-alt1.1
- Rebuild with Python-2.7

* Tue Mar 01 2011 Vladimir Lettiev <crux@altlinux.ru> 0.4.0-alt1
- New version 0.4.0

* Sat Nov 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.6-alt1
- New version 0.3.6

* Fri Oct 22 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.5-alt1
- New version 0.3.5

* Tue Jun 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.4-alt1
- New version 0.3.4

* Sat Jun 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.3-alt1
- New version 0.3.3

* Thu Apr 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt2
- added python-module-beaker to requires (Closes: #23203)

* Mon Mar 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1
- New version 0.3.2

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1.1
- Rebuilt with python 2.6

* Sun Oct 18 2009 Vladimir Lettiev <crux@altlinux.ru> 0.2.5-alt1
- initial build

