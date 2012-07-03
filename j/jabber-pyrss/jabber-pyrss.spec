Name: jabber-pyrss
Version: 0.9.9.1
Release: alt1.1

Summary: RSS XMPP service
License: GPL
Group: System/Servers

Source: %name-%version-%release.tar
BuildRequires: jabber-common

%description
PyRSS is component for jabber servers.
PyRSS fetch rss and notify registered users.

%prep
%setup
sed -i 's,/usr/lib,%_libdir,' pyrss.init

%install
mkdir -p %buildroot%_libdir/pyrss %buildroot%_logdir/pyrss %buildroot%_var/run/pyrss
install -pm0644 pyrss.py %buildroot%_libdir/pyrss
install -pm0644 -D pyrss.xml %buildroot%_sysconfdir/pyrss.xml

install -pm0755 -D pyrss.init %buildroot%_initdir/jabber-pyrss
install -pm0755 -D pyrss.adapter %buildroot%_jabber_component_dir/pyrss

%pre
/usr/sbin/groupadd -r -f _pyrss &>/dev/null
/usr/sbin/useradd -r -g _pyrss -d %_var/run/pyrss -s /dev/null \
    -c "XMPP RSS service" -M -n _pyrss &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc AUTHORS README pyrss.sql
%attr(0640,root,_pyrss) %config(noreplace) %_sysconfdir/pyrss.xml
%_initdir/%name
%_libdir/pyrss
%_jabber_component_dir/pyrss
%attr(0770,root,_pyrss) %dir %_logdir/pyrss
%attr(0770,root,_pyrss) %dir %_var/run/pyrss

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9.1-alt1.1
- Rebuild with Python-2.7

* Thu Dec 31 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.9.1-alt1
- Initial build.
