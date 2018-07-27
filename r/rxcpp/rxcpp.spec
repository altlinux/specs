%define _unpackaged_files_terminate_build 1

%def_without check

Name:    rxcpp
Version: 4.0.0
Release: alt1
Summary: Reactive Extensions for C++
License: Apache 2.0
Group:   Development/C++
URL:     https://github.com/ReactiveX/RxCpp

BuildArch: noarch

# https://github.com/ReactiveX/RxCpp.git
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake ctest
BuildRequires: catch2-devel
BuildRequires: doxygen
BuildRequires: graphviz

%description
The Reactive Extensions for C++ (RxCpp) is a library of algorithms
for values-distributed-in-time.

%package devel
Summary: Reactive Extensions for C++
Group:   Development/C++

%description devel
The Reactive Extensions for C++ (RxCpp) is a library of algorithms
for values-distributed-in-time.

%package doc
Summary: API-documentation for %{name}
Group:   Development/C++

%description doc
This package contains the API-documentation for %{name}.

%prep
%setup

# Fix path to catch.
sed -i.catch -e 's!\${RXCPP_DIR}/ext/catch/include!%{_includedir}/catch!g' \
  projects/CMake/shared.cmake

%build
%cmake
# it's not necessary to build project if tests are skipped
%if_with check
%make -C BUILD
%endif

# Build docs
pushd projects/doxygen
doxygen doxygen.conf
popd

%install
%cmakeinstall_std

mkdir -p %buildroot%_includedir
mv %buildroot%_prefix/%name %buildroot%_includedir/%name

%check
pushd BUILD/build/test
ctest --output-on-failure
popd

%files devel
%doc AUTHORS.txt DeveloperManual.md license.md Readme.html README.md
%_includedir/*

%files doc
%doc projects/doxygen/html

%changelog
* Tue Jul 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1
- Initial build for ALT.
