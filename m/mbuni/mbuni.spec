%set_automake_version 1.9
Name: mbuni
Version: 1.4.0
Release: alt7
Summary: Open Source MMS Gateway

Group: System/Servers
License: GPL
Url: http://www.mbuni.org/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Mon Mar 21 2011 (-bb)
BuildRequires: glibc-devel-static kannel-devel libmysqlclient-devel libpam-devel libpcre-devel libsqlite3-devel libssl-devel libxml2-devel postgresql-devel zlib-devel

%description
Open Source MMS Gateway

%prep
%setup

%build
./bootstrap
%configure \
	--enable-ssl \
	--enable-largefile \
	--enable-shared \
	--enable-dependency-tracking

%make_build

%install
mkdir -p %buildroot%_sysconfdir/mbuni
mkdir -p %buildroot%_logdir/mbuni
mkdir -p %buildroot%_runtimedir/mbuni
%makeinstall

%pre
%_sbindir/groupadd mbuni ||:
%_sbindir/useradd -r -d /dev/null -s /dev/null -g mbuni -n mbuni \
  2> /dev/null > /dev/null ||:

%files
%_bindir/*
%attr(0770,root,mbuni) %dir %_sysconfdir/mbuni
%attr(0770,mbuni,mbuni) %dir %_logdir/mbuni
%attr(0770,mbuni,mbuni) %dir %_runtimedir/mbuni
%_libdir/libmms_pgsql_queue.a
%_libdir/libmms_pgsql_queue.so
%_libdir/libmms_pgsql_queue.so.0
%_libdir/libmms_pgsql_queue.so.0.0.0
%doc doc AUTHORS ChangeLog

%changelog
* Mon Mar 21 2011 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt7
- fix build 

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt6
- rebuild with new openssl

* Sun Sep 19 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt5
- rebuild with new libmysqlclient

* Sat Apr 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt4
- fix build on i586

* Sat Apr 17 2010 Denis Smirnov <mithraen@altlinux.ru> 1.4.0-alt3
- fix build on Sisyphus

* Sun Aug 02 2009 Michael Bochkaryov <misha@altlinux.ru> 1.4.0-alt2
- Create user and group for mbuni MMSC
- Create catalogs for logs and PID files

* Mon Jul 27 2009 Michael Bochkaryov <misha@altlinux.ru> 1.4.0-alt1
- 1.4.0 version build

* Tue Jun 30 2009 Michael Bochkaryov <misha@altlinux.ru> 1.3.0-alt1.cvs20071221
- Initial build for ALT Linux
