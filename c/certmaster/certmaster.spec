Summary: Remote certificate distribution framework
Name: certmaster
Version: 0.28
Release: alt2
Source0: %name-%version.tar
License: GPLv2+
Group: System/Configuration/Other

BuildArch: noarch
Url: https://fedorahosted.org/certmaster

BuildRequires: python-module-setuptools perl-podlators

%description
certmaster is a easy mechanism for distributing SSL certificates

%package sync
Summary: certmaster-sync -- synchronize client certificates with Func
Group: Development/C
Requires: %name = %version-%release

%description sync
certmaster-sync synchronizes client certificates amongst certmaster
clients via Func.  It is assumed that the hosts who have requested
certificates are reachable via Func for synchronization operations.

%prep
%setup -q

%build
%make manpage
%__python setup.py build

%install
%__python setup.py install --prefix=/usr --root=%buildroot
ln -s %_bindir/certmaster-sync %buildroot/var/lib/certmaster/triggers/sign/post/certmaster-sync
ln -s %_bindir/certmaster-sync %buildroot/var/lib/certmaster/triggers/remove/post/certmaster-sync
touch %buildroot/var/log/certmaster/certmaster.log
touch %buildroot/var/log/certmaster/audit.log

install -pD -m 755 init-scripts/certmaster.alt  %buildroot%_initrddir/certmaster

%post
%post_service %name

%preun
%preun_service %name

%files
%python_sitelibdir/*
%_bindir/*
%_initrddir/*
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/minion-acl.d/
%dir %_sysconfdir/pki/%name
%config(noreplace) /etc/certmaster/minion.conf
%config(noreplace) /etc/certmaster/certmaster.conf
%config(noreplace) /etc/logrotate.d/certmaster_rotate
%config /etc/certmaster/version

%dir /var/log/certmaster
%attr(0600,root,root)  %config(noreplace) %verify(not md5 size mtime) /var/log/certmaster/certmaster.log
%attr(0600,root,root)  %config(noreplace) %verify(not md5 size mtime) /var/log/certmaster/audit.log

%attr(700,root,root) %dir /var/lib/certmaster
%attr(700,root,root) %dir /var/lib/certmaster/certmaster
%attr(700,root,root) %dir /var/lib/certmaster/certmaster/certs
%attr(700,root,root) %dir /var/lib/certmaster/certmaster/csrs
%dir /var/lib/certmaster/peers
%dir /var/lib/certmaster/triggers
%dir /var/lib/certmaster/triggers/sign/
%dir /var/lib/certmaster/triggers/sign/pre
%dir /var/lib/certmaster/triggers/sign/post
%dir /var/lib/certmaster/triggers/request/
%dir /var/lib/certmaster/triggers/request/pre
%dir /var/lib/certmaster/triggers/request/post
%dir /var/lib/certmaster/triggers/remove/
%dir /var/lib/certmaster/triggers/remove/pre
%dir /var/lib/certmaster/triggers/remove/post
%doc AUTHORS README LICENSE
%_mandir/man1/*

%exclude %_bindir/certmaster-sync
%exclude %_mandir/man1/certmaster-sync.*

%files sync
%_bindir/certmaster-sync
%_mandir/man1/certmaster-sync.*
/var/lib/certmaster/triggers/sign/post/certmaster-sync
/var/lib/certmaster/triggers/remove/post/certmaster-sync


%changelog
* Thu Jan 03 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.28-alt2
- Add subpackage certmaster-sync

* Mon Nov 12 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.28-alt1
- New version

* Sun Feb 20 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.27-alt1
- Build for ALT
