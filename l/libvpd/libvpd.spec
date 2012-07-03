# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define name libvpd
%define version 2.1.1

Name:		%{name}
Version:	%{version}
Release:	alt2_2
Summary:	VPD Database access library for lsvpd

Group:		System/Libraries
License:	LGPLv2+
URL:		http://linux-diag.sf.net/Lsvpd.html
Source:		http://downloads.sourceforge.net/linux-diag/%{name}-%{version}.tar.gz

BuildRequires:	libsqlite3-devel zlib-devel libstdc++-devel
Source44: import.info

%description
The libvpd package contains the classes that are used to access a vpd database
created by vpdupdate in the lsvpd package.

%package devel
Summary:	Header files for libvpd
Group:		Development/C
Requires:	%{name} = %{version}-%{release}
%description devel
Contains header files for building with libvpd.

%prep
%setup -q

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files 
%doc COPYING NEWS README TODO AUTHORS
%{_libdir}/libvpd_cxx-2.1.so.*
%{_libdir}/libvpd-2.1.so.*

%files devel
%{_includedir}/libvpd-2
%{_libdir}/libvpd_cxx.so
%{_libdir}/libvpd.so
%{_libdir}/pkgconfig/libvpd-2.pc
%{_libdir}/pkgconfig/libvpd_cxx-2.pc

%changelog
* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_2
- initial import by fcimport

