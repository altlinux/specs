%define _htmldir /var/www/html

Name: free-sa
Version: 1.6.2
Release: alt3

Packager: Avramenko Andrew <liks@altlinux.ru>
Summary: Squid report generator per user/ip/name
URL: http://free-sa.sourceforge.net/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
ExclusiveArch: i586 x86_64

License: GPL
Group: Monitoring

%description
Free-SA is statistic analyzer for daemons log files similar to SARG. 
Its main advantages over SARG are much better speed (7x-20x times), 
more reports support, crossplatform work and W3C compliance of generated 
HTML/CSS reports code.

%prep
%setup -q
%patch0 -p1

%build
%make OSTYPE=altlinux-%_target_cpu-gcc4

%install
make install DESTDIR=%buildroot OSTYPE=altlinux-%_target_cpu-gcc4
mkdir -p %buildroot/%_mandir
mkdir -p %buildroot/%_sysconfdir/%name
mv %buildroot/usr/man/* %buildroot/%_mandir/
rm -rf %buildroot/usr/man
mv %buildroot%_sysconfdir/%name/%name.conf.sample %buildroot/%_sysconfdir/%name/%name.conf
subst "s,%buildroot,," %buildroot/%_sysconfdir/%name/%name.conf

%files
%defattr(-,root,squid)
%_man1dir/*
%_man5dir/*
%_bindir/%name
%_datadir/%name
%_datadir/doc/%name-%version
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/*
%attr(0775,root,squid) %dir %_htmldir/%name
%_htmldir/%name/*
%dir /var/cache/%name

%changelog
* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt3
- remove buildroot path from comments in default config

* Tue May 19 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt2
- forgotten directories added

* Tue May 19 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- new version

* Tue Aug  7 2007 Avramenko Andrew <liks@altlinux.ru> 1.3.3-alt1
- Initial build for sisyphus.
