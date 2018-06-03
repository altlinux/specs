Name: catch2
Version: 2.2.2
Release: alt1

Summary: C++ Unit Test framework ("all in one header")

License: Boost Software License, Version 1.0
Group: Development/C++
Url: https://github.com/catchorg/Catch2

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Source-url: https://github.com/catchorg/Catch2/archive/v%{version}.tar.gz
Source: %name-%version.tar

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%package devel
Summary: C++ Unit Test framework ("all in one header")
Group: Development/C++

%description devel
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup

%build

%install
mkdir -p %buildroot%_includedir/%{name}
mv -f single_include/*.hpp %buildroot%_includedir/%{name}/

%files devel
%dir %_includedir/%{name}
%_includedir/%{name}/*.hpp

%changelog
* Sun Jun 03 2018 Pavel Vainerman <pv@altlinux.ru> 2.2.2-alt1
- new version (2.2.2) with rpmgs script

