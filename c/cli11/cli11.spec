Group: Development/C++
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: boost-devel rpm-build-python3
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name cli11
# Install documentation with the devel package documentation
%global _docdir_fmt %{name}-devel

Name:           cli11
Version:        2.3.1
Release:        alt1_1
Summary:        Command line parser for C++11

License:        BSD-3-Clause
URL:            https://github.com/CLIUtils/CLI11
Source0:        https://github.com/CLIUtils/CLI11/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  boost-complete
BuildRequires:  ctest cmake
BuildRequires:  catch2-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
Source44: import.info

%description
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set with a simple and intuitive interface.

%package devel
Group: Development/C++
Summary:        Command line parser for C++11
Provides:       %{name}-static = %{version}-%{release}

%description devel
CLI11 is a command line parser for C++11 and beyond that provides a
rich feature set with a simple and intuitive interface.

%package        docs
Group: Development/C++
# Doxygen adds files with licenses other than BSD-3-Clause.
# GPL-1.0-or-later: bc_s*.png, bdwn.png, closed.png, doc.png, doxygen.css,
#     doxygen.svg, folderclosed.png, folderopen.png, nav_*.png, open.png,
#     search/close.svg, search/mag*.svg, search/search.css, splitbar*.png,
#     sync_off.png, sync_on.png, tab_*.png, tabs.css
# MIT: dynsections.js, jquery.js, menu.js, menudata.js, search/search.js
License:        BSD-3-Clause AND GPL-1.0-or-later AND MIT
Summary:        Documentation for CLI11
BuildArch: noarch

%description    docs
Documentation for CLI11.

%prep
%setup -q -n CLI11-%{version}


# Alter the icon path in README.md for the installed paths
sed -i.orig 's,\./docs,.,' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build
CXXFLAGS='%{build_cxxflags} -DCLI11_OPTIONAL -DCLI11_STD_OPTIONAL=1'
%{fedora_v2_cmake} \
    -DCLI11_BUILD_DOCS:BOOL=TRUE \
    -DCLI11_BUILD_TESTS:BOOL=TRUE \
    -DCMAKE_CXX_STANDARD=17
%fedora_v2_cmake_build

# Build the documentation
%fedora_v2_cmake_build --target docs

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files devel
%doc CHANGELOG.md README.md docs/CLI11_300.png
%doc --no-dereference LICENSE
%{_includedir}/CLI/
%{_datadir}/cmake/CLI11/
%{_datadir}/pkgconfig/CLI11.pc

%files docs
%doc %{_vpath_builddir}/docs/html
%doc docs/CLI11.svg docs/CLI11_100.png

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 2.3.1-alt1_1
- update to new release by fcimport

* Sat May 07 2022 Igor Vlasenko <viy@altlinux.org> 2.2.0-alt1_1
- update to new release by fcimport

* Mon Oct 25 2021 Igor Vlasenko <viy@altlinux.org> 2.1.2-alt1_1
- update to new release by fcimport

* Tue Oct 12 2021 Igor Vlasenko <viy@altlinux.org> 2.1.1-alt1_1
- update to new release by fcimport

* Tue Sep 21 2021 Igor Vlasenko <viy@altlinux.org> 2.0.0-alt1_1
- update to new release by fcimport

* Tue Nov 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_3
- new version

