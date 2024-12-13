%define repo qt6mpris
%define lname libmpris-qt6
%define soname 1

Name: libmpris-dqt6
Version: 1.0.0.1
Release: alt1

Summary: Qt6 and QML6 MPRIS interface and adaptor

License: LGPL-2.1+
Group: System/Libraries
Url: https://github.com/deepin-community/qt6mpris
Vcs: git://github.com/deepin-community/qt6mpris.git

Source: %url/archive/%version/qt6mpris-%version-1deepin1.tar.gz

BuildRequires: gcc-c++ dqt6-base-devel dqt6-declarative-devel

# find libraries
%add_findprov_lib_path %_dqt6_libdir

%description
%summary.

%package %soname
Summary: %summary
Group: System/Libraries

%description %soname
Header files and libraries for %name.

%package devel
Summary: Development package for %name
Group: Development/Other

%description devel
Header files and libraries for %name.

%prep
%setup -n qt6mpris-%version-1deepin1

%build
%qmake_dqt6 \
  CONFIG+=nostrip \
  QMAKE_RPATHDIR=%_dqt6_libdir \
#
%make_build

%install
%install_dqt6

%files %soname
%_dqt6_libdir/%lname.so.%{soname}*
%dir %_dqt6_qmldir/org/nemomobile/
%_dqt6_qmldir/org/nemomobile/mpris/

%files devel
%_dqt6_libdir/%lname.so
%_dqt6_headerdir/MprisQt/
%_dqt6_libdir/pkgconfig/mpris-qt6.pc
%_dqt6_mkspecsdir/features/mpris-qt6.prf

%changelog
* Fri Dec 13 2024 Leontiy Volodin <lvol@altlinux.org> 1.0.0.1-alt1
- Initial build for ALT Sisyphus (for deepin-music).
