%define maj_ver 3.0
Name: GLC_lib
Version: %maj_ver.1
Release: alt1.20211001
Summary: C++ class library for OpenGL application based on Qt 5

Group: System/Libraries
License: LGPL-2.1
Url: https://github.com/laumaya/GLC_lib

Source: %name-%version.tar
Patch: unbundled_library.patch

BuildRequires: qt5-base-devel
BuildRequires: qt5-designer
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: lib3ds-devel
BuildRequires: libquazip-qt5-devel
BuildRequires: zlib-devel

# Project ERROR: GLC_lib does not support OpenGL ES 2!
ExcludeArch: %arm

%description
GLC_lib is a C++ class library that enables the quick creation of OpenGL
application based on Qt 5. Some GLC_lib features : Camera orbiting, Obj
textured file support, 3D Primitive... And more.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release
Requires: libqt5-declarative
Requires: qt5-designer
Requires: qt5-base-devel
Requires: qt5-quickcontrols2-devel

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p2

#Fix library Path on lib64
%__subst 's|LIB_DIR = /usr/lib|LIB_DIR = %_libdir|' glc_lib.pro install.pri

%build
%qmake_qt5 CONFIG+="force_debug_info qml_debug" LIBS+="-l3ds -lquazip5 -lz" glc_lib.pro
%make_build

%install
%make_install install INSTALL_ROOT=%buildroot

# remove built examples
rm -r %buildroot%prefix/src/GLC_lib-%maj_ver/examples

%files
%doc README
%_libdir/*.so.*
%_libdir/qt5/qml/glclib

%files devel
%_includedir/GLC_lib-%maj_ver/
%_libdir/*.so

%changelog
* Sun Nov 07 2021 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1.20211001
- new version from commit 5e86cbb1049ea7b32f7329dd391bc2df88882d71
  with https://github.com/laumaya/GLC_lib
- update URL tag
- update License tag
- build with qt5
- drop import.info
- ExcludeArch: %arm

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_15
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_9
- update to new release by fcimport

* Thu May 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt2_8
- moved to Sisyphus by request of dd@

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_8
- update to new release by fcimport

* Mon Mar 11 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_7
- update to new release by fcimport

* Fri Dec 28 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.0-alt1_6
- initial fc import

