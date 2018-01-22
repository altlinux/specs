%define _unpackaged_files_terminate_build 1

%define mname ldap
Name: python-module-%mname
Version: 3.0.0
Release: alt1.b4%ubt
Summary: An object-oriented API to access LDAP directory servers from Python programs
License: Python-style
Group: Development/Python
Url: https://www.python-ldap.org
# Source-git: https://github.com/python-ldap/python-ldap
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python-module-setuptools
BuildRequires: python3-module-setuptools
BuildRequires: libldap-devel
BuildRequires: libsasl2-devel
BuildRequires: libssl-devel
# for tests
BuildRequires: openldap-servers
BuildRequires: openldap-clients
BuildRequires: python-module-tox
BuildRequires: python-module-pyasn1
BuildRequires: python-module-pyasn1-modules
BuildRequires: python-module-coverage
BuildRequires: python-module-virtualenv
BuildRequires: python3-module-tox
BuildRequires: python3-module-pyasn1
BuildRequires: python3-module-pyasn1-modules
BuildRequires: python3-module-coverage
BuildRequires: python3-module-virtualenv
#

Provides: python-module-pyldap = %EVR
Obsoletes: python-module-pyldap < %EVR

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP client libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%package -n python3-module-%mname
Summary: An object-oriented API to access LDAP directory servers from Python3 programs
Group: Development/Python3
Provides: python3-module-pyldap = %EVR
Obsoletes: python3-module-pyldap < %EVR

%description -n python3-module-%mname
python-ldap provides an object-oriented API to access LDAP
directory servers from Python3 programs. Mainly it wraps the
OpenLDAP client libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%prep
%setup
%patch0 -p1
rm -rf ../python3
cp -a . ../python3

# Fix python interpreter path in Demo directory
grep -rl '^#!/usr/bin/env python' ./ | \
	xargs sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python|'
grep -rl '^#!/usr/bin/env python' ../python3 | \
	xargs sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|'

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

pushd ../python3
%python3_build_debug
popd

%check
export PIP_INDEX_URL=http://host.invalid./
export PYTHONPATH=%python_sitelibdir_noarch:%python_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox -e py27 -v

pushd ../python3
export PYTHONPATH=%python3_sitelibdir_noarch:%python3_sitelibdir
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py35 -v
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%files
%doc LICENCE CHANGES README TODO Demo
%exclude %python_sitelibdir/slapdtest
%python_sitelibdir/_ldap.so
%python_sitelibdir/ldap
%python_sitelibdir/ldapurl.py*
%python_sitelibdir/ldif.py*
%python_sitelibdir/python_ldap-%{version}*-*.egg-info

%files -n python3-module-%mname
%doc LICENCE CHANGES README TODO Demo
%exclude %python3_sitelibdir/slapdtest
%python3_sitelibdir/_ldap.cpython-*.so
%python3_sitelibdir/ldap
%python3_sitelibdir/ldapurl.py*
%python3_sitelibdir/ldif.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/python_ldap-%{version}*-*.egg-info

%changelog
* Mon Jan 15 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1.b4%ubt
- v2.3 -> v3.0.0b4

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
