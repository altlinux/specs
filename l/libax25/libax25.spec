# BEGIN SourceDeps(oneline):
BuildRequires: zlib-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libax25
Version:	0.0.12
Release:	alt2_0.7.rc2
Summary:	AX.25 library for hamradio applications

Group:		System/Libraries
License:	LGPLv2+
URL:		http://ax25.sourceforge.net/
Source0:	http://downloads.sourceforge.net/ax25/%{name}-%{version}-rc2.tar.gz
Source44: import.info

#BuildRequires:  
#Requires:       

%description
libax25 is a library for ham radio applications that use the ax25 protocol. 
Included are routines to do ax25 address parsing, common ax25 application
config file parsing, etc. 


%package	devel

Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qn %{name}-%{version}-rc2
# hack; added -lz; report upstream
sed -i -e "s,libax25_la_SOURCES,libax25_la_LIBADD = -lz\nlibax25_la_SOURCES," Makefile.am
sed -i -e "s,libax25io_la_SOURCES,libax25io_la_LIBADD = -lz\nlibax25io_la_SOURCES," Makefile.am



%build
autoreconf -fisv
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/*.so.*
%{_mandir}/man?/*

%files devel
%doc AUTHORS ChangeLog COPYING README
%{_includedir}/*
%{_libdir}/*.so


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.7.rc2
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.6.rc2
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.5.rc2
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.4.rc2
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.3.rc2
- update to new release by fcimport

* Sat Dec 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt2_0.2.rc2
- fixed build after mass spec cleanup

* Fri Jul 08 2011 Igor Vlasenko <viy@altlinux.ru> 0.0.12-alt1_0.2.rc2
- initial release by fcimport

