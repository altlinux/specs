%def_disable static

Name: libexif-gtk
Version: 0.5.0
Release: alt1

Summary: libexif-gtk provides GTK+ widgets to display/edit EXIF tags
Summary (ru_RU.UTF-8): libexif-gtk содержит элементы интерфейса GTK+ для показа и редактирования EXIF данных
License: LGPLv2+
Group: System/Libraries
Url: http://www.sourceforge.net/projects/libexif
Source0: %name.tar
Patch1: gettext-gtk-version.patch
# Automatically added by buildreq on Wed Mar 13 2013
BuildRequires: libexif-devel libgtk+2-devel

%description
This library provides GTK+ widgets to display/edit EXIF tags.

%description -l ru_RU.UTF-8
Данная библиотека предоставляет элементы интерфейса GTK+ для
показа и редактирования EXIF данных.

%package devel
Summary: Development file for %name library
Summary (ru_RU.UTF-8): Файлы необходимые для написания программ с использованием библиотеки %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This library provides GTK+ widgets to display/edit EXIF tags.

%description devel -l ru_RU.UTF-8
Данная библиотека предоставляет элементы интерфейса GTK+ для
показа и редактирования EXIF данных.

%if_enabled static
%package devel-static
Summary: Static %name library
Summary (ru_RU.UTF-8): Статическая версия библиотеки %name
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This library provides GTK+ widgets to display/edit EXIF tags.

%description devel-static -l ru_RU.UTF-8
Данная библиотека предоставляет элементы интерфейса GTK+ для
показа и редактирования EXIF данных.
%endif

%prep
%setup -n %name
%patch1 -p1

%build
%configure %{subst_enable static}
%make_build

%install
%makeinstall
%find_lang --output=%name.lang %name-5

%files -f %name.lang
%_libdir/*.so.*
%doc NEWS README

%files devel
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/%name

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Mon Oct 09 2023 Dmitriy Khanzhin <jinn@altlinux.org> 0.5.0-alt1
- 0.5.0

* Wed Mar 13 2013 Dmitriy Khanzhin <jinn@altlinux.org> 0.4.0-alt1
- 0.4.0
- buildreq

* Sun May 27 2012 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.6-alt4.cvs2
- rebuilt for debuginfo

* Wed Oct 13 2010 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.6-alt3.cvs2
- rebuilt for soname set-versions

* Tue Dec 09 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.6-alt2.cvs2
- removed obsolete post{,un}_ldconfig calls

* Sun May 18 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.6-alt1.cvs2
- disabled build devel-static subpackage by default
- updated BuildRequires

* Mon Mar 10 2008 Dmitriy Khanzhin <jinn@altlinux.ru> 0.3.6-alt0.cvs2
- 0.3.6cvs2
- license tag updated to LGPLv2+

* Thu Apr 14 2005 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Thu Jun 24 2004 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.3-alt3
- removed -DGTK-DISABLE-DEPRECATED flags

* Thu Dec 11 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.3-alt2
- .la removed

* Tue Sep 16 2003 Sergey V Turchin <zerg at altlinux dot org> 0.3.3-alt1.1
- only rebuild with new libexif

* Fri Mar 21 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.3.3-alt1
- ALTLinux build, ru.po
