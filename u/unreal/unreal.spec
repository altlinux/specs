%define chroot %_localstatedir/%name

Name: unreal
Version: 3.2.8.1
Release: alt1

Summary: UnrealIRCD is a powerful irc daemon
License: GPL
Group: Networking/IRC

URL: http://www.unrealircd.org
Source0: Unreal%version.tar
Source1: %name.init
Source6: uircd.chroot.all
Source7: uircd.chroot.conf
Source8: uircd.chroot.lib
Source9: uircd.chroot.bin
Source10: uircd.chroot.log
Source11: uircd.motd
Source12: uircd.rules
Source13: uircd.tune
Source14: %name.sysconfig

# Automatically added by buildreq on Wed Dec 05 2007
BuildRequires: libssl-devel openssl zlib-devel

PreReq: /etc/chroot.d
Requires: chrooted openssl libssl zlib cert-sh-functions

%description
Unreal was created from the Dreamforge IRCd that was
formerly used by the DALnet IRC Network. Over the years,
many new and exciting features have been added to Unreal.
UnrealIRCd is designed to be an advanced IRCd, so it is
probably not the best choice for beginners.

%package doc
Summary: Documentation files for Unreal IRC daemon
Summary(ru_RU.KOI8-R): Документация irc сервера Unreal
Group: Networking/IRC
BuildArch: noarch
Provides: unreal-doc = %version-%release

%description doc
Documentation files for Unreal IRC daemon

%prep
%setup -n Unreal3.2
find . -type d -name CVS -print0 | xargs -0 rm -rf -- ||:

%build 
%configure \
	--with-showlistmodes \
	--enable-nospoof \
	--enable-hub \
	--enable-ssl \
	--enable-ziplinks \
	--enable-prefixaq \
	--with-listen=5 \
	--with-dpath=%chroot \
	--with-spath=%_sbindir/uircd \
	--with-nick-history=2000 \
	--with-sendq=3000000 \
	--with-bufferpool=18 \
	--with-permissions=0600 \
	--with-fd-setsize=1024 \
	--enable-dynamic-linking
	
%make_build

%install

install -pD -m0755 %SOURCE1 %buildroot%_initdir/%name
install -pD -m0755 %SOURCE14 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_sysconfdir/unrealircd/{aliases,ssl}
mkdir -p %buildroot%_sbindir
mkdir -p %buildroot%_libdir/%name/modules
mkdir -p %buildroot%chroot/aliases
mkdir -p %buildroot%chroot%_sysconfdir
mkdir -p %buildroot%chroot/dev
mkdir -p %buildroot%chroot%_var/run
mkdir -p %buildroot%chroot/{lib,lib64}
mkdir -p %buildroot%chroot/tmp
mkdir -p %buildroot%chroot/bin
mkdir -p %buildroot%chroot/modules
mkdir -p %buildroot%chroot%_sbindir
install -pD -m640 doc/example.conf %buildroot%_sysconfdir/unrealircd/unrealircd.conf
install -pD -m640 %SOURCE11 %buildroot%_sysconfdir/unrealircd/uircd.motd
install -pD -m640 %SOURCE12 %buildroot%_sysconfdir/unrealircd/uircd.rules
install -pD -m640 %SOURCE13 %buildroot%_sysconfdir/unrealircd/ircd.tune
cp *.conf %buildroot%_sysconfdir/unrealircd/
cp aliases/*.conf %buildroot%_sysconfdir/unrealircd/aliases/
cp src/modules/*.so %buildroot%_libdir/%name/modules/
cp src/ircd %buildroot%_sbindir/uircd
install -m 0750 -D %SOURCE6 %buildroot%_sysconfdir/chroot.d/%name.all
install -m 0750 -D %SOURCE7 %buildroot%_sysconfdir/chroot.d/%name.conf
install -m 0750 -D %SOURCE8 %buildroot%_sysconfdir/chroot.d/%name.lib
install -m 0750 -D %SOURCE9 %buildroot%_sysconfdir/chroot.d/%name.bin
install -m 0750 -D %SOURCE10 %buildroot%_sysconfdir/chroot.d/%name.log
install -pDm0755 networks/makenet %buildroot%_bindir/%name-makenet

touch %buildroot%_sysconfdir/unrealircd/ssl/unreal.cert
touch %buildroot%_sysconfdir/unrealircd/ssl/unreal.csr
touch %buildroot%_sysconfdir/unrealircd/ssl/unreal.key

%pre
if [ $1 = 1 ]; then
	%_sbindir/groupadd -r uircd >/dev/null 2>&1 ||:
	%_sbindir/useradd -M -r uircd -g uircd -s /dev/null -c "Unreal IRC server" \
	-d %_localstatedir/%name >/dev/null 2>&1 ||:
fi

%post
%post_service %name

%preun
%preun_service %name
subst 's,-a %chroot/dev/log,,' %_sysconfdir/sysconfig/syslogd >/dev/null 2>&1 ||:

%files
%doc Changes Donation INSTALL.REMOTEINC README
%config %_sysconfdir/chroot.d/*
%config(noreplace) %_sysconfdir/unrealircd/*.conf
%config(noreplace) %_sysconfdir/unrealircd/ircd.tune
%config(noreplace) %_sysconfdir/unrealircd/uircd*
%config(noreplace) %_sysconfdir/unrealircd/aliases/*.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %_sysconfdir/unrealircd
%dir %_sysconfdir/unrealircd/aliases
%dir %attr(750,root,uircd) %_sysconfdir/unrealircd/ssl
%ghost %attr(640,root,uircd) %verify(not md5 mtime size) %_sysconfdir/unrealircd/ssl/unreal.cert
%ghost %attr(640,root,uircd) %verify(not md5 mtime size) %_sysconfdir/unrealircd/ssl/unreal.csr
%ghost %attr(640,root,uircd) %verify(not md5 mtime size) %_sysconfdir/unrealircd/ssl/unreal.key
%_initdir/%name
%_libdir/%name/modules/commands.so
%_libdir/%name/modules/cloak.so
%exclude %_libdir/%name/modules/m_*.so
%_sbindir/uircd
%_bindir/%name-makenet
%dir %attr(1770,root,uircd) %chroot
%dir %chroot/etc
%dir %chroot/aliases
%dir %chroot/dev
%dir %chroot%_var/run
%dir %chroot/lib
%dir %chroot/lib64
%dir %chroot/tmp
%dir %chroot/usr
%dir %chroot/var
%dir %chroot/modules
%dir %chroot%_sbindir

%files doc
%doc doc

%changelog
* Wed Oct 13 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 3.2.8.1-alt1
- 3.2.8.1. Security fix:
  http://www.unrealircd.com/txt/unrealsecadvisory.20090413.txt

* Thu Mar 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 3.2.8-alt1
- 3.2.8

* Mon Dec 01 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 3.2.7-alt6
- Rebuild with libcrypto.so.7/libssl.so.7
- Package "-doc" subpackage as noarch

* Wed Jun 18 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.7-alt5
- Fixed %%preun script (Closes: #16077)

* Tue Jun 17 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.7-alt4
- Fixed directory packaging according to new sisyphus_check

* Tue Jan 29 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.7-alt3
- Remove autogenerated ssl-certs after package uninstall
- Initscript fixes:
  + Fixed permissions of ssl-certs
  + Fix typo in adjust() message
  + Don't use full path for binary

* Mon Aug 13 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.7-alt2
- Remove CVS metadata at build-time. Closes: #12538
- Remove altlinux real domain from example config and maintainer's email
- Listen only on 127.0.0.1 by default
- Silently ignore `service syslogd reload` fail

* Sat Aug 04 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.7-alt1
- 3.2.7

* Tue Apr 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.6-alt3
- Use cert-sh-functions for ssl certificate generation
- Do not start on any runlevel by default
- Do not install many networks files (who needs this?)
- Move makenet to /usr/bin, rename to unreal-makenet

* Mon Feb 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.6-alt2
- Use urandom instead of random

* Tue Jan 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.6-alt1
- 3.2.6
- Do not package modules as separate packages. I don't know why this is done
  in the past, all these modules are contained in the library commands.so

* Thu Dec 21 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.5-alt3
- No more ugly output in initscript (Closes: #10466)
- Intergate patches into source tree

* Mon Oct 02 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.5-alt2
- x86_64 fixes (corrected pathes to libraries)
- Corrected *.pem permissions
- Now use symlink /etc/syslog.d/unreal for provide dev/log in chroot
- Added sysconfig/%name file

* Mon Jun 05 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 3.2.5-alt1
- 3.2.5
- unreal-chroot-alt.patch rediffed and renamed to unreal-3.2.5-alt-chroot.patch
- Updated BuildRequires (s,pkgconfig,pkg-config)
- Corrected chroot permissions (Closes: #9606)
- Improved initscript - add `service unreal rehash` support (Closes: #9639)
- Change Packager

* Thu Jun 02 2005 Vitaly Smirnov <device@altlinux.org> 3.2.3-alt0.9
- Fixed #6992

* Sat May 28 2005 Vitaly Smirnov <device@altlinux.org> 3.2.3-alt0.8
- No fixed uid/gid values needed anymore
- Don't remove uircd user on uninstall

* Wed Apr 27 2005 Vitaly Smirnov <device@altlinux.org> 3.2.3-alt0.7
- Inital build for Sisyphus
