%define origname mysql++

Name: lib%origname
Version: 3.1.0
Release: alt2

Summary: C++ API for MySQL
License: LGPL
Group: System/Libraries

Url: http://tangentsoft.net/mysql++
Source: %url/releases/%origname-%version.tar.gz
Source100: libmysql++.watch
Patch0: mysql++-gcc.patch
# http://lists.mysql.com/plusplus/9115 is not enough
Patch1: mysql++-3.1.0-as-needed.patch
Packager: Michael Shigorin <mike@altlinux.ru>

# Automatically added by buildreq on Sat Mar 29 2008
BuildRequires: gcc-c++ libMySQL-devel zlib-devel

Summary(ru_RU.KOI8-R): C++ API для MySQL
Summary(uk_UA.KOI8-U): C++ API для MySQL

%description
The goal of this API is to make working with queries as easy
as working with other STL Containers.

%description -l ru_RU.KOI8-R
Целью этого API является возможность работы с запросами
как с обычными контейнерами STL.

%description -l uk_UA.KOI8-U
Метою цього API ╓ можлив╕сть роботи ╕з запитами як ╕з звичайними
контейнерами STL.

%package devel
Summary: C++ API for MySQL - development part
Summary(ru_RU.KOI8-R): C++ API для MySQL - для разработчика
Summary(uk_UA.KOI8-U): C++ API для MySQL - для розробника
Group: Development/C++
Requires: %name = %version-%release

%description devel
The goal of this API is to make working with queries as easy as
working with other STL Containers.

This package contains files needed to compile software
using %name as a share library.

%description devel -l ru_RU.KOI8-R
Целью этого API является возможность работы с запросами
как с обычными контейнерами STL.

Этот пакет содержит файлы, которые нужны для компиляции программ,
которые используют %name как разделяемую библиотеку.

%description devel -l uk_UA.KOI8-U
Метою цього API ╓ можлив╕сть роботи ╕з запитами як ╕з звичайними
контейнерами STL.

Цей пакунок м╕стить файли, що потр╕бн╕ для комп╕ляц╕╖ програм,
як╕ використовують %name як колективну б╕бл╕отеку.

%if_enabled static
%package devel-static
Summary: C++ API for MySQL - static development library
Summary(ru_RU.KOI8-R): C++ API для MySQL - для разработчика (статическая часть)
Summary(uk_UA.KOI8-U): C++ API для MySQL - для розробника (статична частина)
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
The goal of this API is to make working with queries as easy
as working with other STL Containers.

This package contains files needed to compile software
using %name in a statically-linked form.

%description devel-static -l ru_RU.KOI8-R
Целью этого API является возможность работы с запросами
как с обычными контейнерами STL.

Этот пакет содержит файлы, которые нужны для компиляции программ,
которые компонуются с %name статически.

%description devel-static -l uk_UA.KOI8-U
Метою цього API ╓ можлив╕сть роботи ╕з запитами як ╕з звичайними
контейнерами STL.

Цей пакунок м╕стить файли, що потр╕бн╕ для комп╕ляц╕╖ програм,
як╕ зкомпоновано ╕з %name статично.

%endif

%prep
%setup -n %origname-%version
%patch0 -p1
#patch1 -p1

%build
# FIXME: see http://lists.mysql.com/plusplus/9118
export LDFLAGS="$LDFLAGS -Wl,--no-as-needed"
%configure
%make_build

%install
%makeinstall

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

# TODO: have a closer look at fedora spec

%changelog
* Wed May 09 2012 Michael Shigorin <mike@altlinux.org> 3.1.0-alt2
- added watch file

* Wed Aug 31 2011 Michael Shigorin <mike@altlinux.org> 3.1.0-alt1
- 3.1.0 (thx viy@)
  + build with gcc4.4 fixed with fedora patch (3.1.0-7)
  + linking with --as-needed NOT fixed with upstream
    proposed patch, had to disable it for the time being

* Mon Sep 20 2010 Michael Shigorin <mike@altlinux.org> 3.0.9-alt1.1
- built against libmysqlclient.so.16
- minor spec cleanup

* Wed May 13 2009 Michael Shigorin <mike@altlinux.org> 3.0.9-alt1
- 3.0.9

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 3.0.8-alt1
- 3.0.8
- applied repocop patch

* Sat Mar 29 2008 Michael Shigorin <mike@altlinux.org> 3.0.1-alt1
- 3.0.1
- spec cleanup

* Mon Feb 13 2006 Stanislav Yadykin <tosick@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Sun Mar 06 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.7.28-alt2
- Corrected link error (it was not linked with libstdc++ again...)

* Tue Mar 01 2005 Albert R. Valiev <darkstar@altlinux.ru> 1.7.28-alt1
- New version build
- Corrected linkage (was not linked with libstdc++)
- Removed old gcc-3.2 patches

* Tue Feb 03 2004 Michael Shigorin <mike@altlinux.ru> 1.7.9-alt5
- force gcc3.2 build (available gcc3.3 patch is broken)

* Mon Dec 08 2003 Michael Shigorin <mike@altlinux.ru> 1.7.9-alt4
- removed *.la; don't build static subpackage by default
- fixed descriptions
- fixed Url (thanks to Andrey S Pankov <casper AT casper org ua>)
- added sqlplusint/undef_short to includes per Andrey's request

* Mon Oct 06 2003 Michael Shigorin <mike@altlinux.ru> 1.7.9-alt3
- added patch for gcc-3.2.2+ from 
  http://www.mysql.com/downloads/api-mysql++.html

* Thu Sep 11 2003 Michael Shigorin <mike@altlinux.ru> 1.7.9-alt2
- rebuild (updated build requires, spec cleanup)
- patch2 removed

* Fri Mar 07 2003 Michael Shigorin <mike@altlinux.ru> 1.7.9-alt1
- built for ALT Linux
- based on package for SuSE 8 (incl. gcc3 patches)
- *heavy* spec cleanups

* Thu Oct 17 2002 Philipp Berndt <philipp.berndt@gmx.net>
- packaged

