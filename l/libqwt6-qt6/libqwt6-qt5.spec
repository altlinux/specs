%define oname libqwt
%define ver_major 6.2
Name: %{oname}6-qt6
Version: %ver_major.0
Release: alt1

Summary: 2D plotting widget extension to the Qt GUI

License: LGPL-2.1 with exceptions
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt

# https://qwt.svn.sourceforge.net/svnroot/qwt/trunk/qwt
Source: http://sourceforge.net/projects/qwt/files/qwt/%version/qwt-%version.tar.bz2
#Source: qwt-%version.tar
Patch1: qwt-6.2.0-qt_install_paths.patch
Patch2: qwt-6.1.3-no_rpath.patch
Patch3: qwt-qt-with-major-version.patch

#Provides: %oname = %version-%release
BuildRequires(pre): rpm-macros-qt6
BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel
BuildRequires: libXext-devel doxygen graphviz
BuildRequires: chrpath

Conflicts: libqwt6-qt5

%description
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

Package build with Qt6.

%package devel
Summary: Development tools for programs which uses Qwt Widget set
Group: Development/C
#Provides: %oname-devel = %version-%release
Requires: %name = %EVR
Conflicts: libqwt6-qt5-devel

%description devel
The libqwt-devel package contains the header files and libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

Package build with Qt6.

%prep
%setup -n qwt-%version
%patch1 -p2
%patch2 -p1
%patch3 -p1
# Build with Qt6
subst 's/Qt5/Qt6/g' src/src.pro

find . -type f -name '*.pro' |while read f; do
echo 'QMAKE_CXXFLAGS += %optflags' >> $f
done

%build
%qmake_qt6 QWT_CONFIG+=QwtMathML QWT_CONFIG+=QwtPkgConfig CONFIG+=nostrip
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot
rm -fr %buildroot%_datadir/qt6/doc
rm -fr %buildroot%_datadir/qt6/features

%files
%doc README COPYING
%_libdir/libqwt-qt6.so.*
%_libdir/libqwt.so.%ver_major

%files devel
%_includedir/qt6/qwt
%_libdir/libqwt-qt6.so
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jan 27 2022 Andrey Cherepanov <cas@altlinux.org> 6.2.0-alt1
- Initial build for Sisyphus.
