%define _unpackaged_files_terminate_build 1

%define oname fplus 

Name:    lib%oname
Version: 0.2.27
Release: alt1
Summary: Functional Programming Library for C++. Write concise and readable C++ code
Group:   Development/C++
License: MIT
URL:     https://github.com/Dobiasd/FunctionalPlus
Vcs:     https://github.com/Dobiasd/FunctionalPlus

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++ python3

BuildArch: noarch

%description
Great code should mostly be self-documenting, but while using C++ in reality
you can find yourself dealing with low-level stuff like iterators or
hand-written loops that distract from the actual essence of your code.

FunctionalPlus is a small header-only library supporting you in reducing
code noise and in dealing with only one single level of abstraction at a time.
By increasing brevity and maintainability of your code it can improve
productivity (and fun!) in the long run. It pursues these goals by providing
pure and easy-to-use functions that free you from implementing commonly used
flows of control over and over again.

%package devel
Summary: Functional Programming Library for C++. Write concise and readable C++ code 
Group:   Development/C++

%description devel
FunctionalPlus is a small header-only library supporting you in reducing
code noise and in dealing with only one single level of abstraction at a time.
By increasing brevity and maintainability of your code it can improve
productivity (and fun!) in the long run. It pursues these goals by providing
pure and easy-to-use functions that free you from implementing commonly used
flows of control over and over again.

%prep
%setup

%build
%cmake \
  -DCMAKE_INSTALL_LIBDIR:PATH=%_datadir \
  %nil
%cmake_build

%install
%cmakeinstall_std

%files devel
%doc LICENSE *.cff
%doc *.md
%_includedir/*
%_datadir/cmake/*

%changelog
* Sat Apr 11 2026 L.A. Kostis <lakostis@altlinux.ru> 0.2.27-alt1
- Initial build for ALTLinux.
