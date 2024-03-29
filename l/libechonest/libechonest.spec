# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/doxygen gcc-c++
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}

%define qt4 0
%define qt5 1
#define tests 1

Name:		libechonest
Version: 	2.3.1
Release:	alt1
Summary:	C++ wrapper for the Echo Nest API

License:	GPLv2+
URL:		https://projects.kde.org/projects/playground/libs/libechonest
#	http://files.lfranchi.com/libechonest-%{version}.tar.bz2
Source0:	libechonest-%{version}.tar

BuildRequires:	ctest cmake
%if 0%{?qt4}
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(QtNetwork)
%endif
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Network)
%endif
Source44: import.info


%description
libechonest is a collection of Qt4 classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package	devel
Group: Development/C
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?qt5}
%package -n libechonest-qt5
Group: System/Libraries
Summary: libechonest Qt5 bindings
%description -n libechonest-qt5
libechonest is a collection of Qt5 classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package -n libechonest-qt5-devel
Group: System/Libraries
Summary: Development files for libechonest-qt5
Requires: libechonest-qt5 = %{version}-%{release}
%description -n libechonest-qt5-devel
%{summary}.
%endif


%prep
%setup -q


%build
export CXXFLAGS="-std=c++14 $RPM_OPT_FLAGS"

%if 0%{?qt4}
%global _vpath_builddir %{_target_platform}
%{fedora_v2_cmake} .. \
  -DBUILD_WITH_QT4:BOOL=ON \
  -DECHONEST_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF}
%fedora_v2_cmake_build
%endif

%if 0%{?qt5}
%global _vpath_builddir %{_target_platform}-qt5
%{fedora_v2_cmake} .. \
  -DBUILD_WITH_QT4:BOOL=OFF \
  -DECHONEST_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} 
%fedora_v2_cmake_build
%endif


%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
%if 0%{?qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
%endif


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
%if 0%{?qt4}
test "$(pkg-config --modversion libechonest)" = "%{version}" 
%endif
%if 0%{?qt5}
test "$(pkg-config --modversion libechonest5)" = "%{version}"
%endif
## The tests need active internet connection, which is not available in koji builds
%if 0%{?tests}
time make test -C %{_target_platform} ARGS="--timeout 300 --output-on-failure" ||:
%endif




%if 0%{?qt4}
%files
%doc AUTHORS COPYING README TODO
%{_libdir}/libechonest.so.2.3*
%files devel
%{_includedir}/echonest/
%{_libdir}/libechonest.so
%{_libdir}/pkgconfig/libechonest.pc
%endif

%if 0%{?qt5}
%files -n libechonest-qt5
%doc AUTHORS COPYING README TODO
%{_libdir}/libechonest5.so.2.3*
%files -n libechonest-qt5-devel
%{_includedir}/echonest5/
%{_libdir}/libechonest5.so
%{_libdir}/pkgconfig/libechonest5.pc
%endif


%changelog
* Tue Oct 18 2022 Sergey V Turchin <zerg@altlinux.org> 2.3.1-alt1
- new version
- drop Qt4 support (closes: 44037)

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 2.3.0-alt1_17
- update to new release by fcimport

* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_15
- regenerated to fix build

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_7
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_5
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_3
- update to new release by fcimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1_1
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_1
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_3
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_1
- initial import by fcimport

