%define rname taglib-extras

Name: libtag-extras
Version: 1.0.1
Release: alt3

Group: System/Libraries
Summary: Unofficial TagLib file type plugins maintained by the Amarok project
Url: http://websvn.kde.org/trunk/kdesupport/taglib-extras/
License: LGPL

Provides: %rname = %version-%release
Obsoletes: %rname < %version-%release

Source: %rname-%version.tar.bz2

#Patch0: taglib-extras-0.1-multilib-1.patch

Requires: libtag >= %{get_version libtag}

BuildRequires(pre): libtag-devel
BuildRequires: cmake gcc-c++ libtag-devel >= 1.6 kde-common-devel

%description
Unofficial TagLib file type plugins maintained by the Amarok project

%package devel
Group: Development/C
Summary: Headers and static lib for taglib development
Requires: %name = %version-%release
Provides: %rname-devel = %version-%release
Obsoletes: %rname-devel < %version-%release

%description devel
Install this package if you want do compile applications using the libtag-extras
library.

%prep
%setup -q -n %rname-%version

%build
%Kcmake \
    -DINCLUDE_INSTALL_DIR=%_includedir
# -DWITH_KDE=1
%Kmake

%install
%Kinstall

%files
%doc AUTHORS ChangeLog
%_libdir/libtag-extras.so.*
%_libdir/libtag-extras.so

%files devel
%_bindir/%rname-config
%_libdir/pkgconfig/%rname.pc
%_includedir/%rname

%changelog
* Wed Mar 02 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt3
- fix to build

* Tue Jan 25 2011 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt2
- rebuilt

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 1.0.1-alt1
- new version (ALT#21734)

* Mon Aug 03 2009 Mikhail Pluzhnikov <amike@altlinux.ru> 0.1.6-alt1
- New version: 0.1.6

* Tue Jul 14 2009 Mikhail Pluzhnikov <amike@altlinux.ru> 0.1.4-alt1
- New version: 0.1.4

* Fri Jul 03 2009 Mikhail Pluzhnikov <amike@altlinux.ru> 0.1.3-alt0.1
- New version 0.1.3

* Tue Apr 14 2009 Mihail A. Pluzhnikov <amike@altlinux.ru> 0.1.2-alt0.1
- First build for ALT Linux

