%define oldname re2
Name: libre2_10
Version: 20230301
Release: alt2
Summary: C++ fast alternative to backtracking RE engines
Group: System/Libraries
License: BSD-3-Clause
Url: https://github.com/google/re2/
Source0: %name-%version.tar
BuildRequires: gcc-c++

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake ctest

%description
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

Backtracking engines are typically full of features and convenient syntactic
sugar but can be forced into taking exponential amounts of time on even small
inputs.

In contrast, RE2 uses automata theory to guarantee that regular expression
searches run in time linear in the size of the input, at the expense of some
missing features (e.g back references and generalized assertions).

%package -n libre2
Summary: C++ fast alternative to backtracking RE engines
Group: System/Libraries

%description -n libre2
RE2 is a C++ library providing a fast, safe, thread-friendly alternative to
backtracking regular expression engines like those used in PCRE, Perl, and
Python.

%prep
%setup

%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DCMAKE_COLOR_MAKEFILE:BOOL=OFF \
  -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmake_install

# Suppress the static library
find %buildroot -name 'libre2.a' -delete

%check
ctest --test-dir %_cmake__builddir --output-on-failure --force-new-ctest-process %_smp_mflags

%files -n libre2
%doc LICENSE
%doc AUTHORS CONTRIBUTORS README
%_libdir/libre2.so.*

%changelog
* Mon Apr 29 2024 Anton Farygin <rider@altlinux.ru> 20230301-alt2
- built as compat library without the devel package

* Wed Apr 19 2023 Alexey Shabalin <shaba@altlinux.org> 20230301-alt1
- update to 2023-03-01
- switch to cmake for build

* Mon Feb 20 2023 Anton Farygin <rider@altlinux.ru> 20230201-alt1
- update to 2023-02-01

* Sat Jun 25 2022 Anton Farygin <rider@altlinux.ru> 20220601-alt1
- update to 2022-06-01

* Wed May 11 2022 Anton Farygin <rider@altlinux.ru> 20220401-alt1
- update to 2022-04-01

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 20220201-alt1
- update to 2022-02-01

* Mon Nov 22 2021 Anton Farygin <rider@altlinux.ru> 20211101-alt1
- update to 2021-11-01

* Thu Sep 09 2021 Anton Farygin <rider@altlinux.ru> 20210901-alt1
- update to 2021-09-01

* Tue Aug 10 2021 Anton Farygin <rider@altlinux.ru> 20210801-alt1
- update to 2021-08-01

* Tue Jun 22 2021 Anton Farygin <rider@altlinux.ru> 20210601-alt1
- update to 2021-06-01

* Tue Apr 13 2021 Anton Farygin <rider@altlinux.org> 20210401-alt1
- update to 2021-04-01

* Tue Mar 09 2021 Anton Farygin <rider@altlinux.org> 20210202-alt1
- update to 2021-02-02

* Mon Nov 16 2020 Anton Farygin <rider@altlinux.ru> 20201101-alt1
- new version

* Mon Oct 19 2020 Anton Farygin <rider@altlinux.ru> 20201001-alt1
- new version

* Fri Aug 21 2020 Anton Farygin <rider@altlinux.ru> 20200801-alt1
- new version

* Thu Jul 16 2020 Anton Farygin <rider@altlinux.ru> 20200706-alt1
- new version

* Fri Jun 05 2020 Anton Farygin <rider@altlinux.ru> 20200601-alt1
- new version

* Wed Apr 01 2020 Anton Farygin <rider@altlinux.ru> 20200401-alt1
- new version

* Thu Jan 16 2020 Anton Farygin <rider@altlinux.ru> 20200101-alt1
- new version

* Wed Dec 04 2019 Anton Farygin <rider@altlinux.ru> 20191201-alt1
- 20191201

* Wed Nov 13 2019 Anton Farygin <rider@altlinux.ru> 20191101-alt1
- 20191101

* Wed Sep 18 2019 Anton Farygin <rider@altlinux.ru> 20190901-alt1
- 20190901

* Fri Aug 09 2019 Anton Farygin <rider@altlinux.ru> 20190801-alt1
- updated to 20190801

* Wed Jun 26 2019 Anton Farygin <rider@altlinux.ru> 20190601-alt1
- updated to 20190601
- cleanup specfile

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_3
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 20160401-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_5
- update to new release by fcimport

* Sun Dec 21 2014 Igor Vlasenko <viy@altlinux.ru> 20131024-alt1_3
- new version

