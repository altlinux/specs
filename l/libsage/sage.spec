# BEGIN SourceDeps(oneline):
BuildRequires: libGL-devel libICE-devel libSM-devel libX11-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname sage
Name:           libsage
Version:        0.2.0
Release:        alt2_7
Summary:        OpenGL extensions library using SDL

Group:          Development/C++
License:        LGPLv2+
URL:            http://worldforge.org/dev/eng/libraries/sage
Source0:        http://downloads.sourceforge.net/worldforge/%{oldname}-%{version}.tar.gz
Patch0:         sage-0.1.2-noopt.patch

BuildRequires:  libSDL-devel
Source44: import.info
Provides: sage = %{version}-%{release}

%description
Sage is an OpenGL extensions library using SDL. It aims to simplify the use of
checking for and loading OpenGL extensions in an application.


%package devel
Summary:        Development files for sage
Group:   Development/C++
Requires: libsage = %{version}-%{release}
Provides: sage-devel = %{version}-%{release}


%description devel
Libraries and header files for developing applications that use sage.



%prep
%setup -q -n %{oldname}-%{version}
touch -r configure.ac configure.ac.stamp
%patch0 -p0
touch -r configure.ac.stamp configure.ac
rm -f sage/glxext_sage.h
rm -f sage/wglext_sage.h


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/lib%{oldname}.la

%check
# There are no tests yet, but upstream tends to be good about adding 
# them.  This is a placeholder for when upstread finally adds the tests.
make %{?_smp_mflags} check



%files
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/lib%{oldname}.so.*


%files devel
%{_includedir}/%{oldname}
%{_libdir}/lib%{oldname}.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*.3.*


%changelog
* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2_7
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_7
- update to new release by fcimport

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt1_6
- initial release by fcimport

