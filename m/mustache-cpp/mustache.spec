Group: Development/C++
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
%define oldname mustache
%define fedora 38
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global appname Mustache

Name: mustache-cpp
Version: 4.1
Release: alt1_10

License: BSL-1.0
Summary: Mustache text templates for modern C++

URL: https://github.com/kainjow/%{appname}
Source0: https://github.com/kainjow/%{appname}/archive/v%{version}/%{oldname}-%{version}.tar.gz

# https://github.com/kainjow/Mustache/pull/42
Patch100: %{oldname}-4.1-catch-fixes.patch

BuildRequires: ctest cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: ninja-build python3-module-ninja_syntax

# mustache currently support only catch v2
%if 0%{?fedora} >= 38 || 0%{?rhel} >= 10
BuildRequires: catch2-devel
%else
BuildRequires: catch-devel catch2-devel
%endif

BuildArch: noarch
Source44: import.info

%description
Text templates implementation for modern C++ (requires C++11).

%package devel
Group: Development/C++
Summary: Development files for %{oldname}
Provides: %{oldname}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{oldname} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
The %{oldname}-devel package contains C++ headers for developing
applications that use %{oldname}.

%prep
%setup -q -n %{appname}-%{version}
%patch100 -p2

sed -e '/-Werror/d' -i CMakeLists.txt
ln -svf %{_includedir}/catch2/catch.hpp ./catch.hpp

%build
%{fedora_v2_cmake} -G Ninja \
    -DCMAKE_BUILD_TYPE=Release
%fedora_v2_cmake_build

%check
%fedora_v2_ctest

%install
mkdir -p %{buildroot}%{_includedir}
install -m 0644 -p %{oldname}.hpp %{buildroot}%{_includedir}

%files devel
%doc README.md
%doc --no-dereference LICENSE
%{_includedir}/%{oldname}.hpp

%changelog
* Tue Oct 10 2023 Igor Vlasenko <viy@altlinux.org> 4.1-alt1_10
- update to new release by fcimport

* Sat Nov 27 2021 Igor Vlasenko <viy@altlinux.org> 4.1-alt1_4
- fixed build

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.1-alt1_1
- update to new release by fcimport

* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1_2
- update to new release by fcimport

* Wed Sep 11 2019 Igor Vlasenko <viy@altlinux.ru> 3.2.1-alt1_2
- new version

