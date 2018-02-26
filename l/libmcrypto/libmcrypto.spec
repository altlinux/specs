# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(gnutls-extra)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		A C++ library providing various cryptography related utilities
Name:			libmcrypto
Version:		0.8.0
Release:		alt2_0.4.20100629svn3775
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3775  svn://svn.minisip.org/minisip/trunk/libmcrypto libmcrypto-0.8.0
# tar cjf libmcrypto-0.8.0.tar.bz2 libmcrypto-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
Patch1:			libmcrypto-0001-Fix-building-with-gnutls-and-new-GCC.patch
Patch2:			libmcrypto-0002-Compile-OpenSSL-module-with-newest-GCC.patch
Patch3:			libmcrypto-0003-Compile-with-OpenSSL-1.0.patch
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libmutil-devel >= 0.8.0
BuildRequires:		libmnetutil-devel >= 0.8.0
BuildRequires:		libssl-devel >= 0.9.6
BuildRequires:		libgnutls-devel
Source44: import.info

%description
Libmcrypto is a library providing C++ cryptography related utilities.
It is used by the Minisip project.

%package devel
Summary:		Development files for the libmcrypto library
Group:			Development/C
Requires:		libmcrypto = %{version}-%{release}
Requires:		automake


%description devel
Development files for the libmcrypto library

%prep
%setup -q
%patch1 -p1 -b .gnutls
%patch2 -p1 -b .gcc4
%patch3 -p1 -b .openssl10

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
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.4.20100629svn3775
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.3.20100629svn3775
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt2_0.2.20100629svn3775
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1_0.2.20100629svn3775
- initial import by fcimport

