Name: errut
Version: 1.0.0
Release: alt1

Summary: This is meant to be a set of simple error handling utilities

Group: Development/C++
License: MIT
URL: http://research.edm.uhasselt.be/jori/errut/
Packager: Sergey Alembekov <rt@altlinux.ru>
Source: %name-%version.tar.gz
BuildRequires: gcc4.1-c++

%description
This is meant to be a set of simple error handling utilities. Currently
it is only one header file. It was originally a part of a larger project,
but turned out to be helpful in several other projects, which is why its
own project was created.

%prep
%setup

%build
%configure --prefix=%prefix
%make

%install
mkdir %buildroot
%make_build install DESTDIR=%buildroot

%files
%_includedir/%name/*

%changelog
* Wed Jun 18 2008 Sergey Alembekov <rt@altlinux.ru> 1.0.0-alt1
- initial build

