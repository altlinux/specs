Name: jabber-pyicqt
Version: 0.8.1.5
Release: alt1.1

Summary: ICQ transport for XMPP servers
License: GPL
Group: System/Servers
Url: http://pyicqt.googlecode.com
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Requires(pre): shadow-utils
Requires(post): %post_service jabber-common
Requires(preun): %preun_service
# more uncatched reqs:
Requires: python-module-twisted-web
Requires: python-module-twisted-words

Provides: pyicq-t = %version-%release
Obsoletes: pyicq-t

BuildRequires(pre): jabber-common
BuildRequires: python-devel

Source0: %name-%version-%release.tar

%package mysql
Summary: ICQ transport for XMPP servers -- MySQL connector
Group: System/Servers
Requires: %name == %version-%release

%package pgsql
Summary: ICQ transport for XMPP servers -- PgSQL connector
Group: System/Servers
Requires: %name == %version-%release

%description
%name is a ICQ transport for Jabber servers.
this package contains only `xmlfiles' backend,
see %name-mysql or %name-pgsql packages.

%description mysql
%name is a ICQ transport for Jabber servers.
this package contains MySQL backend for %name

%description pgsql
%name is a ICQ transport for Jabber servers.
this package contains PostgreSQL backend for %name

%prep
%setup
sed -i 's/@altversion@/%version-%release/' src/services/VersionTeller.py
sed -i 's,/usr/lib,%_libdir,' pyicqt.init

%install
mkdir -p %buildroot%_var/run/pyicqt %buildroot%_var/log/pyicqt %buildroot%_spooldir/pyicqt
install -pm0644 -D PyICQt.py %buildroot%_libdir/pyicqt/PyICQt.py
find src data -type f -not '(' -path 'src/web/*' -o -path 'data/www/*' ')' |\
    cpio -pmdv %buildroot%_libdir/pyicqt
install -pm 0755 -D pyicqt.init %buildroot%_initdir/%name
install -pm 0755 -D pyicqt.adapter %buildroot%_jabber_component_dir/pyicqt
install -pm 0640 -D config_example.xml %buildroot%_sysconfdir/pyicqt.xml
install -pm 0644 -D pyicqt.sysconfig %buildroot%_sysconfdir/sysconfig/pyicqt
install -pm 0640 -D pyicqt.logrotate %buildroot%_sysconfdir/logrotate.d/pyicqt

%add_python_lib_path %_libdir/pyicqt/src
%add_python_lib_path %_libdir/pyicqt/lang
%set_python_req_method strict
# mask req to full-blown p-i-l
%add_python_req_skip Image

%pre
/usr/sbin/groupadd -r -f _pyicqt &>/dev/null ||:
/usr/sbin/useradd -r -g _pyicqt -d /dev/null -s /dev/null \
    -c "ICQ Jabber transport" -M -n _pyicqt &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README tools
%attr(0640,root,_pyicqt) %config(noreplace) %_sysconfdir/pyicqt.xml
%config(noreplace) %_sysconfdir/sysconfig/pyicqt
%attr(640,root,root) %config %_sysconfdir/logrotate.d/pyicqt

%_initdir/%name

%_libdir/pyicqt
%exclude %_libdir/pyicqt/src/xdb/mysql.py*
%exclude %_libdir/pyicqt/src/xdb/postgresql.py*

%_jabber_component_dir/pyicqt

%attr(0770,root,_pyicqt) %dir %_spooldir/pyicqt
%attr(0770,root,_pyicqt) %dir %_var/run/pyicqt
%attr(0770,root,_pyicqt) %dir %_var/log/pyicqt

%files mysql
%_libdir/pyicqt/src/xdb/mysql.py*

%files pgsql
%_libdir/pyicqt/src/xdb/postgresql.py*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.1.5-alt1.1
- Rebuild with Python-2.7

* Wed Jan 13 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1.5-alt1
- 0.8.1.5 released

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1.2-alt2.1
- Rebuilt with python 2.6

* Thu Feb 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1.2-alt2
- logrotate script added (#18902), by erthad@
- updated to git-4cbfbc74

* Fri Jan 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1.2-alt1
- 0.8.1.2 released

* Thu Jan 22 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1.1-alt1
- 0.8.1.1 released
- avatar support is off by default from now, install of python-module-imaging
  before enabling it is required
- workaround for upstream issue #156 added

* Thu Dec 18 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt2
- fixed unwanted nicknames recode [upstream #145]

* Wed Dec 17 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt1
- 0.8.1 released

* Sun Dec  7 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt0.3
- updated to 0.8.1b3

* Tue Oct 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.1-alt0.2
- updated to 0.8.1b2
- sql schemas changed [INCOMPATIBILITY]

* Sun Aug 31 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt6
- added few python reqs manually (#15661)

* Sat Mar  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt5
- updated to svn rev.236, near 0.8b release
- fixed initscript to check for already running instance (#14762)

* Wed Feb 13 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt4
- rebuilt against python 2.5
- obsoletes pyicq-t from now

* Thu Dec 20 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt3
- rebuilt with strict reqs finding

* Sun Dec  9 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt2
- updated to 20070823 patchset
- MySQL & PostgreSQL backends packaged separately

* Sat Aug 11 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8-alt1
- Initial build.
