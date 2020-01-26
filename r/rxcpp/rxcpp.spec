%define _unpackaged_files_terminate_build 1

%def_with check

Name:    rxcpp
Version: 4.0.0
Release: alt2

Summary: Reactive Extensions for C++

License: Apache 2.0
Group:   Development/C++
URL:     https://github.com/ReactiveX/RxCpp

BuildArch: noarch

# https://github.com/ReactiveX/RxCpp.git
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: cmake ctest
BuildRequires: catch-devel
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

%__subst "/-Werror/d" projects/CMake/shared.cmake

%build
%cmake_insource
# it's not necessary to build project if tests are skipped
%if_with check
%make_build
%endif

# Build docs
pushd projects/doxygen
doxygen doxygen.conf
popd

%install
%makeinstall_std

mkdir -p %buildroot%_includedir
mv %buildroot%_prefix/%name %buildroot%_includedir/%name

%check
pushd build/test
ctest --output-on-failure
popd

%files devel
%doc AUTHORS.txt DeveloperManual.md license.md Readme.html README.md
%_includedir/*

%files doc
%doc projects/doxygen/html

%changelog
* Sun Jan 26 2020 Vitaly Lipatov <lav@altlinux.ru> 4.0.0-alt2
- enable build test (use catch1 really)
- cleanup spec, use cmake_insource

* Tue Jul 31 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt1
- Initial build for ALT.
