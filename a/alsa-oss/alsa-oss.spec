Name: alsa-oss
Version: 1.0.17
Release: alt7

Summary: Advanced Linux Sound Architecture (ALSA) OSS compatibility library
License: GPL
Group: System/Libraries

Url: http://www.alsa-project.org
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Obsoletes: libalsa2-oss <= 0.9.8
Conflicts: sound-scripts <= 1.0.1-alt1

BuildRequires: gcc-c++ libalsa-devel

Summary(ru_RU.UTF-8): Запуск OSS-программ под ALSA
Summary(uk_UA.UTF-8): Запуск OSS-програм під ALSA

%description
Advanced Linux Sound Architecture (ALSA) OSS compatibility libs.
Modularized architecture with support for a large range of ISA
and PCI cards. Fully compatible with OSS/Lite but contains many
enhanced features.

This package contains a OSS compatibility library.

It might come handy when usual /dev/dsp emulation is not enough,
e.g. with dmix software multichannel mixer.

%description -l ru_RU.UTF-8
Пакет содержит скрипт aoss, предназначенный для запуска программ,
ориентированных на звуковую подсистему OSS, под ALSA (современной
звуковой подсистемой Linux).

Полезен, когда не хватает эмуляции /dev/dsp; например,
при использовании программного микширования dmix.

%description -l uk_UA.UTF-8
Пакунок містить скрипт aoss, що застосовується для запуску
програм, які орієнтовані на звукову підсистему OSS, під ALSA
(сучасною звуковою системою Linux).

Може стати у нагоді, коли не вистачає емуляції /dev/dsp;
наприклад, за використання програмного мікшування dmix.

%prep
%setup
%patch -p1

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/*.so*
%_man1dir/*

%changelog
* Thu Dec 17 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt7
- spec cleanup

* Sun Oct 25 2009 Michael Shigorin <mike@altlinux.org> 1.0.17-alt6
- fixed interbug of aoss script and packaging wrt *.so and *.so.*
  (closes: #21227)
- spec cleanup

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt5
- installed original aoss script

* Mon Jul 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt4
- removed semiworking /etc/modprobe.d/oss (patches are welcomed)

* Tue Mar 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt3
- added /etc/modprobe.d/oss

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Jul 16 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.17-alt1
- 1.0.17

* Sun Jan 27 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.0.15-alt1
- 1.0.15

* Mon Jun 11 2007 Michael Shigorin <mike@altlinux.org> 1.0.14-alt1
- 1.0.14

* Sat Sep 02 2006 Michael Shigorin <mike@altlinux.org> 1.0.12-alt1
- 1.0.12
- minor spec cleanup

* Wed Apr 19 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt1
- 1.0.11

* Sat Mar 04 2006 Michael Shigorin <mike@altlinux.org> 1.0.11-alt0.3
- 1.0.11rc3
- fixed description; thanks Sergey Vlasov (vsu@)

* Wed Nov 16 2005 Michael Shigorin <mike@altlinux.org> 1.0.10-alt1
- 1.0.10

* Mon Jul 04 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt2
- fixed Obsoletes: (libalsa2-oss, was libalsa-oss)

* Thu Jun 23 2005 Michael Shigorin <mike@altlinux.org> 1.0.9-alt1
- 1.0.9

* Thu Jan 13 2005 Michael Shigorin <mike@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Dec 16 2004 Michael Shigorin <mike@altlinux.ru> 1.0.7-alt1
- 1.0.7

* Sat Jun 26 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt2
- added ru/uk package info
- minor spec cleanup :)

* Mon May 31 2004 Michael Shigorin <mike@altlinux.ru> 1.0.5-alt1
- 1.0.5

* Wed May 05 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt2
- fixed #4041, thanks Sergey Bolshakov (sbolshakov@)
  for report/fix.

* Sat Apr 03 2004 Michael Shigorin <mike@altlinux.ru> 1.0.4-alt1
- 1.0.4

* Tue Mar 02 2004 Michael Shigorin <mike@altlinux.ru> 1.0.3a-alt1
- 1.0.3a

* Thu Jan 29 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt2
- 1.0.2, Final Upload by ALSA Project (TM) 20040129 18:35 +0200
- thanks to Sergey Vlasov (vsu@) for alerting about re-uploads

* Wed Jan 28 2004 Michael Shigorin <mike@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Jan 15 2004 Michael Shigorin <mike@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sun Nov 23 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt1
- renamed to alsa-oss as the library is only used for preloading
- dropped devel subpackages due to the very same issue
- aoss script was missing (and broken anyway); thanks to Sergey Vlasov (vsu@)
  for pointing out and providing proper version (#3308)

* Wed Oct 22 2003 Michael Shigorin <mike@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Thu Jul 31 2003 Michael Shigorin <mike@altlinux.ru> 0.9.6-alt1
- 0.9.6
- forgot this part.  Getting back :)

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt2
- Rebuilt in new environment

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0rc1-alt1
- 0.9.0rc1

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta11-alt1
- 0.9.0beta11

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta10-alt1a
- 0.9.0beta10a

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta9-alt1
- 0.9.0beta9

* Fri Oct 12 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta8-alt1
- 0.9.0beta8

* Fri Sep 21 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.0beta7-alt1
- First build for Sisyphus
