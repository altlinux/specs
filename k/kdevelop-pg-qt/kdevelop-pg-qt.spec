%define _unpackaged_files_terminate_build 1
%define unstable 0
%if %unstable
%define pkg_sfx -unstable
%else
%define pkg_sfx %nil
%endif
%define first_unstable_ver 0.9.80
%define obsoleted_unstable_version 1.0.0

Name: kdevelop%pkg_sfx-pg-qt
Version: 1.0.0
Release: alt2
%if %unstable
Conflicts: kdevelop-pg-qt <= %first_unstable_ver
Provides: kdevelop-pg-qt = %version-%release
%else
Obsoletes: kdevelop-unstable-pg-qt <= %obsoleted_unstable_version
%endif

Group: Development/Other
Summary: KDevelop parser generator
Url: http://techbase.kde.org/Development/KDevelop-PG-Qt_Introduction
License: GPLv2+

Source: kdevelop-pg-qt-%version.tar.gz
Patch0: %name-post-%version.patch

# Automatically added by buildreq on Tue Oct 26 2010 (-bi)
#BuildRequires: flex gcc-c++ glib2-devel glibc-devel-static kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel libXdmcp-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libXxf86vm-devel libqt3-devel libxkbfile-devel qt4-designer
BuildRequires: flex gcc-c++ glibc-devel kde4libs-devel kde-common-devel

%description
KDevelop-PG-Qt is a parser generator written in readable source-code and
generating readable source-code. Its syntax was inspirated by AntLR. It
implements the visitor-pattern and uses the Qt library. That is why it
is ideal to be used in Qt-/KDE-based applications like KDevelop.

%package devel
Summary: KDevelop-PG-Qt development files
Group: Development/Other
Requires: %name = %version
%if %unstable
Conflicts: kdevelop-pg-qt-devel <= %first_unstable_ver
Provides: kdevelop-pg-qt-devel = %version-%release
%else
Obsoletes: kdevelop-unstable-pg-qt-devel <= %obsoleted_unstable_version
%endif
%description devel
This package contains development files of KDevelop-PG-Qt.

%prep
%setup -q -n kdevelop-pg-qt-%version
%patch0 -p1

%build
%K4build

%install
%K4install

%files
%_K4bindir/kdev-pg-qt

%files devel
%_includedir/kdevelop-pg-qt
%_libdir/cmake/*

%changelog
* Thu Mar 21 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt2
- Dropped -unstable suffix because of the official release

* Sun Jan 29 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt1
- 1.0.0 release

* Fri Jan 27 2012 Alexey Morozov <morozov@altlinux.org> 1.0.0-alt0.1.git
- a new unstable git snapshot (f823d767a1799a14d32fe9152bba3bee35c15178,
  pre-1.0.0)

* Wed Dec 14 2011 Alexey Morozov <morozov@altlinux.org> 0.9.82-alt0.1.git
- a new unstable git snapshot (6570e01287e9eb45f7bdaab2b81b1d7082d2558a,
  0.9.82 aka 1.0 Beta)
- package gained -unstable suffix to peacefully co-exist with the
  version needed for "stable" versions of the KDevelop modules

* Thu Jun 16 2011 Alexey Morozov <morozov@altlinux.org> 0.9.5-alt2.git
- post 0.9.5 git snapshot (ba59270f286c50569de5bbe8eb0261d2280b6913)

* Wed Apr 27 2011 Alexey Morozov <morozov@altlinux.org> 0.9.5-alt1.git
- post 0.9.5 git snapshot (16d67d1082f1f2d69491c4e22131df89a39f32f9)
- buildreqs adjusted

* Wed Mar 16 2011 Alexey Morozov <morozov@altlinux.org> 0.9.0-alt2.git
- build git snapshot (7dff783443)

* Tue Oct 26 2010 Sergey V Turchin <zerg@altlinux.org> 0.9.0-alt1
- initial build

