%define _unpackaged_files_terminate_build 1
%def_disable static
%def_without bootstrap
%def_with ldap

Name: audit
Version: 4.0.1
Release: alt2

Summary: User space tools for Linux kernel 2.6+ auditing
License: GPL-2.0-or-later and LGPL-2.1-or-later
Group: Monitoring

URL: https://people.redhat.com/sgrubb/audit
VCS: https://github.com/linux-audit/audit-userspace

Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Requires: libaudit1 = %EVR

# Make audit installable on systems without systemd
# (upstream dropped support for SysVinit since 4.0)
%filter_from_requires /^\/bin\/systemctl$/d
%add_findreq_skiplist %_initdir/auditd

%if_without bootstrap
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

BuildRequires: swig
BuildRequires: automake
BuildRequires: perl-XML-Parser
BuildRequires: libkrb5-devel
BuildRequires: libcap-ng-devel
%endif

%if_enabled static
BuildRequires: glibc-devel-static
%endif

%if_with ldap
BuildRequires: libldap-devel
%endif

%description
The audit package contains the user space utilities for
storing and searching the audit records generate by
the audit subsystem in the Linux 2.6+ kernel.

%package -n libaudit1
Summary: Dynamic library for audit framework
License: LGPL-2.1-or-later
Group: System/Libraries
Provides: libaudit = %EVR
Obsoletes: libaudit = 2.0.4-alt1

%description -n libaudit1
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n libauparse0
Summary: Dynamic library for audit framework
License: LGPL-2.1-or-later
Group: System/Libraries
Conflicts: libaudit = 2.0.4-alt1
Conflicts: libaudit < 1.7.16-alt2

%description -n libauparse0
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n libaudit-devel
Summary: Header files and static library for libaudit
License: LGPL-2.1-or-later
Group: Development/C
Requires: libaudit1 = %EVR
Requires: libauparse0 = %EVR

%description -n libaudit-devel
This package contains the static libraries and header
files needed for developing applications that need to use the audit
framework libraries.

%package -n python3-module-audit
Summary: Python3 bindings for libaudit
License: LGPL-2.1-or-later
Group: Development/Python3
Requires: libaudit1 = %EVR

%description -n python3-module-audit
The python3-module-audit package contains the bindings so that libaudit
and libauparse can be used by python.

%prep
%setup
%patch0 -p1

# set initdir to _unitdir for compatibility with usr-merged systems
sed -i 's|^initdir = .*|initdir = %_unitdir|' init.d/Makefile.am

# correct sbindir in init scripts
sed -i 's|/sbin/auditctl|%_sbindir/auditctl|' init.d/*

# workaround automake strictness settings
touch README

%build
export PYTHON=python3
export PYTHON3=python3
%autoreconf

%configure \
	--sbindir=%_sbindir \
	--libdir=%_libdir \
	--libexecdir=%prefix/libexec \
	--with-aarch64 \
	--with-arm \
	--with-libcap-ng=auto \
	--without-golang \
	--enable-experimental \
	--with-io_uring \
%if_with bootstrap
	--without-python3 \
%else
	--enable-gssapi-krb5 \
%endif
%if_without ldap
	--disable-zos-remote \
%endif
	%{subst_enable static}

%make_build

%install
export PYTHON=python3
export PYTHON3=python3
%makeinstall_std

install -d %buildroot%_logdir/audit
install -d %buildroot%_libdir/audit

install -pD -m644 rules/10-base-config.rules \
        %buildroot%_sysconfdir/audit/rules.d/10-base-config.rules

install -Dpm755 audit.init %buildroot/%_initdir/auditd

%check
export PYTHON=python3
export PYTHON3=python3
%make check

%post
%post_service auditd
if [ $1 -gt 1 ]; then
    service auditd condrestart ||:
fi

%preun
%preun_service auditd
if [ $1 -eq 0 ]; then
    service auditd stop ||:
fi

%files
%doc README.md ChangeLog contrib init.d/auditd.cron
%_bindir/aulastlog
%_bindir/aulast
%_bindir/ausyscall
%_sbindir/ausearch
%_sbindir/aureport
%attr(750,root,root) %_sbindir/auditctl
%attr(750,root,root) %_sbindir/augenrules
%attr(750,root,root) %_sbindir/auditd
%attr(750,root,root) %_sbindir/audisp-af_unix
%attr(750,root,root) %_sbindir/audisp-filter
%attr(750,root,root) %_sbindir/audisp-ids
%attr(750,root,root) %_sbindir/audisp-remote
%attr(750,root,root) %_sbindir/audisp-statsd
%attr(750,root,root) %_sbindir/audisp-syslog
%if_with ldap
%attr(750,root,root) %_sbindir/audispd-zos-remote
%endif

%_initdir/auditd

%attr(700,root,root) %_logdir/audit
%_unitdir/auditd.service
%_unitdir/audit-rules.service

%_datadir/audit-rules
%_man5dir/*
%_man8dir/*
%_man7dir/*

%attr(700,root,root) %dir %_sysconfdir/audit
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/auditd.conf
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/audit-stop.rules

%attr(700,root,root) %dir %_sysconfdir/audit/rules.d
%config(noreplace) %attr(600,root,root) %_sysconfdir/audit/rules.d/*.rules

%attr(700,root,root) %dir %_sysconfdir/audit/plugins.d
%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/plugins.d/*.conf

%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/audisp-remote.conf
%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/zos-remote.conf
%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/ids.conf
%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/audisp-statsd.conf
%config(noreplace) %attr(640,root,root) %_sysconfdir/audit/audisp-filter.conf

/usr/libexec/service/legacy-actions/auditd

%files -n libaudit1
%_libdir/libaudit.so.*
%config(noreplace) %attr(600,root,root) %_sysconfdir/libaudit.conf

%files -n libauparse0
%_libdir/libauparse.so.*

%files -n libaudit-devel
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*
%_man3dir/*
%_aclocaldir/audit.m4

%if_without bootstrap
%files -n python3-module-audit
%python3_sitelibdir/audit.py
%python3_sitelibdir/_audit.la
%python3_sitelibdir/_audit.so
%python3_sitelibdir/auparse.la
%python3_sitelibdir/auparse.so
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Wed Jun 26 2024 Egor Ignatov <egori@altlinux.org> 4.0.1-alt2
- filter /bin/systemctl dependency (closes: 50744)
- bring back our downstream audit.init script

* Thu Jun 06 2024 Egor Ignatov <egori@altlinux.org> 4.0.1-alt1
- new version 4.0.1

* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt2.1
- NMU: Add build dependency on setuptools.

* Wed Sep 20 2023 Michael Shigorin <mike@altlinux.org> 3.1.2-alt2
- add %%check

* Fri Aug 11 2023 Egor Ignatov <egori@altlinux.org> 3.1.2-alt1
- new version 3.1.2
- remove swig flexible array workaround (fixed by upstream)

* Fri Apr 28 2023 Egor Ignatov <egori@altlinux.org> 3.1.1-alt1
- new version 3.1.1

* Wed Feb 15 2023 Egor Ignatov <egori@altlinux.org> 3.1-alt1
- new version 3.1

* Tue Aug 30 2022 Egor Ignatov <egori@altlinux.org> 3.0.9-alt1
- new version 3.0.9

* Fri Apr 01 2022 Egor Ignatov <egori@altlinux.org> 3.0.8-alt2
- Make swig flexible array workaround compatible with p10

* Wed Mar 30 2022 Egor Ignatov <egori@altlinux.org> 3.0.8-alt1
- new version 3.0.8

* Tue Mar 22 2022 Egor Ignatov <egori@altlinux.org> 3.0.7-alt2
- Fix FTBFS: add flex-array-workaround patch

* Mon Jan 31 2022 Egor Ignatov <egori@altlinux.org> 3.0.7-alt1
- new version 3.0.7
- Update scripts in init.d
- spec: Build with libcap-ng and krb5

* Mon Oct 04 2021 Egor Ignatov <egori@altlinux.org> 3.0.6-alt1
- new version 3.0.6

* Mon Sep 06 2021 Egor Ignatov <egori@altlinux.org> 3.0.5-alt2
- Fix bi-arch check (closes: #40852)
- Add armv8l support
- ausyscall: Add support for 'b32' and 'b64' aliases

* Fri Aug 13 2021 Egor Ignatov <egori@altlinux.org> 3.0.5-alt1
- new version 3.0.5

* Sat Jul 17 2021 Egor Ignatov <egori@altlinux.org> 3.0.3-alt1
- new version 3.0.3

* Tue Jun 22 2021 Egor Ignatov <egori@altlinux.org> 3.0.2-alt1
- new version 3.0.2

* Fri Feb 19 2021 Egor Ignatov <egori@altlinux.org> 3.0.1-alt1
- Update to version 3.0.1
- Exclude libpthread dependency from libaudit

* Thu Feb 11 2021 Egor Ignatov <egori@altlinux.org> 3.0-alt1
- Update to version 3.0

* Tue Oct 06 2020 Anton Farygin <rider@altlinux.ru> 2.8.5-alt5.git.e4021a9
- enabled ELF mapping for arm and aarch64 processors

* Mon Jan 27 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt4.git.e4021a9
- Ported fix from different branch.

* Fri Jan 24 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt3.git.e4021a9
- Pulled updates from upstream, including memory leak fixes.

* Mon Mar 18 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2.8.5-alt2
- Built python-3 bindings.

* Tue Mar 12 2019 Anton Farygin <rider@altlinux.ru> 2.8.5-alt1
- 2.8.5

* Thu Oct 04 2018 Stanislav Levin <slev@altlinux.org> 2.8.4-alt2
- Fixed log's server mode on IPV4 machines.

* Mon Jun 25 2018 Anton Farygin <rider@altlinux.ru> 2.8.4-alt1
- 2.8.4

* Fri Apr 20 2018 Stanislav Levin <slev@altlinux.org> 2.8.3-alt3
- Fix dependency to systemd in post script

* Wed Apr 18 2018 Stanislav Levin <slev@altlinux.org> 2.8.3-alt2
- Make it possible not to limit the restart of a crashed plugin

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 2.8.3-alt1
- new version

* Fri Jan 26 2018 Anton Farygin <rider@altlinux.ru> 2.8.2-alt1
- new version
- disabled prelude support (code is outdated and needs to be revised)

* Sun Oct 15 2017 Anton Farygin <rider@altlinux.ru> 2.8.1-alt1
- new version

* Fri Sep 22 2017 Anton Farygin <rider@altlinux.ru> 2.7.8-alt1
- new version

* Thu Sep 07 2017 Michael Shigorin <mike@altlinux.org> 2.7.7-alt2
- BOOTSTRAP:
  + make krb5/ldap/prelude/python support conditional
  + make zos-remote plugin build depend on ldap support explicitly
  - minor spec cleanup

* Thu Jun 22 2017 Anton Farygin <rider@altlinux.ru> 2.7.7-alt1
- new version

* Mon Apr 24 2017 Anton Farygin <rider@altlinux.ru> 2.7.6-alt1
- new version

* Fri Apr 14 2017 Anton Farygin <rider@altlinux.ru> 2.7.5-alt1
- new version

* Fri Mar 10 2017 Anton Farygin <rider@altlinux.ru> 2.7.3-alt1
- new version

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 2.7.2-alt1
- new version

* Wed Feb 08 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1
- new version

* Wed Feb 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.6.7-alt1.1
- rebuild with libprelude

* Thu Sep 15 2016 Anton Farygin <rider@altlinux.ru> 2.6.7-alt1
- new version

* Tue Jul 19 2016 Anton Farygin <rider@altlinux.ru> 2.6.5-alt1
- new version

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 2.5.2-alt1
- new version

* Thu Jan 14 2016 Anton Farygin <rider@altlinux.ru> 2.5-alt1
- new version

* Wed Oct 21 2015 Anton Farygin <rider@altlinux.ru> 2.4.4-alt1
- new version

* Tue May 26 2015 Anton Farygin <rider@altlinux.ru> 2.4.2-alt2
- rebuild for new environment

* Tue May 19 2015 Anton Farygin <rider@altlinux.ru> 2.4.2-alt1
- new version

* Thu Jan 22 2015 Anton Farygin <rider@altlinux.ru> 2.4.1-alt1
- new version
- added legacy actions scripts (closes: #28931, #27843)

* Wed Sep 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4-alt1.1
- Rebuilt with new libprelude

* Mon Sep 08 2014 Anton Farygin <rider@altlinux.ru> 2.4-alt1
- new version

* Thu Jun 05 2014 Anton Farygin <rider@altlinux.ru> 2.3.7-alt1
- new version

* Mon Apr 14 2014 Anton Farygin <rider@altlinux.ru> 2.3.6-alt1
- new version

* Fri Mar 21 2014 Anton Farygin <rider@altlinux.ru> 2.3.5-alt1
- new version

* Thu Feb 20 2014 Anton Farygin <rider@altlinux.ru> 2.3.3-alt1
- new version

* Mon Oct 07 2013 Anton Farygin <rider@altlinux.ru> 2.3.2-alt1
- new version

* Mon Jun 24 2013 Anton Farygin <rider@altlinux.ru> 2.3.1-alt1
- new version

* Fri Apr 19 2013 Anton Farygin <rider@altlinux.ru> 2.2.3-alt1
- new version
- add systemd support

* Wed Sep 19 2012 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- new version

* Tue Sep 13 2011 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- new version

* Fri Feb 25 2011 Anton Farygin <rider@altlinux.ru> 2.0.6-alt1
- new version

* Tue Sep 28 2010 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- new version

* Tue Jul 20 2010 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt2
- fix summaries and descriptions.
- package libauparse as separate subpackage libauparse0.
- rename libaudit -> libaudit1.

* Thu Jul 01 2010 Mikhail Efremov <sem@altlinux.org> 2.0.4-alt1
- spec cleanup.
- drop depends on python-module-pygtk-libglade.
- new version

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.16-alt1.1
- Rebuilt with python 2.6

* Mon Nov 16 2009 Anton Farygin <rider@altlinux.ru> 1.7.16-alt1
- new version

* Tue Sep 01 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt3
- rebuild with libldap2.4

* Sun Aug 09 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt2
- python-dev requires changed to python-devel
- menu entry fixed for system-config-audit

* Mon Apr 27 2009 Anton Farygin <rider@altlinux.ru> 1.7.13-alt1
- new version
- fixed build

* Wed Apr 08 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt6
- added python-module-pygtk-libglade to requires for python-module-audit (#19431)

* Wed Mar 11 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt4
- service auditd off by default

* Tue Mar 10 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.7.12-alt3
- added support of libprelude

* Wed Mar 04 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt2
- added system-config-audit subpackage with graphical utility for editing audit configuration

* Wed Mar 04 2009 Anton Farygin <rider@altlinux.ru> 1.7.12-alt1
- new version

* Thu Jan 15 2009 Anton Farygin <rider@altlinux.ru> 1.7.11-alt1
- new version
- subpackage python-module-audit added
- Packager changed

* Wed Dec 17 2008 Anton Farygin <rider@altlinux.ru> 1.7.10-alt1
- new version

* Fri Dec 12 2008 Anton Farygin <rider@altlinux.ru> 1.7.9-alt1
- new version

* Tue Sep 23 2008 Stanislav Ievlev <inger@altlinux.org> 1.7-alt2
- silent rotate

* Thu Apr 03 2008 Stanislav Ievlev <inger@altlinux.org> 1.7-alt1
- 1.7

* Fri Jul 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.5.4-alt1
- 1.5.4

* Thu May 24 2007 Stanislav Ievlev <inger@altlinux.org> 1.5.3-alt1
- Initial release
