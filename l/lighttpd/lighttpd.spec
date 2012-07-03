%def_with mysql
%def_with ssl
%def_with ldap
%def_with memcache
%def_with lua
%def_with gamin

%define lighttpd_user lighttpd
%define lighttpd_group lighttpd
%define lighttpd_spool %_spooldir/%name

%define docdir %_docdir/%name-%version-doc
%define svnrev 2710

Name: lighttpd
Version: 1.4.28
#Release: alt1.svn.%svnrev
Release: alt2

Summary: A fast webserver with minimal memory-footprint
License: BSD
Group: System/Servers

# git svn init -Ttrunk -ttags -bbranches svn://svn.lighttpd.net/lighttpd/
Url: http://www.lighttpd.net

Source0: lighttpd.tar

Requires(pre): shadow-utils shadow-groups webserver-common
Provides: webserver

BuildRequires(pre): rpm-macros-webserver-common
# Automatically added by buildreq on Wed Sep 02 2009
BuildRequires: bzlib-devel libfcgi-devel libpcre-devel zlib-devel

%{?_with_mysql:BuildPreReq: libMySQL-devel}
%{?_with_ssl:BuildPreReq: libssl-devel}
%{?_with_ldap:BuildPreReq: libldap-devel}
%{?_with_memcache:BuildPreReq: libmemcache-devel}
%{?_with_lua:BuildPreReq:liblua5-devel}
%{?_with_gamin:BuildPreReq: libgamin-devel}

%description
%name is intented to be a frontend for ad-servers which have to deliver
small files concurrently to many connections.

%package mysql-vhost
Summary: MySQL based vhosting %name module
Group: System/Servers
Requires: %name = %version-%release

%description mysql-vhost
This module provides virtual hosts (vhosts) based on a MySQL table.

%package cml
Summary: CML (Cache Meta Language) %name module
Group: System/Servers
Requires: %name = %version-%release

%description cml
CML is a Meta language to describe the dependencies of a page at one side and
building a page from its fragments on the other side using LUA. 

%package trigger_b4_dl
Summary: another anti hot-linking %name module
Group: System/Servers
Requires: %name = %version-%release

%description trigger_b4_dl
another anti hot-linking module.

%package rrdtool
Summary: rrdtool support %name module
Group: System/Servers
Requires: %name = %version-%release, rrdtool

%description rrdtool
mod_rrdtool is used to monitor the traffic and load on the webserver.

%package doc
Summary: %name documentation
Group: Documentation

%description doc
Documentation for %name.

%prep
%setup -n %name
libtoolize -f -c
%autoreconf

%build
%configure --libdir=%_libdir/%name \
    %{?_with_mysql:       --with-mysql} \
    %{?_with_ssl:         --with-openssl} \
    %{?_with_ldap:	  --with-ldap} \
    %{?_with_memcache:	  --with-memcache} \
    %{?_with_lua:	  --with-lua} \
    %{?_with_gamin:	  --with-fam} \
    %{?_with_lua:	  LUA_CFLAGS="-I/usr/include/" LUA_LIBS="-llua"}
%make_build

# run tests for sanity checks
#pushd tests
#./wrapper.sh . .. ./prepare.sh
#./wrapper.sh . .. ./run-tests.pl
#popd

%install
%makeinstall libdir=%buildroot%_libdir/%name

mkdir -p %buildroot%_sysconfdir/{rc.d/init.d,sysconfig}
mkdir -p %buildroot{%_spooldir/%name/tmp,%_var/log/%name}

# inirscript and sysconfig
install -m755 %name.init %buildroot%_initdir/%name
install -m644 doc/initscripts/sysconfig.lighttpd %buildroot%_sysconfdir/sysconfig/lighttpd

# configs
cp -rp doc/config %buildroot%_sysconfdir/%name
find %buildroot%_sysconfdir/%name -type f -name "Makefile*" -delete

# logrotate script
install -pDm644 lighttpd.logrotate %buildroot%_sysconfdir/logrotate.d/%name

# docs
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
cp -a doc/*.txt %buildroot%docdir/

%pre
%_sbindir/groupadd -r -f %lighttpd_group ||:
%_sbindir/useradd -r -g %lighttpd_group -d /dev/null -s /dev/null -n %lighttpd_user \
	2> /dev/null > /dev/null ||:
gpasswd -a %lighttpd_user %webserver_group

%post
%post_service lighttpd

%preun
%preun_service lighttpd

%files
%doc README INSTALL COPYING AUTHORS
%config %_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/lighttpd
%config(noreplace) %_sysconfdir/logrotate.d/%name
%dir %attr(0750,root,%lighttpd_group) %_sysconfdir/%name
%dir %attr(0750,root,%lighttpd_group) %_sysconfdir/%name/conf.d
%dir %attr(0750,root,%lighttpd_group) %_sysconfdir/%name/vhosts.d
%config(noreplace) %attr(0644,root,%lighttpd_group) %_sysconfdir/%name/*.conf
%config(noreplace) %attr(0644,root,%lighttpd_group) %_sysconfdir/%name/*/*.conf
%_sysconfdir/%name/*/mod.template
%_sysconfdir/%name/vhosts.d/*
%_man8dir/*
%dir %attr(1770,root,%lighttpd_group) %lighttpd_spool
%dir %attr(1770,root,%lighttpd_group) %lighttpd_spool/tmp
%dir %attr(1770,root,%lighttpd_group) %_var/log/%name
%dir %_libdir/%name
%_libdir/%name/*.so
%if_with mysql
%exclude %_libdir/%name/*_mysql_vhost.so
%endif #mysql
%if_with lua
%exclude %_libdir/%name/*_cml.so
%endif #cml
%if_with memcache
%exclude %_libdir/%name/*_trigger_b4_dl.so
%endif #trigger_b4_dl
%exclude %_libdir/%name/*_rrdtool.so
%_sbindir/*
%exclude %_libdir/%name/*.la

%files doc
%docdir

%if_with mysql
%files mysql-vhost
%_libdir/%name/*mysql_vhost.so
%endif #mysql

%if_with lua
%files cml
%_libdir/%name/*cml.so
%endif lua

%if_with memcache
%files trigger_b4_dl
%_libdir/%name/*trigger_b4_dl.so
%endif #memcache

%files rrdtool
%_libdir/%name/*rrdtool.so

%changelog
* Mon Oct 18 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.28-alt2
- Rebuild with libssl.so.10 and libcrypto.so.10.

* Fri Oct 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.28-alt1
- 1.4.28.
- New config scheme introduced by upstream: small main config which
  includes configs for modules and vhosts (Closes: #23233).
- Add lighttpd pseudouser to %%webserver_group according to WebPolicy
  (Closes: #23232).
- Don't create docdir when starting lighttpd service.

* Thu Feb 04 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.25-alt1.svn.2710
- Update to 2710 revision of 1.4.x branch.
- Security fix: CVE-2010-0295 (lighttpd Slow Request Denial of Service
  Vulnerability).

* Thu Dec 31 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.23-alt3
- Properly create all docroots specified in config file, patch by
  Nikolay A. Fetisov (Closes: #22652).

* Fri Oct 16 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.23-alt2
- Fix building with fresh liblua

* Wed Sep 02 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.23-alt1
- 1.4.23
- Move spawn-fcgi package to separate git repository because spawn-fcgi
  was removed from lighttpd main tree, see
  http://blog.lighttpd.net/articles/2009/04/03/spawn-fcgi-removed-from-lighttpd-1-4
- Rebuilt with libldap2.4

* Thu Mar 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.22-alt1
- 1.4.22
- Fix+add cond* actions in spawn-fcgi initscript

* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.20-alt2.svn.2364
- Updated to 2364 revision of 1.4.x branch
- Add condrestart action for spawn-fcgi initscript

* Tue Sep 30 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.20-alt1
- 1.4.20 release
- Security fix: duplicate Request Headers Memory Leak Vulnerability
  http://secunia.com/advisories/32069/

* Tue Sep 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 1.4.19-alt6.svn.2299
- Updated to 2299 revision of 1.4.x branch
- Move spawn-fcgi to separate subpackage (thresh, vvk)

* Wed Aug 27 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.19-alt5.svn.2296
- Updated to 2296 revision of 1.4.x branch
- initscript: add restart() (Closes: #16417)
- logrotate-script: redirect output to /dev/null

* Fri Apr 04 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.19-alt4.svn.2142
- Updated to 2142 revision of 1.4.x branch
- Security fixes:
  + CVE-2008-1531 lighttpd OpenSSL Error Queue Denial of Service Vulnerability
- Enable memcache support

* Fri Mar 14 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.19-alt3
- Add logrotate script
- Initscript changes:
  + Check docdir existance and create it if it doesn't exist (Closes: #12725)
  + Introduce log_reopen() function for sending SIGHUP to daemon - needed for
  log rotation

* Tue Mar 11 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.19-alt2
- There is an error in previous package version: real version was 1.4.18, not
  1.4.19!
- This is real 1.4.19 release. Security fixes:
  + CVE-2008-0983: remote DoS
  + CVE-2008-1111: exposure of sensitive information (Fix sending source of cgi
  script instead of 500 error if fork fails)

* Tue Sep 11 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.19-alt1
- Real version is 1.4.18 - there is error in package version!!!
- Security fix: CVE-2007-4727: FastCGI header overrun in mod_fastcgi

* Tue Sep 04 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.18-alt1.svn.1981
- Updated to 1981 revision of 1.4.x branch:
  + many bugs fixed (see HISTORY)
- Fixed ALT Security Policy violation (spooldir permissions)

* Mon Jul 16 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.15-alt2.svn.1881
- Updated to 1881 revision of 1.4.x branch
- Security fixes:
  + Remote crash on duplicate header keys with line-wrapping (fixes #1230)
  + Missing check for base64 encoded string in mod_auth and Basic
    auth (reported by Stefan Esser)
  + Crash with md5-sess and cnonce not set in mod_auth (reported
    by Stefan Esser)
  + Possible crash in Auth-Digest header parser on trailing WS in
    mod_auth (reported by Stefan Esser)
  + mem-leak in mod_auth (reported by Stefan Esser)
  + URL Access restrictions bypass in mod_access
  + Local DOS with broken FastCGI applications

* Mon Apr 16 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.15-alt1
- Updated to 1.4.15 release

* Thu Apr 12 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.13-alt3.1745
- Updated to 1745 revision of 1.4.x branch
- Added sis/sisx mime types (Closes: #11462)

* Thu Apr 05 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.13-alt2.1719
- Updated to 1719 revision of 1.4.x branch
  + Fix crash if gethostbyaddr() fails on redirect

* Sat Mar 24 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.13-alt2.1716
- Build without memcache

* Tue Mar 20 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.13-alt1.1716
- Updated to 1716 revision of 1.4.x branch

* Thu Feb 08 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.4.13-alt1.1607
- Updated to 1.4.x branch svn revision 1607
- Security fix:
  + Fix remote DOS in CRLF parsing (CVE-2007-1869)
  + Fix a crash for files with an mtime of 0 reported by cubiq on irc
  (CVE-2007-1870)
- Integrate lighttpd-1.4.3-config.patch

* Mon Jan 30 2006 LAKostis <lakostis at altlinux.org> 1.4.9-alt1
- 1.4.9;
- change fam support to gamin;
- pack ChangeLog and move it to -doc subpackage.

* Sat Jan 07 2006 LAKostis <lakostis at altlinux.org> 1.4.8-alt1
- 1.4.8;
- fix #8431.

* Sat Oct 29 2005 LAKostis <lakostis at altlinux.org> 1.4.6-alt1
- 1.4.6.
- fix config dir permissions.
- fix requires.
- add libfcgi-devel to BuildRequires.
- add lua,memcache,fam,ldap support.
- split out to many packages.

* Sun Sep 11 2005 LAKostis <lakostis at altlinux.org> 1.4.3-alt1
- first build for ALTLinux Sisyphus.

* Thu Sep 30 2004 12:41 <jan@kneschke.de> 1.3.1
- upgraded to 1.3.1

* Tue Jun 29 2004 17:26 <jan@kneschke.de> 1.2.3
- rpmlint'ed the package
- added URL
- added (noreplace) to start-script
- change group to Networking/Daemon (like apache)

* Sun Feb 23 2003 15:04 <jan@kneschke.de>
- initial version
