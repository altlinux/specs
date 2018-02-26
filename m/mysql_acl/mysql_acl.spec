Name: mysql_acl
Version: 0.1.1
Release: alt3

Summary: Mysql based external acl helper for Squid Proxy

License: GPL
Group: System/Servers

Url: http://onebithq.com/root/squid/mysqlacl
Source: http://onebithq.com/root/download/squid/mysqlacl/%name-%version.tar.gz

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Requires: squid

# Automatically added by buildreq on Wed Aug 22 2007
BuildRequires: libMySQL-devel

%description
mysql_acl - squid helper for use as external acl for get data from mysql
 
%prep
%setup -q

find %_builddir/%name-%version -type f -print0 | xargs -r0 %__subst "s|/usr/local/squid/etc|/etc/squid|g"
find %_builddir/%name-%version -type f -print0 | xargs -r0 %__subst "s|/usr/local|/usr|g"
find %_builddir/%name-%version -type f -print0 | xargs -r0 %__subst "s|/usr/lib|%_libdir|g"

%build
%make_build

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_sysconfdir/squid
%__mkdir_p %buildroot%_man5dir
%__mkdir_p %buildroot%_man8dir

%__install -p -m 755 mysql_acl %buildroot%_bindir/
%__install -p -m 640 mysql_acl.conf %buildroot%_sysconfdir/squid/
%__install -p mysql_acl.conf.5 %buildroot%_man5dir
%__install -p mysql_acl.8 %buildroot%_man8dir


%files
%doc COPYING-2.0
%_bindir/*
%config(noreplace) %attr(640,root,squid) %verify(not md5 size mtime) %_sysconfdir/squid/mysql_acl.conf
%_man5dir/*
%_man8dir/*

%changelog
* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.1-alt3
- Rebuild with new MySQL

* Tue Jul 20 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.1-alt2
- Remove packages-info-i18n-common from BuildRequires

* Wed Aug 22 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1.1-alt1
- New version
  + Fix memory leak

* Thu Aug 09 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.1-alt1
- initial build

