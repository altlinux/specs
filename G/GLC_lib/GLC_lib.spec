# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libqt4-devel unzip
# END SourceDeps(oneline)
Name:           GLC_lib
Version:        2.2.0
Release:        alt2_9
Summary:        C++ class library for OpenGL application based on Qt 4

Group:          System/Libraries
License:        LGPLv3+
URL:            http://www.glc-lib.net/
Source0:        http://downloads.sourceforge.net/glc-lib/GLC_lib_src_%{version}.zip
Patch0:         GLC_lib_src_2.2.0-nointernal.patch
Patch1:         GLC_lib_src_2.2.0-gcc46.patch

BuildRequires:  qt4-devel
BuildRequires:  lib3ds-devel
BuildRequires:  libquazip-devel
Source44: import.info


%description
GLC_lib is a C++ class library that enables the quick creation of OpenGL
application based on Qt 4. Some GLC_lib features : Camera orbiting, Obj
textured file support, 3D Primitive... And more.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.



%prep
%setup -q -c
cd glc_lib
%patch0 -p2 -b .nointernal
%patch1 -p2 -b .gcc46

#Fix library Path on lib64
sed -i -e 's|LIB_DIR = /usr/local/lib|LIB_DIR = %{_libdir}|' GLC_lib.pro
sed -i -e 's|/usr/local/include|%{_includedir}|' GLC_lib.pro

# Fix internal use of several libraries
sed -i -e 's|lib3ds minizip|lib3ds|' GLC_lib.pro
rm -rf 3rdparty



%build
cd glc_lib
qmake-qt4 GLC_lib.pro
make %{?_smp_mflags}


%install
cd glc_lib
make install INSTALL_ROOT=$RPM_BUILD_ROOT


%files
%doc glc_lib/COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/GLC_lib/
%{_libdir}/*.so


%changelog
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

