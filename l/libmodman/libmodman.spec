# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libmodman
Version:        2.0.1
Release:        alt2_4
Summary:        A simple library for managing C++ modules (plug-ins)

Group:          System/Libraries
License:        LGPLv2+
URL:            http://code.google.com/p/libmodman/
Source0:        http://libmodman.googlecode.com/files/%{name}-%{version}.tar.gz

BuildRequires:  ctest cmake >= 2.8.0
BuildRequires:  zlib-devel
Source44: import.info

%description
libmodman is a simple library for managing C++ modules (plug-ins).

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       libmodman = %{version}-%{release}
Requires:       ctest cmake >= 2.8.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
#sed -i 's|-Werror||' libmodman/CMakeLists.txt

%build
%{fedora_cmake}
make VERBOSE=1 %{?_smp_mflags}

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libmodman-2.0.pc
%{_datadir}/cmake/Modules/Findlibmodman.cmake

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_2
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_2
- initial import by fcimport

