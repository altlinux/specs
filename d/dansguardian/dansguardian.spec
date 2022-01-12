Name: dansguardian
Version: 2.12.0.3
Release: alt3.1

Summary: Content filter
Summary(ru_RU.UTF-8): Фильтр WEB-содержимого
License: GPLv2
Url: http://www.dansguardian.org
Group: System/Servers

Source0: %name-%version.tar
Patch1: %name-%version-alt.patch
Patch2: %name-lists-2.9.8.1.patch
Patch3: %name-2.10.1.1-alt-gcc4.6.patch

BuildRequires: gcc-c++ libpcre-devel zlib-devel

%description
DansGuardian is a web content filtering proxy that uses Squid to do all the fetching.
It filters using multiple methods. These methods include URL and domain filtering,
content phrase filtering, PICS filtering, MIME filtering, file extension filtering,
POST limiting.

%description -l ru_RU.UTF-8
DansGuardian - фильтр WEB содержимого, который использует Squid для получения данных.
Предусмотрена возможность фильтрации несколькими методами. Эти методы включают фильтрацию
по URL и имени домена, по фразам, по картинкам, по типам MIME, по расширению файлов, ограничение
метода POST.

%prep
%setup -q
%patch1 -p1
%patch2
%patch3 -p2

%build
%add_optflags -std=c++11 
%configure  --enable-clamd \
	    --enable-ntlm \
	    --with-logdir=/var/log/%name \
	    --with-proxyuser=%name \
	    --with-proxygroup=%name \
	    --with-piddir=/var/run \
#	    --with-dgdebug

%make_build

%install
make install DESTDIR=%buildroot
cd data/languages; %make_install; cd ../..
mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_initdir
mkdir -p %buildroot/var/run/%name
mkdir -p %buildroot%_sysconfdir/logrotate.d
install -p -m 0755 data/scripts/systemv-init %buildroot%_initdir/%name
install -p data/scripts/%name %buildroot%_sysconfdir/logrotate.d/
rm -rf %buildroot/usr/share/doc/%name

%pre
%_sbindir/groupadd -r -f %name >/dev/null 2>&1
%_sbindir/useradd -r -n -g %name -d /dev/null -s /dev/null %name >/dev/null 2>&1 ||:

%preun
%preun_service %name

%post
%post_service %name

%files
%config(noreplace) %_sysconfdir/%name/*
%doc INSTALL AUTHORS README NEWS COPYING doc/AuthPlugins doc/ContentScanners doc/DownloadManagers doc/FAQ doc/FAQ.html doc/Plugins
%_sbindir/*
%_datadir/%name/*
%_man8dir/*
%attr(2770,root,%name) %dir %_logdir/%name
%attr(755,root,root) %_initdir/*
%attr(644,root,root) %_sysconfdir/logrotate.d/*
%attr(2775,root,%name) /var/run/%name

%changelog
* Wed Jan 12 2022 Andrey Cherepanov <cas@altlinux.org> 2.12.0.3-alt3.1
- FTBFS: fix build with gcc11.

* Sat Jun 22 2019 Igor Vlasenko <viy@altlinux.ru> 2.12.0.3-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.12.0.3-alt2
- NMU: remove %ubt from release

* Wed May 10 2017 Anton Farygin <rider@altlinux.ru> 2.12.0.3-alt1%ubt
- new version

* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 2.10.1.1-alt3.1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Tue Jul 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.10.1.1-alt3.1
- Fixed build

* Sun Jul 19 2009 Sergey Y. Afonin <asy@altlinux.ru> 2.10.1.1-alt3
- NMU
- ClamAV support disabled (can not build with new libclamav)

* Tue May 26 2009 Anton Farygin <rider@altlinux.ru> 2.10.1.1-alt2
- squid-server and clamav removed from requires
- fixed non-latin-1 charsets support in phrase lists
- extend russian phrase lists (porno, bad worlds)

* Mon May 18 2009 Anton Farygin <rider@altlinux.ru> 2.10.1.1-alt1
- update to new version

* Mon May 18 2009 Anton Farygin <rider@altlinux.ru> 2.10.0.3-alt1
- new version
- rewrited initscript
- fixed build on Sisyphus

* Fri Sep 19 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.9.9.8-alt1
- New version

* Fri Sep 19 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.9.9.7-alt1
- New version

* Wed Aug 13 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.9.9.6-alt1
- New version

* Wed Jun 25 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.9.9.5-alt1
- New version
- Some changes in init script

* Thu Jun 05 2008 Vladimir Scherbaev <vladimir@altlinux.org> 2.9.9.4-alt1
- New version

* Wed Dec 19 2007 Avramenko Andrew <liks@altlinux.ru> 2.9.9.2-alt1
- New version
- Remove dependence on clamav (I think libclamav is enough)
- Fix permissions on several directories (due to policy)

* Mon Sep 10 2007 Avramenko Andrew <liks@altlinux.ru> 2.9.9.1-alt1
- New version
- Patch for man (thanks to php-coder)

* Fri Apr 13 2007 Avramenko Andrew <liks@altlinux.ru> 2.9.8.5-alt2
- Spec clean up
- Moved to git repo

* Fri Mar 30 2007 Avramenko Andrew <liks@altlinux.ru> 2.9.8.5-alt1
- New version build
- SPEC clean up
- Add user/group dansguardian
- Add clamav support (fixed troubles with -lidn)
- Add docs
- Add logrotate
- Add languages

* Mon Mar 12 2007 Avramenko Andrew <liks@altlinux.ru> 2.9.8.2-alt1
- New version build

* Wed Dec 27 2006 Avramenko Andrew <liks@altlinux.ru> 2.9.8.1-alt2
- Patch for blacklists (rambler have not to be blocked by default)

* Thu Dec 21 2006 Avramenko Andrew <liks@altlinux.ru> 2.9.8.1-alt1
- New version build
- Clamd support
- ClamAV support disabled (troubles with -lidn)
- NTLM support

* Tue Jul 18 2006 Avramenko Andrew <liks@altlinux.ru> 2.9.7.1-alt1
- New version build

* Tue May 30 2006 Avramenko Andrew <liks@altlinux.ru> 2.9.7.0-alt1
- New version build
- ClamAV support

* Sun Jan 29 2006 Avramenko Andrew <liks@altlinux.ru> 2.9.5.0-alt1
- Initial build
