%set_gcc_version 4.1

Name: libncursesxx
Version: 0.0.1
Release: alt15

Summary: C++ bindings for ncurses library
License: LGPL
Group: System/Libraries

Url: http://sisyphus.ru/ru/srpm/Sisyphus/libncursesxx

%define real_name ncursesxx

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

# Automatically added by buildreq on Fri Mar 19 2004
BuildRequires: gcc4.1-c++ libncurses-devel libstdc++4.1-devel libtinfo-devel

Conflicts: libcolorifer <= 1.0.1-alt7

%description
C++ bindings for ncurses library

%package devel
Summary: Development part of %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Contents header files and development libraries for %name

%package devel-static
Summary: Static libraries for %name
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
Contents static libraries for %name

%prep
%setup

%build
%make_build

%install
%makeinstall

%files
%doc ChangeLog
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%files devel-static
%_libdir/*.a

%changelog
* Tue May 22 2012 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt15
- fix build

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt14
- rebuild

* Tue Oct 27 2009 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt13
- add Url tag

* Wed Dec 03 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt12
- fixed build

* Sun Nov 30 2008 Denis Smirnov <mithraen@altlinux.ru> 0.0.1-alt11
- build with gcc 4.1

* Fri Mar 10 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt10
- fixed libdir

* Thu Mar 09 2006 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt9
- fixed linkage

* Tue Jan 18 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt8
- temporary turn off compilation of ncursesw sample

* Wed Jan 12 2005 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt7
- ready for gcc3.4

* Tue May 11 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt6
- beta2:
  - improve update/refresh technics (remove unnesessary static methods)
  - remove getkey method (it's unnesessary with normal update/refresh)
  - fix top/bottom/show/hide methods (continue walk to the childs)
  - added ability to compare panels on z-order.

* Wed Apr 14 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt5
- beta1
  - minor bugfixes
  - window,pad and panel are copyable objects now
  - split pen and wpen, now we can work only if non-widechar version of ncurses installed
  - link most samples with libncurses (not with libncursesw)

* Tue Mar 30 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt4
- 0.0.1alpha3

* Wed Mar 24 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt3
- update from CVS.

* Mon Mar 22 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt2
- alpha2

* Fri Mar 19 2004 Stanislav Ievlev <inger@altlinux.org> 0.0.1-alt1
- Initial release
