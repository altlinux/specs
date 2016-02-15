%add_optflags %optflags_shared
Name:           libharu
Version:        2.2.1
Release:        alt1_7
Summary:        C library for generating PDF files
Group:          System/Libraries
License:        zlib with acknowledgement
URL:            http://libharu.org
Source0:        http://libharu.org/files/%{name}-%{version}.tar.gz
Patch0:		libharu-2.2.1-png15.patch
BuildRequires:	glibc-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
Source44: import.info

%description
libHaru is a library for generating PDF files. 
It is free, open source, written in ANSI C and cross platform.

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%patch0 -p1 -b .png15

%build
%configure --disable-static --enable-debug
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%doc README 
%{_libdir}/libhpdf-%{version}.so

%files devel
%{_includedir}/*
%{_libdir}/libhpdf.so

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_2
- update to new release by fcimport

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 2.2.1-alt1_1
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt2_3
- spec cleanup thanks to ldv@

* Fri Dec 16 2011 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1_3
- converted by srpmconvert script

