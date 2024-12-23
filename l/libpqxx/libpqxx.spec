%def_without doc
Name: libpqxx
Summary: C++ client API for PostgreSQL
License: BSD
Epoch: 1
Version: 7.10.0
Release: alt1
Group: System/Libraries
BuildRequires(pre): rpm-macros-cmake
Url: https://pqxx.org
VCS: https://github.com/jtv/libpqxx/
Source0: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: ninja-build python3-module-ninja_syntax
BuildRequires: ctest cmake
BuildRequires: postgresql-devel
%if_with check
BuildRequires: postgresql-test-rpm-macros
%endif
%if %{with doc}
BuildRequires: doxygen
BuildRequires: graphviz libgraphviz
BuildRequires: xmlto
%endif

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Group: Development/C
Summary: Development files for %name
Requires: %name = %epoch:%version-%release
Requires: pkgconfig
%description devel
%summary.

%if %{with doc}
%package doc
Group: System/Libraries
Summary: Developer documentation for %name
BuildArch: noarch
%description doc
%summary.
%endif

%prep
%setup
%ifarch %e2k
sed -i '/Args, Args/{N;s/\.\.\./ /g}' include/pqxx/internal/conversions.hxx
%endif

%build
%cmake -G Ninja \
  -DBUILD_SHARED_LIBS=on \
%if_with doc
  -DBUILD_DOC=ON
%endif
  %nil
%cmake_build

%install
%cmake_install

%files
%doc AUTHORS NEWS README.md VERSION
%doc --no-dereference COPYING
%_libdir/%name-7.10.so

%files devel
%dir %_libdir/cmake/%name
%_includedir/pqxx
%_libdir/%name.so
%_libdir/pkgconfig/%name.pc
%_libdir/cmake/%name/%name-config.cmake
%_libdir/cmake/%name/%name-config-version.cmake
%_libdir/cmake/%name/%name-targets.cmake
%_libdir/cmake/%name/%name-targets-noconfig.cmake

%if_with doc
%files doc
%dir %_docdir/%name
%_docdir/%name/accessing-results.md
%_docdir/%name/binary-data.md
%_docdir/%name/datatypes.md
%_docdir/%name/escaping.md
%_docdir/%name/getting-started.md
%_docdir/%name/mainpage.md
%_docdir/%name/parameters.md
%_docdir/%name/performance.md
%_docdir/%name/prepared-statement.md
%_docdir/%name/streams.md
%_docdir/%name/thread-safety.md
%_docdir/%name/html
%endif

%changelog
* Mon Dec 23 2024 Anton Farygin <rider@altlinux.ru> 1:7.10.0-alt1
- 7.7.5 -> 7.10.0
- disabled documentation build

* Fri Oct 13 2023 Igor Vlasenko <viy@altlinux.org> 1:7.7.5-alt2_2
- e2k support

* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 1:7.7.5-alt1_2
- update to new release by fcimport

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 1:7.6.0-alt1_1
- update to new release by fcimport

* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt2_17
- fixed build

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt2_13
- update to new release by fcimport

* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:4.0.1-alt2_10
- Updated build dependencies.

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_8
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_6
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1:4.0.1-alt1_5
- update to new release by fcimport

* Sat Jul 11 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1:3.2-alt2_0.6.1
- Rebuilt for gcc5 C++11 ABI (ALT#31135).

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt2_0.6
- fixed build

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.5
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1:3.2-alt1_0.4
- initial fc import

