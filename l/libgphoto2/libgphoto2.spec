%define sover 6
%define sover_port 12
%def_disable static
%define _libexecdir /usr/libexec

Name: libgphoto2
Version: 2.5.30
Release: alt2

Group: System/Libraries
Summary: Library to access to digital cameras
Summary (ru_RU.UTF-8): Библиотека функций для работы с цифровыми фотокамерами
Url: http://www.gphoto.org/
License: LGPLv2+
Packager: Dmitriy Khanzhin <jinn@altlinux.org>

# Automatically added by buildreq on Mon Oct 11 2010
BuildRequires: doxygen flex gcc-c++ libcurl-devel libexif-devel libgd2-devel libjpeg-devel
BuildRequires: liblockdev-devel libltdl7-devel libusb-devel libxml2-devel

# IMHO, this build requires are needs when build with cdk
#BuildRequires: libncurses-devel libtinfo-devel

# Url for source code downloads now http://sourceforge.net/project/showfiles.php?group_id=8874
Source0: %name-%version.tar
Patch0: %name-2.5.30-alt-translation.patch

%description
This library contains all the functionality to access to modern digital
cameras via USB or the serial port.

%package -n %name-%sover
Group: System/Libraries
Summary: Library to access to digital cameras
Summary (ru_RU.UTF-8): Библиотека функций для работы с цифровыми фотокамерами
License: LGPLv2+
Provides: %name = %version-%release
Obsoletes: %name < %version-%release

%description -n %name-%sover
The %name library can be used by applications to access various digital
camera models, via standard protocols such as USB Mass Storage and PTP,
or vendor-specific protocols.
This package contains the library.

%package -n %{name}_port-%sover_port
Group: System/Libraries
Summary: Library to access to digital camera ports
Summary (ru_RU.UTF-8): Библиотека функций для работы с цифровыми фотокамерами
License: LGPLv2+

%description  -n %{name}_port-%sover_port
The %name library can be used by applications to access various digital
camera models, via standard protocols such as USB Mass Storage and PTP,
or vendor-specific protocols.
This package contains the runtime code for port access. 

%package -n %name-devel
Group: Development/C
Summary: Headers and links to compile against the %name library
Summary (ru_RU.UTF-8): Заголовочные и другие файлы для компиляции приложений с библиотекой libgphoto2
License: LGPLv2+
Requires: %name-%sover = %version-%release

%description -n %name-devel
This package contains all files which one needs to compile programs using
the %name library.

%package -n %name-devel-doc
Group: Development/Other
Summary: Development documentation of the %name library
Summary (ru_RU.UTF-8): Докумнтация для разработчиков библиотеки libgphoto2
License: LGPLv2+
BuildArch: noarch
Requires: %name-%sover = %version-%release

%description -n %name-devel-doc
This package contains development documentation of the %name library.

%if_enabled static
%package -n %name-devel-static
Group: Development/C
Summary: Static versions of %name
Summary (ru_RU.UTF-8): Статические версии библиотек libgphoto2
License: LGPLv2+
Requires: %name-devel = %version-%release

%description -n %name-devel-static
This package contains libraries which one needs to compile programs statically linked
against %name library.
%endif

##### TRANSLATED DESCRIPTIONS  #####

%description -l ru_RU.UTF-8
Библиотека предоставляет все необходимые функции для обмена данными
с современными цифровыми фотокамерами посредством USB или последовательного порта.

%description -n %name-%sover -l ru_RU.UTF-8
Библиотека libgphoto2 используется приложениями для доступа к различным моделям
цифровых камер, посредством стандартных протоколов, таких как USB-накопитель
и PTP, или специфических протоколов производителей.
Этот пакет ссодержит собственно библиотеку.

%description -n %{name}_port-%sover_port -l ru_RU.UTF-8
Библиотека libgphoto2 используется приложениями для доступа к различным моделям
цифровых камер, посредством стандартных протоколов, таких как USB-накопитель
и PTP, или специфических протоколов производителей.
Этот пакет ссодержит исполнимый код для доступа к портам.

%description -n %name-devel -l ru_RU.UTF-8
Пакет содержит все необходимые файлы для компиляции программ, использующих
библиотеку libgphoto2.

%description -n %name-devel-doc -l ru_RU.UTF-8
Пакет содержит докумнтацию для разработчиков библиотеки libgphoto2.

%if_enabled static
%description -n %name-devel-static  -l ru_RU.UTF-8
Пакет содержит статические версии библиотек для компиляции программ, использующих
библиотеку libgphoto2.
%endif

%prep
%setup -n %name-%version
%patch0 -p1

%build
sed -i '/driverdir/d' libgphoto2_port/libgphoto2_port.pc.in
%autoreconf
export udevscriptdir=/lib/udev
export utilsdir=%_libexecdir/%name
%configure \
    %{subst_enable static} \
    --with-drivers=all \
    --disable-rpath
%make_build

%install
%makeinstall_std

# create udev support
/bin/mkdir -p %buildroot/lib/udev/rules.d
/bin/touch %buildroot/lib/udev/rules.d/40-%name.rules
/bin/mkdir -p %buildroot/lib/udev/hwdb.d
/bin/touch %buildroot/lib/udev/hwdb.d/40-%name.hwdb

# correct content of doc. directory
/bin/rm -rf %buildroot/%_datadir/doc/%name/{linux-hotplug,ABOUT-NLS,COPYING,ChangeLog,RELEASE-HOWTO.md}
/bin/cp OUTDATED.txt %buildroot/%_datadir/doc/%name/

# remove circular symlink in /usr/include/gphoto2
/bin/rm -f %buildroot%_includedir/gphoto2/gphoto2
# udev helper not used now
/bin/rm -f %buildroot/lib/udev/check-ptp-camera
# remove .la files
/bin/rm -f %buildroot%_libdir/%name/*/*.la
/bin/rm -f %buildroot%_libdir/%{name}_port/*/*.la

%find_lang --output=%name.lang %name-%sover
%find_lang --append --output=%name.lang %{name}_port-%sover_port

##### PRE/POST INSTALL SCRIPTS #####

%pre -n %name-%sover
# create group
/usr/sbin/groupadd -fr camera || :

%post -n %name-%sover
# create udev rules
%_libexecdir/%name/print-camera-list --verbose udev-rules version 201 owner root mode 0660 group camera > /lib/udev/rules.d/40-%name.rules 2> /dev/null
%_libexecdir/%name/print-camera-list hwdb > /lib/udev/hwdb.d/40-%name.hwdb 2> /dev/null

%triggerpostun -- %name <= 2.4.0
/sbin/ldconfig


##### FILE LISTS FOR ALL BINARY PACKAGES #####

%files -n %name-%sover -f %name.lang
%_libdir/%name.so.*
%dir %_libdir/%name
%dir %_libdir/%name/*
%_libdir/%name/*/*.so
%dir %_libexecdir/%name
%_libexecdir/%name/print-camera-list
%ghost /lib/udev/hwdb.d/*
%ghost /lib/udev/rules.d/*
%dir %_datadir/%name
%_datadir/%name/*
%dir %_datadir/doc/%name
%_datadir/doc/%name/AUTHORS
%_datadir/doc/%name/NEWS
%_datadir/doc/%name/README.md
%_datadir/doc/%name/OUTDATED.txt
%exclude %_datadir/locale/*/LC_MESSAGES/%{name}_port*

%files -n %{name}_port-%sover_port -f %name.lang
%_libdir/%{name}_port.so.*
%dir %_libdir/%{name}_port
%dir %_libdir/%{name}_port/*
%_libdir/%{name}_port/*/*.so
%dir %_datadir/%{name}_port
%_datadir/%{name}_port/*
%dir %_datadir/doc/%{name}_port
%_datadir/doc/%{name}_port/*
%exclude %_datadir/locale/*/LC_MESSAGES/%{name}*

%files -n %name-devel
%_bindir/*-config
%_includedir/gphoto2
%_libdir/*.so
%_libdir/pkgconfig/*
%_man3dir/%{name}*

%files -n %name-devel-doc
%_datadir/doc/%name/*
%exclude %_datadir/doc/%name/AUTHORS
%exclude %_datadir/doc/%name/NEWS
%exclude %_datadir/doc/%name/README.md
%exclude %_datadir/doc/%name/OUTDATED.txt

%if_enabled static
%files -n %name-devel-static
%_libdir/*.a
%_libdir/%name/*/*.a
%_libdir/%{name}_port/*/*.a
%endif

%changelog
* Mon Jan 23 2023 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.30-alt2
- updated russian translation, thanks to Maria Shikunova (translation-team at basealt.ru)

* Fri Aug 19 2022 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.30-alt1
- 2.5.30

* Mon Mar 07 2022 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.29-alt1
- 2.5.29

* Mon Jan 03 2022 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.28-alt1
- 2.5.28

* Tue Jul 20 2021 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.27-alt2
- finally removed hal support

* Sun Feb 21 2021 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.27-alt1
- 2.5.27

* Thu Oct 15 2020 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.26-alt1
- 2.5.26

* Wed May 27 2020 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.25-alt1
- 2.5.25

* Fri Mar 13 2020 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.24-alt1
- 2.5.24
- added libcurl-devel into BR for support new Lumix WiFi cameras
- removed unneeded patch and libusb0 support

* Thu Jul 25 2019 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.23-alt1
- 2.5.23
- drivers for cameras older than 15 years disabled for installation,
  see OUTDATED.txt for notes

* Thu Jan 03 2019 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.22-alt1
- 2.5.22

* Thu Dec 13 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.21-alt1
- 2.5.21
- updated patch

* Sun Oct 28 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.20-alt1
- 2.5.20

* Wed Jul 25 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.19-alt1
- 2.5.19

* Mon May 14 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.18-alt1
- 2.5.18

* Sat Apr 21 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.17-alt1
- 2.5.17

* Sun Mar 11 2018 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.16-alt1
- 2.5.16

* Sat Aug 05 2017 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.14-alt1
- 2.5.14

* Wed Apr 12 2017 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.13-alt1
- 2.5.13
- updated patch

* Sat Dec 17 2016 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.11-alt1
- 2.5.11

* Fri Mar 18 2016 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.9-alt1
- 2.5.9

* Mon Jul 06 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.8-alt1
- 2.5.8

* Tue Mar 17 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.7-alt2
- cut out more smaller subpackages to comply with the Shared libs policy
- added Provides/Obsoletes

* Tue Jan 27 2015 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.7-alt1
- 2.5.7

* Mon Oct 06 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.5.1-alt1
- 2.5.5.1 - regression fix release of 2.5.5

* Mon Apr 07 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.4-alt1
- 2.5.4

* Fri Jan 31 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.3.1-alt1
- 2.5.3.1

* Fri Jan 31 2014 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.3-alt1
- 2.5.3
- removed unneeded macro add_optflags

* Mon Jun 10 2013 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.2-alt1
- 2.5.2
- dropped patch1
- added libxml2-devel to buildrequires
  + added add_optflags macro for find libxml2 includes (thx to at@ and ldv@)

* Mon Feb 11 2013 Dmitriy Khanzhin <jinn@altlinux.org> 2.5.1.1-alt1
- 2.5.1.1
- print-camera-list moved to /usr/libexec

* Tue Jul 10 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.5.0-alt1
- 2.5.0
- dropped increase_max_entries patch
- fixed warnings of undefined symbols

* Sun May 20 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.14-alt2
- added libgd2-devel to BuildRequires and recovered libusb-compat-devel

* Wed Apr 25 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.14-alt1
- 2.4.14
- build with libusb-1.0 support
- fixed underlinked libraries

* Mon Mar 19 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.13-alt1
- 2.4.13

* Mon Feb 06 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.12-alt1
- 2.4.12

* Sat Aug 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.11-alt1
- 2.4.11
- removed unneeded patch11
- udev rules file moved to /lib/udev/rules.d/

* Sun Mar 20 2011 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10.1-alt2
- disabled rpath
- removed circular symlink in /usr/include/gphoto2

* Tue Oct 12 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10.1-alt1
- 2.4.10.1

* Mon Oct 04 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10-alt2
- start packing libgphoto2 separate from gphoto2
- build without libhal

* Tue Aug 17 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Tue Mar 23 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.8-alt1
- 2.4.8

* Mon Oct 19 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.7-alt2
- removed unneeded symlink and provides

* Sat Aug 22 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.7-alt1
- 2.4.7
- removed unneeded timeout
- added usb id for Canon PowerShot A580

* Sun May 17 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt3
- added timeout into script check-ptp-camera

* Sun May 10 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt2
- increased max number of entries in the camera list (ALT #19752)

* Sat Apr 18 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.5-alt1
- 2.4.5
- updated build requires

* Sun Mar 29 2009 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.4-alt1
- 2.4.4
- dropped unnecessary patch
- updated build requires
- changed the means of creating additional provides

* Sun Dec 07 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.3-alt2
- removed obsolete post{,un}_ldconfig calls

* Tue Oct 28 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.3-alt1
- 2.4.3

* Wed Sep 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.2-alt2
- added patch for compatibility with libusb-1 API (fix bug #17264, thanks to ab@)

* Wed Aug 27 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.2-alt1
- 2.4.2
- updated BuildRequires
- soname changed back to %name.so.2 (#16542) and saved so.6 for
  compatibility with previous build (thanks to eostapets@ and rider@)
- returned russian summaries and descriptions from slava@

* Sat May 24 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt2.svn10945
- moved HAL support into %name, %name-hal has deleted
- changed postinstall script (#15548)

* Thu May 22 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt1.svn10945
- hal supported (#15547, added %name-hal subpackage)
- perfected location of docs

* Wed Mar 26 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.3
- removed *.la files

* Sun Mar 23 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.2
- switched back to build with separate source code tarballs
- disabled build hotplug subpackage
- corrected content of doc. directory
- turn back requires = %%version-%%release for %name
- build with included .la files

* Sun Mar 09 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 2.4.0-alt0.svn10945.1
- updated version to 2.4.0
- svn snapshot 10945
- drop unneeded patches
- fixed bug #13823

* Mon Nov 19 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt7
- add Fuji FinePix S5700 (patch backported from svn commit 10728)
- russian summary and description removed
- license tags changed to GPLv2+ and LGPLv2+

* Sat Sep 22 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt6
- add Canon PowerShot A450 (patch from svn)
- change alt-fix-rules.patch
- enabled check ptp camera for unknown cameras

* Tue Jun 05 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt5
- disable Canon fast directory retrieval (even so patch2 imported from SVN)
- bzip ChangeLog
- added tag License into %name-hotplug

* Sat May 26 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt4.10
- renamed patch1
- fix fast directory retrieval on Canon PowerShot A430

* Sun Mar 11 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt4
- fix requires
- move creating udev rules back into %name package

* Mon Jan 29 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt3
- Requires: hotplug removed from libgphoto2 package (#10695)
- udev and hotplug communications moved into separate packages

* Fri Jan 19 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt2
- used builtin generator udev and hotplug rules

* Tue Jan 16 2007 Dmitriy Khanzhin <jinn@altlinux.ru> 2.3.1-alt1
- new version
- renamed and little corrected udev rules
  (use udev >= 0.98)

* Sun Jan 14 2007 Alexey Morsov <swi@altlinux.ru> 2.3.0-alt2.1
- Add udev rules (fix bug #10661)
- change Packager

* Fri Dec 29 2006 Alexey Morsov <swi@altlinux.ru> 2.3.0-alt2
- NMU

* Fri Dec 08 2006 Alexey Morozov <morozov@altlinux.org> 2.3.0-alt1
- New version (2.3.0)
- static libraries made optional and skipped by default
- buildreqs cleanup
- switched to gphoto-suite for builds
- dropped obsoleted Nikon-4600-ptp-Support.c.patch (#0)

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 2.1.6-alt2.1
- Rebuilt with libreadline.so.5.

* Thu Nov 24 2005 Anton Farygin <rider@altlinux.ru> 2.1.6-alt2
- NMU:
    - updated to new version
    - removed included to mainstream pathes
    - added Nikon 4600 autodetect
    - added firsttime.d script
    - fixed postscript for use DURING_INSTALL

* Mon Apr 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1.1
- rebuild against libexif.so.12.
- removed hostinfo, libgphoto2-devel from BuildRequires.

* Sat Jan 01 2005 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.5-alt1
- 2.1.5
- partial Russian translation
- i18n fix

* Wed Jun 23 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt3
- no update-usb.usermap call in postinstall script

* Tue Jun 08 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt2
- usbcam.group replaced by usbcam.console. Group camera removed.

* Sat Feb 21 2004 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Fri Dec 12 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.2-alt2
- .la removed

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 2.1.2-alt1
- new version
- some spec cleanup
- fix requires

* Sat Aug 23 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.7
- Serial fix

* Sun Jun 15 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.6
- libgphoto2 requirements fix (hotplug).

* Wed May 28 2003 Vyacheslav Dikonov <slava@altlinux.ru> 2.1.1-alt0.5
- non-root execution (all users in group 'camera' can now use gphoto2)

* Wed Apr 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt0.4
- russian descriptions (slava).

* Wed Apr 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt0.3
- more improvements.
- build with new libexif.

* Sun Mar 30 2003 ZerG <zerg@altlinux.ru> 2.1.1-alt0.2
- new version
- improve spec

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.1.0-alt1
- Rebuilt in new environment
- Rebuilt with liblockdev
- Some spec fixes
- 2.1.0

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt2
- Rebuild with new binutils

* Fri Mar 01 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt1
- Release %name 2.0

* Thu Dec 06 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt0.3cvs20011204
- Build from CVS
- Rebuild with new libusb

* Fri Aug 24 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.0-alt0.2beta1
- Added devel-static package
- Some spec cleanup
- Fixed filelists

* Fri Aug 23 2001 Rider <rider@altlinux.ru> 2.0-alt0.1beta1
- first BUILD for ALT
