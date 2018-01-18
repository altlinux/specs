%define _libexecdir %_prefix/libexec

Name: collection4
Version: 4.0.0
Release: alt2.git20130220

Summary: Web-based front-end to the RRD files updated by collectd

License: LGPL
Group: Monitoring
Url: http://octo.it/c4/
Source0: %name-%version.tar

Source1: collection4-apache.conf

Patch0: collection4-conf.diff
Patch1: collection4-pkglibexec.patch
Patch2: collection4-rrd.patch

# Automatically added by buildreq on Tue Jul 24 2012
# optimized out: fontconfig pkg-config
BuildRequires: flex libcollectdclient-devel libfcgi-devel librrd-devel libyajl1-devel

%description
collection 4 (c4) is a web-based front-end to the RRD files updated
by collectd. It is designed to be highly efficient and handle large
installations - with 50,000 and more RRD files - well.

%package apache2
Summary: apache2 stuff for collection 4
Group: Monitoring
BuildArch: noarch

%description apache2
apache2 stuff for collection 4

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

mv share/collection.conf share/collection4.conf

%build
%autoreconf
%configure LIBS="-lm" --libexecdir=%_libexecdir
%make_build

%install
%makeinstall

mkdir -p %buildroot%_sysconfdir/httpd2/conf/sites-available
sed -e 's|@@LIBEXECDIR@@|%_libexecdir|' < %SOURCE1 > %buildroot%_sysconfdir/httpd2/conf/sites-available/c4.conf

%post

%postun

%files
%config(noreplace) %_sysconfdir/collection4.conf
%dir %_libexecdir/collection
%_libexecdir/collection/collection.fcgi
%dir %_datadir/collection
%_datadir/collection/*.js
%_datadir/collection/*.css

%files apache2
%config(noreplace) %_sysconfdir/httpd2/conf/sites-available/c4.conf

%changelog
* Thu Jan 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt2.git20130220
- Fixed build with new librrd.

* Tue Jun 04 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.0.0-alt1.git20130220
- added -lm to LIBS
- moved collection/collection.fcgi to /usr/libexec
- added %config(noreplace) for Apache 2 config

* Tue Jun 04 2013 Sergey Y. Afonin <asy@altlinux.ru> 4.0.0-alt0.git20130220
- initial spec file
