Name: ganglia
Version: 3.1.7
Release: alt1

License: BSD
Summary: Ganglia Distributed Monitoring System
Group: Monitoring
URL: http://ganglia.info/

Source: %name-%version.tar
Source100: gmond.init
Source101: gmetad.init


# Automatically added by buildreq on Tue Aug 07 2007
BuildRequires: gcc-c++ glibc-devel-static libapr1-devel libconfuse-devel libexpat-devel librrd-devel
BuildRequires: libpcre-devel perl-podlators 

Packager: Stanislav Ievlev <inger@altlinux.org>

%description
Ganglia is a scalable, real-time monitoring and execution environment

%package web
Summary: Ganglia Web Frontend
Group: System/Base
Obsoletes: ganglia-webfrontend
Provides: ganglia-webfrontend
Requires: rrd-utils apache2-mod_php5

%description web
This package provides a web frontend to display the XML tree published by
ganglia, and to provide historical graphs of collected metrics. This website is
written in the PHP4 language.


%package gmetad
Summary: Ganglia Meta daemon http://ganglia.sourceforge.net/
Group: Monitoring
Requires(pre): shadow-utils
Requires(post,preun): service

%description gmetad
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmetad daemon aggregates monitoring data from several clusters
to form a monitoring grid. It also keeps metric history using rrdtool.

%package gmond
Summary: Ganglia Monitor daemon http://ganglia.sourceforge.net/
Group: Monitoring
Requires(pre): shadow-utils
Requires(post,preun): service

%description gmond
Ganglia is a scalable, real-time monitoring and execution environment
with all execution requests and statistics expressed in an open
well-defined XML format.

This gmond daemon provides the ganglia service within a single cluster or
Multicast domain.

%package -n lib%name
Summary: Ganglia Library http://ganglia.sourceforge.net/
Group: System/Libraries

%description -n lib%name
Ganglia library - development part

%package -n lib%name-devel
Summary: Ganglia Library http://ganglia.sourceforge.net/
Group: Development/C

%description -n lib%name-devel
The Ganglia Monitoring Core library provides a set of functions that programmers
can use to build scalable cluster or grid applications
Ganglia library

%prep 
%setup -q -n %name-%version

#__subst 's,nobody,_gmond,' gmond/g25_config.c  lib/libgmond.c
%__subst 's,nobody,_gmetad,' gmetad/conf.c.in  gmetad/gmetad.conf.in

%build

%autoreconf
%configure --with-gmetad --enable-setuid=_gmond
%make_build

cd gmond
    rm gmond.conf.5
    make gmond.conf.5
cd -


%install

%makeinstall

%__install -d  %buildroot/%_sysconfdir
%__install -d  %buildroot/{%_man1dir,%_man5dir}

cp -p mans/*.1 %buildroot/%_man1dir
gmond/gmond -t >%buildroot/%_sysconfdir/gmond.conf
%__install -Dpm 644 gmetad/gmetad.conf %buildroot/%_sysconfdir/gmetad.conf
%__cp -f gmond/gmond.conf.5 %buildroot/%_man5dir/gmond.conf.5

%__install -Dpm 755 %SOURCE100 %buildroot/%_initdir/gmond
%__install -Dpm 755 %SOURCE101 %buildroot/%_initdir/gmetad
%__install -d %buildroot/%_localstatedir/%name/rrds

%__install -d %buildroot%_var/www/apache2/html/%name
cp -a web/* %buildroot%_var/www/apache2/html/%name

%pre gmetad
/usr/sbin/groupadd -r -f _gmetad
/usr/sbin/useradd -r -g _gmetad -d /dev/null -s /dev/null -n _gmetad >/dev/null 2>&1 ||:


%pre gmond
/usr/sbin/groupadd -r -f _gmond
/usr/sbin/useradd -r -g _gmond -d /dev/null -s /dev/null -n _gmond >/dev/null 2>&1 ||:


%post gmetad
%post_service gmetad

%preun gmetad
%preun_service gmetad


%post gmond
%post_service gmond

%preun gmond
%preun_service gmond

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_bindir/ganglia-config


%files gmetad
%config(noreplace) /etc/gmetad.conf
%_initdir/gmetad
%_sbindir/gmetad
%_man1dir/gmetad*
%attr(0755,_gmetad,_gmetad)%_localstatedir/%name/rrds

%files gmond
%config(noreplace) %_sysconfdir/gmond.conf
%_initdir/gmond
%_bindir/gmetric
%_bindir/gstat
%_sbindir/gmond
%_libdir/ganglia/*.so
%_man5dir/gmond*
%_man1dir/gmond*
%_man1dir/gstat*
%_man1dir/gmetric*

%files web
%_var/www/apache2/html/%name

%changelog
* Sun Nov 21 2010 Denis Pynkin <dans@altlinux.ru> 3.1.7-alt1
- new version
- fixed autoreconf macro
- fixed gmetad user
- added BuildRequires

* Tue Apr 27 2010 Sergey Y. Afonin <asy@altlinux.ru> 3.1.1-alt2.1
- rebuild with rrd 1.4.3

* Mon Dec 01 2008 Denis Klimov <zver@altlinux.ru> 3.1.1-alt1
- new version
- remove patch of previos version
- add modules files to gmond subpackage

* Tue Sep 11 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.4-alt2
- fix prereq

* Tue Aug 07 2007 Stanislav Ievlev <inger@altlinux.org> 3.0.4-alt1
- Initial release
