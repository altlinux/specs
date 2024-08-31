%define zm_builddir %{?_cmake__builddir:%_cmake__builddir}%{!?_cmake__builddir:BUILD}

%define zmuser apache2
%define zmgroup _webserver
%define phpver 8.1
ExcludeArch: armh

Name: zoneminder
Version: 1.36.34
Release: alt2
Summary: A camera monitoring and analysis tool
Group: System/Servers 
License: GPLv2
# VCS: https://github.com/ZoneMinder/ZoneMinder.git
Url: http://www.zoneminder.com
Source: %name-%version-alt.tar
Source4: zoneminder.conf
Source5: README.alt
Source6: README-nginx-ru.alt
Source7: nginx-zoneminder.conf.sample
Source8: zm-fcgi.inc.in
Source9: php-fpm-zoneminder.conf.in

Source100: %name-%version-dep-RtspServer.tar
Source101: %name-%version-web-api-app-Plugin-CakePHP-Enum-Behavior.tar
Source102: %name-%version-web-api-app-Plugin-Crud.tar


Conflicts: zm <= 1.22.3
BuildRequires(pre): rpm-macros-webserver-common
Requires: libgnutls libgnutls-openssl zlib ffmpeg
Requires: php%phpver-pdo_mysql php%phpver-openssl php%phpver-gd php%phpver-apcu php%phpver-intl
Requires: su
Requires: perl-Data-Entropy perl-Crypt-Eksblowfish perl-Sys-Mmap webserver perl-Pod-Usage 
Requires: perl-Sys-MemInfo perl-Number-Bytes-Human perl-JSON-MaybeXS perl-Sys-CPU 
Requires: perl-SOAP-WSDL perl-Class-Std-Fast perl-Data-UUID perl-IO-Socket-Multicast 
Requires: perl-Digest-SHA perl-Class-Date perl-DateTime perl-Date-Manip perl-libwww
Requires: perl-X10 perl-Sys-Mmap perl-DBD-mysql perl-Storable
AutoReq: noperl
BuildRequires: bzlib-devel ffmpeg gcc-c++ libswresample-devel libavdevice-devel libavformat-devel libgcrypt-devel libgnutls-openssl-devel libjpeg-devel libmysqlclient-devel libpcre-devel libswscale-devel netpbm perl-Archive-Tar perl-Archive-Zip perl-DBD-mysql perl-Date-Manip perl-MIME-Lite perl-MIME-tools perl-Module-Load perl-Sys-Mmap perl-X10 perl-devel perl-libwww zlib-devel libpolkit-devel cmake libv4l-devel rpm-macros-cmake libvlc-devel libcurl-devel libssl-devel libsystemd-devel libffi-devel libx264-devel libmount-devel libuuid-devel libselinux-devel libblkid-devel libmp4v2

%description
ZoneMinder is a set of applications which is intended to provide a complete
solution allowing you to capture, analyse, record and monitor any cameras you
have attached to a Linux based machine. It is designed to run on kernels which
support the Video For Linux (V4L) interface and has been tested with cameras
attached to BTTV cards, various USB cameras and IP network cameras. It is
designed to support as many cameras as you can attach to your computer without
too much degradation of performance. This package includes cambozola.jar.

%package api
Summary: Zoneminder Web API
Group: Networking/WWW
Requires: zoneminder php%phpver-apcu

%description api
The API is built in CakePHP and lives under the /api directory. It provides a RESTful service 
and supports CRUD (create, retrieve, update, delete) functions for Monitors, Events, Frames, 
Zones and Config.

%package nginx
Summary: Zoneminder configuration file and requires for nginx
Group: Networking/WWW
Requires: php8.1-fpm-fcgi fcgiwrap nginx
BuildArch: noarch
%description nginx
Zoneminder configuration file and requires for nginx

%prep
%setup -n %name-%version-alt -a100 -a101 -a102

cp %SOURCE5 README.alt
cp %SOURCE6 README-nginx-ru.alt

cat <<EOF >> db/zm_create.sql.in
use mysql;
CREATE user 'zmuser'@localhost identified by 'zmpass';
grant select,insert,update,delete on zm.* to 'zmuser'@localhost;
EOF

./utils/zmeditconfigdata.sh ZM_OPT_CAMBOZOLA yes
./utils/zmeditconfigdata.sh ZM_OPT_CONTROL yes
./utils/zmeditconfigdata.sh ZM_CHECK_FOR_UPDATES no
./utils/zmeditconfigdata.sh ZM_DYN_SHOW_DONATE_REMINDER no
./utils/zmeditconfigdata.sh ZM_OPT_FAST_DELETE no

%ifarch %e2k
# unsupported as of lcc 1.25.15
sed -i 's,-Wconditionally-supported,,' cmake/compiler/gcc/settings.cmake
sed -i "s/srcN\[\]/srcN[0]/" src/zm_rtp_ctrl.h
%endif

%build
%cmake -DZM_TARGET_DISTRO="alt" -DPCRE_INCLUDE_DIR=/usr/include/pcre -DZM_SYSTEMD=ON -DZM_WEB_USER=%{zmuser} -DZM_WEB_GROUP=%{zmgroup}

%cmake_build

%install
install -d %buildroot%_var/run
%cmakeinstall_std
rm -rf %buildroot%prefix/%_lib/perl5/vendor_perl/*.*/*-*
rm -rf %buildroot%prefix/%_lib/perl5/*.*/*-*


install -m 755 -d %buildroot%_var/log/zoneminder
for dir in events images temp
do
	install -m 755 -d %buildroot%_localstatedir/zoneminder/$dir
done
install -D -m 755 %zm_builddir/scripts/zm %buildroot%_initdir/zoneminder
install -D -m 644 %zm_builddir/misc/zoneminder.service %buildroot/%_unitdir/%name.service
install -D -m 644 %zm_builddir/misc/zoneminder-tmpfiles.conf %buildroot/%_tmpfilesdir/zoneminder.conf
install -D -m 644 %SOURCE4 %buildroot%_sysconfdir/httpd/conf/addon-modules.d/zoneminder.conf
install -D -m 644 %SOURCE7 %buildroot%_sysconfdir/nginx/sites-enabled.d/nginx-zoneminder.conf.sample
install -D -m 644 %SOURCE8 %buildroot%_sysconfdir/nginx/sites-enabled.d/zm-fcgi.inc
sed -si 's,@phpver@,%phpver,g' %buildroot%_sysconfdir/nginx/sites-enabled.d/zm-fcgi.inc
install -D -m 644 %SOURCE9 %buildroot%_sysconfdir/fpm%phpver/php-fpm.d/fpm-zm.conf
sed -si 's,@phpver@,%phpver,g' %buildroot%_sysconfdir/fpm%phpver/php-fpm.d/fpm-zm.conf
mkdir -p %buildroot/%_cachedir/%name

ln -s ../../../../..%_cachedir/%name %buildroot%_datadir/%name/www/cache


rm -f %buildroot%perl_vendor_archlib/perllocal.pod
mkdir -p %buildroot%_datadir/%name/db
cp db/*.sql %buildroot%_datadir/%name/db

%pre
%_sbindir/groupadd -r -f %zmgroup 2>/dev/null ||:
%_sbindir/useradd -g %zmgroup -c 'WWW server' -d %webserver_datadir -s '/dev/null' \
        -G %webserver_group -r %zmuser 2>/dev/null || :

%post
%post_service zoneminder

%preun
%preun_service zoneminder

%files
%doc COPYING README.md README.alt
%config(noreplace) %_sysconfdir/zm/zm.conf
%config(noreplace) %_sysconfdir/zm/conf.d/*.conf
%ghost %_cachedir/%name
%_sysconfdir/zm/conf.d/README
%_tmpfilesdir/zoneminder.conf
%_unitdir/%name.service
%_initdir/zoneminder
%_bindir/*
%_datadir/%name
%_man8dir/zm*
%perl_vendorlib/ZoneMinder*
%perl_vendorlib/ONVIF*
%perl_vendorlib/WSDiscovery*
%perl_vendorlib/WSSecurity*
%perl_vendorlib/WSNotification*

%_libexecdir/%name
%dir %attr(755,%zmuser,%zmgroup) %_var/log/zoneminder
%dir %attr(755,%zmuser,%zmgroup) %_localstatedir/zoneminder
%dir %attr(755,%zmuser,%zmgroup) %_localstatedir/zoneminder/events
%dir %attr(755,%zmuser,%zmgroup) %_localstatedir/zoneminder/images
%dir %attr(755,%zmuser,%zmgroup) %_localstatedir/zoneminder/temp
%_datadir/polkit-1/*/*
%exclude %_datadir/%name/www/api


%files nginx
%doc README-nginx-ru.alt
%config(noreplace) %_sysconfdir/nginx/sites-enabled.d/*
%config(noreplace) %_sysconfdir/fpm%phpver/php-fpm.d/*

%files api
%_datadir/%name/www/api

%changelog
* Thu Aug 29 2024 Anton Farygin <rider@altlinux.ru> 1.36.34-alt2
- removed 3gp format from output video generation
  due to limitations in supported sizes list (closes: #46708)

* Thu Aug 22 2024 Anton Farygin <rider@altlinux.ru> 1.36.34-alt1
- 1.36.33 -> 1.36.34 (fixes: CVE-2024-43360)

* Wed Sep 06 2023 Anton Farygin <rider@altlinux.ru> 1.36.33-alt2
- removed unnecessary BuildRequires libavresample

* Fri Jun 09 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.36.33-alt1.1
- fixed build for Elbrus

* Sun Jun 04 2023 Anton Farygin <rider@altlinux.ru> 1.36.33-alt1
- 1.36.33

* Mon Nov 28 2022 Anton Farygin <rider@altlinux.ru> 1.36.32-alt2
- 1.36.31 -> 1.36.32

* Sat Nov 12 2022 Anton Farygin <rider@altlinux.ru> 1.36.31-alt2
- migrated to php8.1 by default
- fixed socket path in zm-fcgi.inc (closes: #44190)
- updated initial sql agains MySQL-8
- added php8.1-intl to requires

* Tue Nov 01 2022 Anton Farygin <rider@altlinux.ru> 1.36.31-alt1
- 1.36.29 -> 1.36.31

* Mon Oct 17 2022 Anton Farygin <rider@altlinux.ru> 1.36.29-alt1
- 1.36.26 -> 1.36.29

* Tue Oct 04 2022 Anton Farygin <rider@altlinux.ru> 1.36.26-alt1
- 1.36.25 -> 1.36.26

* Wed Sep 07 2022 Anton Farygin <rider@altlinux.ru> 1.36.25-alt1
- 1.36.12 -> 1.36.25 (Fixes: CVE-2022-29806)

* Mon Dec 27 2021 Michael Shigorin <mike@altlinux.org> 1.36.12-alt2
- E2K: avoid lcc-unsupported option

* Mon Dec 20 2021 Anton Farygin <rider@altlinux.ru> 1.36.12-alt1
- 1.36.12

* Thu Dec 09 2021 Anton Farygin <rider@altlinux.ru> 1.36.11-alt2
- api: don't install twice
- api: add php7-apcu to Requires

* Sun Nov 28 2021 Anton Farygin <rider@altlinux.ru> 1.36.11-alt1
- 1.36.10 -> 1.36.11

* Sun Nov 07 2021 Anton Farygin <rider@altlinux.ru> 1.36.10-alt1
- 1.36.10

* Sun Oct 10 2021 Anton Farygin <rider@altlinux.ru> 1.36.8-alt1
- 1.36.8

* Fri Sep 10 2021 Anton Farygin <rider@altlinux.ru> 1.36.6-alt1
- 1.36.6
- added php7-apcu to Requires (closes: #39340)
- exclude the armh architecture due to build errors

* Thu Jul 08 2021 Anton Farygin <rider@altlinux.ru> 1.36.5-alt1
- 1.36.5

* Tue Jun 22 2021 Anton Farygin <rider@altlinux.ru> 1.36.4-alt1
- 1.36.4

* Mon May 31 2021 Anton Farygin <rider@altlinux.ru> 1.36.3-alt2
- removed include to upstream patch with MySQL-8 support
- used cmakeinstall_std for compatability with old ALT repositories

* Mon May 31 2021 Anton Farygin <rider@altlinux.ru> 1.36.3-alt1
- 1.36.3

* Sun May 30 2021 Arseny Maslennikov <arseny@altlinux.org> 1.36.1-alt1.1
- NMU: spec: adapted to new cmake macros.

* Tue May 25 2021 Anton Farygin <rider@altlinux.ru> 1.36.1-alt1
- 1.36.1

* Fri May 21 2021 Anton Farygin <rider@altlinux.ru> 1.36.0-alt1
- 1.36.0

* Thu Apr 22 2021 Anton Farygin <rider@altlinux.ru> 1.34.26-alt1
- 1.34.26

* Mon Apr 19 2021 Anton Farygin <rider@altlinux.ru> 1.34.24-alt1
- 1.34.24

* Thu Feb 25 2021 Anton Farygin <rider@altlinux.org> 1.34.23-alt1
- 1.34.23

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 1.34.22-alt1
- 1.34.22

* Wed Sep 23 2020 Anton Farygin <rider@altlinux.ru> 1.34.21-alt1
- 1.34.21

* Fri Aug 21 2020 Anton Farygin <rider@altlinux.ru> 1.34.19-alt1
- 1.34.19

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 1.34.16-alt1
- 1.34.16

* Fri Jun 05 2020 Anton Farygin <rider@altlinux.ru> 1.34.15-alt1
- 1.34.15

* Tue Apr 07 2020 Anton Farygin <rider@altlinux.ru> 1.34.9-alt1
- 1.34.9

* Sun Mar 01 2020 Anton Farygin <rider@altlinux.ru> 1.34.5-alt1
- 1.34.5
- default socket path for php7-fpm changed to
  unix:/var/run/php7-fpm/php7-zoneminder.sock and this change allow
  to switch uid of the php7-fpm process to apache2 user

* Fri Feb 14 2020 Anton Farygin <rider@altlinux.ru> 1.34.2-alt1
- 1.34.2
- added perl-Digest-SHA to requires for zmonvif-probe.pl (closes: #38136)

* Mon Feb 03 2020 Anton Farygin <rider@altlinux.ru> 1.34.1-alt1
- 1.34.1

* Tue Jan 21 2020 Anton Farygin <rider@altlinux.ru> 1.34.0-alt1
- 1.34.0 (fixes: CVE-2019-13072, CVE-2019-6777, CVE-2019-8429, CVE-2019-8428,
	  CVE-2019-8427, CVE-2019-8426, CVE-2019-8425, CVE-2019-8424, CVE-2019-8423,
	  CVE-2019-7352, CVE-2019-7351, CVE-2019-7350, CVE-2019-7349, CVE-2019-7348,
	  CVE-2019-7347, CVE-2019-7346, CVE-2019-7345, CVE-2019-7344, CVE-2019-7343,
	  CVE-2019-7342, CVE-2019-7341, CVE-2019-7340, CVE-2019-7339, CVE-2019-7338,
	  CVE-2019-7337, CVE-2019-7336, CVE-2019-7335, CVE-2019-7334, CVE-2019-7333,
	  CVE-2019-7332, CVE-2019-7331, CVE-2019-7330, CVE-2019-7329, CVE-2019-7328,
	  CVE-2019-7326, CVE-2019-7325, CVE-2019-6992, CVE-2019-6991, CVE-2019-6990)
- switched to apache2 as default user for ZoneMinder
- removed MySQL-client require

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.32.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Mon Jan 14 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.32.3-alt2
- fix FTBFS due to transition to libmysqlclient21

* Fri Dec 14 2018 Anton Farygin <rider@altlinux.ru> 1.32.3-alt1
- 1.32.3

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 1.32.2-alt1
- 1.32.2

* Thu Oct 11 2018 Anton Farygin <rider@altlinux.ru> 1.32.1-alt1
- 1.32.1

* Tue Sep 25 2018 Anton Farygin <rider@altlinux.ru> 1.32.0-alt1
- 1.32.0

* Mon Oct 02 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt3
- removed spawn-fcgi requires for nginx
	(it does not need on configuration with systemd)

* Wed Jun 21 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt2
- removed apache subpackage

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 1.30.4-alt1
- new version

* Mon Jan 16 2017 Anton Farygin <rider@altlinux.ru> 1.30.0-alt1
- added ubt tag to facilitate the backporting process

* Mon Jan 16 2017 Anton Farygin <rider@altlinux.ru> 1.30.0-alt1
- new version

* Fri Mar 11 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.27.0-alt4
- rebuild with recent libav

* Fri Aug 22 2014 Mikhail Efremov <sem@altlinux.org> 1.27.0-alt3
- Rebuild with libgnutls28.

* Mon May 19 2014 Anton Farygin <rider@altlinux.ru> 1.27.0-alt2
- rebuild with new libav

* Wed Apr 16 2014 Anton Farygin <rider@altlinux.ru> 1.27.0-alt1
- new version
- added subpackage with sample nginx configuration for zoneminder web interface

* Tue May 15 2012 Andrey Cherepanov <cas@altlinux.org> 1.24.4-alt2.1.M60P.2
- Rebuild with new version of libav

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
