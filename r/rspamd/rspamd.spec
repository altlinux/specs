# TODO: add .pc-file to libhiredis-devel (to build with one)
Name: rspamd
Version: 0.4.7
Release: alt1

Summary: Fast and modular antispam system written in C

License: BSD
Group: Networking/Other
Url: http://bitbucket.org/vstakhov/rspamd/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Original repo cloning instruction:
# $ hg clone http://bitbucket.org/vstakhov/rspamd rspamd.hg
# $ mkdir rspamd && cd mkdir rspamd
# $ hg-fast-export -r ../rspamd.hg [--force]
# $ git branch

# For update hg:
# $ hg pull ; hg update
# $ cd rspamd (check branch hg after)
# $ hg-fast-export -r ../rspamd.hg [--force]

Source: %name-%version.tar
Source1: %name.init

# Automatically added by buildreq on Sat May 05 2012
# optimized out: cmake cmake-modules glib2-devel libgio-devel libgpg-error pkg-config python-base python-module-distribute python-module-peak python-module-zope python-modules
# BuildRequires: ccmake dpkg git-core glibc-devel-static libbsd-devel libdb4-devel libevent-devel libgmime-devel liblua5-devel libpcre-devel libsqlite3-devel mercurial python-module-mwlib python-module-paste
BuildRequires: ccmake libbsd-devel libdb4-devel libevent-devel libgmime-devel liblua5-devel libpcre-devel libsqlite3-devel python-module-mwlib python-module-paste

BuildPreReq: perl-XML-Parser perl-Term-Cap

BuildPreReq(pre): rpm-build-intro

%description
Rspamd filtering system is created as a replacement of popular
spamassassin spamd and is designed to be fast, modular and easily
extendable system. Rspamd core is written in C language using event
driven paradigma. Plugins for rspamd can be written in lua. Rspamd is
designed to process connections completely asynchronous and do not block
anywhere in code.

%prep
%setup

%build
#__subst "s|/init.d|/rc.d/init.d|g" CMakeLists.txt
%__subst 's|SET(ETC_PREFIX "\${CMAKE_INSTALL_PREFIX}/etc")|SET(ETC_PREFIX "/etc")|g' CMakeLists.txt
%__subst 's|gmime-2.4|gmime-2.6|g' CMakeLists.txt
%__subst 's|TARGET_LINK_LIBRARIES(rspamdclient pcre)|TARGET_LINK_LIBRARIES(rspamdclient pcre m)|g' lib/CMakeLists.txt
%cmake_insource
# SMP incompatible build
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_runtimedir/%name/

mkdir -p %buildroot%_datadir/
#mv -f %buildroot/usr/man/ %buildroot/%_datadir/
#mv -f %buildroot/usr/etc/ %buildroot/
test -d %buildroot%_libdir/ || mv -f %buildroot/usr/lib/ %buildroot%_libdir/

mv -f %buildroot%_sysconfdir/%name.xml.sample %buildroot%_sysconfdir/%name/%name

# TODO
rm -f %buildroot%_includedir/librspamdclient.h
rm -f %buildroot%_libdir/librspamdclient_static.a
rm -rf %buildroot/etc/init.d/

mkdir -p %buildroot%_sysconfigdir/
touch %buildroot%_sysconfigdir/%name

install -m755 -D %SOURCE1 %buildroot%_initddir/%name

%files
%config(noreplace) %_initddir/%name
%_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/%name
%config(noreplace) %_sysconfdir/%name/*.inc
%config(noreplace) %_sysconfigdir/%name
%_bindir/rspamc*
%_bindir/rspamd*
%_libdir/librspamdclient.so.*
%_libdir/*.so
%_man1dir/*
%_man8dir/*
%attr(0710,root,root) %dir %_runtimedir/%name/

%changelog
* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt1
- new build 0.4.7
- ALT specific init script

* Wed Jun 15 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.14-alt1
- new build 0.3.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1.1
- rebuilt with perl 5.12

* Sun Oct 17 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
