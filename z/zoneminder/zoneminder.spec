%define zmuid $(id -un)
%define zmgid $(id -gn)
%define zmuid_final apache
%define zmgid_final apache

Name: zoneminder
Version: 1.24.4
Release: alt2.2
Summary: A camera monitoring and analysis tool
Group: System/Servers 
License: GPL
Url: http://www.zoneminder.com
Source: ZoneMinder-%version.tar.bz2
Source1: cambozola-%version.tar.bz2
Source2: zoneminder.conf
Source3: redalert.wav
Source4: README.alt
Patch: zm1244.diff
Patch1: zoneminder-alt-libav-0.8.diff
Conflicts: zm <= 1.22.3
Requires: libgnutls libgnutls-openssl zlib perl-Class-Date perl-DateTime perl-Date-Manip perl-libwww ffmpeg perl-X10 perl-Sys-Mmap perl-DBD-mysql perl-Storable MySQL-client php5-mysql su perl-Sys-Mmap webserver
Requires(post): /sbin/chkconfig
Requires(preun): /sbin/chkconfig
Requires(preun): /sbin/service
Requires(postun): /sbin/service
AutoReq: noperl
BuildRequires: bzlib-devel ffmpeg gcc-c++ libavdevice-devel libavformat-devel libgcrypt-devel libgnutls-openssl-devel libjpeg-devel libmysqlclient-devel libpcre-devel libswscale-devel netpbm perl-Archive-Tar perl-Archive-Zip perl-DBD-mysql perl-Date-Manip perl-MIME-Lite perl-MIME-tools perl-Module-Load perl-Sys-Mmap perl-X10 perl-devel perl-libwww zlib-devel

%description
ZoneMinder is a set of applications which is intended to provide a complete
solution allowing you to capture, analyse, record and monitor any cameras you
have attached to a Linux based machine. It is designed to run on kernels which
support the Video For Linux (V4L) interface and has been tested with cameras
attached to BTTV cards, various USB cameras and IP network cameras. It is
designed to support as many cameras as you can attach to your computer without
too much degradation of performance. This package includes cambozola.jar.

%package apache
Summary: Zoneminder configuration file and requires for apache
Group: Networking/WWW
Requires: apache apache-mod_php5 apache-mod_perl
BuildArch: noarch
%description apache
Zoneminder configuration file and requires for apache

%prep
%setup -n ZoneMinder-%version
#%set_gcc_version 4.3
bunzip2 -c %SOURCE1 | tar xf -  cambozola-1.24.4/dist/cambozola.jar
cp %SOURCE4 README.alt

cat <<EOF >> db/zm_create.sql.in
update Config set Value = '/cgi-bin/zm/nph-zms' where Name = 'ZM_PATH_ZMS';
use mysql;
grant select,insert,update,delete on zm.* to 'zmuser'@localhost identified by 'zmpass';
EOF

%patch -p1
%patch1 -p2
%build
autoreconf
OPTS=""

%configure \
	--with-libarch=%_lib \
	--with-mysql=%prefix \
	--with-webdir=%_datadir/%name/www \
	--with-cgidir=%_libexecdir/%name/cgi-bin \
	--with-webuser=%zmuid \
	--with-webgroup=%zmgid \
	--disable-debug \
	--with-ffmpeg=%prefix \
	--enable-mmap CPPFLAGS="-D__STDC_CONSTANT_MACROS" \
	--disable-crashtrace \
	$OPTS
make %{?_smp_mflags}
perl -pi -e 's/(ZM_WEB_USER=).*$/${1}%{zmuid_final}/;' \
    -e 's/(ZM_WEB_GROUP=).*$/${1}%{zmgid_final}/;' zm.conf

%install
install -d %buildroot%_var/run
%make_install install DESTDIR=%buildroot \
	     INSTALLDIRS=vendor
rm -rf %buildroot%prefix/%_lib/perl5/vendor_perl/*.*/*-*
rm -rf %buildroot%prefix/%_lib/perl5/*.*/*-*

install -m 755 -d %buildroot%_var/log/zoneminder
for dir in events images temp
do
	install -m 755 -d %buildroot%_localstatedir/zoneminder/$dir
	rmdir %buildroot%_datadir/%name/www/$dir
	ln -sf ../../../..%_localstatedir/zoneminder/$dir %buildroot%_datadir/%name/www/$dir
done
install -D -m 755 scripts/zm %buildroot%_initdir/zoneminder
install -D -m 644 cambozola-*/dist/cambozola.jar %buildroot%_datadir/%name/www/cambozola.jar
install -D -m 644 %SOURCE2 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/zoneminder.conf
install -D -m 644 zm.conf %buildroot%_sysconfdir/zm.conf
install -D -m 755 %SOURCE3 %buildroot%_datadir/%name/www/sounds/redalert.wav
rm -f %buildroot%perl_vendor_archlib/perllocal.pod
mkdir -p %buildroot%_datadir/%name/db
cp db/*.sql %buildroot%_datadir/%name/db


%post
/sbin/chkconfig --add zoneminder

%post apache
%post_service httpd

%preun apache
%preun_service httpd

%preun
if [ $1 -eq 0 ]; then
	/sbin/service zoneminder stop > /dev/null 2>&1 || :
	/sbin/chkconfig --del zoneminder
fi

%postun
if [ $1 -ge 1 ]; then
	/sbin/service zoneminder condrestart > /dev/null 2>&1 || :
fi

%files
%doc AUTHORS COPYING README README.alt
%config(noreplace) %_sysconfdir/zm.conf
%_initdir/zoneminder
%_bindir/*
%_datadir/%name
%perl_vendorlib/ZoneMinder*
%_libexecdir/%name
%dir %perl_vendor_autolib/ZoneMinder
%dir %attr(755,%zmuid_final,%zmgid_final) %_var/log/zoneminder
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/events
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/images
%dir %attr(755,%zmuid_final,%zmgid_final) %_localstatedir/zoneminder/temp

%files apache
%config(noreplace) %_sysconfdir/httpd/conf/addon-modules.d/zoneminder.conf

%changelog
* Tue Feb 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.24.4-alt2.2
- Fixed build with libav 0.8

* Wed Dec 07 2011 Yuri N. Sedunov <aris@altlinux.org> 1.24.4-alt2.1
- rebuilt against libgnutls-openssl.so.27 (gnutls26-2.12.14)

* Tue Aug 09 2011 Alex Negulescu <alecs@altlinux.org> 1.24.4-alt2
- changed buildreq
- reapplied some 1.24.2 patches (cumulative patch)
  - fixed debian bug #608790, already fixed in 1.24.2-alt2
  - mpeg.cpp patch
  - zm_sdp.cpp un-patch (av_alloc_format_context issue)
  - fixed MySQL 4.x compatibility issue
  - fix incomplete image errors in zmf
- added cambozola 0.92
- initscript complies with Alt policy

* Mon Aug 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.24.4-alt1
- 1.24.4

* Tue Jan 18 2011 Alex Negulescu <alecs@altlinux.org> 1.24.2-alt3
- fixed issues reported by Roman Lesnichenko
  - removed apache from requires, added webserver
  - changed path from /var/lib/lib/zoneminder to /var/lib/zoneminder
  - fixed ffmpeg path
  - removed unnecessary /var/lib/run, /var/lib/log
  - added /var/log/zoneminder to files
  - small changes to init script

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 1.24.2-alt2
- readded to sisyphus
- spec changes & cumulative patch, fixing following issues:
  - Function ereg is deprecated warning
  - Missing progress bar for certain users
  - Marking a monitor from a restricted user
  - Delete group "undefined index" warning
  - Disabling a monitor from monitor options page
  - Unarchive button in events list page
  - Opera, Safari and iPhone MJPEG streaming capability
  - Gapless and All events replay mode
  - strftime() and strtotime() PHP warnings
  - Changing scale when viewing an event kills the stream
  - Incomplete read of frame image data error
  - "`errno' was not declared in this scope" error
  - "V4L2_PIX_FMT_HM12' was not declared in this scope" error
  - "avformat_alloc_context' was not declared in this scope" error
  - "You have an error in your SQL syntax;... 'where Name = 'Monitors'" MySQL 4.x compatibility issue

* Fri Nov 27 2009 Denis Klimov <zver@altlinux.org> 1.24.2-alt1
- new version
- use install patch as git commit
- remove patch for install sql files
- install sql files in spec

* Tue Apr 29 2008 Denis Medvedev <nbr@altlinux.ru> 1.23.3-alt2
- zm init script condstop added

* Tue Apr 29 2008 Denis Medvedev <nbr@altlinux.ru> 1.23.3-alt1
- http://secunia.com/advisories/29995/ and new version

* Tue Dec 25 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt4
- fixed stupid bug with wrong param to url_close

* Tue Nov 06 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt3
- Changed README.alt

* Tue Sep 04 2007 Denis Klimov <zver@altlinux.ru> 1.22.3-alt2
- Add requires: perl-Storable MySQL-client su
- Add subpackage zoneminder-apache
- Add %%config(noreplace) for zm.conf

* Thu Aug 30 2007 Denis Medvedev <nbr@altlinux.ru> 1.22.3-alt1
- Initial build for ALT

* Thu Jul 12 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-7
- Fixes from testing by Jitz including missing dependencies and database creation

* Sat Jun 30 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-6
- Disable crashtrace on ppc

* Sat Jun 30 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-5
- Fix uid for directories in /var/lib/zoneminder

* Tue Jun 26 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-4
- Added perl Archive::Tar dependency
- Disabled web interface due to lack of access control on the event images

* Sun Jun 10 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-3
- Changes recommended in review by Jason Tibbitts

* Mon Apr  2 2007 Martin Ebourne <martin@zepler.org> - 1.22.3-2
- Standardised on package name of zoneminder

* Thu Dec 28 2006 Martin Ebourne <martin@zepler.org> - 1.22.3-1
- First version. Uses some parts from zm-1.20.1 by Corey DeLasaux and Serg Oskin
