%define spawn_fcgi_user _spawn_fcgi
%define spawn_fcgi_group _spawn_fcgi

Name: spawn-fcgi
Version: 1.6.4
Release: alt2%ubt

Summary: spawn FastCGI applications
License: BSD
Group: System/Servers
BuildRequires(pre):rpm-build-ubt

# git remote add upstream git://git.lighttpd.net/spawn-fcgi
Url: http://redmine.lighttpd.net/projects/spawn-fcgi/wiki

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

%description
  spawn-fcgi is used to spawn FastCGI applications

  Features
  --------
  - binds to IPv4/IPv6 and Unix domain sockets
  - supports privilege separation: chmod/chown socket, drop to uid/gid
  - supports chroot
  - supports daemontools supervise

%prep
%setup
%patch0 -p1
%autoreconf

%build
%configure
%make_build

%install
%makeinstall

mkdir -p %buildroot%_var/run/spawn-fcgi
install -pDm755 altlinux/spawn-fcgi.init %buildroot%_initdir/spawn-fcgi
install -pDm644 altlinux/spawn-fcgi.sysconfig %buildroot%_sysconfdir/sysconfig/spawn-fcgi

%pre
%_sbindir/groupadd -r -f %spawn_fcgi_group ||:
%_sbindir/useradd -r -g %spawn_fcgi_group -d /dev/null -s /dev/null -n %spawn_fcgi_user \
        2> /dev/null > /dev/null ||:

%post
%post_service spawn-fcgi

%preun
%preun_service spawn-fcgi

%files
%_bindir/spawn-fcgi
%_man1dir/spawn-fcgi*
%config(noreplace) %_sysconfdir/sysconfig/spawn-fcgi
%_initdir/spawn-fcgi
%dir %attr(1770,root,%spawn_fcgi_group) %_var/run/spawn-fcgi

%changelog
* Wed Dec 21 2016 Anton Farygin <rider@altlinux.ru> 1.6.4-alt2%ubt
- fixes fcgiwrap location in default config

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1
- updated to 1.6.4

* Fri Apr 18 2014 Anton Farygin <rider@altlinux.ru> 1.6.3-alt4
- initfile: don't check pidfile in stop target

* Fri Apr 18 2014 Anton Farygin <rider@altlinux.ru> 1.6.3-alt3
- tune default config and initscript for run fcgiwrap instead of php5-cgi

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 1.6.3-alt2
- fixed condrestart and condreload targets in initscript (closes: #29456)

* Tue Sep 17 2013 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.2-alt3.qa1
- NMU: rebuilt for debuginfo.

* Sun Sep 19 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt3
- typo in initscript fixed

* Tue Aug 10 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.2-alt2.1
- allow use of unix domain socket

* Thu Sep 24 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6.2-alt2
- spawn-fcgi.sysconfig: add variable for interface binding and bind to
  127.0.0.1 by default (Closes: #21581)

* Wed Sep 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.6.2-alt1
- Initial build for Sisyphus

