%define ejudge_user ejudge
%define ejudge_group judges
%define ejudge_home /var/lib/ejudge
%define cgi_bin_dir /var/www/cgi-bin
%define httpd_htdocs_dir /var/www/html
%define ejudge_socket_dir /var/run/ejudge
%define lang_config_dir %_sysconfdir/ejudge/lang.d

Name: ejudge
Version: 2.3.23
Release: alt1

Summary: Ejudge is a programming contest managment system
Summary(ru_RU.UTF-8): Ejudge это система для проведения соревнований по программированию

License: GPL
Group: System/Servers
Url: http://www.ejudge.ru
Packager: Denis Kirienko <dk@altlinux.ru>

Source0: %name-svn6956.tar.bz2
Source1: %name.rc
Source2: ejudge-install.sh
Source3: ejudge-README-ALT.utf8
Source5: ejudge-cntsguide.pdf
Source6: ejudge-refmanual.pdf

Patch1: ejudge-stylecheck.patch
Patch2: ejudge-tsc.c.patch
Patch3: ejudge-fpc-version.patch

BuildPreReq: flex, sed, mktemp, libexpat-devel, zlib-devel, libzip-devel, libncursesw-devel, libMySQL-devel, libcurl-devel

Requires: sharutils, apache2, iconv, gawk, a2ps

Obsoletes: libreuse

%description
Ejudge is a programming contest managment system.

You must configure ejudge before running it.
Please read ejudge-README-ALT.utf8 for defails.

%description -l ru_RU.UTF-8
Ejudge - это система для организации соревнований по программированию.
Она позволяет участникам соревнований сдавать решения предлагаемых
задач, которые проверяются на заранее подготовленных тестах.
Также ejudge позволяет проводить тестирования на различных видах
задач: с выбором ответа, с кратким или развернутым ответом

Ejudge требует аккуратной настройки перед использованием.
Ссылка на инструкции по настройке в файле ejudge-README-ALT.utf8

%package doc
Summary: Documentation for ejudge
Summary(ru_RU.UTF-8): Документация для системы ejudge
Group: System/Servers
Requires: %name = %version-%release
BuildArch: noarch

%description doc
User and contest administrator manual for ejudge system.

%description doc -l ru_RU.UTF-8
Документация пользователя и администратора для системы
проведения соревновний по программированию ejudge.

%prep
%setup -q -n ejudge
%patch1 -p1
%patch2 -p1
%patch3 -p1
cp %SOURCE2 %SOURCE3 %SOURCE5 %SOURCE6 .

bzip2 -9k ChangeLog NEWS NEWS.RUS

%build

%configure                                                                \
--enable-charset=utf-8                                                    \
--enable-socket-path=%ejudge_socket_dir/userlist-socket                   \
--enable-super-serve-socket=%ejudge_socket_dir/super-serve-socket         \
--enable-new-server-socket=%ejudge_socket_dir/new-server-socket           \
--enable-contests-home-dir=%ejudge_home                                   \
--enable-local-dir=%ejudge_socket_dir                                     \
--libexec=%_libexecdir                                                    \
--enable-cgi-bin-dir=%_libexecdir/%name/cgi-bin                           \
--enable-conf-dir=%ejudge_home/data                                       \
--enable-cgi-conf-dir=../cgi-data                                         \
--enable-hidden-server-bins                                               \
--with-httpd-cgi-bin-dir=%cgi_bin_dir                                     \
--with-httpd-htdocs-dir=%httpd_htdocs_dir                                 \
--enable-ajax                                                             \
--enable-lang-config-dir=%lang_config_dir                                 \
--disable-rpath

%make_build RELEASE=1

%install
%make_install DESTDIR=%buildroot install
install -p -m755 -D %SOURCE1 %buildroot%_initdir/%name
install -d %buildroot%ejudge_home
install -d %buildroot%ejudge_socket_dir
install -d %buildroot%lang_config_dir
%find_lang %name

%pre
%_sbindir/groupadd -r -f %ejudge_group 2>/dev/null || :
%_sbindir/useradd -g %ejudge_group -c 'Ejudge server' -d %ejudge_home -r %ejudge_user 2>/dev/null || :

%post
%post_service ejudge

%preun
%preun_service ejudge

%files -f %name.lang
%_sysconfdir/ejudge
%attr(2775,%ejudge_user,%ejudge_group) %dir %ejudge_home
%_initdir/%name
%_bindir/*
%_includedir/*
%_libdir/libchecker*
%_libexecdir/%name
%_datadir/%name
%doc AUTHORS ChangeLog.bz2 NEWS.bz2 NEWS.RUS.bz2 ejudge-install.sh ejudge-README-ALT.utf8

%files doc
%doc ejudge-*.pdf

%changelog
* Mon Jul 09 2012 Denis Kirienko <dk@altlinux.org> 2.3.23-alt1
- Version 2.3.23 (SVN 6956)

* Sat Jun 16 2012 Denis Kirienko <dk@altlinux.org> 2.3.22-alt4
- SVN 6890

* Thu Jun 07 2012 Denis Kirienko <dk@altlinux.org> 2.3.22-alt3
- SVN 6886

* Sat Jun 02 2012 Denis Kirienko <dk@altlinux.org> 2.3.22-alt2
- SVN 6872

* Wed May 23 2012 Denis Kirienko <dk@altlinux.org> 2.3.22-alt1
- Version 2.3.22 (SVN 6849)

* Sun May 13 2012 Denis Kirienko <dk@altlinux.org> 2.3.21-alt4
- SVN 6818

* Thu May 10 2012 Denis Kirienko <dk@altlinux.org> 2.3.21-alt3
- SVN 6816

* Fri Apr 27 2012 Denis Kirienko <dk@altlinux.org> 2.3.21-alt2
- SVN 6778

* Wed Apr 04 2012 Denis Kirienko <dk@altlinux.org> 2.3.21-alt1
- Version 2.3.21 release candidate (SVN 6726)

* Sat Mar 31 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt8
- SVN 6707

* Sat Mar 31 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt7
- SVN 6705

* Fri Mar 30 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt6
- SVN 6703

* Sun Mar 18 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt5
- SVN 6657
- Updated ejudge-install.sh (support for Java 7, python3 and FreeBASIC)

* Fri Mar 02 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt4
- Init-script fix

* Thu Mar 01 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt3
- SVN 6653

* Sat Jan 07 2012 Denis Kirienko <dk@altlinux.org> 2.3.20-alt2
- SVN 6610

* Fri Dec 30 2011 Denis Kirienko <dk@altlinux.org> 2.3.20-alt1
- Version 2.3.20 (SVN 6603)

* Fri Dec 23 2011 Denis Kirienko <dk@altlinux.org> 2.3.19-alt7
- SVN 6590

* Fri Dec 16 2011 Denis Kirienko <dk@altlinux.org> 2.3.19-alt6
- SVN 6557

* Tue Dec 13 2011 Denis Kirienko <dk@altlinux.org> 2.3.19-alt5
- SVN 6554

* Tue Dec 13 2011 Denis Kirienko <dk@altlinux.org> 2.3.19-alt4
- SVN 6551

* Fri Aug 05 2011 Denis Kirienko <dk@altlinux.ru> 2.3.19-alt3
- SVN 6415

* Sat Jul 09 2011 Denis Kirienko <dk@altlinux.ru> 2.3.19-alt2
- SVN 6402

* Sat Jul 09 2011 Denis Kirienko <dk@altlinux.ru> 2.3.19-alt1
- Version 2.3.19 (SVN 6399)

* Tue Jul 05 2011 Denis Kirienko <dk@altlinux.ru> 2.3.18-alt5
- SVN 6394

* Thu Jun 30 2011 Denis Kirienko <dk@altlinux.ru> 2.3.18-alt4
- SVN 6389

* Fri Apr 29 2011 Denis Kirienko <dk@altlinux.ru> 2.3.18-alt3
- All temporary files moved to /var/run/ejudge

* Fri Apr 29 2011 Denis Kirienko <dk@altlinux.ru> 2.3.18-alt2
- SVN 6283
- Updated ejudge-install.sh
- ejudge-README-ALT.utf8 moved to ejudge wiki

* Wed Apr 27 2011 Denis Kirienko <dk@altlinux.ru> 2.3.18-alt1
- Version 2.3.18
- Updated ejudge-install.sh and ejudge-README-ALT.utf8

* Sat Apr 09 2011 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt7
- SVN 6241

* Thu Apr 07 2011 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt6
- SVN 6232

* Wed Mar 30 2011 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt5
- SVN 6205
- Merge with libreuse package (libreuse now obsolete)

* Sat Mar 05 2011 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt4
- SVN 6110

* Wed Dec 01 2010 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt3
- SVN 6068
- Support for kumir language (package kumir-console is required)

* Fri Nov 05 2010 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt2
- Upstream bugfix

* Thu Nov 04 2010 Denis Kirienko <dk@altlinux.ru> 2.3.17-alt1
- Version 2.3.17

* Wed Oct 27 2010 Denis Kirienko <dk@altlinux.ru> 2.3.16-alt3
- SVN 6013
- Rebuild with libreuse-4.3.10-alt2

* Sun Sep 19 2010 Denis Kirienko <dk@altlinux.ru> 2.3.16-alt2
- SVN 5993
- Rebuild with libMySQL-5.1.50

* Mon Aug 23 2010 Denis Kirienko <dk@altlinux.ru> 2.3.16-alt1
- Version 2.3.16 (SVN 5984)

* Fri Jul 30 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt12
- SVN 5965

* Fri Jul 2 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt11
- SVN 5925

* Mon Jun 21 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt10
- SVN 5903

* Mon May 24 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt9.1
- Removed dependency on a2ps

* Wed May 12 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt9
- SVN 5795

* Tue Mar 02 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt8
- SVN 5780

* Wed Feb 24 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt7
- SVN 5776

* Mon Feb 01 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt6
- Version 2.3.15 final release (SVN 5762)

* Tue Jan 26 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt5
- SVN 5754

* Sat Jan 23 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt4
- SVN 5725

* Wed Jan 20 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt3
- SVN 5699

* Tue Jan 19 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt2
- Requires: libreuse-4.3.9

* Tue Jan 19 2010 Denis Kirienko <dk@altlinux.ru> 2.3.15-alt1
- Version 2.3.15 (SVN 5690)

* Sun Nov 29 2009 Denis Kirienko <dk@altlinux.ru> 2.3.14-alt3
- SVN snapshot 5601
- User documentation moved to the separate ejudge-doc package
- Removed some obsolete documentation
- Updated ejudge initscript

* Sun Sep 13 2009 Denis Kirienko <dk@altlinux.ru> 2.3.14-alt2
- SVN snapshot 5594

* Sat Sep 05 2009 Denis Kirienko <dk@altlinux.ru> 2.3.14-alt1
- Version 2.3.14 (SVN 5589)

* Thu Aug 13 2009 Denis Kirienko <dk@altlinux.ru> 2.3.13-alt4
- SVN snapshot 5581
- Requires: apache2 instead of webserver
- Updated README-ALT

* Sun May 31 2009 Denis Kirienko <dk@altlinux.ru> 2.3.13-alt3
- SVN snapshot 5574
- Fixed ejudge-install.sh

* Sun Jan 18 2009 Denis Kirienko <dk@altlinux.ru> 2.3.13-alt2
- SVN snapshot 5544 (security bugfix)

* Sun Jan 04 2009 Denis Kirienko <dk@altlinux.ru> 2.3.13-alt1
- Version 2.3.13 (SVN 5532)

* Sun Dec 28 2008 Denis Kirienko <dk@altlinux.ru> 2.3.12-alt4
- SVN snapshot 5526

* Sun Dec 21 2008 Denis Kirienko <dk@altlinux.ru> 2.3.12-alt3
- SVN snapshot 5447

* Mon Dec 08 2008 Denis Kirienko <dk@altlinux.ru> 2.3.12-alt2
- SVN snapshot 5405

* Sun Nov 30 2008 Denis Kirienko <dk@altlinux.ru> 2.3.12-alt1
- Version 2.3.12+ (SVN 5366)
- Updated README-ALT

* Sun Oct 12 2008 Denis Kirienko <dk@altlinux.ru> 2.3.11-alt1
- Version 2.3.11 (svn 5201)
- Enabled MySQL support

* Thu Sep 11 2008 Denis Kirienko <dk@altlinux.ru> 2.3.9-alt5
- SVN snapshot 5048

* Sun Aug 24 2008 Denis Kirienko <dk@altlinux.ru> 2.3.9-alt4
- Fixed bug with wrong shell for user ejudge
- Fixed bug with JAVA_HOME variable
- Updated README-ALT

* Fri Aug 15 2008 Denis Kirienko <dk@altlinux.ru> 2.3.9-alt3
- SVN snapshot 4999
- Rebuild with libreuse-4.3.6-alt2

* Fri Aug 15 2008 Denis Kirienko <dk@altlinux.ru> 2.3.9-alt2
- Update for version 2.3.9 (svn 4998) - important bugfix

* Sat Aug 09 2008 Denis Kirienko <dk@altlinux.ru> 2.3.9-alt1
- Version 2.3.9 (svn 4993)

* Thu Jul 7 2008 Denis Kirienko <dk@altlinux.ru> 2.3.8-alt1
- Version 2.3.8 (svn 4990)
- New programming languages configuration scheme
- Updated README-ALT

* Sun Mar 16 2008 Denis Kirienko <dk@altlinux.ru> 2.3.7-alt1
- Version 2.3.7 (svn 4802)
- Added dependencies on e2fsprogs and iconv (required by ejudge-install.sh)
- Language config files are marked as config(noreplace)

* Tue Feb 26 2008 Denis Kirienko <dk@altlinux.ru> 2.3.6-alt1.svn4705
- Version 2.3.6

* Fri Jan 11 2008 Denis Kirienko <dk@altlinux.ru> 2.3.5-alt0.svn4652
- Version 2.3.5

* Sun Dec 23 2007 Denis Kirienko <dk@altlinux.ru> 2.3.3-alt0.svn4638
- New svn snapshot
- Fixed ejudge-install.sh script
- Fixed java support
- Updated README-ALT
- Added PDF documentation

* Sat Sep 15 2007 Denis Kirienko <dk@altlinux.ru> 2.3.3-alt0.svn4327
- New svn snapshot
- Fixed configure bug (ejudge refused to start at i586)

* Sun Aug 26 2007 Denis Kirienko <dk@altlinux.ru> 2.3.3-alt0.svn4320
- Version 2.3.3
- rebuilded with new configure option: --enable-hidden-server-bins

* Thu Aug 16 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4307
- New svn snapshot
- updated README-ALT

* Wed Aug 08 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4303
- New svn snapshot

* Sun Aug 05 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4282
- New svn snapshot
- Rebuild with new reuse library
- Fixed support for g++, javac, fpc compilers
- Updated alt-locale patch

* Fri Aug 03 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4255
- New svn snapshot

* Sun Apr 15 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4105
- New svn snapshot

* Mon Apr 09 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4088
- New svn snapshot
- alt-locale patch
- updated README-ALT
- updated ejudge-install.sh

* Sun Apr 08 2007 Denis Kirienko <dk@altlinux.ru> 2.3.2-alt0.svn4084
- Initital build for ALT Linux
