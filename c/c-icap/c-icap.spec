Name: c-icap
Version: 20080706.01
Release: alt2.2
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: ICAP server
License: GPL
Group: System/Servers
Url: http://c-icap.sourceforge.net/

Source0: %name-%version.tar.gz
Source1: %name.init
Patch: %name-20080706-alt.patch

# Automatically added by buildreq on Thu Apr 09 2009
BuildRequires: gcc4.4-c++ libadns-devel libclamav-devel libmemcache-devel opendbx-devel zlib-devel

Requires(pre): shadow-utils

%description
Implementation of an Internet Content Adaptation Protocol (ICAP) server.

%package devel
Summary: ICAP development files
Group: Development/C
Requires: %name = %version-%release

%description devel
Headers and libraries for an Internet Content Adaptation Protocol (ICAP) 
server implementation.

%package clamav
Summary: ICAP ClamAV module
Group: System/Servers
Requires: %name = %version-%release

%description clamav
ICAP module for scanning content with ClamAV.

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
autoheader
cp /usr/share/libtool-2.2/config/ltmain.sh ltmain.sh
automake --add-missing --copy
cp INSTALL INSTALL.txt

%undefine __libtoolize
%configure
%make_build --debug -j

%install
%make_install DESTDIR=%buildroot install

install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/%name %buildroot%_sbindir/%name

mkdir -p %buildroot%_logdir/%name
touch %buildroot%_logdir/%name/{server,access}.log

mkdir -p %buildroot{%_var/run/%name,%_cachedir/%name}

%pre
/usr/sbin/groupadd -r -f _c_icap ||:
/usr/sbin/useradd -M -n _c_icap -r -d /dev/null -s /dev/null -c "system user for %name" -g _c_icap > /dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%post clamav
/sbin/service %name condrestart ||:

%preun clamav
/sbin/service %name condrestart ||:

%files
%doc AUTHORS README INSTALL.txt TODO contrib/get_file.pl
%config(noreplace) %_sysconfdir/%name.conf*
%config(noreplace) %_sysconfdir/%name.magic*
%attr (755,root,root) %_initdir/%name
%_bindir/*
%attr (755,root,root) %_sbindir/%name
%dir %_libdir/%name/
%exclude %_libdir/%name/srv_clamav.so
%_libdir/%name/*.so
%_libdir/libicapapi.so.*
%dir %attr (750,_c_icap,root) %_logdir/%name/
%ghost %_logdir/%name/*.log
%dir %attr (750,_c_icap,root) %_var/run/%name/
%dir %attr (750,_c_icap,root) %_cachedir/%name/

%files devel
%_includedir/%name
%_libdir/libicapapi.so

%files clamav
%_libdir/%name/srv_clamav.so

%changelog
* Mon Apr 05 2010 Anton Pischulin <letanton@altlinux.ru> 20080706.01-alt2.2
- Fix base64.c

* Fri Feb 26 2010 Andrey Cherepanov <cas@altlinux.org> 20080706-alt0.1.M50P.1
- backport to p5

* Wed Nov 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 20080706-alt1.1
- build for sisyphus

* Mon Sep 28 2009 Grigory Batalov <bga@altlinux.ru> 20080706-alt2.M40.1
- New upstream release (c_icap-20080706).
- Updated url_filter.

* Wed Apr 15 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.2
- Pre-requirement of shadow-utils were added.
- Url-filter provides c-icap-skf.

* Thu Apr 09 2009 Grigory Batalov <bga@altlinux.ru> 20060603-alt1.M40.1
- Rebuilt with custom url_filter.
- Built for ALT Linux branch 4.0.

* Thu Mar 22 2007 ALT QA Team Robot <qa-robot@altlinux.org> 20060603-alt1.0
- Rebuilt with libclamav.so.2.

* Wed Jan 17 2007 Grigory Batalov <bga@altlinux.ru> 20060603-alt1
- Initial ALTLinux release.
