%define oname libqwt
%define ver_major 6.1

Name: %{oname}6-qt5
Version: %ver_major.3
Release: alt1

Summary: 2D plotting widget extension to the Qt5 GUI

License: LGPL
Group: System/Libraries
Url: http://sourceforge.net/projects/qwt

# https://qwt.svn.sourceforge.net/svnroot/qwt/trunk/qwt
Source: http://sourceforge.net/projects/qwt/files/qwt/%version/qwt-%version.tar.bz2
#Source: qwt-%version.tar
Patch: qwt-6.1.2-qt5-qwtconfig.pri.patch

#Provides: %oname = %version-%release
Conflicts: %{oname}6

BuildRequires: gcc-c++ libXext-devel doxygen graphviz
BuildRequires: qt5-base-devel qt5-svg-devel libqt5-designer qt5-tools-devel
BuildRequires: chrpath

%description
Qwt is an extension to the Qt5 GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

%package designer-plugin
Summary: Qwt plugin for qt5-designer
Group: Development/KDE and QT
Requires: %name = %version-%release
Conflicts: %name < %version-%release

%description designer-plugin
Qwt is an extension to the Qt GUI library from Troll Tech AS.
The Qwt library contains widgets and components which are
primarily useful for technical and scientifical purposes.
It includes a 2-D plotting widget, different kinds of sliders,
and much more.

This package contains Qwt plugin for qt5-designer

%package devel
Summary: Development tools for programs which uses Qwt Widget set
Group: Development/C
#Provides: %oname-devel = %version-%release
Requires: %name = %version-%release
Conflicts: %oname-devel %{oname}6-devel

%description devel
The libqwt-devel package contains the header files and libraries
necessary for developing programs using the Qwt Widget set

If you want to develop programs which will use this set of widgets,
you should install this package. You need also to install the libqwt package.

%package devel-doc
Summary: Documentation and examples for Qwt Widget set
Group: Development/Documentation
BuildArch: noarch
Conflicts: %oname-devel-doc %{oname}6-devel-doc

%description devel-doc
This package contains development documentation and examples for Qwt
Widget set.

%prep
%setup -n qwt-%version
%patch
	sed -i "s|/lib|/%_lib|g" qwtconfig.pri
	find . -type f -name '*.pro' |while read f; do
	echo 'QMAKE_CXXFLAGS += %optflags' >> $f
	done
%build
%qmake_qt5 QWT_CONFIG+=QwtMathML
%make_build

pushd doc
doxygen
popd

%install
%make_install install INSTALL_ROOT=%buildroot

mkdir -p %buildroot%_man3dir
mv %buildroot%prefix/doc/man/man3/* %buildroot%_man3dir/

chrpath -d %buildroot%_qt5_plugindir/designer/libqwt_designer_plugin.so

%files
%doc README COPYING
%_libdir/libqwt.so.*
%_libdir/libqwtmathml.so.*
%exclude %prefix/doc

%files designer-plugin
%_qt5_plugindir/designer/*.so

%files devel
%_includedir/qwt
%_libdir/libqwt.so
%_libdir/libqwtmathml.so

%files devel-doc
%doc doc/html
%doc examples
%_man3dir/*

%changelog
* Mon Jun 27 2016 Yuri N. Sedunov <aris@altlinux.org> 6.1.3-alt1
- first build for Sisyphus

