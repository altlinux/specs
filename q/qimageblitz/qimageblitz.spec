Name: qimageblitz
Version: 0.0.6
Release: alt4

Summary: Graphical effect and filter library for KDE4.0
License: BSD
Group: System/Libraries
Url: http://www.kde.org/
Packager: Sergey V Turchin <zerg@altlinux.org>

Source: %name-%version.tar
# FC
Patch1: qimageblitz-0.0.4-noexecstack.patch

Requires: libqt4-core >= %{get_version libqt4-core}

BuildRequires(pre): libqt4-devel
BuildRequires: cmake gcc-c++ libqt4-devel
BuildRequires: kde-common-devel

%description 
Blitz is a graphical effect and filter library for KDE4.0 that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.


%package -n lib%name
Summary: Graphical effect and filter library for KDE4.0
Group: System/Libraries

%description -n lib%name
Blitz is a graphical effect and filter library for KDE4.0 that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

%package -n lib%name-devel
Summary: %name development library and headers
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Blitz is a graphical effect and filter library for KDE4.0 that contains
many improvements over KDE 3.x's kdefx library including bugfixes,
memory and speed improvements, and MMX/SSE support.

This package contains %name development library and headers.


%prep
%setup
%patch1 -p1

%build
%Kbuild

%install
%Kinstall


%files -n lib%name
%_bindir/*
%_libdir/*.so.*

%files -n lib%name-devel
%doc README.BLITZ README.PORTING
%_libdir/*.so
%_includedir/%name/
%_pkgconfigdir/*.pc

%changelog
* Thu Sep 11 2014 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt4
- Added a patch from FC to fix "executable-stack" rpmlint warning

* Wed Sep 28 2011 Dmitry V. Levin <ldv@altlinux.org> 0.0.6-alt3
- Fixed interpackage dependencies.
- Rebuilt for debuginfo.

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt2
- rebuilt

* Tue Apr 20 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt0.M51.1
- build for M51

* Wed Apr 07 2010 Sergey V Turchin <zerg@altlinux.org> 0.0.6-alt1
- buildsystem updated

* Wed Jul 22 2009 Sergey V Turchin <zerg@altlinux.org> 0.0.4-alt3
- update from svn r1000977

* Sun Jan 13 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.4-alt2
- use optflags
- add watch file

* Sat Jan 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.0.4-alt1
- initial build
