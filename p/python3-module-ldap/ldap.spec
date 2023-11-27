%define _unpackaged_files_terminate_build 1
%define pypi_name python-ldap
%define mname ldap

%def_with check

Name: python3-module-%mname
Version: 3.4.4
Release: alt1
Summary: Python modules for implementing LDAP clients
License: Python-style or MIT
Group: Development/Python3
Url: https://www.python-ldap.org
Vcs: https://github.com/python-ldap/python-ldap
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
Provides: python3-module-pyldap = %EVR
Obsoletes: python3-module-pyldap < %EVR
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libldap-devel
BuildRequires: libsasl2-devel
BuildRequires: libssl-devel
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
BuildRequires: openldap-servers
BuildRequires: openldap-clients
%endif

%description
python-ldap provides an object-oriented API to access LDAP
directory servers from Python programs. Mainly it wraps the
OpenLDAP client libs for that purpose.

Additionally the package contains modules for other LDAP-related
stuff (e.g. processing LDIF, LDAPURLs, LDAPv3 sub-schema, etc.).

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

# Fix python interpreter path in Demo directory
grep -rl '^#!/usr/bin/env python' | \
	xargs sed -i '1s|^#!/usr/bin/env python|#!/usr/bin/python3|'

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
export BIN="$PATH:%_sbindir"
%pyproject_run_unittest discover -v -s Tests -p 't_*'

%files
%doc LICENCE CHANGES README TODO Demo
%python3_sitelibdir/slapdtest/
%python3_sitelibdir/_ldap.cpython-*.so
%python3_sitelibdir/ldap
%python3_sitelibdir/ldapurl.py*
%python3_sitelibdir/ldif.py*
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Nov 27 2023 Stanislav Levin <slev@altlinux.org> 3.4.4-alt1
- 3.4.3 -> 3.4.4 (closes: #48579).

* Fri Jun 09 2023 Stanislav Levin <slev@altlinux.org> 3.4.3-alt2
- Shipped slapdtest package.

* Tue Sep 20 2022 Stanislav Levin <slev@altlinux.org> 3.4.3-alt1
- 3.4.2 -> 3.4.3.

* Wed Sep 14 2022 Stanislav Levin <slev@altlinux.org> 3.4.2-alt1
- 3.4.0 -> 3.4.2.

* Tue Nov 30 2021 Stanislav Levin <slev@altlinux.org> 3.4.0-alt1
- 3.3.1 -> 3.4.0.

* Mon Jul 06 2020 Stanislav Levin <slev@altlinux.org> 3.3.1-alt1
- 3.2.0 -> 3.3.1.

* Fri May 01 2020 Stanislav Levin <slev@altlinux.org> 3.2.0-alt2
- Fixed FTBFS.

* Sun Mar 17 2019 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0.

* Thu May 31 2018 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- 3.0.0 -> 3.1.0

* Wed Apr 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt3
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 29 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt2
- 3.0.0b4 -> 3.0.0

* Mon Jan 15 2018 Stanislav Levin <slev@altlinux.org> 3.0.0-alt1.b4
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
