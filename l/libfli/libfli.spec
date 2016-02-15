# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name: libfli
Version: 1.7
Release: alt2_18
Summary: Library for FLI CCD Camera & Filter Wheels

%define majorver 1

Group: Development/C
# Code and LICENSE.LIB have different versions of the BSD license
# https://sourceforge.net/tracker2/?func=detail&aid=2568511&group_id=90275&atid=593019
License: BSD
URL: http://indi.sourceforge.net/index.php

Source0: http://downloads.sourceforge.net/indi/%{name}%{majorver}_%{version}.tar.gz
Patch0: libfli-suffix.patch

BuildRequires: ctest cmake 
Source44: import.info
Patch33: libfli1_1.7-alt-link-libm.patch

%description
Finger Lakes Instrument library is used by applications to control FLI 
line of CCDs and Filter wheels

%package devel
Summary: Libraries, includes, etc. used to develop an application with %{name}
Group: Development/C
Requires: %{name}%{?_isa} = %{version}
%description devel
These are the header files needed to develop a %{name} application

%prep
%setup -q -n %{name}%{majorver}-%{version}
%patch0 -p1
%patch33 -p1

%build
%{fedora_cmake}
make VERBOSE=1 %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE.BSD
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
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

