Packager: Repocop Q. A. Robot <repocop@altlinux.org>
%def_disable rpath
%def_with pic
%def_disable devel
%def_enable debug
%def_disable warnings
%def_disable profile
%def_disable final
%def_enable mt
%def_enable threading
%def_enable shared
%def_disable static
%def_enable largefile
%def_enable ntfs
%def_enable ext3fs
%def_enable jfs
%def_enable xfs
%def_enable reiserfs
%def_enable labels


%define Name QtParted
Name: qtparted
Version: 0.5.0
Release: alt1
Group: System/Configuration/Hardware
Summary: Flexible GUI partitioning tool
Summary(ru_RU.CP1251): Графический инструмент для работы с разделами жесткого диска
Summary(uk_UA.CP1251): Графічний інструмент для роботи з разділами жорсткого диску
License: %gpl2plus
URL: http://%name.sourceforge.net/
Source0: %name-%version.tar
Source1: %name-pam
Source2: %name-security
Source3: %{name}_ua.ts
Source4: CMakeCache.txt
Patch0: %name-0.4.5-libparted_1.7.patch
Patch1: %name-0.4.5-notable.patch
Patch2: %name-0.4.5-ide.patch
Patch3: %name-0.4.5-makefile.patch

BuildRequires: fontconfig libqt4-devel libXext-devel libXt-devel
BuildRequires: libparted-devel libstdc++-devel gcc-c++ zlib-devel
BuildRequires: libuuid-devel ImageMagick rpm-build-licenses
BuildPreReq: e2fsprogs cmake
BuildPreReq: qt4-designer libGL-devel libGLU-devel libjpeg-devel
BuildPreReq: libmng-devel librsvg-devel libopenmotif-devel
%{?_enable_ntfs:BuildRequires: ntfsprogs}
%{?_enable_ext3fs:BuildRequires: libe2fs-devel}
%{?_enable_jfs:BuildRequires: jfsprogs}
%{?_enable_xfs:BuildRequires: xfsprogs}
%{?_enable_reiserfs:BuildRequires: libprogsreiserfs-devel}

%description
%Name is a Partition Magic clone written in C++ using the Qt
toolkit, GUI partitioning tool. %Name is GNU Parted based. It's a
program that allows you to create, destroy, resize, move and copy hard
disk partitions. This is useful for creating space for new operating
systems, reorganising disk usage, and copying data to new hard disks.

%description -l ru_RU.CP1251
%Name является подобием программы "Partition Magic" -- инструмента
для редактирования дисковых разделов с графическим интерфейсом
пользователя. Он написан на C++ с использованием пакета Qt для
графического интерфейса и основан на программе Parted, являющейся
частью проекта GNU. Программа позволяет Вам создавать, удалять,
перемещать, копировать и изменять размер разделов жесткого диска.
%Name будет полезен при создании разделов для новых операционных
систем, при изменениях в использовании диска и копировании данных на
новый жёсткий диск.

%description -l uk_UA.CP1251
%Name є написанным на C++ з використанням тулкіта Qt клоном "Partition
Magic", графічним інструментом для роботи з розділами жорсткого диску.
%Name базується на GNU Parted. Це программа, яка дозволяє
створювати, знищувати, мереміщати, копіювати розділи, а також змінювати
їх розміри. Вона може бути корисною для створення місця для нових
операційних систем, реорганізації використання диску та копіювання
даних на новий жорсткий диск.


%prep
%setup
install -m 0644  %SOURCE3 ts/%{name}_ua.ts
install -m644 %SOURCE4 .


%build
PATH=%_libdir/qt4/bin:$PATH \
cmake .

%make_build VERBOSE=1
#convert -resize 48x48 -depth 8 data/%{name}_{64,48}.png


%install
%makeinstall_std menudir=%_desktopdir
for s in 16 32 64; do
    install -d -m 0755 %buildroot%_iconsdir/hicolor/${s}x$s/apps
    mv %buildroot{%_datadir/%name/pics/%{name}_$s,%_iconsdir/hicolor/${s}x$s/apps/%name}.png
done
#install -D -m644 data/%{name}_48.png %buildroot%_liconsdir/%name.png

# usermode
install -pD -m640 %SOURCE1 %buildroot%_sysconfdir/pam.d/%name
install -pD -m640 %SOURCE2 %buildroot%_sysconfdir/security/console.apps/%name
install -d -m755 %buildroot%_sbindir
mv %buildroot%_bindir/%name %buildroot%_sbindir/
ln -s %_bindir/consolehelper %buildroot%_bindir/%name

install -d %buildroot%_man1dir
install -p -m644 doc/%name.1 %buildroot%_man1dir

%find_lang %name


%files -f %name.lang
%doc AUTHORS ChangeLog doc/README doc/BUGS doc/TODO.txt
%_bindir/*
%_sbindir/*
%_sysconfdir/pam.d/*
%_sysconfdir/security/console.apps/*
%_datadir/%name
%_man1dir/*	
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*


%changelog
* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Mon Mar 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt26
- Rebuilt for debuginfo

* Wed Mar 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt25
- Fixed build (see http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=534001 )

* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt24.1
- NMU (by repocop): the following fixes applied:
  * update_menus for qtparted

* Fri Aug 08 2008 Led <led@altlinux.ru> 0.4.5-alt24
- fixed %name.desktop

* Tue Mar 04 2008 Led <led@altlinux.ru> 0.4.5-alt23
- fixed %name.desktop

* Fri Feb 29 2008 Led <led@altlinux.ru> 0.4.5-alt22
- added 32x32, 48x48 and 64x64 icons

* Wed Aug 15 2007 Led <led@altlinux.ru> 0.4.5-alt21
- rebuild with libparted-1.8.so.8
- updated %name-0.4.5-ide.patch
- fixed License

* Mon Jul 23 2007 Led <led@altlinux.ru> 0.4.5-alt20
- fixed %name-0.4.5-ide.patch
- added %name-0.4.5-makefile.patch

* Fri Jul 20 2007 Led <led@altlinux.ru> 0.4.5-alt19
- updated %name-0.4.5-ide.patch

* Fri Jul 20 2007 Led <led@altlinux.ru> 0.4.5-alt18
- optimized %name-0.4.5-ide.patch

* Fri Jul 20 2007 Led <led@altlinux.ru> 0.4.5-alt17
- added %name-0.4.5-ide.patch (fixed #12346)
- cleaned up spec

* Mon May 14 2007 Led <led@altlinux.ru> 0.4.5-alt16
- rebuild with libparted-1.8.so.7

* Sun Mar 25 2007 Led <led@altlinux.ru> 0.4.5-alt15
- rebuild with libparted-1.8.so.6
- cleaned up spec

* Mon Mar 19 2007 Led <led@altlinux.ru> 0.4.5-alt14
- rebuild with libparted-1.8.so.4

* Tue Jan 16 2007 Led <led@altlinux.ru> 0.4.5-alt13
- rebuild with libparted-1.8.so.2

* Mon Dec 04 2006 Led <led@altlinux.ru> 0.4.5-alt12
- fixed %name.desktop

* Thu Nov 23 2006 Led <led@altlinux.ru> 0.4.5-alt11
- rebuild with new libparted
- added %name-0.4.5-notable.patch

* Tue Jul 18 2006 Led <led@altlinux.ru> 0.4.5-alt10
- fixed version
- fixed BuildRequires

* Tue May 30 2006 Led <led@altlinux.ru> 0.4.5-alt9
- enabled jfs again :)
- rebuilt with libparted-1.7.1

* Mon May 29 2006 Led <led@altlinux.ru> 0.4.5-alt8
- disbaled jfs because jfsprogs unmaintained now :(

* Tue May 23 2006 Led <led@altlinux.ru> 0.4.5-alt7
- fixed %name-0.4.5-libparted_1.7.patch

* Mon May 22 2006 Led <led@altlinux.ru> 0.4.5-alt6
- rebuild with libparted-1.7.0
- added %name-0.4.5-libparted_1.7.patch

* Mon May 22 2006 Led <led@altlinux.ru> 0.4.5-alt5
- fixed %%files
- fixed spec

* Wed Feb 15 2006 Led <led@altlinux.ru> 0.4.5-alt4
- added fixed %{name}_ua.ts

* Mon Jan 30 2006 Led <led@altlinux.ru> 0.4.5-alt3
- rebuild with libparted-1.6.25.1

* Tue Jan 26 2006 Led <led@altlinux.ru> 0.4.5-alt2
- enable reiserfs

* Mon Jan 23 2006 Led <led@altlinux.ru> 0.4.5-alt1
- use autoconf instead unsermake.
- uk_UA description and Summary.
- added %name.desktop

* Mon Sep 12 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.4-alt3.1
- rebuild with libparted.

* Mon Mar 21 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt3
- rebuild without reiserfs support

* Sun Feb 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt2
- fix menu
- add run with consolehelper
- update buildreqs

* Thu Sep 02 2004 ALT QA Team Robot <qa-robot@altlinux.org> 0.4.4-alt1.1
- Rebuilt with libparted-1.6.so.12.

* Fri Jun 11 2004 Vitaly Lipatov <lav@altlinux.ru> 0.4.4-alt1
- new version
- cleanup spec, update requires (bug #4318)

* Sun Feb 29 2004 Alexander Nekrasov <canis@altlinux.ru> 0.4.0-alt1
- first build
