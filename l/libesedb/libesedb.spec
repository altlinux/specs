Group: Other
%add_optflags %optflags_shared
Name:           libesedb
Version:        20120102
Release:        alt2_10
Summary:        Library to access the Extensible Storage Engine (ESE) Database File (EDB) format

License:        GPLv3+
#URL:           http://code.google.com/p/libesedb/
URL:            https://github.com/libyal/libesedb
#Tarball for version 20120102 no longer available from googlecode.com and the
#new site on github doesn't have this ersion tagged as release
#https://github.com/libyal/libesedb/commit/49017c644da85bd7c6df50a3da94b500cf14dbc9
Source0:        http://libesedb.googlecode.com/files/%{name}-alpha-%{version}.tar.gz

#Patch backpoerted from newer experimental versions on
Patch0:         %{name}-inline.patch
Source44: import.info


%description
Library and tools to access the Extensible Storage Engine (ESE) Database File
(EDB) format. ESEDB is used in may different applications like Windows Search,
Windows Mail, Exchange, Active Directory, etc.


%package        devel
Group: Other
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q
%patch0 -b .inline -p 1

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
* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_10
- update to new release by fcimport

* Mon Nov 23 2015 Igor Vlasenko <viy@altlinux.ru> 20120102-alt2_7
- fixed build

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_5
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 20120102-alt1_4
- initial fc import

