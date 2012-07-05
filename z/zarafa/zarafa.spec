###############################################################################
#
# General
#
###############################################################################

%define svnrevision	33926
%define php5_extension	mapi
%define webprefix	%_datadir/zarafa-webaccess
%define mobprefix	%_datadir/zarafa-webaccess-mobile
%define licensepath	%_docdir

Name: zarafa
Version: 7.1.0
Release: alt4.1
License: AGPLv3
Group: Networking/Mail
Summary: Server program for the Zarafa Collaboration Platform
Packager: Radik Usupov <radik@altlinux.org>
Url: http://www.zarafa.com/

Source: %name-%version.tar.gz
Source1: php-zarafa.params
Patch: zarafa-7.1.0beta1-alt-makefile.patch
Patch1: zarafa-7.0rc2-alt-ossbuild.patch
Patch2: zarafa-7.0rc1-alt-php-ext-makefile.patch
Patch3: zarafa-7.0.1-alt-fix-userscript-path.patch

BuildRequires(pre): rpm-build-php5
BuildRequires(pre): rpm-build-apache2
# Automatically added by buildreq on Fri Apr 15 2011
# optimized out: boost-devel boost-devel-headers libcom_err-devel libgpg-error libkrb5-devel libncurses-devel libstdc++-devel libtinfo-devel pkg-config python-base python-modules
BuildRequires: boost-filesystem-devel flex-old gcc-c++ libclucene-devel libical-devel libicu-devel libldap-devel libmysqlclient-devel
BuildRequires: libpam-devel libssl-devel libuuid-devel libvmime-devel libxml2-devel php5-devel rpm-build-python swig tzdata xmlto zlib-devel
BuildRequires: perl-CGI libncurses-devel python-devel libkyotocabinet-devel

Requires: zarafa-server = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libs
Requires: zarafa-utils
Requires: zarafa-monitor
Requires: zarafa-spooler
Requires: zarafa-dagent
Requires: zarafa-ical
Requires: zarafa-gateway
Requires: zarafa-search

%description
The Zarafa Collaboration Platform (ZCP) combines the usability of
Outlook with the stability and flexibility of a Linux server. It
features a rich web-interface, the Zarafa WebAccess, and provides
brilliant integration options with all sorts of clients including
all most popular mobile platforms.

#'emacs colors

%package devel
Group: Development/C++
Summary: C++ development files for the Zarafa Collaboration Platform

%description devel
Development files to create MAPI aware programs under Linux.
Examples and documentation can be found on our website:
http://developer.zarafa.com/

%package devel-static
Group: Development/C++
Summary: C++ development files for the Zarafa Collaboration Platform

%description devel-static
Development files to create MAPI aware programs under Linux.
Examples and documentation can be found on our website:
http://developer.zarafa.com/

%package common
Group: Networking/Mail
Summary: Shared files between ZCP services
BuildArch: noarch

%description common
Common components for services of the Zarafa Collaboration Platform

%package server
Group: Networking/Mail
Summary: Server component for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release

%description server
The key component of the ZCP, providing the server to which ZCP
clients connect. The server requires a MySQL server to use for
storage.

%package client
Group: Networking/Mail
Summary: MAPI4Linux and the Zarafa MAPI provider libraries

%description client
The main libraries for any Zarafa client program. This package is
required by all Zarafa client programs.

%package libs
Group: Networking/Mail
Summary: Conversion libraries between Open Standards and MAPI
Requires: libvmime >= 0.9.2
Requires: libical >= 0.44

%description libs
Commonly used libraries by Zarafa Collaboration Platform client
programs.

%package libarchiver
Group: Networking/Mail
Summary: Library with shared ZCP archiver functionality
Requires: zarafa-client = %version-%release
Requires: zarafa-common = %version-%release

%description libarchiver
Library with shared archiver functionality for the Zarafa Collaboration Platform.

%package utils
Group: Networking/Mail
Summary: Admin command-line utils for the Zarafa Collaboration Platform
Requires: zarafa-client = %version-%release

%description utils
Commandline clients to control and check the ZCP server.

%package monitor
Group: Networking/Mail
Summary: Quota Monitor for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release

%description monitor
Regularly checks stores for total usage. If a quota limit has been
exceeded, an e-mail will be internally sent to this account.

%package spooler
Group: Networking/Mail
Summary: E-mail Spooler for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release

%description spooler
Sends all outgoing e-mail requests from Zarafa to an SMTP server.

%package dagent
Group: Networking/Mail
Summary: E-Mail Delivery Agent for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release

%description dagent
Delivers incoming e-mail from your SMTP server to stores in the
Zarafa server.

%package gateway
Group: Networking/Mail
Summary: POP3 and IMAP Gateway for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release

%description gateway
Provides access to the Zarafa server through the POP3 and IMAP
protocols.

%package ical
Group: Networking/Mail
Summary: ICal and CalDAV Gateway for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release

%description ical
Provides access to the Zarafa server through the ICal and CalDAV
protocols.

%package -n python-module-mapi
Group: Networking/Mail
Summary: Python MAPI bindings
#By http://www.altlinux.org/Python_Policy
Requires: python = %_python_version
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release

%description -n python-module-mapi
Using this module, you can create python programs which use MAPI
calls to interact with Zarafa.

%package -n php5-%php5_extension
Group: Networking/Mail
Summary: PHP MAPI bindings
Requires: zarafa-client = %version-%release
Requires: zarafa-libs = %version-%release
# add provide package name:
Provides: php(mapi) = %version-%release
Provides: php-mapi = %version-%release

%description -n php5-%php5_extension
Using this module, you can create PHP programs which use MAPI
calls to interact with Zarafa.

%package search
Group: Networking/Mail
Summary: Indexed search engine for the Zarafa Collaboration Platform
Requires: zarafa-common = %version-%release
Requires: zarafa-client = %version-%release
Requires: zarafa-libarchiver = %version-%release
Requires: coreutils mktemp bash gawk lynx libxslt poppler unzip file catdoc

%description search
The zarafa-search process makes an index
per user of messages and attachments. When this service is enabled,
search queries on the server will use this index to quickly find
messages and even in contents of attached documents.

%package contacts
Group: Networking/Mail
Summary: MAPI provider adding contact folders in the addressbook
Requires: zarafa-client = %version-%release

%description contacts
Additional MAPI provider which finds all contact folders of a user
and adds the contents transparently into the MAPI addrbook.

# noarch packages
%package webaccess
Group: Networking/Mail
Summary: A web interface for the Zarafa Collaboration Platform
License: AGPLv3
Requires: php-mapi >= %version-%release
BuildArch: noarch
Requires: tzdata
Conflicts: zarafa-webaccess-ajax
Obsoletes: zarafa-webaccess-ajax

%description webaccess
Provides a web-client written in PHP that makes use of AJAX to allow
users to make full use of the Zarafa Collaboration Platform through a
modern web browser.

#end noarch packages

###############################################################################
#
# Build
#
###############################################################################

%prep
%setup
%patch -p2
%patch1 -p2
%patch2 -p2
%patch3 -p2

%build
%add_optflags -DBOOST_FILESYSTEM_VERSION=2 -fPIC -L%_libdir

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
export LDFLAGS=-lphp-%_php5_version

%autoreconf
%configure --with-distro=alt \
	--prefix=%prefix \
	--sysconfdir=%_sysconfdir \
	--localstatedir=%_localstatedir \
	--libdir=%_libdir \
	--mandir=%_mandir \
	--with-userscript-prefix=%_sysconfdir/zarafa/userscripts \
	--with-quotatemplate-prefix=%_sysconfdir/zarafa/quotamail \
	--with-searchscripts-prefix=%_datadir/zarafa/searchscripts \
	--disable-static \
	--with-clucene-lib-prefix=%_libdir \
	--enable-unicode \
	--enable-tcmalloc \
	--with-tcmalloc-prefix=%_libdir \
	--enable-python \
	--enable-epoll \
	--disable-perl \
	--disable-swig \
	--enable-oss
%make_build

###############################################################################
#
# Install
#
###############################################################################

%install
%makeinstall_std

# move license files to doc dirs
	%__mkdir_p %buildroot%licensepath/%name
	%__cp %buildroot%_docdir/%name/AGPL-3 %buildroot%licensepath/%name/LICENSE
	for package in spooler gateway monitor dagent ical search devel client libs utils contacts; do
		%__mkdir_p %buildroot%licensepath/%name-$package
		%__cp %buildroot%_docdir/%name/AGPL-3 %buildroot%licensepath/%name-$package/LICENSE
	done
	for package in php python; do
		%__mkdir_p %buildroot%licensepath/$package-mapi
		%__cp %buildroot%_docdir/%name/AGPL-3 %buildroot%licensepath/$package-mapi/LICENSE
	done

# move example-config files
	for package in spooler gateway monitor dagent ical search; do
		%__mkdir_p %buildroot%_docdir/%name-$package/example-config
		%__mv %buildroot%_docdir/%name/example-config/$package.cfg %buildroot%_docdir/%name-$package/example-config
	done
	%__mv %buildroot%_docdir/%name/example-config/autorespond %buildroot%_docdir/%name-dagent/example-config

# link userscripts in %_datadir/zarafa/userscripts
	%__mkdir_p %buildroot%_datadir/%name/userscripts
	for file in $(find %buildroot%_sysconfdir/%name/userscripts -maxdepth 1 -type f); do
		%__mv $file %buildroot%_datadir/%name/userscripts
		%__ln_s -f %_datadir/%name/userscripts/$(basename $file) $file
	done
# link searchscripts
	%__ln_s -f %_datadir/%name/searchscripts %buildroot%_sysconfdir/%name/searchscripts

# add default empty directories
	%__mkdir_p %buildroot%_sysconfdir/%name/license
	%__mkdir_p %buildroot/var/log/%name


# fix php-config path
	%__mkdir_p %buildroot%php5_extconf/%php5_extension
	    %__mv -f -- %buildroot%_sysconfdir/%name.ini %buildroot%php5_extconf/%php5_extension/config
	    %__install -D -m 644 -- %SOURCE1 %buildroot%php5_extconf/%php5_extension/params
	%__mkdir_p %buildroot%php5_datadir/%php5_extension
	    %__mv -f -- %buildroot%_datadir/*.php %buildroot%php5_datadir/%php5_extension

# install webaccess
	%makeinstall_std install-ajax-webaccess

# fix libdir in server config for user plugins
	%__sed -e "s@/usr/lib/zarafa@%_libdir/zarafa@" -i %buildroot%_sysconfdir/%name/server.cfg

# install ajax apache config
	%__mkdir_p %buildroot%apache2_sites_available
	%__mkdir_p %buildroot%apache2_sites_enabled
	%__mv %buildroot%webprefix/%name-webaccess.conf %buildroot%apache2_sites_available
	pushd %buildroot%apache2_sites_enabled
	    %__ln_s -f ../sites-available/%name-webaccess.conf
	popd

# move init-script
	%__mkdir_p %buildroot%_initdir
	%__mv %buildroot/etc/init.d/%name-* %buildroot%_initdir/

# remove debug files
	%__rm %buildroot%_libdir/libzarafaclient.la 
	%__rm %buildroot%_libdir/%name/*.la
	%__rm %buildroot%_libdir/python*/site-packages/*.la
	%__rm %buildroot%php5_extdir/*.la

# remove garbage
	%__rm %buildroot%_sysconfdir/%name-*
	%__rm %buildroot%_sysconfdir/%name.ini
	%__rm %buildroot%_datadir/*.php

###############################################################################
#
# Scripts
#
###############################################################################
# Zarafa-Server
%post server
%post_service %name-server

%preun server
%preun_service %name-server

# Zarafa-Spooler
%post spooler
%post_service %name-spooler

%preun spooler
%preun_service %name-spooler

# Zarafa-Dagent
%post dagent
%post_service %name-dagent

%preun dagent
%preun_service %name-dagent

# Zarafa-Gateway
%post gateway
%post_service %name-gateway

%preun gateway
%preun_service %name-gateway

# Zarafa-Monitor
%post monitor
%post_service %name-monitor

%preun monitor
%preun_service %name-monitor

# Zarafa-Ical
%post ical
%post_service %name-ical

%preun ical
%preun_service %name-ical

#Zarafa-Search
%post search
%post_service %name-search

%preun search
%preun_service %name-search

#PHP5-Mapi
%post -n php5-%php5_extension
%php5_extension_postin

%preun -n php5-%php5_extension
%php5_extension_preun

###############################################################################
#
# File list
#
###############################################################################

%files
%files common
%dir %_datadir/%name/
%dir %_sysconfdir/%name
%dir %_logdir/%name
%config %attr(0644,root,root) %_sysconfdir/logrotate.d/%name
%_sysconfdir/cron.daily/%name-client-update

%files server
%dir %_libdir/%name
%_bindir/%name-server
%_bindir/%name-mr-accept
%_libdir/%name/dbplugin.so
%_libdir/%name/unixplugin.so
%_libdir/%name/ldapplugin.so
%_sysconfdir/sysconfig/%name
%_docdir/%name/*
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/ldap.active-directory.cfg
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/ldap.openldap.cfg
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/ldap.propmap.cfg
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/unix.cfg
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/server.cfg
%dir %_sysconfdir/%name/userscripts
%attr(0755,root,root) %_sysconfdir/%name/userscripts/createcompany
%attr(0755,root,root) %_sysconfdir/%name/userscripts/creategroup
%attr(0755,root,root) %_sysconfdir/%name/userscripts/createuser
%attr(0755,root,root) %_sysconfdir/%name/userscripts/deletecompany
%attr(0755,root,root) %_sysconfdir/%name/userscripts/deletegroup
%attr(0755,root,root) %_sysconfdir/%name/userscripts/deleteuser
%attr(0644,root,root) %_sysconfdir/%name/userscripts/*common.sh
%dir %_sysconfdir/%name/userscripts/createuser.d
%dir %_sysconfdir/%name/userscripts/creategroup.d
%dir %_sysconfdir/%name/userscripts/createcompany.d
%dir %_sysconfdir/%name/userscripts/deleteuser.d
%dir %_sysconfdir/%name/userscripts/deletegroup.d
%dir %_sysconfdir/%name/userscripts/deletecompany.d
%config(noreplace) %attr(0755,root,root) %_sysconfdir/%name/userscripts/createuser.d/*
%config(noreplace) %attr(0755,root,root) %_sysconfdir/%name/userscripts/createcompany.d/*
%dir %_datadir/%name/userscripts
%attr(0755,root,root) %_datadir/%name/userscripts/createcompany
%attr(0755,root,root) %_datadir/%name/userscripts/creategroup
%attr(0755,root,root) %_datadir/%name/userscripts/createuser
%attr(0755,root,root) %_datadir/%name/userscripts/deletecompany
%attr(0755,root,root) %_datadir/%name/userscripts/deletegroup
%attr(0755,root,root) %_datadir/%name/userscripts/deleteuser
%attr(0644,root,root) %_datadir/%name/userscripts/*common.sh
%config %attr(0755,root,root)  %_initdir/%name-server
%_man1dir/%name-server.1*
%_man1dir/%name-msr.1*
%_man1dir/%name-msr-verify.1*
%_man1dir/za-aclsync.1*
%_man1dir/%name-archiver.1*
%_man1dir/%name-backup.1*
%_man1dir/%name-licensed.1*
%_man1dir/%name-report.1*
%_man1dir/%name-restore.1*
%_man1dir/%name.1*
%_man5dir/%name-ldap.cfg.5*
%_man5dir/%name-server.cfg.5*
%_man5dir/%name-msr.cfg.5*
%_man5dir/%name-unix.cfg.5*
%_man5dir/%name-archiver.cfg.5*
%_man5dir/%name-ldapms.cfg.5*
%_man5dir/%name-licensed.cfg.5*
%_man5dir/%name-backup.cfg.5.*
%dir %licensepath/%name

%files devel
%_libdir/libarchiver.so
%_libdir/libmapi.so
%_libdir/libicalmapi.so
%_libdir/libinetmapi.so
%dir %_includedir/mapi4linux
%_includedir/mapi4linux/*
%dir %_includedir/zarafa
%_includedir/zarafa/*
%dir %_includedir/inetmapi
%_includedir/inetmapi/*
%dir %_includedir/icalmapi
%_includedir/icalmapi/*
%dir %_includedir/libfreebusy
%_includedir/libfreebusy/*
%dir %_includedir/libzarafasync
%_includedir/libzarafasync/*
%_pkgconfigdir/zarafa.pc
%dir %licensepath/%name-devel
%licensepath/%name-devel/LICENSE

%files devel-static
%_libdir/libcommon_mapi.a
%_libdir/libcommon_util.a
%_libdir/libcommon_ssl.a
%_libdir/libfreebusy.a
%_libdir/libcommon_service.a

%files client
%dir %_sysconfdir/mapi
%dir %licensepath/%name-client
%_sysconfdir/mapi/zarafa.inf
%_libdir/libmapi*.so.*
%_libdir/libzarafaclient*.so*
%_libdir/libzarafasync*.so.*
%_libdir/libzarafasync.so
%_datadir/locale/*/LC_MESSAGES/*mo
%licensepath/%name-client/LICENSE

%files libs
%_libdir/libicalmapi*.so.*
%_libdir/libinetmapi*.so.*
%dir %licensepath/%name-libs
%licensepath/%name-libs/LICENSE

%files libarchiver
%_bindir/%name-archiver
%_libdir/libarchiver*.so.*
%_libdir/libarchiver-core.so
%_libdir/libarchiver-core*.so.*
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/archiver.cfg


%files utils
%_bindir/%name-admin
%_bindir/%name-fsck
%_bindir/%name-passwd
%_bindir/%name-stats
%_man1dir/%name-admin.1*
%_man1dir/%name-fsck.1*
%_man1dir/%name-passwd.1*
%_man1dir/%name-stats.1*
%_man1dir/za-restore.1*
%dir %licensepath/%name-utils
%licensepath/%name-utils/LICENSE

%files monitor
%_bindir/%name-monitor
%dir %_sysconfdir/%name/quotamail
%config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/quotamail/*
%config %attr(0755,root,root) %_initdir/%name-monitor
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/monitor.cfg
%_man1dir/%name-monitor.1*
%_man5dir/%name-monitor.cfg.5*
%dir %_docdir/%name-monitor/
%_docdir/%name-monitor/*

%files spooler
%_bindir/%name-spooler
%config %attr(0755,root,root) %_initdir/%name-spooler
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/spooler.cfg
%_man1dir/%name-spooler.1*
%_man5dir/%name-spooler.cfg.5*
%dir %_docdir/%name-spooler/
%_docdir/%name-spooler/*
%dir %_datadir/%name-spooler/
%dir %_datadir/%name-spooler/python/
%_datadir/%name-spooler/python/*

%files dagent
%_bindir/%name-autorespond
%_bindir/%name-dagent
%config %attr(0755,root,root) %_initdir/%name-dagent
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/dagent.cfg
%verify(not mode) %config(noreplace) %attr(0644,root,root) %_sysconfdir/%name/autorespond
%_man1dir/%name-dagent.1*
%_man5dir/%name-dagent.cfg.5*
%dir %_docdir/%name-dagent/
%_docdir/%name-dagent/*
%dir %_datadir/%name-dagent/
%dir %_datadir/%name-dagent/python/
%_datadir/%name-dagent/python/*

%files gateway
%_bindir/%name-gateway
%config %attr(0755,root,root) %_initdir/%name-gateway
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/gateway.cfg
%_man1dir/%name-gateway.1*
%_man5dir/%name-gateway.cfg.5*
%dir %_docdir/%name-gateway/
%_docdir/%name-gateway/*

%files ical
%_bindir/%name-ical
%config %attr(0755,root,root) %_initdir/%name-ical
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/ical.cfg
%_man1dir/%name-ical.1*
%_man5dir/%name-ical.cfg.5*
%dir %_docdir/%name-ical/
%_docdir/%name-ical/*

%files -n php5-mapi
%dir %_docdir/php-mapi/
%dir %php5_datadir/%php5_extension/
%php5_extconf/%php5_extension
%php5_extdir/*
%php5_datadir/%php5_extension/*
%licensepath/php-mapi/LICENSE

%files search
%_bindir/%name-search
%config %attr(0755,root,root) %_initdir/%name-search
%verify(not mode) %config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/search.cfg
%_sysconfdir/%name/searchscripts
%dir %_datadir/%name/searchscripts
%_datadir/%name/searchscripts/attachments_parser
%_datadir/%name/searchscripts/attachments_parser.db
%_datadir/%name/searchscripts/xmltotext.xslt
%_datadir/%name/searchscripts/zmktemp
%_man1dir/%name-search.1*
%_man5dir/%name-search.cfg.5*
%dir %licensepath/%name-search
%licensepath/%name-search/LICENSE
%dir %_docdir/%name-search/
%_docdir/%name-search/*

%files -n python-module-mapi
%_libdir/python*/*/*.py*
%_libdir/python*/*/*.so
%_libdir/python*/*/MAPI/
%_libdir/python*/*/*.egg-info
%dir %licensepath/python-mapi
%licensepath/python-mapi/LICENSE

%files contacts
%dir %_docdir/%name-contacts
%_sysconfdir/mapi/zcontacts.inf
%_libdir/libzarafacontacts.so
%_docdir/%name-contacts

# noarch package files

%files webaccess
#is this the correct prefix now?
%dir %webprefix/
%dir %_sysconfdir/%name
# add writeable temp dir
%dir %_localstatedir/%name-webaccess
%dir %_localstatedir/%name-webaccess/plugins
%attr(3775,root,apache2) %dir %_localstatedir/%name-webaccess/tmp
%webprefix/.htaccess
%webprefix/*
%config %dir %_sysconfdir/%name/webaccess-ajax
%config(noreplace) %_sysconfdir/%name/webaccess-ajax/config.php
%config(noreplace) %apache2_sites_available/%name-webaccess.conf
%config(noreplace) %apache2_sites_enabled/%name-webaccess.conf

# end noarch files

%changelog
* Thu Jul 05 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 7.1.0-alt4.1
- Rebuild with libkyotocabinet.so.16

* Fri Jun 29 2012 Radik Usupov <radik@altlinux.org> 7.1.0-alt4
- New upstreame snapshot (7.1.0rc1)
- Drop zarafa-7.0.6-alt-boost-1.49.0.patch

* Fri Jun 01 2012 Radik Usupov <radik@altlinux.org> 7.1.0-alt3
- New upstreame snapshot (7.1.0beta3)
- Removed indexer package
- Added search package

* Sat May 12 2012 Radik Usupov <radik@altlinux.org> 7.1.0-alt2
- New upstreame snapshot (7.1.0beta2)

* Fri Apr 20 2012 Radik Usupov <radik@altlinux.org> 7.1.0-alt1
- New version (7.1.0beta1-33926)

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.6-alt1.1
- Rebuilt with Boost 1.49.0

* Fri Mar 16 2012 Radik Usupov <radik@altlinux.org> 7.0.6-alt1
- New version (7.0.6-32752)

* Tue Feb 21 2012 Radik Usupov <radik@altlinux.org> 7.0.5-alt5
- Added russian language in zarafa-client
- Update russian translations from webaccess

* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 7.0.5-alt4
- Rebuild with php5-5.3.10.20120202-alt1

* Sat Feb 04 2012 Radik Usupov <radik@altlinux.org> 7.0.5-alt3
- Added postin trigger (thanks snejok@)

* Thu Feb 02 2012 Radik Usupov <radik@altlinux.org> 7.0.5-alt2
- New version (7.0.5-31880)

* Tue Jan 24 2012 Radik Usupov <radik@altlinux.org> 7.0.5-alt1
- New version (7.0.5beta1-31699)

* Thu Dec 29 2011 Radik Usupov <radik@altlinux.org> 7.0.4-alt2
- Updated russian translation for zarafa-webaccess
- Fixed zarafa-dagent init files

* Fri Dec 09 2011 Radik Usupov <radik@altlinux.org> 7.0.4-alt1
- New version (7.0.4-31235). Thanks legion@!
- Drop webaccess-mobile

* Mon Dec 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.0.3-alt2.1
- Rebuilt with Boost 1.48.0

* Sun Nov 27 2011 Radik Usupov <radik@altlinux.org> 7.0.3-alt2
- New version (7.0.3-30515)

* Fri Nov 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 7.0.3-alt1.1
- Rebuild with Python-2.7

* Thu Nov 03 2011 Radik Usupov <radik@altlinux.org> 7.0.3-alt1
- New version (7.0.3beta1-30283)

* Fri Sep 30 2011 Radik Usupov <radik@altlinux.org> 7.0.2-alt3
- New version (7.0.2-29470)
- Changed alt-use-init.alt.patch

* Wed Sep 28 2011 Radik Usupov <radik@altlinux.org> 7.0.2-alt2
- Fixed zarafa-dagent init script
- Fixed ssl-certificates script

* Fri Sep 16 2011 Radik Usupov <radik@altlinux.org> 7.0.2-alt1
- New version (7.0.2beta1-29238)

* Wed Sep 11 2011 Radik Usupov <radik@altlinux.org> 7.0.1-alt3
- zarafa-common, zarafa-webaccess and
  zarafa-webaccess-mobile is now noarch
- Macros usage
- New version (7.0.1-28479)

* Sat Sep 10 2011 Anton Farygin <rider@altlinux.ru> 7.0.1-alt2
- Rebuild with php5-5.3.8.20110823-alt1

* Tue Jul 26 2011 Radik Usupov <radik@altlinux.org> 7.0.1-alt1
- New version  (7.0.1beta1-28354)

* Tue Jun 28 2011 Radik Usupov <radik@altlinux.org> 7.0.0-alt2
- Zarafa Collaboration Platform final (7.0.0-27791)
- Fixed preuninstall scriptlet

* Sat May 07 2011 Radik Usupov <radik@altlinux.org> 7.0.0-alt1
- Initial build for ALT Linux Sisyphus
- Thanks snejok@, andyc@, raorn@, wrar@ and vitty@!
