# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname vsqlite++
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:        libvsqlite++
Version:    0.3.13
Release:    alt1_17
Summary:    Well designed C++ sqlite 3.x wrapper library

Group:      Development/Other
License:    BSD
URL:        http://vsqlite.virtuosic-bytes.com
Source0:    http://evilissimo.fedorapeople.org/releases/vsqlite--/%{version}/%{oldname}-%{version}.tar.gz

BuildRequires:  boost-asio-devel boost-context-devel boost-coroutine-devel boost-devel boost-devel-headers boost-filesystem-devel boost-flyweight-devel boost-geometry-devel boost-graph-parallel-devel boost-interprocess-devel boost-locale-devel boost-lockfree-devel boost-log-devel boost-math-devel boost-mpi-devel boost-msm-devel boost-multiprecision-devel boost-polygon-devel boost-program_options-devel boost-python-devel boost-python-headers boost-signals-devel boost-wave-devel
BuildRequires:  libsqlite3-devel
BuildRequires:  libtool-common
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
Provides: vsqlite++ = %{version}-%{release}

%description
VSQLite++ is a C++ wrapper for sqlite3 using the C++ standard library and boost.
VSQLite++ is designed to be easy to use and focuses on simplicity.

%package devel
Summary:        Development files for %{oldname}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Provides: vsqlite++-devel = %{version}-%{release}

%description devel
This package contains development files for %{oldname}.

%package doc
BuildArch:      noarch
Summary:        Development documentation for %{oldname}
Group:          Development/Other
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

