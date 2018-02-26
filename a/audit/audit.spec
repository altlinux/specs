Name: audit
Version: 2.1.3
Release: alt1.1

Packager: Anton Farygin <rider@altlinux.com>

Summary: User space tools for 2.6 kernel auditing

License: GPL
Group: Monitoring
URL: http://people.redhat.com/sgrubb/audit/
Source: %name-%version.tar
Source1: %name.init
Source2: %name.cron
Patch0: %name-%version-%release.patch

Requires: lib%{name}1 = %version-%release

# Automatically added by buildreq on Wed Mar 04 2009
BuildRequires: glibc-devel-static libkrb5-devel libldap-devel perl-XML-Parser python-devel swig libprelude-devel intltool

%description
The audit package contains the user space utilities for
storing and searching the audit records generate by
the audit subsystem in the Linux 2.6 kernel.

%package -n lib%{name}1
Summary: Dynamic library for audit framework
License: LGPL
Group: System/Libraries
Provides: lib%name = %version-%release
Obsoletes: libaudit = 2.0.4-alt1

%description -n lib%{name}1
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n libauparse0
Summary: Dynamic library for audit framework
License: LGPL
Group: System/Libraries
Conflicts: lib%name = 2.0.4-alt1
Conflicts: lib%name < 1.7.16-alt2

%description -n libauparse0
This package contains the dynamic libraries needed for
applications to use the audit framework.

%package -n lib%name-devel
Summary: Header files and static library for libaudit
License: LGPL
Group: Development/C
Requires: lib%{name}1 = %version-%release
Requires: libauparse0 = %version-%release

%description -n lib%name-devel
This package contains the static libraries and header
files needed for developing applications that need to use the audit
framework libraries.

%package -n python-module-%name
Summary: Python bindings for libaudit
License: LGPL
Group: Development/Python
Requires: lib%{name}1 = %version-%release

%description -n python-module-%name
The python-module-%name package contains the bindings so that libaudit
and libauparse can be used by python.

%prep
%setup -q
%patch0 -p1

%build
%autoreconf

%configure --sbindir=/sbin --libdir=/%_lib --disable-static --with-prelude

%make_build CFLAGS=-D_GNU_SOURCE

%install
make DESTDIR=%buildroot install

install -d %buildroot%_logdir/%name
install -d %buildroot%_sysconfdir/audispd/plugins.d
install -d %buildroot/%_libdir/%name

#move development part to libdir
install -d %buildroot%_libdir
for i in libaudit libauparse;do
LIBNAME=$(readlink %buildroot/%_lib/$i.so)
ln -s  /%_lib/${LIBNAME##*/}  %buildroot/%_libdir/$i.so
done

#replace init script
install -Dpm755 %SOURCE1 %buildroot/%_initdir/%{name}d

#install rotate script
install -Dpm755 %SOURCE2 %buildroot/%_sysconfdir/cron.weekly/%{name}d

%post
%post_service %{name}d

%preun
%preun_service %{name}d

%files
%doc README ChangeLog contrib
%config(noreplace) %_sysconfdir/cron.weekly/%{name}d
%_initdir/%{name}d
%attr(700,root,root) %_logdir/%name

/sbin/ausearch
/sbin/aureport
%attr(750,root,root) /sbin/auditctl
%attr(750,root,root) /sbin/auditd
%attr(750,root,root) /sbin/autrace
%attr(750,root,root) /sbin/audispd
%attr(750,root,root) /sbin/audisp-remote
%attr(750,root,root) /sbin/audisp-prelude
%attr(750,root,root) /sbin/audispd-zos-remote
%attr(750,root,root) %_bindir/aulastlog
%attr(750,root,root) %_bindir/aulast
%attr(750,root,root) %_bindir/ausyscall


%_man5dir/*
%_man8dir/*
%_man7dir/*

%attr(700,root,root) %dir %_sysconfdir/%name
%config(noreplace) %attr(600,root,root) %_sysconfdir/%name/auditd.conf
%config(noreplace) %attr(600,root,root) %_sysconfdir/%name/audit.rules

%attr(700,root,root) %dir %_sysconfdir/audispd
%config(noreplace) %attr(640,root,root) /etc/audisp/*.conf

%attr(700,root,root) %dir %_sysconfdir/audispd/plugins.d
%config(noreplace) %attr(640,root,root) /etc/audisp/plugins.d/*.conf

%attr(700,root,root) %dir %_libdir/audit



%files -n lib%{name}1
/%_lib/libaudit.so.*
%config(noreplace) %attr(600,root,root) /etc/libaudit.conf

%files -n libauparse0
/%_lib/libauparse.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*
%_man3dir/*

%files -n python-module-%name
%python_sitelibdir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.3-alt1.1
- Rebuild with Python-2.7

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
