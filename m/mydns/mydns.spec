Name: mydns
Version: 1.2.8.31
Release: alt2
License: GPL
Summary: A MySQL-based Internet DNS server
Group: System/Servers
Url: http://www.mydns-ng.com
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source: %name-%version.tar
Source1: %name.alt

# Automatically added by buildreq on Sat Jul 05 2008
BuildRequires: cvs libMySQL-devel libssl-devel-static zlib-devel texlive-latex-recommended

%define webadminroot /var/www/html/admin
%define admin 0

%description
MyDNS is a free DNS server for UNIX implemented from scratch and
designed to utilize the MySQL database for data storage.

Its primary objectives are stability, security, interoperability,
and speed, though not necessarily in that order.

MyDNS does not include recursive name service, nor a resolver
library. It is primarily designed for organizations with many
zones and/or resource records who desire the ability to perform
real-time dynamic updates on their DNS data via MySQL.

MyDNS starts and is ready to answer questions immediately, no
matter how much DNS data you have in the database. It is extremely
fast and memory-efficient. It includes complete documentation,
including a manual and a FAQ. It supports a few frills, including
round robin DNS, dynamic load balancing, and outgoing AXFR for
non-MyDNS nameservers.

%if %admin
%package admin
Summary: Web admin GUI written in php for %name
Group: System/Servers
Requires: webserver mod_php php-common php-mysql
Requires: %name = %version

%description admin
This package contains a web admin GUI written in php for %name
%endif

%prep
%setup

%build
%autoreconf
%configure \
    --with-openssl \
    --with-openssl-lib=%_libdir \
    --with-mysql \
    --with-mysql-lib=%_libdir \
    --with-zlib=%_libdir \
    --without-pgsql

# use "--without-pgsql" until people complain about it ;)

%make_build

# build the pdf
pushd doc
    make pdf
popd

%install
# don't fiddle with the initscript!
export DONT_GPRINTIFY=1

%makeinstall_std

%__install -d %buildroot%_initdir
%__install -d %buildroot/var/run/%name
%__install -m640 %name.conf %buildroot%_sysconfdir/%name.conf

# install sysv script
%__install -m0755 %SOURCE1 %buildroot%_initdir/%name

%if %admin
%__install -d %buildroot%webadminroot/%name
%__install -m644 contrib/admin.php %buildroot%webadminroot/%name/index.php
%__install -m644 contrib/stats.php %buildroot%webadminroot/%name/
%endif

%find_lang %name

%pre
/usr/sbin/groupadd -r -f %name &> /dev/null ||:
/usr/sbin/useradd -r -g %name -d /dev/null -c 'Mydns name server' -s /bin/false -n %name &> /dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files -f %name.lang
%doc AUTHORS BUGS ChangeLog NEWS QUICKSTART* README* TODO doc/*.pdf
%doc contrib/README.alias
%config(noreplace) %attr(0640,root,mydns) %_sysconfdir/%name.conf
%_initdir/%name
%_bindir/*
%_sbindir/*
%_mandir/man?/*
%_infodir/*
%dir %attr(0755,%name,%name) /var/run/%name

%if %admin
%files admin
%doc contrib/README
%dir %webadminroot/%name
%config(noreplace) %attr(0644,root,root) %webadminroot/%name/index.php
%attr(0644,root,root) %webadminroot/%name/stats.php
%endif

%changelog
* Tue Apr 24 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8.31-alt2
- Fix build

* Sat Feb 05 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8.31-alt1
- New version
- Remove -devel subpackage
- Spec update

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8.27-alt2
- Rebuild with new MySQL

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.2.8.27-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for mydns
  * postclean-05-filetriggers for spec file

* Mon Apr 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8.27-alt1
- New version
- Switch to git

* Tue Aug 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8.4-alt1
- New version

* Sat Jul 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8-alt2.pre9
- Fix build for x86_64

* Sat Jul 05 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.2.8-alt1.pre9
- New version

* Fri Jun 13 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0-alt2
- Fix start priority to start after mysql

* Sat Feb 23 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0-alt1
- Build for ALT
