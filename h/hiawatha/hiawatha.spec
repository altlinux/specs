Name: hiawatha
Version: 7.8.2
Release: alt1

Summary: A secure and advanced webserver
License: GPLv2+
Group: System/Servers

Url: http://www.hiawatha-webserver.org/
Source: http://www.hiawatha-webserver.org/files/hiawatha-%version.tar.gz
Source1: hiawatha.init
Source2: hiawatha.logrotate
Patch1: hiawatha-6.12-nobody99.patch

# Automatically added by buildreq on Mon Mar 28 2011
BuildRequires: libssl-devel libxslt-devel zlib-devel

%description
Hiawatha is an advanced and secure Web server for Unix. It has been written with
security as its main goal. It's very secure and fast and is really easy to
configure. It features a rootjail, the ability to run CGIs under any UID/GID you
want, prevention of SQL injection and cross-site scripting, banning of clients
who try such exploits, and many other features. These features make Hiawatha an
interesting Web server for those who need more security than what the other
available Web servers are offering.

%prep
%setup
%patch1 -p1

%build
%configure --localstatedir=/var --enable-xslt
%make_build

%install
%makeinstall_std
install -d %buildroot%_logdir/hiawatha
install -pDm 755 %_sourcedir/hiawatha.init %buildroot%_initrddir/hiawatha
install -pDm 644 %_sourcedir/hiawatha.logrotate %buildroot/etc/logrotate.d/hiawatha

%post
%post_service hiawatha

%preun
%preun_service hiawatha

%files
%dir %_sysconfdir/hiawatha
%config(noreplace) %_sysconfdir/hiawatha/*
%config(noreplace) %_initrddir/hiawatha
%config(noreplace) /etc/logrotate.d/hiawatha
%dir /var/www/hiawatha
%config(noreplace) /var/www/hiawatha/*
%_bindir/*
%_sbindir/*
%_man1dir/*
%_logdir/hiawatha

%changelog
* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 7.8.2-alt1
- 7.8.2

* Wed Aug 31 2011 Victor Forsiuk <force@altlinux.org> 7.6-alt1
- 7.6

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 7.5-alt1
- 7.5

* Sat Apr 09 2011 Victor Forsiuk <force@altlinux.org> 7.4.1-alt1
- 7.4.1

* Mon Mar 28 2011 Victor Forsiuk <force@altlinux.org> 7.4-alt2
- Fix BuildRequires.

* Mon Nov 15 2010 Victor Forsiuk <force@altlinux.org> 7.4-alt1
- 7.4

* Thu Jun 17 2010 Victor Forsiuk <force@altlinux.org> 7.3-alt1
- 7.3

* Tue Mar 30 2010 Victor Forsiuk <force@altlinux.org> 7.1-alt1
- 7.1

* Mon Feb 15 2010 Victor Forsiuk <force@altlinux.org> 7.0-alt1
- 7.0

* Mon Dec 07 2009 Victor Forsyuk <force@altlinux.org> 6.19-alt1
- 6.19

* Wed Nov 25 2009 Victor Forsyuk <force@altlinux.org> 6.18-alt2
- Add condstop target to init-script.

* Mon Nov 16 2009 Victor Forsyuk <force@altlinux.org> 6.18-alt1
- Initial build.
