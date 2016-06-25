# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm)
# END SourceDeps(oneline)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name tap
%define version 1.03
%define	major	0
%define	libname	    lib%{name}%{major}
%define develname   lib%{name}-devel

Name:		tap
Version:	1.03
Release:	alt1_7
Summary:	Write tests that implement the Test Anything Protocol
License:	GPL
Group:		System/Libraries
URL:		http://jc.ngo.org.uk/trac-bin/trac.cgi/wiki/LibTap
Source:		http://download.berlios.de/web-cpan/tap-1.03.tar.gz
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
%setup -q

%build
%configure \
	--disable-static
%make CFLAGS+=-UHAVE_LIBPTHREAD

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc COPYING NEWS README
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{develname}
%{_libdir}/lib%{name}.so
%{_includedir}/*
%{_mandir}/man3/*


%changelog
* Sat Jun 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_7
- converted for ALT Linux by srpmconvert tools

