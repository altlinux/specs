# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
Group: Development/Other
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       libfli
Version:    1.9.0
Release:    alt1_2
Summary:    Library for FLI CCD Camera & Filter Wheels

License:    BSD
URL:        http://indilib.org/

# Tar is generated from the huge all-in-one tar from INDI
# by using ./libfli-generate-tarball.sh %%{version}
# The main source from upstream is at
# https://github.com/indilib/indi-3rdparty/archive/refs/tags/v%%{version}.tar.gz
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-generate-tarball.sh

BuildRequires:  ctest cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  rpm-macros-systemd
BuildRequires:  pkgconfig(libindi) = %{version}
BuildRequires:  pkgconfig(libusb-1.0)
Source44: import.info

%description
Finger Lakes Instrument library is used by applications to control FLI 
line of CCDs and Filter wheels

%package devel
Group: Development/Other
Summary: Libraries, includes, etc. used to develop an application with %{name}
Requires: %{name} = %{version}-%{release}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}-%{version}
sed -i 's|/lib/udev/rules.d|%{_udevrulesdir}|g' CMakeLists.txt

%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build 

%install
%fedora_v2_cmake_install


%files
%doc --no-dereference LICENSE.BSD
%{_libdir}/*.so.2*
%{_udevrulesdir}/99-fli.rules

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Sat Nov 13 2021 Igor Vlasenko <viy@altlinux.org> 1.9.0-alt1_2
- update to new release by fcimport

* Sat Sep 19 2020 Igor Vlasenko <viy@altlinux.ru> 1.7-alt3_29
- migrated to new fc cmake macros

* Fri Sep 18 2020 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_29
- update

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_21
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_19
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_12
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_10
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_9
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_8
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt2_7
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1_7
- initial import by fcimport

