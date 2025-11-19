%global _unpackaged_files_terminate_build 1

Name: cachefilesd
Version: 0.10.10
Release: alt1

Summary: CacheFiles user-space management daemon
License: GPLv2+
Group: Networking/Other
Url: http://people.redhat.com/~dhowells/fscache/

Source: %name-%version.tar
Patch: %name-%version.patch

%description
The cachefilesd daemon manages the caching files and directory that are that
are used by network file systems such a AFS and NFS to do persistent caching to
the local disk.

%prep
%setup
%patch -p1

%build
make all \
    ETCDIR=%_sysconfdir \
    SBINDIR=%_sbindir \
    MANDIR=%_mandir \
    CFLAGS="-Wall -Werror $RPM_OPT_FLAGS"

%install
mkdir -p %buildroot{%_sbindir,%_unitdir,%_initdir,%_man5dir,%_man8dir,%_cachedir/fscache}
make install \
    DESTDIR=%buildroot \
    ETCDIR=%_sysconfdir \
    SBINDIR=%_sbindir \
    MANDIR=%_mandir \
    CFLAGS="-Wall -Werror $RPM_OPT_FLAGS"

install -m 755 cachefilesd.initd %buildroot%_initdir/cachefilesd
install -m 644 cachefilesd.conf %buildroot%_sysconfdir/cachefilesd.conf
install -m 644 cachefilesd.service %buildroot%_unitdir/cachefilesd.service

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README howto.txt
%config(noreplace) %_sysconfdir/cachefilesd.conf
%_initdir/%name
%_unitdir/%name.service
%_sbindir/%name
%_man5dir/*
%_man8dir/*

%dir %attr(700,root,root) %_cachedir/fscache

%changelog
* Wed Nov 19 2025 Alexey Shabalin <shaba@altlinux.org> 0.10.10-alt1
- 0.10.10.

* Wed Mar 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.10.1-alt1.qa2
- NMU: added URL

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.10.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 16 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 released

* Thu Jul  2 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- Initial build

