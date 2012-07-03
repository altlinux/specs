%def_with pic

%define Name GParted
Name: gparted
Version: 0.8.0
Release: alt1.1
Summary: %Name Partition Editor
Summary(ru_RU.CP1251): Редактор разделов %Name
Summary(uk_UA.CP1251): Редактор розділів %Name
License: %gpl2plus
Group: System/Configuration/Hardware
URL: http://%name.sourceforge.net/
Source0: %name-%version.tar
#http://prdownloads.sourceforge.net/%name/%name-%version.tar.bz2?download
Source1: %name-pam
Source2: %name-security
Patch0: %name-%version-%release.patch
Patch1: %name-0.8.0-alt-DSO.patch
#Patch1: %name-%version-led.patch
Packager: Led <led@altlinux.ru>
AutoReq: yes, noshell

BuildRequires(pre): rpm-build-licenses
BuildRequires: libparted-devel >= 1.7.1
BuildRequires: libgtkmm2-devel >= 2.8
BuildRequires: gcc-c++ libprogsreiserfs-devel libuuid-devel intltool
BuildRequires: perl-XML-Parser gnome-doc-utils librarian

%description
%Name stands for %Name Partition Editor. It uses libparted to detect
and manipulate devices and partitiontables while several (optional)
filesystemtools provide support for filesystems not included in
libparted. These optional packages will be detected at runtime and
don't require a rebuild of %Name.
%Name is written in C++ and uses gtkmm as Graphical Toolkit. The
general approach is to keep the GUI as simple as possible.

%description -l ru_RU.CP1251
%Name - %Name Partition Editor. Он использует libparted для
обнаружения и манипуляций с устройствами и таблицами разделов, а также
некоторые (необязательные) инструменты (не включенные в libparted),
обеспечивающие поддержку файловых систем. Эти необязательные пакеты
обнаруживаются во время выполнения и не требуют пересборки %Name.
%Name написан на C++ с использованием gtkmm в качестве графического
инструментария. Главная задача - оставить GUI максимально простым.

%description -l uk_UA.CP1251
%Name - %Name Partition Editor. Він використовує libparted для
виявлення та маніпуляцій з пристроями і таблицями разділів, а також
деякі (необов'язкові) інструменти (не включені в libparted), які
забезпечують підтримку файлових систем. Ці необов'язкові пакети
виявляються під час виконання і не потребують перебудови %Name.
%Name написано на C++ з використанням gtkmm в якості графічного
інструментарію. Головне завдання - залишити GUI максимально простим.


%prep
%setup
%patch0 -p1
%patch1 -p0


%build
%define _optlevel s
%autoreconf
%configure %{subst_with pic} --bindir=%_sbindir
%make_build
bzip2 --best --keep --force ChangeLog


%install
%make_install DESTDIR=%buildroot install

# usermode
install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
install -d -m 0755 %buildroot%_bindir
ln -s %_bindir/consolehelper %buildroot%_bindir/%name

%find_lang --with-gnome %name


%files -f %name.lang
%doc AUTHORS ChangeLog.* README
%_sbindir/*
%_bindir/*
%_man8dir/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*


%changelog
* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.1
- Fixed build

* Thu Feb 17 2011 Mykola Grechukh <gns@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Sat Dec 25 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.7.1-alt1
- 0.7.1

* Sat Sep 25 2010 Michael Shigorin <mike@altlinux.org> 0.5.2-alt1
- rebuilt for Sisyphus (fixes: #23807)

* Sun Jul 25 2010 Led <led@altlinux.ru> 0.5.2-tmc2
- fixed ext4 support

* Sun Jul 04 2010 Led <led@altlinux.ru> 0.5.2-tmc1
- 0.5.2

* Sun Mar 21 2010 Michael Shigorin <mike@altlinux.org> 0.5.1-alt1
- rebuilt for Sisyphus on aris@' request;
  thanks led@ for gear repo

* Wed Mar 03 2010 Led <led@altlinux.ru> 0.5.1-tmc1
- 0.5.1

* Sun Jan 24 2010 Led <led@altlinux.ru> 0.5.0-tmc1
- 0.5.0

* Mon Dec 07 2009 Led <led@altlinux.ru> 0.4.8-alt2
- added nilfs2 support

* Sat Dec 05 2009 Led <led@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Tue Oct 27 2009 Alexey Rusakov <ktirf@altlinux.org> 0.4.6-alt1.1
- thanks to led@ for keeping the package fresh in his git

* Tue Oct 20 2009 Led <led@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Mon Aug 10 2009 Led <led@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Mon May 11 2009 Led <led@altlinux.ru> 0.4.5-alt2
- added common class for FAT 16/32 and EXT 2/3/4
- updated BuildRequires

* Sat May 09 2009 Led <led@altlinux.ru> 0.4.5-alt1
- 0.4.5:
  + Improved crypt-luks detection
  + Improved dmraid device detection
  + Improved UUID detection
  + Enhanced to search for udevadm if udevsettle not found
  + Improved file system detection

* Fri Apr 03 2009 Led <led@altlinux.ru> 0.4.4-alt1
- 0.4.4:
  + enhanced move/resize functionality
  + added detection of LUKS encrypted partitions
  + added detection of btrfs file system
  + added initial support for dmraid devices

* Wed Mar 04 2009 Led <led@altlinux.ru> 0.4.3-alt2
- fixed mistranslation in ru.po (#19047) (thanx lav@)

* Sun Feb 15 2009 Led <led@altlinux.ru> 0.4.3-alt1
- 0.4.3:
  + fixed #18367

* Fri Dec 26 2008 Led <led@altlinux.ru> 0.4.1-alt2
- cleaned up spec
- fixed Exec in %name.desktop
- fixed ru and uk translations
- fixed descriptions and summaries

* Tue Dec 02 2008 Led <led@altlinux.ru> 0.4.1-alt1
- 0.4.1
- cleaned up spec

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.3.9-alt1
- 0.3.9
- fixed %name.desktop

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.3.8-alt2
- fixed %name.desktop

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.3.8-alt1
- 0.3.8

* Mon Mar 31 2008 Led <led@altlinux.ru> 0.3.6-alt1
- 0.3.6

* Sun Mar 02 2008 Led <led@altlinux.ru> 0.3.5-alt2
- added icons

* Sun Feb 10 2008 Led <led@altlinux.ru> 0.3.5-alt1
- 0.3.5
- updated BuildRequires

* Sun Sep 16 2007 Led <led@altlinux.ru> 0.3.3-alt7
- added %name-0.3.3-disable_hal_dirty_hack.patch for disable dirty hack
  for HAL (fixed #12753)

* Wed Aug 15 2007 Led <led@altlinux.ru> 0.3.3-alt6
- rebuild with libparted-1.8.so.8
- fixed License

* Mon May 14 2007 Led <led@altlinux.ru> 0.3.3-alt5
- rebuild with libparted-1.8.so.7

* Sun Mar 25 2007 Led <led@altlinux.ru> 0.3.3-alt4
- rebuild with libparted-1.8.so.6

* Mon Mar 19 2007 Led <led@altlinux.ru> 0.3.3-alt3
- rebuild with libparted-1.8.so.4

* Tue Jan 16 2007 Led <led@altlinux.ru> 0.3.3-alt2
- rebuild with libparted-1.8.so.2

* Fri Dec 08 2006 Led <led@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Mon Dec 04 2006 Led <led@altlinux.ru> 0.3.2-alt1
- 0.3.2:
  + added support for reading volumelabels (ext2/3 now)
- removed %name-0.3.1-configure.patch (fixed in upstream)
- fixed BuildRequires
- cleaned up %%setup due fixes in upstream
- fixed %name.desktop

* Thu Nov 23 2006 Led <led@altlinux.ru> 0.3.1-alt2
- rebuild with new libparted
- added %name-0.3.1-configure.patch
- fixed spec

* Tue Sep 12 2006 Led <led@altlinux.ru> 0.3.1-alt1
- 0.3.1
- fixed configure*

* Thu Sep 07 2006 Led <led@altlinux.ru> 0.3-alt1
- 0.3
- fixed BuildRequires

* Mon Jun 19 2006 Led <led@altlinux.ru> 0.2.5-alt4
- rebuild without changes for fixing unmets

* Tue May 30 2006 Led <led@altlinux.ru> 0.2.5-alt3
- rebuild with libparted-1.7.1

* Mon May 22 2006 Led <led@altlinux.ru> 0.2.5-alt2
- rebuild with libparted-1.7.0

* Mon May 22 2006 Led <led@altlinux.ru> 0.2.5-alt1
- fixed spec

* Mon May 15 2006 Led <led@altlinux.ru> 0.2.5-alt0.1
- 0.2.5
- removed unneedful BuildReq's

* Wed Apr 05 2006 Led <led@altlinux.ru> 0.2.4-alt0.1
- 0.2.4

* Wed Mar 29 2006 Led <led@altlinux.ru> 0.2.3-alt0.1
- 0.2.3

* Fri Feb 24 2006 Led <led@altlinux.ru> 0.2.2-alt0.1
- 0.2.2

* Fri Feb 17 2006 Led <led@altlinux.ru> 0.2.1-alt0.1
- 0.2.1
- removed unneedful BuildReq's

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.2-alt1
- 0.2

* Mon Jan 23 2006 Led <led@altlinux.ru> 0.1-alt1
- 0.1
- removed empty NEWS from docs
- uk and ru Summary and description
- added usermode

* Sun Nov 27 2005 Alexey Rusakov <ktirf@altlinux.ru> 0.0.9-alt1
- new version
- the binary now lives in bindir instead of sbindir (it's an upstream change actually).

* Mon Sep 12 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.0.8-alt0.1.1
- rebuild with libparted.

* Sat Jan 29 2005 Yuri N. Sedunov <aris@altlinux.ru> 0.0.8-alt0.1
- 0.0.8

* Wed Dec 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.7-alt0.1
- First build for Sisyphus.
