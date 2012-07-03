# TODO from PLD:
#  - service ntop init steals terminal (it doesnt finish nor background)
#  - paths wrong somewhere /var/lib/ntop/ntop is expected (should be without last path component)
#  - ntop apperars to be daemon, so it should be in _sbindir not in _bindir
#

Name: ntop
Version: 4.1.0
Release: alt1.1

Summary: A network traffic probe similar to the UNIX top command

License: GPL
Group: Monitoring

Url: http://www.ntop.org/

# FIXME: libntop needs linking with ntop binary??
%set_verify_elf_method unresolved=relaxed

Source: %name-%version.tar
Source1: %name.init
Source2: %name.conf
Source3: %name.sysconfig

# updated from inet: make p2c, make dnvt, make dnetter
Source4: ntop-p2c.opt.table.gz
Source5: ntop-oui.txt.gz
Source6: ntop-etter.finger.os.gz

Patch1: %name-free.patch
# TODO
Patch2: %name-plugins.patch
Patch3: %name-autoconf.patch

Patch4: %name-as-needed.patch

Patch11: %name-am.patch
Patch12: %name-running-user.patch
Patch13: %name-dbfile-default-dir.patch
Patch15: %name-path_to_dot.diff
Patch16: %name-automake_fixes.diff
Patch17: ntop-system_geoip.diff
Patch19: ntop-tmp-usage.patch
Patch20: ntop-disable-etter_fingerprint_download.patch
Patch21: ntop-no-wget.patch
Patch22: ntop-build-without-darwin.patch

%define _localstatedir		/var
%define ntopdir	%_localstatedir/lib/ntop

#Requires: GeoIP-Lite-City GeoIP-ASNum
Requires: /usr/share/GeoIP/GeoLiteCity.dat
Requires: /usr/share/GeoIP/GeoIPASNum.dat

# Automatically added by buildreq on Mon Oct 17 2011 (-bi)
BuildRequires: gcc-c++ libGeoIP-devel libevent-devel libgdbm-devel liblua5-devel libnet-snmp-devel libpam-devel libpcap-devel libpcre-devel librrd-devel lsb-core perl-PDF-ReportWriter perl-devel wget zlib-devel

# optimized out by libnet-snmp-devel
BuildRequires: libwrap-devel

%description
ntop is a network traffic probe that shows the network usage, similar to what
the popular top Unix command does. ntop is based on libpcap and it has been
written in a portable way in order to virtually run on every Unix platform and
on Win32 as well.

ntop users can use a a web browser (e.g. netscape) to navigate through ntop
(that acts as a web server) traffic information and get a dump of the network
status. In the latter case, ntop can be seen as a simple RMON-like agent with
an embedded web interface. The use of:

    * a web interface
    * limited configuration and administration via the web interface
    * reduced CPU and memory usage (they vary according to network size and
      traffic)

make ntop easy to use and suitable for monitoring various kind of networks.

ntop should be manually started the first time so that the administrator
password can be selected.

%prep
%setup -q -n %name-%version
%__subst "s|<pcre.h>|<pcre/pcre.h>|g" ntop.h
%__subst "s|pcre.h|pcre/pcre.h|g" configure.in

# kill libtool.m4 copy
cp -f acinclude.m4.ntop acinclude.m4

# executable bits are set on some config files and docs that go into 
# %%{_sysconfdir}/ntop and %%{_datadir}, and some debug source files.  Remove 
# the execute bits - in the build directory 
find . \( -name \*\.gz -o -name \*\.c -o -name \*\.h -o -name \*\.pdf \
     -o -name \*\.dtd -o -name \*\.html -o -name \*\.js \) -print     \
     | xargs chmod a-x

%patch1
# %patch2
%patch3
%patch4

%patch11 -p1 -b .am
%patch13 -p1 -b .dbfile-default-dir
%patch15 -p0 -b .dot
%patch16 -p1 -b .automake
%patch17 -p1
%patch19 -p2
%patch20 -p1
%patch21 -p1
%patch22 -p1


%build
#autoreconf
./autogen.sh  --noconfig
# "verified.awk -u" calls require gawk
%configure \
	AWK=gawk \
	--disable-static \
	--with-gnu-ld \
	--with-ossl-root=%prefix \
	--with-localedir=%_libdir/locale \
	--enable-snmp \
	--enable-jumbo-frames
# --enable-mysql

%make_build

%install
install -d %buildroot{%ntopdir,%_initrddir,%_sysconfdir,%_sysconfdir/sysconfig}

%makeinstall_std

install %SOURCE1 %buildroot%_initdir/ntop
install -m0644 %SOURCE2 %buildroot%_sysconfdir/ntop/ntop.conf
install -m0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/ntop
install -m0644 %SOURCE4 %buildroot%_sysconfdir/ntop/p2c.opt.table.gz
install -m0644 %SOURCE5 %buildroot%_sysconfdir/ntop/oui.txt.gz
install -m0644 %SOURCE6 %buildroot%_sysconfdir/ntop/etter.finger.os.gz

# we need devel package?
rm -f %buildroot%_libdir/*.{la,a}
rm -f %buildroot%_libdir/lib*Plugin*.so

# Create files to be %%ghost'ed - %%ghost'ed files must exist in the buildroot
install -d %buildroot%ntopdir/rrd/{flows,graphics}
install -d %buildroot%ntopdir/rrd/interfaces
touch %buildroot%ntopdir/{addressQueue,dnsCache,fingerprint,LsWatch,macPrefix,ntop_pw,prefsCache}.db

%pre
groupadd -r -f ntop || :
useradd -M -r -d %ntopdir -s /bin/false -c "ntop User" -g ntop ntop || :

%post
%post_service %name

%preun
%preun_service %name


%files
%doc AUTHORS ChangeLog NEWS README THANKS
%doc www docs NetFlow utils
%_sbindir/*
%_libdir/*.so
%_datadir/%name/
%dir %_libdir/%name/
%_libdir/%name/plugins/
%_man8dir/*
%_initdir/ntop
%attr(640,root,root) %config(noreplace) %_sysconfdir/sysconfig/ntop
%dir %_sysconfdir/ntop/
%config(noreplace) %_sysconfdir/ntop/ntop.conf
%_sysconfdir/ntop/*.gz
%config(noreplace) %_sysconfdir/ntop/*.pem
#%attr(644,root,ntop) %config(noreplace) %verify(not md5 mtime size) %_sysconfdir/ntop.conf

%attr (0770,root,ntop) %dir %ntopdir/
%defattr(0640,root,ntop,-)
%ghost %ntopdir/addressQueue.db
%ghost %ntopdir/dnsCache.db
%ghost %ntopdir/fingerprint.db
%ghost %ntopdir/LsWatch.db
%ghost %ntopdir/macPrefix.db
%ghost %ntopdir/ntop_pw.db
%ghost %ntopdir/prefsCache.db
# This will catch all the directories in rrd.  If %ghost'ed files are added
# under rrd, this will have to be changed to %dir and more directives for
# directories under rrd will have to be added.
%defattr(0770,root,ntop,-)
%ntopdir/rrd/


%changelog
* Mon Nov 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.1.0-alt1.1
- Rebuild with Python-2.7

* Wed Nov 02 2011 Alexey Shabalin <shaba@altlinux.ru> 4.1.0-alt1
- 4.1.0 (#26359)
- add post/preun_service (#14509)

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 3.3.10-alt2.2
- rebuilt for perl-5.14

* Sat Jun 25 2011 Igor Vlasenko <viy@altlinux.ru> 3.3.10-alt2.1.1
- rebuilt with libevent2

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.3.10-alt2.1
- rebuilt with perl 5.12

* Wed May 12 2010 Sergey Y. Afonin <asy@altlinux.ru> 3.3.10-alt2
- fix Repocop's tests: unsafe-tmp-usage-in-scripts, init-lsb
- remove fogot config description from init script

* Mon Apr 26 2010 Sergey Y. Afonin <asy@altlinux.ru> 3.3.10-alt1.1
- rebuild with rrd 1.4.3

* Wed Mar 03 2010 Alexey Shabalin <shaba@altlinux.ru> 3.3.10-alt1
- 3.3.10
- use system libGeoIP, GeoIP-Lite-City, GeoIP-ASNum

* Sun Dec 21 2008 Vitaly Lipatov <lav@altlinux.ru> 3.3.8-alt3
- add conf file in sysconfig
- add check if ntop already initializing during start (fix bug #18265)
- remove message after install
- remove post/postun sections
- update p2c.opt.table.gz, oui.txt.gz, etter.finger.os.gz

* Thu Dec 18 2008 Vitaly Lipatov <lav@altlinux.ru> 3.3.8-alt2
- build for Sisyphus

* Mon Dec 15 2008 Alexey Shabalin <shaba@altlinux.ru> 3.3.8-alt1
- 3.3.8
- move binary to %_sbindir
- fix description in init script
- some changes in init scripts
- add and revised patches from PLD, fedora, mandriva

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 3.3-alt3.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Mon Jun 23 2008 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt3
- set locale dir (fix bug #15207)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt2
- update Summary, description
- remove chmod/chown from pre section, add ghost files to /var/lib/ntop
- cleanup spec, add some ideas from FC specs (written by Bernard Johnson)

* Sun Oct 21 2007 Vitaly Lipatov <lav@altlinux.ru> 3.3-alt1
- fix compiling, update buildreq
- add --enable-sslv3 --enable-jumbo-frames to configure

* Thu Jun 28 2007 Vitaly Lipatov <lav@altlinux.ru> 3.3rel-alt1
- new version (3.3rel)

* Sat Apr 28 2007 Vitaly Lipatov <lav@altlinux.ru> 3.3rc1-alt1
- new version (3.3rc1)

* Mon Sep 11 2006 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt0.2
- change Packager, cleanup spec
- unresolved=relaxed :(

* Wed Dec 14 2005 Anton Korbin <ahtoh@altlinux.ru> 3.2-alt0.1
- First new version for Alt Linux

* Wed Nov 02 2005 Vitaly Lipatov <lav@altlinux.ru> 3.1-alt0.1
- spec from PLD Team <feedback@pld-linux.org> (thanks)
