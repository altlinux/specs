Serial: 51104
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		A C++ library implementing the SIP protocol
Name:			libmsip
Version:		0.8.0
Release:		alt2_0.4.20100629svn3775
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3775 svn://svn.minisip.org/minisip/trunk/libmsip libmsip-0.8.0
# tar cjf libmsip-0.8.0.tar.bz2 libmsip-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libmcrypto-devel >= 0.8.0
BuildRequires:		libmutil-devel >= 0.8.0
BuildRequires:		libmnetutil-devel >= 0.8.0
Source44: import.info

%description
libmsip is a C++ library that implements the SIP protocol, as defined in
RFC3261.

%package devel
Summary:		Development files for the libmsip library
Group:			Development/C
Requires:		libmsip = %{version}-%{release}
Requires:		automake


%description devel
Development files for the libmsip library

%prep
%setup -q
chmod 644 include/libmsip/SipDialogManagement.h
chmod 644 source/dialogs/SipDialogManagement.cxx

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
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.4.20100629svn3775
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.3.20100629svn3775
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.2.20100629svn3775
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt1_0.2.20100629svn3775
- initial import by fcimport

