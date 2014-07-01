Group: Other
%add_optflags %optflags_shared
Name:           libesedb
Version:        20120102
Release:        alt1_6
Summary:        Library to access the Extensible Storage Engine (ESE) Database File (EDB) format

License:        GPLv3+
URL:            http://code.google.com/p/libesedb/
Source0:        http://libesedb.googlecode.com/files/%{name}-alpha-%{version}.tar.gz
Source44: import.info


%description
Library and tools to access the Extensible Storage Engine (ESE) Database File
(EDB) format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%files
%doc COPYING AUTHORS
%{_libdir}/*.so.*
%{_bindir}/esedbexport
%{_bindir}/esedbinfo
%{_mandir}/man1/esedbinfo.1.*
%{_mandir}/man3/libesedb.3.*

%files devel
%doc
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libesedb.pc


%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_5
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_4
- initial fc import

