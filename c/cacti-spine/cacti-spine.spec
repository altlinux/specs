
Name: cacti-spine
Version: 1.2.23
Release: alt1

License: GPL2
Group: Monitoring

Summary: Fast c-based poller for package Cacti
Summary(ru_RU.UTF8): Быстрый сборщик данных для Cacti, написанный на языке C

URL: http://www.cacti.net
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: %name-1.2.0-alt-mysql8-transition.patch

Obsoletes: cacti-cactid
Provides: cacti-cactid = %version-%release

# since cacti-0.8.7e-alt2 chenged log and config path
Requires: cacti >= 0.8.7e-alt2
BuildRequires: libcap-devel libmysqlclient-devel libnet-snmp-devel zlib-devel libssl-devel
BuildRequires: help2man

%description
Spine is a supplemental poller for Cacti that makes use of pthreads to
achieve excellent performance.

%description -l ru_RU.UTF8
Spine -  это дополнительный сборщик информации для Cacti, который использует
pthreads для достижения высокой производительности.

%prep
%setup -q
%patch -p1
%patch1 -p0

%build
%autoreconf
%configure
#--enable-lcap
%make_build

%install
%makeinstall_std
mv %buildroot%_sysconfdir/cacti/{spine.conf.dist,spine.conf}

%files
%config(noreplace) %attr(0640,root,cacti) %_sysconfdir/cacti/spine.conf
%doc CHANGELOG README.md LICENSE
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 22 2023 Alexey Shabalin <shaba@altlinux.org> 1.2.23-alt1
- new version 1.2.23

* Sat Jul 17 2021 Alexey Shabalin <shaba@altlinux.org> 1.2.18-alt1
- new version 1.2.18

* Sun Mar 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.2.10-alt1
- 1.2.10

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.3-alt1
- 1.2.3

* Wed Mar 06 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.2.2-alt2
- fix FTBFS against libmysqlclient21

* Tue Mar 05 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.2-alt1
- 1.2.2

* Fri Jan 04 2019 Alexey Shabalin <shaba@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Tue May 10 2016 Alexey Shabalin <shaba@altlinux.ru> 0.8.8h-alt1
- 0.8.8h

* Wed Aug 14 2013 Alexey Shabalin <shaba@altlinux.ru> 0.8.8b-alt1
- 0.8.8b

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.8a-alt1.qa1
- NMU: rebuilt with libmysqlclient.so.18.

* Wed May 02 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8a-alt1
- 0.8.8a

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Wed Dec 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7i-alt1
- 0.8.7i

* Thu Oct 06 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7h-alt1
- 0.8.7h

* Mon Dec 06 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt3
- rebuild with net-snmp-5.6

* Mon Sep 27 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt2
- add official patche:
  + Multiple fixes for Windows and fixes for host threading issues

* Mon Jul 12 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7g-alt1
- 0.8.7g

* Tue Apr 06 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt3
- move config to /etc/cacti/, but /etc/ must work too
- chenge group spine.conf to cacti

* Thu Apr 01 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.7e-alt2
- sync path to log and config with cacti-0.8.7e-alt2

* Sat Feb 06 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7e-alt1
- New version
- Apply official patches

* Fri Mar 13 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7c-alt1
- New version
- Update spec

* Mon Jan 12 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7a-alt3
- Rebuild with new net-snmp (#18488)
- Convert spec to utf8

* Tue Dec 25 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7a-alt2
- Fix #13747

* Fri Nov 30 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.7a-alt1
- New version
- Rename to spine

* Mon Jan 29 2007 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.8.6i-alt3
- Separate in own package
- Spec cleanups 

* Sat Jan 13 2007 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt2
- Security fixes (CVE-2006-6799)

* Mon Dec 04 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6i-alt1
- New version
- Spec cleanups 
- config.php was marked as config with noreplace

* Fri Apr 14 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt2
- Fixed BuildRequires

* Wed Apr 05 2006 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6h-alt1
- New version
- Spec cleanups

* Sun Jul 10 2005 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6f-alt1
- Many critical security bugfixes in upstream
- Spec fixes (now daemon and main module may have different versions)

* Fri Oct 22 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6b-alt1
- New version

* Sun Sep 19 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt4
- Removed BuildArch tag because our rpm doesn't support multiple buildarch's
  in one spec ;-( Now php stuff has i586 arch ;-)

* Fri Sep 17 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt3
- Spec fixups (correct %%setup macroses)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt2
- Spec update (information for upgrade)

* Thu Sep 16 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.6-alt1
- New upstream version (has many new features)
- Russian translation for spec
- cactid now in separated package
- spec cleanups (permissions, path)

* Mon Aug 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt6
- Added missing buildrequires (libssl and other)

* Fri Aug 06 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5a-alt5
- New version

* Fri Jul 09 2004 Andrew Kornilov <hiddenman@altlinux.ru> 0.8.5-alt4
- New build

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt3
- Removed redundant docs from /var/www/html/cacti

* Fri Mar 12 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt2
- Added -M to useradd to skip homedir skeleton 

* Tue Mar 09 2004 Andrew Kornilov <andy@eva.dp.ua> 0.8.5-alt1
- First alpha build for Sisyphus. All works, but...;-)
