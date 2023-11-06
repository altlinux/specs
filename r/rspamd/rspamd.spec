#define optflags_lto %nil

# TODO: add .pc-file to libhiredis-devel (to build with one)
Name: rspamd
Version: 3.7.3
Release: alt2

Summary: Fast and modular antispam system written in C

License: BSD
Group: Networking/Other
Url: https://rspamd.com/

# Source-url: https://github.com/rspamd/rspamd/archive/%version.tar.gz
Source: %name-%version.tar
Source1: %name.init
Source3: %name.service
Source4: %name.sysconfig
Source5: %name.logrotate

Patch1: rspamd-fix-error.patch
Patch3500: rspamd-loongarch.patch

BuildRequires: gcc-c++
BuildRequires: cmake libdb4-devel libevent-devel libgmime-devel liblua5-devel
BuildRequires: libpcre2-devel libsqlite3-devel libunwind-devel libicu-devel
BuildRequires: libssl-devel libmagic-devel zlib-devel libluajit-devel libsodium-devel
BuildRequires: libxxhash-devel libzstd-devel doctest-devel libfmt-devel

BuildRequires: perl-XML-Parser perl-Term-Cap perl-Pod-Usage

BuildRequires: ragel

BuildRequires(pre): rpm-build-intro

#add_verify_elf_skiplist %_libdir/rspamd/lib*.so
#./usr/lib64/librspamd-actrie.so

AutoReq: yes,nolua

%description
Rspamd filtering system is created as a replacement of popular
spamassassin spamd and is designed to be fast, modular and easily
extendable system. Rspamd core is written in C language using event
driven paradigma. Plugins for rspamd can be written in lua. Rspamd is
designed to process connections completely asynchronous and do not block
anywhere in code.

%prep
%setup
%patch1 -p2
%patch3500 -p1

%build
%cmake_insource -DSYSTEMDDIR=%{_unitdir} \
                -DENABLE_LUAJIT=ON \
                -DLIBDIR=%{_libdir}/rspamd/ \
                -DRUNDIR=/run \
                -DNO_SHARED=ON \
                -DENABLE_LIBUNWIND=ON \
                -DENABLE_PCRE2=ON \
                -DCONFDIR=%{_sysconfdir}/rspamd \
                -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF -DCMAKE_SKIP_RPATH:BOOL=OFF \
                -DSYSTEM_ZSTD=ON \
                -DSYSTEM_FMT=ON \
                -DSYSTEM_DOCTEST=ON \
                -DSYSTEM_XXHASH=ON

%make_build

%install
%makeinstall_std
mkdir -p %buildroot/%_datadir/

# TODO
rm -f %buildroot%_includedir/librspamdclient.h
rm -f %buildroot%_libdir/librspamdclient_static.a
rm -rf %buildroot/etc/init.d/

install -d -m 0750 %buildroot%_sysconfdir/%name/local.d/
install -d -m 0750 %buildroot%_sysconfdir/%name/override.d/
install -d -m 0770 %buildroot%_localstatedir/%name
install -d -m 0770 %buildroot%_logdir/%name

install -pD -m 0755 %SOURCE1 %buildroot%_initddir/%name
install -pD -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -pD -m 0644 %SOURCE4 %buildroot%_sysconfigdir/%name
install -pD -m 0644 %SOURCE5 %buildroot%_logrotatedir/%name

%pre
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -N -M -g %name -d /dev/null -s /dev/null %name 2>/dev/null ||:

%files
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/maps.d/
%dir %_sysconfdir/%name/modules.d/
%dir %_sysconfdir/%name/scores.d/
%dir %_libdir/%name/
%dir %attr(0750,root,rspamd) %_sysconfdir/%name/local.d/
%dir %attr(0750,root,rspamd) %_sysconfdir/%name/override.d/
%config(noreplace) %_sysconfdir/%name/*.conf
%config(noreplace) %_sysconfdir/%name/maps.d/*.inc
%config(noreplace) %_sysconfdir/%name/modules.d/*.conf
%config(noreplace) %_sysconfdir/%name/scores.d/*.conf
%config(noreplace) %_sysconfdir/%name/*.inc
%config(noreplace) %_sysconfigdir/%name
%config(noreplace) %_logrotatedir/%name
%_bindir/rspamc*
%_bindir/rspamd*
%_bindir/rspamadm*
%_libdir/%name/*.so
%_initddir/%name
%_datadir/rspamd/
%_unitdir/*
%_man1dir/*
%_man8dir/*
%dir %attr(0770,root,rspamd) %_localstatedir/rspamd
%dir %attr(0770,root,rspamd) %_logdir/rspamd

%changelog
* Mon Nov 06 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 3.7.3-alt2
- NMU: fixed FTBFS on LoongArch

* Mon Nov 06 2023 Vitaly Lipatov <lav@altlinux.ru> 3.7.3-alt1
- new version 3.7.3 (with rpmrb script)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 3.5-alt1
- new version 3.5 (with rpmrb script)
- build with system libxxhash-devel libzstd-devel doctest-devel libfmt-devel
- add AutoReq: yes,nolua (all lua requires are internal: rspamd/lualib)

* Sun Apr 23 2023 Vitaly Lipatov <lav@altlinux.ru> 3.4-alt1
- new version 3.4 (with rpmrb script)

* Tue Apr 05 2022 Vitaly Lipatov <lav@altlinux.ru> 3.2-alt1
- new version 3.2 (with rpmrb script)

* Sat Jul 17 2021 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.7-alt1
- 2.7 release

* Tue Jul 13 2021 Vitaly Lipatov <lav@altlinux.ru> 2.6-alt2
- drop unneeded BR: python-module-paste

* Tue Oct 06 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.6-alt1
- 2.6 release
- logrotate post-rotate script systemd/sysvinit detection

* Wed Apr 22 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.5-alt1
- 2.5 release

* Fri Mar 27 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.4-alt1
- 2.4 release

* Thu Feb 06 2020 Dmitriy D. Shadrinov <shadrinov@altlinux.org> 2.3-alt1
- 2.3 release

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
