%def_enable shared
%def_disable static
%define debug no
%def_with pic
%def_disable rpath
%def_enable warnings
%def_disable profile
%def_enable dependency_tracking
%def_enable pch
%def_enable new_ldflags
%def_disable final
%def_disable closure
%def_disable nmcheck
%def_disable embedded
%def_disable qtopia
%def_disable mac
%def_enable mt
%def_enable threading
%def_enable nfs_hack
%def_without arts
%def_with ext_sqlite2
%def_with ext_sqlite3
#----------------------------------------------------------------------
%define subst_enable_to() %{expand:%%{?_enable_%{1}:--enable-%{2}}} %{expand:%%{?_disable_%{1}:--disable-%{2}}}

%add_findpackage_path %_K3bindir

%define Name digiKam
Name: digikam
%define lname lib%name
%define prerel %nil
%define tail %nil
Version: 0.9.6
Release: alt4
Group: Graphics
Summary: A Photo Management Application for KDE
Summary(uk_UA.CP1251): Програма керування фотографіями для KDE
Summary(ru_RU.CP1251): Программа управления фотографиями для KDE
License: GPLv2
URL: http://www.%name.org/
Source: %name-%version%prerel%tail.tar
Patch: %name-%version%prerel-%release.patch
Patch1: digikam-0.9.6-alt-fix-compile.patch
Requires: kdeaddons-konqueror
Requires: %lname = %version-%release
Requires: %name-data = %version-%release
Requires: %name-i18n = %version-%release
Packager: Led <led@altlinux.ru>

BuildRequires: doxygen gcc-c++ imake xml-utils
BuildRequires: libgphoto2-devel libjpeg-devel imlib2-devel
BuildRequires: libdnet-devel
%{?_with_ext_sqlite2:BuildRequires: libsqlite-devel}
%{?_with_ext_sqlite3:BuildRequires: libsqlite3-devel}
BuildRequires: libXext-devel libXrender-devel libXt-devel xorg-cf-files
BuildRequires: autoconf >= 2.5
BuildRequires: automake >= 1.7
BuildRequires: libqt3-devel >= 3.3
BuildRequires: kdelibs-devel >= 3.4
BuildRequires: libkipi-devel >= 0.1.6
BuildRequires: libtiff-devel >= 3.6
BuildRequires: libpng-devel >= 1.2
BuildRequires: liblcms-devel >= 1.14
BuildRequires: libjasper-devel >= 1.7
BuildRequires: libkexiv2-devel >= 0.1.7
BuildRequires: libkdcraw-devel >= 0.1.5
BuildRequires: desktop-file-utils

%description
%Name is an easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating digital
photos a "snap". An easy to use interface is provided to connect to
your digital camera, preview the images and download and/or delete
them.
%Name buildin image editor makes the common photo correction a
simple task. The image editor is extensible via plugins.
%Name can also make use of the KIPI image handling plugins to extend
it's capabilities even further for photo manipulations, import and
export, etc.

%description -l uk_UA.CP1251
%Name - проста у використанні, але потужна програма керування
цифровими фотографіями, яка робить  імпорт, організацію та
маніпулювання цифровими фотографіями "миттєвим". Простий у використанні
інтерфейс забезпечує з'єднання з вашою цифровою камерою, попередній
перегляд зображень та завантаження і/або видалення їх.
Вбудований редактор зображень %Name робить поширені коректування
фотографій простим завданням. Редактор зображення може розширюватись за
рахунок плагінів.
%Name може також використовувати плагіни підтримки зображень KIPI
для розширення своїх можливостей в маніпулюванны фотографіями, імпорту
та експорту, та інше.

%description -l ru_RU.CP1251
%Name - простая в использовании, но мощная программа управления
цифровыми фотографиями, которая делает импорт, организацию и
манипулирование цифровыми фотографиями "мгновенным". Простой в
использовании интерфейс обеспечивает соединение с вашей цифровой
камерой, предварительный просмотр и загрузку и/или их удаление.
Встроенный редактор изображений %Name делает распространённые
корректировки фотографий простой задачей. Редактор изображений может
расширяться за счёт плагинов.
%Name может также использовать плагины поддержки изображений KIPI
для расширения своих возможностей в манипулировании фотографиями,
импорта и экпорта, и другое.


%package data
Group: Graphics
Summary: A Photo Management Application for KDE
Summary(uk_UA.CP1251): Програма керування фотографіями для KDE
Summary(ru_RU.CP1251): Программа управления фотографиями для KDE
Requires: %name = %version-%release
BuildArch: noarch

%description data
%Name is an easy to use and powerful digital photo management
application, which makes importing, organizing and manipulating digital
photos a "snap". An easy to use interface is provided to connect to
your digital camera, preview the images and download and/or delete
them.
%Name buildin image editor makes the common photo correction a
simple task. The image editor is extensible via plugins.
%Name can also make use of the KIPI image handling plugins to extend
it's capabilities even further for photo manipulations, import and
export, etc.

%description data -l uk_UA.CP1251
%Name - проста у використанні, але потужна програма керування
цифровими фотографіями, яка робить  імпорт, організацію та
маніпулювання цифровими фотографіями "миттєвим". Простий у використанні
інтерфейс забезпечує з'єднання з вашою цифровою камерою, попередній
перегляд зображень та завантаження і/або видалення їх.
Вбудований редактор зображень %Name робить поширені коректування
фотографій простим завданням. Редактор зображення може розширюватись за
рахунок плагінів.
%Name може також використовувати плагіни підтримки зображень KIPI
для розширення своїх можливостей в маніпулюванны фотографіями, імпорту
та експорту, та інше.

%description data -l ru_RU.CP1251
%Name - простая в использовании, но мощная программа управления
цифровыми фотографиями, которая делает импорт, организацию и
манипулирование цифровыми фотографиями "мгновенным". Простой в
использовании интерфейс обеспечивает соединение с вашей цифровой
камерой, предварительный просмотр и загрузку и/или их удаление.
Встроенный редактор изображений %Name делает распространённые
корректировки фотографий простой задачей. Редактор изображений может
расширяться за счёт плагинов.
%Name может также использовать плагины поддержки изображений KIPI
для расширения своих возможностей в манипулировании фотографиями,
импорта и экпорта, и другое.


%package utils
Group: Graphics
Summary: %Name utils
Requires: %lname = %version-%release
Conflicts: %name < 0.9.5-alt0.3

%description utils
Utilities for %Name data.


%package i18n
Group: Graphics
Summary: Languages support for %Name
Requires: %name = %version-%release
BuildArch: noarch

%description i18n
Languages support for %Name.


%if_enabled shared
%package -n %lname
Group: System/Libraries
Summary: %Name library

%description -n %lname
%Name library.
%endif


%package image-plugins
Group: Graphics
Summary: %Name image plugins
Summary(uk_UA.CP1251): Втулки обробки зображень для %Name
Summary(ru_RU.CP1251): Плагины обработки изображений для %Name
Requires: %name = %version-%release

%description image-plugins
%Name plugins for additional functionalities in ImageEditor and
Showfoto.


%package -n %lname-devel
Group: Development/KDE and QT
Summary: Development files for %Name
Requires: %lname = %version-%release

%description -n %lname-devel
Development files for %Name.


%prep
%setup -n %name-%version%prerel%tail
%patch -p1
%patch1 -p1


%build
%add_optflags -I%_includedir/tqtinterface
#    %{subst_enable shared} \
#    %{subst_enable static} \
#    %{subst_enable rpath} \
#    %{subst_enable_to new_ldflags new-ldflags} \
#    %{subst_enable_to dependency_tracking dependency-tracking} \
#    %{subst_enable threading} \
#    %{subst_with arts} \
%K3configure \
    %{?debug:--enable-debug=%debug} \
    %{subst_with pic} \
    %{subst_enable warnings} \
    %{subst_enable profile} \
    %{subst_enable pch} \
    %{subst_enable final} \
    %{subst_enable closure} \
    %{subst_enable nmcheck} \
    %{subst_enable embedded} \
    %{subst_enable qtopia} \
    %{subst_enable mac} \
    %{subst_enable mt} \
    %{subst_enable_to nfs_hack nfs-hack} \
    %{subst_enable gcc-hidden-visibility} \
    %{?_with_ext_sqlite3:--without-included-sqlite3}

%make_build
#bzip --best --force --keep ChangeLog


%install
%K3install
install -d -m 0755 %buildroot%_docdir/%name-%version
install -m 0644 AUTHORS NEWS README TODO %buildroot%_docdir/%name-%version/
#install -m 0644 ChangeLog.* %buildroot%_docdir/%name-%version/

%K3find_lang %name
%K3find_lang --with-kde --without-mo --output=%name-data.lang %name


%files
%_K3bindir/%name
%_K3bindir/showfoto
%_K3lib/kio_%{name}*.so


%files utils
%_K3bindir/%{name}themedesigner
%_K3bindir/digitaglinktree
%_man1dir/*


%if_enabled shared
%files -n %lname
%_libdir/%lname.so.*
%endif


%files data -f %name-data.lang
%doc %_docdir/%name-%version
%_K3apps/%name
%_K3apps/showfoto
%_K3apps/konqueror/servicemenus/*
%_K3srv/%{name}*.protocol
%_kde3_iconsdir/hicolor/*/apps/*.*
%_K3xdg_apps/*.desktop


%files i18n -f %name.lang


%files image-plugins
%_K3lib/%{name}imageplugin_*.so
%_K3srv/%{name}imageplugin_*.desktop
%_K3srvtyp/digikamimageplugin.desktop


%files -n %lname-devel
%doc HACKING
%_libdir/%lname.so
%_K3includedir/*


%changelog
* Tue Feb 22 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt4
- move to alternate place

* Mon Jan 24 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt3
- fix to build

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 0.9.6-alt2
- rebuilt with new kexiv2

* Sat Jul 04 2009 Led <led@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sat Mar 21 2009 Led <led@altlinux.ru> 0.9.5-alt1
- 0.9.5 release

* Sun Feb 01 2009 Led <led@altlinux.ru> 0.9.5-alt0.5
- 0.9.5-beta3

* Sun Jan 25 2009 Led <led@altlinux.ru> 0.9.5-alt0.4
- really applied digikam-0.9.3-drops-count.patch

* Sat Jan 24 2009 Led <led@altlinux.ru> 0.9.5-alt0.3
- added subpackages -data, -utils, -i18n

* Sat Jan 24 2009 Led <led@altlinux.ru> 0.9.5-alt0.2
- applied digikam-0.9.3-drops-count.patch (fixed #17763),
  thanx Andrey Klaus

* Sat Dec 27 2008 Led <led@altlinux.ru> 0.9.5-alt0.1
- 0.9.5-beta2
- cleaned up spec
- update BuildRequires

* Sun Sep 14 2008 Led <led@altlinux.ru> 0.9.4-alt3
- rebuild with libkdcraw.so.4

* Sat Aug 09 2008 Led <led@altlinux.ru> 0.9.4-alt2
- fixed *.desktop

* Sun Jul 20 2008 Led <led@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sat Jul 12 2008 Led <led@altlinux.ru> 0.9.4-alt0.9
- 0.9.4-rc2

* Wed Jun 18 2008 Led <led@altlinux.ru> 0.9.4-alt0.8
- added %name-0.9.4-rc1-ext_sqlite.patch

* Wed Jun 18 2008 Led <led@altlinux.ru> 0.9.4-alt0.7
- 0.9.4-rc1
- updated %name-0.9.4-rc1-compat.patch

* Tue May 27 2008 Led <led@altlinux.ru> 0.9.4-alt0.6
- 0.9.4-beta5

* Mon May 05 2008 Led <led@altlinux.ru> 0.9.4-alt0.5
- 0.9.4-beta4
- updated %name-0.9.4-beta4-compat.patch

* Wed Apr 09 2008 Led <led@altlinux.ru> 0.9.4-alt0.4
- 0.9.4-beta3

* Fri Apr 04 2008 Led <led@altlinux.ru> 0.9.4-alt0.3
- fixed License
- fixes desktop-mime-entry

* Sun Mar 30 2008 Led <led@altlinux.ru> 0.9.4-alt0.2
- 0.9.4-beta2
- updated %name-0.9.4-beta2-compat.patch

* Fri Mar 14 2008 Led <led@altlinux.ru> 0.9.4-alt0.1
- 0.9.4-beta1
- added %name-0.9.4-beta1-compat.patch

* Sat Dec 22 2007 Led <led@altlinux.ru> 0.9.3-alt1
- 0.9.3 release

* Wed Dec 19 2007 Led <led@altlinux.ru> 0.9.3-alt0.4
- 0.9.3-rc1

* Sat Dec 08 2007 Led <led@altlinux.ru> 0.9.3-alt0.3
- 0.9.3-beta3

* Tue Nov 06 2007 Led <led@altlinux.ru> 0.9.3-alt0.2
- 0.9.3-beta2
- removed %name-0.9.3-beta1-po.patch

* Thu Oct 11 2007 Led <led@altlinux.ru> 0.9.3-alt0.1
- 0.9.3-beta1
- added %name-0.9.3-beta1-po.patch

* Sat Sep 22 2007 Led <led@altlinux.ru> 0.9.2-alt2
- rebuild with new libkdcraw.so.2 and libkexiv2.so.3

* Thu Jun 14 2007 Led <led@altlinux.ru> 0.9.2-alt1
- 0.9.2 release

* Mon Jun 04 2007 Led <led@altlinux.ru> 0.9.2-alt0.2
- 0.9.2-beta3
- cleaned up %%files

* Sat May 12 2007 Led <led@altlinux.ru> 0.9.2-alt0.1
- 0.9.2-beta1
- removed %name-0.9.0-include.patch
- updated BuildRequires
- cleaned up spec
- added %name-image-plugins subpackage
- renamed subpackage %name-devel to %lname-devel
- fixed %%description

* Mon May 07 2007 Led <led@altlinux.ru> 0.9.1-alt2
- rebuild with libkexiv2.so.0.2.0

* Wed Mar 07 2007 Led <led@altlinux.ru> 0.9.1-alt1
- 0.9.1
- updated BuildRequires

* Wed Dec 20 2006 Led <led@altlinux.ru> 0.9.0-alt1
- fixed %name-0.9.0-include.patch

* Mon Dec 18 2006 Led <led@altlinux.ru> 0.9.0-alt0.1
- 0.9.0
- removed %name-0.8.0-kgamma.patch (fixed in upstream)
- added %name-0.9.0-include.patch

* Thu Nov 23 2006 Led <led@altlinux.ru> 0.8.2-alt0.1
- 0.8.2
- cleaned up spec
- removed separate uk translation (in upstream now)

* Thu Mar 16 2006 Led <led@altlinux.ru> 0.8.1-alt1
- 0.8.1
- added uk translation
- fix %name.desktop
- update %%description

* Thu Dec 29 2005 Sergey V Turchin <zerg at altlinux dot org> 0.8.0-alt1
- new version

* Wed Aug 17 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.3-alt1
- new version

* Fri Jan 21 2005 Sergey V Turchin <zerg at altlinux dot org> 0.7.1-alt1
- new version

* Tue Dec 07 2004 Sergey V Turchin <zerg at altlinux dot org> 0.7-alt1
- new version

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.2-alt1
- new version

* Wed May 12 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6.1-alt1
- new version

* Mon Mar 22 2004 Sergey V Turchin <zerg at altlinux dot org> 0.6-alt1
- new version

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 0.5.1-alt4
- rebuild with new libexif

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt3
- rebuild with new libexif

* Thu Oct 24 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt2
- rebuild with new gphoto2 && KDE3.1

* Thu Sep 12 2002 Sergey V Turchin <zerg@altlinux.ru> 0.5.1-alt1
- build for ALT

* Fri Aug 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-4mdk
- from Xavier Granier <xavier.granier@laposte.net> :
	- Move menu to Multimedia/Graphics
	- add BuildRequires:            libexif7-devel

* Tue Jul 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- add in-spec-menu

* Tue Jul 23 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- adjust buildrequires

* Wed Jul 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- from Gilles CAULIER <caulier.gilles@free.fr> :
	- Update release 0.5.0 : KDE3 port. Update spec file.

* Fri Jul 12 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.4.1-2mdk
- Fix some bugs on 'spec' file

* Mon Jul 08 2002 Gilles CAULIER <caulier.gilles@free.fr> 0.4.1-1mdk
- Original release
