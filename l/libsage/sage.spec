# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ imake libX11-devel libXt-devel libglvnd-devel xorg-cf-files
# END SourceDeps(oneline)
Group: Development/Other
%add_optflags %optflags_shared
%define oldname sage
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libsage
Version:        0.2.0
Release:        alt2_29
Summary:        OpenGL extensions library using SDL

License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/sage
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.gz
Patch0:         sage-0.1.2-noopt.patch
Patch1: sage-configure-c99.patch

BuildRequires:  gcc
BuildRequires:  libSDL-devel
Source44: import.info
Provides: sage = %{version}-%{release}

%description
Sage is an OpenGL extensions library using SDL. It aims to simplify the use of
checking for and loading OpenGL extensions in an application.


%package devel
Group: Development/Other
Summary:        Development files for sage
Requires: pkgconfig %{oldname} = %{version}-%{release}
Provides: sage-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use sage.



%prep
%setup -n %{oldname}-%{version} -q
touch -r configure.ac configure.ac.stamp
%patch0 -p0
%patch1 -p1
touch -r configure.ac.stamp configure.ac
rm -f sage/glxext_sage.h
rm -f sage/wglext_sage.h


%build
%configure --disable-static
%make_build


%install
%makeinstall_std

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}.la

%check
# There are no tests yet, but upstream tends to be good about adding 
# them.  This is a placeholder for when upstread finally adds the tests.
%make_build check






%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib%{oldname}.so.*


%files devel
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3*


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 0.2.0-alt2_29
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_24
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_15
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_13
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_12
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_11
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_10
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_8
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_6
- initial release by fcimport

