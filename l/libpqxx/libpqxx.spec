# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%bcond_with check
%bcond_with doc

Name:           libpqxx
Summary:        C++ client API for PostgreSQL
Epoch:          1
Version:        7.7.5
Release:        alt1_2

%global         forgeurl https://github.com/jtv/%{name}/
%global         tag %{version}
# FedoraForgeMeta2ALT: generated meta
%global forgeurl https://github.com/jtv/libpqxx/
%global forgesource https://github.com/jtv/libpqxx//archive/7.7.5/libpqxx-7.7.5.tar.gz
%global archivename libpqxx-7.7.5
%global archiveext tar.gz
%global archiveurl https://github.com/jtv/libpqxx//archive/7.7.5/libpqxx-7.7.5.tar.gz
%global topdir libpqxx-7.7.5
%global extractdir libpqxx-7.7.5
%global repo libpqxx
#global owner %nil
#global namespace %nil
%global scm git
%global tag 7.7.5
#global commit %nil
#global shortcommit %nil
#global branch %nil
%global version 7.7.5
#global date %nil
%global distprefix .git7.7.5
# FedoraForgeMeta2ALT: end generated meta

License:        BSD
URL:            http://pqxx.org/
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  ninja-build python3-module-ninja_syntax
BuildRequires:  ctest cmake
BuildRequires:  postgresql-devel
%if %{with check}
BuildRequires:  postgresql-test-rpm-macros
%endif
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz libgraphviz
BuildRequires:  xmlto
%endif
Source44: import.info

%description
C++ client API for PostgreSQL. The standard front-end (in the sense of
"language binding") for writing C++ programs that use PostgreSQL.
Supersedes older libpq++ interface.

%package devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       %{name} = %{epoch}:%{version}-%{release}
Requires:       pkgconfig
%description devel
%{summary}.

%if %{with doc}
%package doc
Group: System/Libraries
Summary: Developer documentation for %{name}
BuildArch: noarch
%description doc
%{summary}.
%endif

%prep
%setup -q -n libpqxx-7.7.5


%build
%{fedora_v2_cmake} -G Ninja \
%if %{with doc}
  -DBUILD_DOC=ON
%endif
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%check
%if %{with check}
%postgresql_tests_run
cd "%{_vpath_builddir}/test"
%__ctest -V --force-new-ctest-process %{?_smp_mflags}
cd -
%endif

%files
%doc AUTHORS NEWS README.md VERSION
%doc --no-dereference COPYING
%{_libdir}/%{name}-7.7.so

%files devel
%dir %{_libdir}/cmake/%{name}
%{_includedir}/pqxx
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/%{name}-config.cmake
%{_libdir}/cmake/%{name}/%{name}-config-version.cmake
%{_libdir}/cmake/%{name}/%{name}-targets.cmake
%{_libdir}/cmake/%{name}/%{name}-targets-noconfig.cmake

%if %{with doc}
%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/accessing-results.md
%{_docdir}/%{name}/binary-data.md
%{_docdir}/%{name}/datatypes.md
%{_docdir}/%{name}/escaping.md
%{_docdir}/%{name}/getting-started.md
%{_docdir}/%{name}/mainpage.md
%{_docdir}/%{name}/parameters.md
%{_docdir}/%{name}/performance.md
%{_docdir}/%{name}/prepared-statement.md
%{_docdir}/%{name}/streams.md
%{_docdir}/%{name}/thread-safety.md
%{_docdir}/%{name}/html
%endif

%changelog
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

