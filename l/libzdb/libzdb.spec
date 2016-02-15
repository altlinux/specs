# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/mysql_config /usr/bin/pg_config /usr/bin/re2c gcc-c++ libssl-devel
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
Name:           libzdb
Version:        3.0
Release:        alt1_5
Summary:        Small, easy to use Database Connection Pool Library
License:        GPLv3+ and MIT
URL:            http://www.tildeslash.com/libzdb/
Source0:        http://www.tildeslash.com/%{name}/dist/%{name}-%{version}.tar.gz
BuildRequires:  flex
BuildRequires:  libmysqlclient-devel
BuildRequires:  postgresql-devel >= 8
BuildRequires:  libsqlite3-devel >= 3.6.12
Source44: import.info

%description
The Zild C Database Library implements a small, fast, and easy to use database
API with thread-safe connection pooling. The library can connect transparently
to multiple database systems, has zero configuration and connections are
specified via a standard URL scheme.

%package        devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

# Errant file
rm -f doc/api-docs/._*

%build
%configure --disable-static --enable-protected --enable-sqliteunlock
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS CHANGES COPYING README
%{_libdir}/%{name}.so.*

%files devel
%{_includedir}/zdb/
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/zdb.pc
%doc doc/api-docs

%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_4
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_2
- update to new release by fcimport

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

