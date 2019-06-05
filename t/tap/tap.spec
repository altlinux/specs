# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++ perl(Test/More.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name tap
%define	major	0
%define	libname	    lib%{name}%{major}
%define develname   lib%{name}-devel

Name:		tap
Version:	1.14.0
Release:	alt1_1
Summary:	Write tests that implement the Test Anything Protocol
License:	GPL
Group:		System/Libraries
URL:		https://www.shlomifish.org/open-source/projects/libtap/
Source:		https://web-cpan.shlomifish.org/downloads/libtap-%{version}.tar.xz
BuildRequires: ccmake cmake ctest
Source44: import.info

%description
The tap library provides functions for writing test scripts that produce output
consistent with the Test Anything Protocol.  A test harness that parses this
protocol can run these tests and produce useful reports indicating their
success or failure.

%package -n	%{libname}
Summary:	Write tests that implement the Test Anything Protocol
Group:		System/Libraries

%description -n	%{libname}
The tap library provides functions for writing test scripts that produce output
consistent with the Test Anything Protocol.  A test harness that parses this
protocol can run these tests and produce useful reports indicating their
success or failure.

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	lib%{name}0-devel

%description -n	%{develname}
This package contains development files for %{name}.

%prep
%setup -q -n libtap-%{version}
# hack
sed -i 's,@VERSION@,%version,' libtap.pc.in

%build
%{mageia_cmake}
%make_build CFLAGS+=-UHAVE_LIBPTHREAD

%install
%makeinstall_std -C build

%files -n %{libname}
%doc COPYING NEWS README
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc
%{_includedir}/*
%{_mandir}/man3/*


%changelog
* Wed Jun 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.14.0-alt1_1
- update by mgaimport

* Sun Jan 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_9
- new version

* Sat Jun 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_7
- converted for ALT Linux by srpmconvert tools

