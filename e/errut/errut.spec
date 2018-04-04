Name: errut
Version: 1.1.0
Release: alt1

Summary: This is meant to be a set of simple error handling utilities

Group: Development/C++
License: MIT
URL: http://research.edm.uhasselt.be/jori/errut/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name-%version.tar.gz
Patch: errut-1.1.0-fix_include_string.patch

BuildRequires: gcc-c++ cmake

%description
This is meant to be a set of simple error handling utilities. Currently
it is only one header file. It was originally a part of a larger project,
but turned out to be helpful in several other projects, which is why its
own project was created.

%prep
%setup
%patch -p2

%build
%cmake_insource

%install
%makeinstall_std

%files
%_libdir/*
%_includedir/%name

%changelog
* Wed Apr 04 2018 Grigory Ustinov <grenka@altlinux.org> 1.1.0-alt1
- Build new version.

* Wed Jun 18 2008 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt1
- initial build
