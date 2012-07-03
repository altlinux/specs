%define sover 0.1
%define rname libQtGTL
%define libname libqtgtl%sover
%define develname libqtgtl-devel

Name: libqtgtl
Version: 0.9.1
Release: alt3

Group: System/Libraries
Summary: Open Graphics Transformation Languages
Url: http://www.opengtl.org/
License: LGPLv2+

Provides: libQtGTL = %version-%release

Source: http://www.opengtl.org/download/%rname-%version.tar.bz2
Patch1: libQtGTL-0.9.1-alt-fix-linking.patch

# Automatically added by buildreq on Thu Jan 20 2011 (-bb)
#BuildRequires: cmake gcc-c++ libopengtl-devel libqt3-devel qt4-designer
BuildRequires: cmake gcc-c++ libopengtl-devel libqt4-devel

%description
Qt bindings for Graphics Transformation Languages (GTL)

%package -n %libname
Summary: Qt bindings for OpenGTL
Group: System/Libraries
%description -n %libname
Qt bindings for OpenGTL

%package -n %{develname}
Summary: libQtGTL development files
Group: Development/C++
Provides: libQtGTL-devel = %version-%release
Requires: %libname = %version-%release
Requires: libopengtl-devel
%description -n %{develname}
This package contains header files needed if you wish to build applications
based on libQtGTL.


%prep
%setup -q -n %rname-%version
%patch1 -p1

%build
%cmake
pushd BUILD
%make VERBOSE=1
popd


%install
pushd BUILD
%make install DESTDIR=%buildroot
popd


%files -n %libname
%_libdir/*.so.%sover
%_libdir/*.so.%version

%files -n %develname
%_libdir/*.so
%_includedir/*
%_libdir/pkgconfig/*.pc

%changelog
* Thu Jun 14 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt3
- fix to build with gcc-4.6

* Mon Apr 23 2012 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt2
- rebuilt

* Thu Jan 20 2011 Sergey V Turchin <zerg@altlinux.org> 0.9.1-alt1
- built for ALT

