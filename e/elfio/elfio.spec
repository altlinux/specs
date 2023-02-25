Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

%global debug_package %{nil}

Name:           elfio
Version:        3.11
Release:        alt1_1
Summary:        C++ library for reading and generating ELF files

# This is the proper SPDX license
License:        MIT
URL:            http://elfio.sourceforge.net/
Source0:        https://downloads.sf.net/elfio/elfio-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
Source44: import.info

%description
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%package devel
Group: Other
Summary:        %{summary}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel
ELFIO is a small, header-only C++ library that provides a simple interface for
reading and generating files in ELF binary format.

It is used as a standalone library - it is not dependent on any other product
or project. Adhering to ISO C++, it compiles on a wide variety of
architectures and compilers.

While the library is easy to use, some basic knowledge of the ELF binary
format is required. Such Information can easily be found on the Web.


%prep
%setup -q



%build
%ifarch %e2k
# -std=c++03 by default as of lcc 1.23.12
%add_optflags -std=c++11
%endif
%{fedora_v2_cmake} -DELFIO_BUILD_EXAMPLES=ON
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install
rm -r %{buildroot}%{_datadir}/docs

%check
# Sanity check
%{_vpath_builddir}/examples/elfdump/elfdump %{_bindir}/cmake

%files devel
%doc --no-dereference LICENSE.txt
%doc doc/elfio.pdf README.md
%{_includedir}/elfio/
%{_datadir}/elfio/


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 3.11-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 3.10-alt1_1
- update to new release by fcimport

* Sun Feb 06 2022 Igor Vlasenko <viy@altlinux.org> 3.9-alt1_4
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 3.9-alt1_1
- update to new release by fcimport

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 3.8-alt1_1
- update to new release by fcimport

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1_1
- update to new release by fcimport

* Tue Mar 24 2020 Igor Vlasenko <viy@altlinux.ru> 3.5-alt1_1
- update to new release by fcimport

* Wed Oct 09 2019 Michael Shigorin <mike@altlinux.org> 3.4-alt2_11
- E2K: explicit -std=c++11

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 3.4-alt1_11
- new version

