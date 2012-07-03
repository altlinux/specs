Name: jabber-j2j
Version: 1.1.8
Release: alt5.1.1

Summary: XMPP transport for jabber servers
License: GPL
Group: System/Servers
Url: http://wiki.jrudevels.org/index.php/J2J
Packager: Sergey Bolshakov <sbolshakov@altlinux.ru>

Source: %name-%version.tar
BuildRequires: jabber-common

Requires(pre): shadow-utils
Requires(post): %post_service jabber-common
Requires(preun): %preun_service
Requires: python-module-twisted-names
%py_requires MySQLdb
%py_requires pgdb mx.DateTime

%description
With this transport you can aggregate contacts from rosters of two (or more) 
Jabber accounts in single roster. E.g., you can communicate through your GTalk
or LiveJournal account, using main account on Jabber.org.

%prep
%setup
sed -i 's,/usr/lib,%_libdir,' j2j.init

%install
mkdir -p %buildroot%_libdir/j2j %buildroot%_logdir/j2j %buildroot%_localstatedir/%name
install -pm0644 *.py %buildroot%_libdir/j2j
install -pm0644 -D j2j.conf.example %buildroot%_sysconfdir/j2j.conf

install -pm0755 -D j2j.init %buildroot%_initdir/jabber-j2j
install -pm0755 -D j2j.adapter %buildroot%_jabber_component_dir/j2j

%set_python_req_method strict
%add_python_req_skip config

%pre
/usr/sbin/groupadd -r -f _j2j &>/dev/null
/usr/sbin/useradd -r -g _j2j -d %_localstatedir/%name -s /dev/null \
    -c "XMPP Jabber transport" -M -n _j2j &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%triggerun -- jabber-j2j < 1.1.8-alt4
if [ $2 -gt 0 ]; then
%post_service %name
fi

%files
%doc pgsql.schema mysql.schema
%attr(0640,root,_j2j) %config(noreplace) %_sysconfdir/j2j.conf
%_initdir/%name
%_libdir/j2j
%_jabber_component_dir/j2j
%attr(0770,root,_j2j) %dir %_localstatedir/%name
%attr(0770,root,_j2j) %dir %_logdir/j2j

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.8-alt5.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2008 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.8-alt5.1
- Rebuilt with python 2.6

* Sun Aug 31 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt5
- added few python reqs manually

* Sat Mar  8 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt4
- updated to svn rev.115

* Sat Feb  9 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt3
- fixed req on jabber-common (#14372)
- allow non-unicode JID value in j2j.conf (#14368)

* Fri Jan 25 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt2
- mysql support added

* Sat Jul 21 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.1.8-alt1
- Initial build.
