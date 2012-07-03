%define srcname  PyProtocols
%define alphatag a0dev_r2082
%define srcver   1.0%{?alphatag}
%define eggver   1.0a0

Name: python-module-protocols
Version: 1.0
Release: alt0.1.1.2.1.1

Summary: Open Protocols and Component Adaptation for Python

Group: Development/Other
License: PSF or ZPL
Url: http://peak.telecommunity.com/PyProtocols.html

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://files.turbogears.org/eggs/%srcname-%srcver.tar.bz2

# manually removed: pybliographic 
# Automatically added by buildreq on Mon Nov 20 2006
BuildRequires: python-module-Pyrex python-modules-encodings python-module-setuptools

%add_python_req_skip zope
%py_provides protocols

%description
PyProtocols is an implementation of PEP 246 allowing Python programmers to
define Interfaces and adapters between them, thereby reducing or eliminating
fragile 'isinstance' if type() comparisons.

%prep
%setup -n %srcname-%srcver

%build
%python_build_debug

%install
%python_install -O1 --single-version-externally-managed

%files
%doc README.txt CHANGES.txt docs/*
%python_sitelibdir/*

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt0.1.1.2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Oct 21 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt0.1.1.2.1
- Rebuild with Python-2.7

* Mon Mar 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt0.1.1.2
- Rebuilt for debuginfo

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt0.1.1.1
- Rebuilt with python 2.6

* Fri Jan 25 2008 Grigory Batalov <bga@altlinux.ru> 1.0-alt0.1.1
- Rebuilt with python-2.5.

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt0.1
- initial build for ALT Linux Sisyphus

* Sat Sep 16 2006 Shahms E. King <shahms@shahms.com> 1.0-0.3-a0dev_r2082
- Rebuild for FC6

* Fri Aug 11 2006 Shahms E. King <shahms@shahms.com> 1.0-0.2.a0dev_r2082
- Include, don't ghost .pyo files per new guidelines

* Wed Apr 19 2006 Shahms E. King <shahms@shahms.com> 1.0-0.1.a0dev_r2082
- Update to new upstream location and snapshot version

* Mon Feb 13 2006 Shahms E. King <shahms@shahms.com> 0.9.3-7
- Rebuild for FC5

* Tue Jan 31 2006 Shahms E. King <shahms@shahms.com> 0.9.3-6
- BuildRequires setuptools, rather than including it

* Thu May 12 2005 Shahms E. King <shahms@shahms.com> 0.9.3-4
- rebuilt, add dist tag

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Mon Mar 21 2005 Shahms E. King <shahms@shahms.com> - 0.9.3-3
- Replace python_sitelib with python_sitearch
- Other misc. specfile cleanups

* Tue Mar 01 2005 Shahms E. King <shahms@shahms.com> 0.9.3-2
- Clean up spec file

* Tue Aug 31 2004 Shahms E. King <shahms@shahms.com> -
- Update to 0.9.3

* Fri Jul 30 2004 Shahms E. King <shahms@shahms.com> -
- Update to 0.9.3rc2

* Thu May 27 2004 Shahms King <shahms@shahms.com> -
- Initial Release

