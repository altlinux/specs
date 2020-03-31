%define _unpackaged_files_terminate_build 1

Name: nlohmann-json
Version: 3.7.2
Release: alt2

Summary: JSON for Modern C++ (c++11) ("single header file")

License: MIT
Group: Development/C++
Url: https://github.com/nlohmann/json

Packager: Pavel Vainerman <pv@altlinux.ru>

# Source: https://github.com/nlohmann/json/releases/download/v%{version}/json.hpp
Source: %name-%version.tar

BuildRequires: cmake ctest gcc-c++

%description
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax.
- Trivial integration.
- Serious testing

%package devel
Summary: JSON for Modern C++ (c++11) ("single header file")
Group: Development/C++
Provides: json-cpp
Obsoletes: json-cpp

%description devel
There are myriads of JSON libraries out there, and each may even have its reason to exist. 
Our class had these design goals:
- intuitive syntax.
- Trivial integration.
- Serious testing

This package contains the single header C++ file and CMake dependency files.

%prep
%setup 

%build
%cmake

%cmake_build

%install
%cmakeinstall_std

%check
%make_build check

%files devel
%_includedir/nlohmann
%_libdir/cmake/nlohmann_json

%changelog
* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt2
- Run the auto-tests.
- Package CMake dependency files.
- This is now an arch package'nlohmann-json' providing nlohmann-json-devel
  and replacing json-cpp.
- Fixed project lincense: MIT.

* Tue Mar 31 2020 Paul Wolneykien <manowar@altlinux.org> 3.7.2-alt1
- Upstream version 3.7.2.
- Also install %_includedir/nlohmann/json.hpp symlink.

* Mon Nov 26 2018 Pavel Vainerman <pv@altlinux.ru> 3.4.0-alt1
- new version

* Sun Mar 19 2017 Pavel Vainerman <pv@altlinux.ru> 2.1.1-alt1
- new version

* Tue Nov 08 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.7-alt1
- new version

* Sun Oct 30 2016 Pavel Vainerman <pv@altlinux.ru> 2.0.6-alt0.1
- initial commit 
