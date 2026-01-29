Group: Development/C++
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake
BuildRequires: boost-devel
# END SourceDeps(oneline)
# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           cli11
Version:        2.6.1
Release:        alt1
Summary:        Command line parser for C++11

License:        BSD-3-Clause
URL:            https://github.com/CLIUtils/CLI11
Source0:        https://github.com/CLIUtils/CLI11/archive/v%version/%name-%version.tar.gz

BuildRequires:  boost-complete
BuildRequires:  catch2-devel
BuildRequires:  ctest cmake
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
BuildArch:      noarch
Provides:       %name-static = %version-%release

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
BuildArch:      noarch

%description    docs
Documentation for CLI11.

%prep
%setup -q -n CLI11-%{version}


# Alter the icon path in README.md for the installed paths
sed -i.orig 's,\./docs,.,' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build
%add_optflags '-DCLI11_OPTIONAL -DCLI11_STD_OPTIONAL=1'
%cmake \
    -DCLI11_BUILD_DOCS:BOOL=TRUE \
    -DCLI11_BUILD_TESTS:BOOL=TRUE \
    -DCMAKE_CXX_STANDARD=17
%cmake_build

# Build the documentation
%cmake_build --target docs

%install
%cmake_install

%check
%ctest

%files devel
%doc CHANGELOG.md README.md docs/CLI11_300.png
%doc --no-dereference LICENSE
%{_includedir}/CLI
%{_datadir}/cmake/CLI11
%{_datadir}/pkgconfig/CLI11.pc

%files docs
%doc %_cmake__builddir/docs/html
%doc docs/CLI11.svg docs/CLI11_100.png

%changelog
* Thu Jan 29 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.6.1-alt1
- update to new release
- minor spec improvements

* Tue Apr 08 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 2.5.0-alt1
- NMU: update to new release

* Thu Apr 20 2023 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt1_3
- update to new release by fcimport

* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 2.3.2-alt1_2
- update to new release by fcimport

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

