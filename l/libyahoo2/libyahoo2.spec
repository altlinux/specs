# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ glib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary:       Library for the Yahoo! Messenger Protocol
Name:          libyahoo2  
Version:       1.0.1
Release:       alt3_3
Group:         System/Libraries
License:       GPLv2
Url:           http://libyahoo2.sourceforge.net/
Source:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Requires:      openssl
BuildRequires: glib2-devel
BuildRequires: libssl-devel
Source44: import.info

%description
libyahoo2 is a C library interface to the new Yahoo! Messenger protocol. It
supports almost all current features of the protocol.

%package devel
Summary:    Headers and development files for libyahoo2
Group:      Development/C
Requires:   libyahoo2 = %{version}-%{release}

%description devel
The header files and some documentation that you'll need to develop with
libyahoo2

%prep
%setup -q
iconv -f iso8859-1 -t UTF8 AUTHORS > AUTHORS.utf8 && %{__mv} AUTHORS.utf8 AUTHORS
iconv -f iso8859-1 -t UTF8 NEWS > NEWS.utf8 && %{__mv} NEWS.utf8 NEWS

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} DESTDIR=%{buildroot} install
%{__rm} -f %{buildroot}/%{_libdir}/*.a
%{__rm} -f %{buildroot}/%{_libdir}/*.la

sed -i -e 's,-@RELEASE@,,' %buildroot%_pkgconfigdir/%name.pc

%files
%doc COPYING AUTHORS ChangeLog
%{_libdir}/*.so.*

%files devel
%doc doc/ymsg-9.txt doc/yab.txt doc/chatcat NEWS COPYING AUTHORS README ChangeLog
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2_2
- spec cleanup thanks to ldv@

* Fri Jul 15 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- initial release by fcimport

