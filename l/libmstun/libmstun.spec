# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		A C++ library providing STUN client utilities
Name:			libmstun
Version:		0.8.0
Release:		alt2_0.4.20091007svn3734
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3734  svn://svn.minisip.org/minisip/trunk/libmstun libmstun-0.8.0
# tar cjf libmstun-0.8.0.tar.bz2 libmstun-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libmutil-devel >= 0.8.0
BuildRequires:		libmnetutil-devel >= 0.8.0
Source44: import.info

%description
libmstun provides support for implementing STUN in client applications.
It is used by the minisip project.

%package devel
Summary:		Development files for the libmnstun library
Group:			Development/C
Requires:		libmstun = %{version}-%{release}
Requires:		automake


%description devel
Development files for the libmstun library

%prep
%setup -q

%build
sh ./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc AUTHORS README COPYING.LIB
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%{_datadir}/aclocal/*.m4


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.4.20091007svn3734
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.3.20091007svn3734
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.2.20091007svn3734
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.2.20091007svn3734
- initial import by fcimport

