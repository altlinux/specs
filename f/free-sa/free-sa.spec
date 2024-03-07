%define _htmldir /var/www/html

Name: free-sa
Version: 1.6.2
Release: alt4

Packager: Avramenko Andrew <liks@altlinux.ru>
Summary: Squid report generator per user/ip/name
URL: http://free-sa.sourceforge.net/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch
Patch1: %name-1.6.2-alt-no-strip.patch
Patch2: %name-%version-alt-gcc-10-fno-common.patch
Patch3: %name-%version-alt-anyarch.patch
Patch4: %name-%version-alt-2big2inline.patch

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
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2

%build
%make OSTYPE=altlinux-generic-gcc

%install
make install DESTDIR=%buildroot OSTYPE=altlinux-generic-gcc
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
* Thu Mar 07 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.6.2-alt4
- NMU: build for all architectures

* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 1.6.2-alt3.3
- Fixed build with gcc-10 (-fno-common FTBFS)

* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt3.2
- Fixed build with gcc 4.7

* Wed Jul 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.2-alt3.1
- Fixed build

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt3
- remove buildroot path from comments in default config

* Tue May 19 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt2
- forgotten directories added

* Tue May 19 2009 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- new version

* Tue Aug  7 2007 Avramenko Andrew <liks@altlinux.ru> 1.3.3-alt1
- Initial build for sisyphus.
