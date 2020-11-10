Group: Development/C++
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: boost-devel python-devel rpm-build-python
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Even though this package does not install any ELF files, it does compute
# pointer sizes.  Therefore, this package cannot be noarch, but it also does
# not produce any debug information.
%global debug_package %{nil}

Name:           cli11
Version:        1.9.1
Release:        alt1_3
Summary:        Command line parser for C++11

License:        BSD
URL:            https://github.com/CLIUtils/CLI11
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use the system gmock/gtest instead of requiring that they be downloaded
Patch0:         %{name}-gtest.patch

BuildRequires:  boost-complete
BuildRequires:  ctest cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
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
Summary:        Documentation for CLI11
BuildArch:      noarch

%description    docs
Documentation for CLI11.

%prep
%setup -q -n CLI11-%{version}
%patch0 -p0


%build
%{fedora_v2_cmake} -DCLI11_BUILD_DOCS:BOOL=TRUE -DCLI11_BUILD_TESTS:BOOL=TRUE
%fedora_v2_cmake_build

# Build the documentation
make -C %{__cmake_builddir} docs

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files devel
%doc CHANGELOG.md README.md
%doc --no-dereference LICENSE
%{_includedir}/CLI/
%{_libdir}/cmake/CLI11/

%files docs
%doc %{__cmake_builddir}/docs/html
%doc docs/CLI11.svg docs/CLI11_100.png docs/CLI11_300.png

%changelog
* Tue Nov 10 2020 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1_3
- new version

