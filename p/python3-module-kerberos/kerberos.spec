%define _unpackaged_files_terminate_build 1
%define mname kerberos

# These tests are crappy
%def_without check

Name: python3-module-%mname
Version: 1.3.1
Release: alt1

Summary: A high-level wrapper for Kerberos (GSSAPI) operations

License: Apache-2.0
Group: System/Libraries
# Source-git: https://github.com/apple/ccs-pykerberos.git
Url: https://pypi.python.org/pypi/kerberos

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libkrb5-devel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-requests
BuildRequires: python3-module-psutil
BuildRequires: /proc
%endif

%description
This Python package is a high-level wrapper for Kerberos (GSSAPI) operations.
The goal is to avoid having to build a module that wraps the entire
Kerberos.framework, and instead offer a limited set of functions that do what
is needed for client/serverKerberos authentication based on
<http://www.ietf.org/rfc/rfc4559.txt>.

Much of the C-code here is adapted from Apache's mod_auth_kerb-5.0rc7.

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python3_build

%install
%python3_install

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-3 -v

%files
%doc *.md
%python3_sitelibdir/kerberos*.so
%python3_sitelibdir/kerberos-%version-py%_python3_version.egg-info

%changelog
* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 1.3.1-alt1
- Automatically updated to 1.3.1.

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt3
- Drop python2 support.

* Wed Jan 16 2019 Evgeny Sinelnikov <sin@altlinux.org> 1.3.0-alt2
- Disable ubt macros due binary package identity change

* Mon Apr 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt1.S1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Mar 16 2018 Stanislav Levin <slev@altlinux.org> 1.3.0-alt1.S1
- 1.2.5 -> 1.3.0

* Tue Nov 14 2017 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.S1
- 1.1.1 -> 1.2.5

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1
- Version 1.1.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Thu May 07 2009 Evgeny Sinelnikov <sin@altlinux.ru> 1.1-alt1
- Build for Sisyphus

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 15 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3.1
- Fix minor issue with delegation patch

* Fri Dec 12 2008 Simo Sorce <ssorce@redhat.com> - 1.1-3
- Add delegation patch

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.1-2
- Rebuild for Python 2.6

* Thu Nov 27 2008 Simo Sorce <ssorce@redhat.com> - 1.1-1
- New Upstream Release
- Remove patches as this version has them included already

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0-6
- Autorebuild for GCC 4.3

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-5
- Package the egg-info too

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-4
- Switch from python_sitelib macro to python_sitearch
- Add python-setuptools to BuildRequires

* Wed Jan 16 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-3
- Use the setup.py install target in order to generate debuginfo.

* Thu Jan  3 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-2
- Add krb5-devel to BuildRequires

* Wed Jan  2 2008 Rob Crittenden <rcritten@redhat.com> - 1.0-1
- Change name to python-kerberos from PyKerberos
- Change license from "Apache License" to ASL 2.0 per guidelines
- Upstream released 1.0 which is equivalent to version 1541. Reverting
  to that.

* Tue Aug 28 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-2
- Include GSS_C_DELEG_FLAG in gss_init_sec_context() so the command-line
  tools can do kerberos ticket forwarding.

* Tue Jul 31 2007 Rob Crittenden <rcritten@redhat.com> - 0.1735-1
- Initial rpm version
