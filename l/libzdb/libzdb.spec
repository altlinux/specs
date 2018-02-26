# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pg_config /usr/bin/re2c libssl-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define fedora 16
Name:           libzdb
Version:        2.8.1
Release:        alt3_2
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
%doc doc/api-docs



%changelog
* Sat Jun 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt2_1
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.8.1-alt1_1
- initial import by fcimport

