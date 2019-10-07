Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat rpm-macros-ninja-build
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This is a header-only library, but it install also cmake
# scripts to %%{_libdir}, so it cannot be noarch.
%global debug_package %{nil}

Name: mpark-variant
Summary: C++17 std::variant for C++11/14/17
Version: 1.4.0
Release: alt1_2

License: Boost
URL: https://github.com/mpark/variant
Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: ctest cmake
BuildRequires: gcc
Source44: import.info

%description
Header-only %{summary}.

%package devel
Group: Other
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n variant-%{version}

mkdir -p %{_target_platform}
sed -i 's@lib/@%{_libdir}/@g' CMakeLists.txt

%build
pushd %{_target_platform}
    %{fedora_cmake} -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    ..
popd
%ninja_build -C %{_target_platform}

%check
pushd %{_target_platform}
    ctest --output-on-failure
popd

%install
%ninja_install -C %{_target_platform}

%files devel
%doc README.md
%doc --no-dereference LICENSE.md
%{_includedir}/mpark
%{_libdir}/cmake/mpark_variant

%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_2
- new version

