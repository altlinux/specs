%define oname python-ldap

Summary: LDAP client API for Python
Name: python-module-ldap
Version: 2.3.11
Release: alt2.1.1
Source0: %oname-%version.tar
License: Python-style license
Group: Development/Python
Url: http://python-ldap.sourceforge.net/

BuildPreReq: python-devel
BuildPreReq: rpm-build-python >= 0.8
BuildRequires: libldap-devel >= 2.3 libssl-devel
BuildPreReq: texlive-latex-recommended python-module-sphinx

Obsoletes: python-ldap
Packager: Python Development Team <python@packages.altlinux.org>

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package demos
Summary: Demos for python-ldap
Group: Development/Documentation
BuildArch: noarch
Requires: %name = %version-%release

%description demos
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains demos for python-ldap.

%package tests
Summary: Tests for python-ldap
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description tests
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains tests for python-ldap.

%package doc
Summary: Documentation for python-ldap
Group: Development/Documentation
BuildArch: noarch

%description doc
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains documentation for python-ldap.

%package pickles
Summary: Pickles for python-ldap
Group: Development/Python

%description pickles
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP 2.x libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

This package contains pickles for python-ldap.

%prep
%setup -n %oname-%version

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build

%make -C Doc latex

%install
%python_install --optimize=2

cp -fR Doc/.build/pickle %buildroot%python_sitelibdir/ldap/

%files
%doc LICENCE CHANGES README TODO
%python_sitelibdir/*
%exclude %python_sitelibdir/ldap/pickle

%files demos
%doc Demo

%files tests
%doc Tests

%files doc
%doc Doc/.build/html Doc/.build/latex/*.pdf

%files pickles
%python_sitelibdir/ldap/pickle

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.11-alt2.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3.11-alt2.1
- Rebuild with Python-2.7

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt2
- Fixed underlinking

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.11-alt1
- Version 2.3.11
- Extracted demos and tests into separate packages
- Added docs and pickles

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.9-alt1.1
- Rebuilt with python 2.6

* Wed Aug 26 2009 Boris Savelev <boris@altlinux.org> 2.3.9-alt1
- new version

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.3-alt1.1
- Rebuilt with python-2.5.

* Sun May 27 2007 Ivan Fedorov <ns@altlinux.ru> 2.3-alt1
- 2.3

* Sat Jul 01 2006 Ivan Fedorov <ns@altlinux.ru> 2.2.0-alt2
- Remove strange requires

* Thu Apr 13 2006 Ivan Fedorov <ns@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Sat Dec 31 2005 Ivan Fedorov <ns@altlinux.ru> 2.0.11-alt1
- 2.0.11

* Fri May  6 2005 Konstantin Klimchev <koka@altlinux.ru> 2.0.7-alt1
- new 2.0.7
- python2.4

* Fri Nov 19 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.5-alt1
- new 2.0.5

* Fri Oct 8 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.3-alt1
- new 2.0.3
- update python-ldap.lib.pdf

* Fri Aug 20 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.2-alt1
- new 2.0.2

* Mon May 24 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.0-alt2
- new 2.0.0 

* Tue May 18 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.0-alt1.pre21
- new python policy
- replace preX in release

* Tue May 11 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.0pre21-alt1.1
- Rebuilt with openssl-0.9.7d.

* Wed Mar 31 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.0pre21-alt1
- new 2.0.0pre21

* Mon Jan 26 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.0pre19-alt1
- new 2.0.0pre19

* Thu Jan  8 2004 Konstantin Klimchev <koka@altlinux.ru> 2.0.0pre18-alt1
- initial build for Sisyphus

* Mon Dec 15 2003 Klimchev Konstantin <koka@atvc.ru> 2.0.0pre18-1
- new release 2.0.0pre18-1

* Mon Sep 15 2003 Klimchev Konstantin <koka@atvc.ru> 2.0.0pre13-1
- Initial build
