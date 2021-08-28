%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Group: Development/Other
%add_optflags %optflags_shared
%define oldname vsqlite++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:        libvsqlite++
Version:    0.3.13
Release:    alt2_28
Summary:    Well designed C++ sqlite 3.x wrapper library

License:    BSD
URL:        http://vsqlite.virtuosic-bytes.com
Source0:    http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/%{oldname}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  boost-complete
BuildRequires:  libsqlite3-devel
BuildRequires:  libtool
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
Source44: import.info
Provides: vsqlite++ = %{version}-%{release}

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Group: Development/Other
Summary:        Development files for %{oldname}
Requires:       %{name} = %{version}-%{release}
Provides: vsqlite++-devel = %{version}-%{release}

%description devel
This package contains development files for %{oldname}.

%package doc
Group: Development/Other
BuildArch:      noarch
Summary:        Development documentation for %{oldname}
Provides: vsqlite++-doc = %{version}-%{release}

%description doc
This package contains development documentation files for %{oldname}.

%prep
%setup -n %{oldname}-%{version} -q

%build
%configure
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
%make_build
doxygen Doxyfile

%install
# devel & base
install -p -m 755 -d %{buildroot}%{_libdir}
# devel only
install -p -m 755 -d %{buildroot}%{_includedir}/sqlite/ext
install -m 644 include/sqlite/*.hpp %{buildroot}%{_includedir}/sqlite
install -m 644 include/sqlite/ext/*.hpp %{buildroot}%{_includedir}/sqlite/ext
# docs
install -p -m 755 -d %{buildroot}%{_docdir}

# build for all
make DESTDIR=%{buildroot} install



%files doc
%doc ChangeLog README COPYING examples/sqlite_wrapper.cpp html/*

%files devel
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so
%{_includedir}/sqlite
# Don't add .la/.a to the package
%exclude %{_libdir}/libvsqlitepp.a

%files
%doc ChangeLog README COPYING
%{_libdir}/libvsqlitepp.so.*

%changelog
* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 0.3.13-alt2_28
- fixed build with LTO

* Thu Jul 05 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt2_21
- use boost-complete

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_21
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_19
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_17
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_14
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_12
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_7
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_6
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_5
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.13-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_3
- update to new release by fcimport

* Sat Jun 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.11-alt1_2
- new version

