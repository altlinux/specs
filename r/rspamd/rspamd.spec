# TODO: add .pc-file to libhiredis-devel (to build with one)
Name: rspamd
Version: 1.8.3
Release: alt1

Summary: Fast and modular antispam system written in C

License: BSD
Group: Networking/Other
Url: https://rspamd.com/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/rspamd/rspamd/archive/%version.tar.gz
Source: %name-%version.tar
Source1: %name.init

BuildRequires: cmake libdb4-devel libevent-devel libgmime-devel liblua5-devel
BuildRequires: libpcre2-devel libsqlite3-devel python-module-paste libunwind-devel libicu-devel
BuildRequires: libssl-devel libmagic-devel zlib-devel libluajit-devel

BuildRequires: perl-XML-Parser perl-Term-Cap perl-Pod-Usage

BuildRequires: ragel

BuildRequires(pre): rpm-build-intro

%add_verify_elf_skiplist %_libdir/rspamd/lib*.so
#./usr/lib64/librspamd-actrie.so

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
#__subst 's|SET(ETC_PREFIX "\${CMAKE_INSTALL_PREFIX}/etc")|SET(ETC_PREFIX "/etc")|g' CMakeLists.txt
#__subst 's|gmime-2.4|gmime-2.6|g' CMakeLists.txt
#__subst 's|TARGET_LINK_LIBRARIES(rspamdclient pcre)|TARGET_LINK_LIBRARIES(rspamdclient pcre m)|g' lib/CMakeLists.txt
%cmake_insource -DSYSTEMDDIR=%{_unitdir} \
                -DENABLE_LUAJIT=ON \
                -DLIBDIR=%{_libdir}/rspamd/ \
                -DNO_SHARED=ON \
                -DENABLE_LIBUNWIND=ON \
                -DENABLE_PCRE2=ON \
                -DCONFDIR=%{_sysconfdir}/rspamd \
                -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF

%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_runtimedir/%name/

mkdir -p %buildroot/%_datadir/
#mv -f %buildroot/usr/man/ %buildroot/%_datadir/
#mv -f %buildroot/usr/etc/ %buildroot/
#test -d %buildroot%_libdir/ || mv -f %buildroot/usr/lib/ %buildroot%_libdir/
#mv %buildroot/%_libdir/rspamd/librspamd-actrie.so %buildroot%_libdir/

#mv -f %buildroot%_sysconfdir/%name.xml.sample %buildroot%_sysconfdir/%name/%name

# TODO
rm -f %buildroot%_includedir/librspamdclient.h
rm -f %buildroot%_libdir/librspamdclient_static.a
rm -rf %buildroot/etc/init.d/

mkdir -p %buildroot%_sysconfigdir/
touch %buildroot%_sysconfigdir/%name

install -m755 -D %SOURCE1 %buildroot%_initddir/%name

%files
%config(noreplace) %_initddir/%name
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/modules.d/
%dir %_sysconfdir/%name/scores.d/
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/modules.d/*.conf
%config(noreplace) %_sysconfdir/%name/scores.d/*.conf
%config(noreplace) %_sysconfdir/%name/*.inc
%config(noreplace) %_sysconfigdir/%name
%_bindir/rspamc*
%_bindir/rspamd*
%_bindir/rspamadm*
%_datadir/rspamd/
#_libdir/librspamdclient.so.*
%_libdir/%name/*.so
%_man1dir/*
%_man8dir/*
%attr(0710,root,root) %dir %_runtimedir/%name/

%changelog
* Thu Feb 21 2019 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- build new version

* Tue Feb 07 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.7-alt1.1
- NMU: rebuild with new lua 5.1

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 0.4.7-alt1
- new build 0.4.7
- ALT specific init script

* Wed Jun 15 2011 Vitaly Lipatov <lav@altlinux.ru> 0.3.14-alt1
- new build 0.3.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.3.2-alt1.1
- rebuilt with perl 5.12

* Sun Oct 17 2010 Vitaly Lipatov <lav@altlinux.ru> 0.3.2-alt1
- initial build for ALT Linux Sisyphus
