Serial: 51104
# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:		A C++ library implementing the Multimedia Internet KEYing protocol
Name:			libmikey
Version:		0.8.0
Release:		alt2_0.5.20100127svn3750
License:		LGPLv2+
URL:			http://www.minisip.org/
Group:			System/Libraries
# svn export -r 3750  svn://svn.minisip.org/minisip/trunk/libmikey libmikey-0.8.0
# tar cjf libmikey-0.8.0.tar.bz2 libmikey-0.8.0/
Source0:		%{name}-%{version}.tar.bz2
Patch1:			libmikey-0001-Remove-the-redundant-specificators-required-by-GCC-4.patch
BuildRequires:		autoconf
BuildRequires:		automake
BuildRequires:		libtool
BuildRequires:		libmcrypto-devel >= 0.8.0
BuildRequires:		libmutil-devel >= 0.8.0
BuildRequires:		libmnetutil-devel >= 0.8.0
Source44: import.info

%description
libmikey is a C++ library that implements the Multimedia Internet KEYing.
This protocol aims to provide a key exchange for secure multimedia streaming.
It is usually embedded in SIP or RTSP session setup.

%package devel
Summary:		Development files for the libmikey library
Group:			Development/C
Requires:		libmikey = %{version}-%{release}
Requires:		automake


%description devel
Development files for the libmikey library

%prep
%setup -q
%patch1 -p1 -b .remove_specificator

%build
sh ./bootstrap
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc AUTHORS COPYING.LIB
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*
%{_datadir}/aclocal/*.m4


%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.5.20100127svn3750
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.4.20100127svn3750
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt2_0.3.20100127svn3750
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 51104:0.8.0-alt1_0.3.20100127svn3750
- initial import by fcimport

