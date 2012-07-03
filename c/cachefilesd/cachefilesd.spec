Name: cachefilesd
Version: 0.10.1
Release: alt1

Summary: caching backend for use with FS-Cache
License: GPL
Group: Networking/Other

Source: %name-%version-%release.tar

%description
CacheFiles is a caching backend that's meant to use as a cache a directory on
an already mounted filesystem of a local type (such as Ext3).

%prep
%setup

%build
make

%install
make install DESTDIR=%buildroot
install -pD -m0755 cachefilesd.initd %buildroot%_initdir/cachefilesd
mkdir -p %buildroot%_cachedir/fscache

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README howto.txt
%config(noreplace) %_sysconfdir/cachefilesd.conf

%_initdir/%name

/sbin/cachefilesd

%_man5dir/*
%_man8dir/*

%dir %attr(700,root,root) %_cachedir/fscache

%changelog
* Tue Nov 16 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.1-alt1
- 0.10.1 released

* Thu Jul  2 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9-alt1
- Initial build

