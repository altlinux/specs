# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mysql_config /usr/bin/pg_config /usr/bin/re2c gcc-c++ libssl-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 20
Name:           libzdb
Version:        3.0
Release:        alt1_1
Summary:        Small, fast, and easy to use database API

Group:          System/Libraries
License:        GPLv3+ and MIT
URL:            http://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz

%if 0%{?fedora} && 0%{?fedora} > 14
BuildRequires:  flex flex
%else
BuildRequires:  flex
%endif
BuildRequires:  libmysqlclient-devel >= 4.1 postgresql-devel >= 8 libsqlite3-devel
Source44: import.info

%description
The Zild C Database Library implements a small, fast, and easy to use database
API with thread-safe connection pooling. The library can connect transparently
to multiple database systems, has zero configuration and connections are
specified via a standard URL scheme.


%prep
%setup -q

# Errant file
rm -f doc/api-docs/._*

%build
%configure --disable-static --enable-protected
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_libdir}/%{name}\.so\.*

%doc AUTHORS CHANGES COPYING README


%package devel
Summary:        Developer header files & libraries for libzdb database API
Group:          Development/C
Requires:       libzdb = %{version}-%{release}

%description devel
Developer header files & libraries for libzdb database API.

%files devel
%{_includedir}/zdb
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%doc doc/api-docs



%changelog
* Wed Mar 19 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt3_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt3_4
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt3_3
- update to new release by fcimport

* Sat Jun 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1
- initial import by fcimport

