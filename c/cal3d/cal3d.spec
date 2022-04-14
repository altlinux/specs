# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-generic-compat
BuildRequires: /usr/bin/blender gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cal3d
%define major 12
%define libname lib%{name}%{major}
%define develname lib%{name}-devel

Summary:	A skeletal based character animation library
Name:		cal3d
Version:	0.11.0
Release:	alt5_22
Group:		System/Libraries
License:	LGPLv2+
URL:		http://gna.org/projects/cal3d/
Source0:	http://download.gna.org/cal3d/sources/%{name}-%{version}.tar.bz2
Patch0:		cal3d-0.11.0-gcc43.patch
Patch1:		cal3d-0.11.0-gcc7.patch
ExclusiveArch:	x86_64 aarch64 ppc64le %e2k
%ifarch x86_64 aarch64 ppc64le
BuildRequires:  valgrind
%endif
BuildRequires:	doxygen
BuildRequires:	docbook-utils
Source44: import.info

%description
Cal3D is a skeletal based character animation library. It is platform-
independent and not bound to a specific graphic API. Originally designed to
be used in a 3d client for the Worldforge project (www.worldforge.org)
it evolved into a stand-alone product that can be used in many different
projects.

%package -n %{libname}
Summary:	A skeletal based character animation library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
Cal3D is a skeletal based character animation library. It is platform-
independent and not bound to a specific graphic API. Originally designed to
be used in a 3d client for the Worldforge project (www.worldforge.org)
it evolved into a stand-alone product that can be used in many different
projects.

%package -n %{develname}
Summary:	Headers for developing programs that will use Cal3D
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	lib%{name}12-devel

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use Cal3D.

%prep
%setup -q
%patch0 -p1
%patch1 -p1


%build
autoreconf -fi
%configure
%make_build

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_bindir}/%{name}_converter
%{_mandir}/man1/%{name}_converter.1*




%changelog
* Thu Apr 14 2022 Igor Vlasenko <viy@altlinux.org> 0.11.0-alt5_22
- update by mgaimport

* Fri Sep 11 2020 Michael Shigorin <mike@altlinux.org> 0.11.0-alt5_18
- ExclusiveArch: 64-bit ones (following blender)

* Sat Oct 05 2019 Michael Shigorin <mike@altlinux.org> 0.11.0-alt4_18
- avoid valgrind on more arches
  + proper ALT way is through rpm-macros-valgrind though

* Fri Nov 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt3_18
- fixed build

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_19
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_16
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_15
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_14
- update to new release by fcimport

* Mon Jan 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt2_13
- rebuild to fix requires

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_13
- update to new release by fcimport

* Thu Mar 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_12
- rebuild to get rid of #27020

* Fri Feb 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_11
- new fc release

* Sat Jul 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.11.0-alt1_10
- initial release by fcimport

