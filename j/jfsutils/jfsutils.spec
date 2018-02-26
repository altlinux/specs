%def_enable largefile

Name: jfsutils
Version: 1.1.15
Release: alt1

Summary: IBM JFS utility programs
License: GPL
Group: System/Kernel and hardware

Url: http://jfs.sourceforge.net
Source: %url/project/pub/%name-%version.tar.gz
Packager: Michael Shigorin <mike@altlinux.org>

Provides: jfsprogs = %version-%release
Obsoletes: jfsprogs

BuildRequires: libuuid-devel linux-libc-headers

%description
IBM's journaled file system technology, currently used in IBM
enterprise servers, is designed for high-throughput server
environments, key to running intranet and other high-performance
e-business file servers.

%description -l ru_RU.UTF-8
Технология журналируемой файловой системы IBM, в настоящее время
используется на enterprise-серверах IBM, разработана для
высокопроизводительных серверных окружений, ключ к работающим
intranet- и другим высокопроизводительным файловым серверам
электронной коммерции.

%description -l uk_UA.UTF-8
Технологія журнальованої файлової системи IBM, яка нині
використовується на enterprise-серверах IBM, розроблена для
високопродуктивних серверних оточень, є ключом до працюючих
intranet- та інших високопродуктивних файлових серверів
електронної комерції.

%prep
%setup

%build
%configure \
	--sbindir=/sbin \
	%{subst_enable largefile}
%make_build

%install
%make_install DESTDIR=%buildroot install
for n in fsck mkfs; do
    ln -sf jfs_$n %buildroot/sbin/$n.jfs
    ln -sf jfs_$n.8 %buildroot/%_man8dir/$n.jfs.8
done
# why so much hassle?
bzip2 --best --keep --force ChangeLog
gzip --best --stdout NEWS > NEWS.gz

%files
%doc AUTHORS ChangeLog.* NEWS.* README
/sbin/*
%_man8dir/*

%changelog
* Sun Sep 25 2011 Michael Shigorin <mike@altlinux.org> 1.1.15-alt1
- 1.1.15
  + mostly 64-bit value related fixups
  + file systems CAN share an external journal

* Tue Dec 22 2009 Michael Shigorin <mike@altlinux.org> 1.1.14-alt2
- rebuilt with libuuid-devel

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 1.1.14-alt1
- 1.1.14
  + log size limit increased from 32M to 128M
  + minor bugfixes
- NB: I don't use JFS so would gladly hand the package
  to proper maintainer :-)

* Thu Jul 17 2008 Michael Shigorin <mike@altlinux.org> 1.1.13-alt1
- 1.1.13
  + better sanity checking when replaying the journal
  + compilation fixes

* Sat Aug 25 2007 Michael Shigorin <mike@altlinux.org> 1.1.12-alt1
- 1.1.12
  + Fix double close of external journal descriptor
  + Fix possible array overflow

* Sun Apr 08 2007 Michael Shigorin <mike@altlinux.org> 1.1.11-alt1
- 1.1.11 (#11263)
- merged in led@'s Daedalus build
  + buildreq
  + trimmed description
  + optional largefile support (enabled by default)
- added Packager:
- added Ukrainian description

* Fri Sep 15 2006 Led <led@altlinux.ru> 1.1.11-alt0.1
- renamed jfsprogs to jfsutils
- added docs
- cleaned up spec

* Mon May 29 2006 Anton Farygin <rider@altlinux.ru> 1.1.10-alt1
- new version
- specfile cleanup

* Sun Feb 29 2004 Alexander Nekrasov <canis@altlinux.ru> 1.1.4-alt1
- 1.1.4
- Rebuilt in new environment

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.1.0-alt1
- 1.1.0
- Rebuilt in new environment

* Mon Mar 18 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.16-alt1
- 1.0.16

* Thu Feb 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.15-alt1
- 1.0.15

* Mon Jan 14 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.12-alt1
- 1.0.12

* Wed Dec 26 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.10-alt1
- 1.0.10

* Tue Nov 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.9-alt1
- 1.0.9

* Wed Oct 31 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.8-alt1
- 1.0.8

* Thu Sep 20 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.5-alt1
- First build for Sisyphus

* Mon Sep 17 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.5-1mdk
- 1.0.5.

* Sat Sep  1 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-1mdk
- 1.0.4.

* Tue Aug 21 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.3-1mdk
- Use optflags.
- 1.0.3.

* Sat Aug  4 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.2-1mdk
- 1.0.2.

* Wed Aug  1 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.1-1mdk
- First version.

# end of file
