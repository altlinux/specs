%define oname urwid

%def_with check

Name: python3-module-urwid
Version: 2.6.14
Release: alt1

Summary: Urwid is a console user interface library for Python.

License: LGPLv2.1
Group: Development/Python3
URL: https://pypi.org/project/urwid
VCS: https://github.com/urwid/urwid

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools-scm
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-typing-extensions
BuildRequires: python3-module-wcwidth
BuildRequires: python3-module-coverage
BuildRequires: python3-modules-curses
%endif

# These requirements are optional
# https://github.com/urwid/urwid/blob/master/urwid/__init__.py#L221
%add_python3_req_skip gi.repository
%add_python3_req_skip tornado
%add_python3_req_skip trio
%add_python3_req_skip twisted.internet.abstract
%add_python3_req_skip twisted.internet.error
%add_python3_req_skip zmq

%py3_provides %oname

BuildArch:     noarch

%description
Urwid is a console user interface library for Python. Urwid is released
under the GNU Lesser General Public License and it includes many features
useful for text console application developers:

 * Fluid interface resizing (xterm window resizing / fbset on Linux console)
 * Web application display mode using Apache and CGI [ Live Demo ]
 * Support for UTF-8, simple 8-bit and CJK encodings
 * Multiple text alignment and wrapping modes built-in
 * Ability create user-defined text layout classes
 * Simple markup for setting text attributes
 * Powerful list box that handles scrolling between different widget types
 * List box contents may be managed with a user-defined class
 * Flexible edit box for editing many different types of text
 * Buttons, check boxes and radio boxes
 * Customizable layout for all widgets
 * Easy interface for creating HTML screen shots

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst examples
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Fri Jun 21 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.14-alt1
- Automatically updated to 2.6.14.
- Made some requirements optional.

* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.12-alt1
- Build new version.
- Build with check.

* Sun Jan 14 2024 Grigory Ustinov <grenka@altlinux.org> 2.3.4-alt1
- Build new version for python3.12.

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- new version 2.1.2 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt2
- build python3 module only

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.1-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.3.1-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.1-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.2.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Aug 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Version 1.2.1
- Added module for Python 3

* Mon Sep 16 2013 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.1.1-alt1
- New version

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.1
- Rebuilt for debuginfo

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.9-alt1
- new version

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt2
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.9.8.4-alt1
- new version

* Thu Dec 13 2007 Alexey Morsov <swi@altlinux.ru> 0.9.8.1-alt1
- initial build

