Name: Catch
Version: 1.0
Release: alt1

Summary: Catch - Automated Test Cases for C++ ("all in one header")

License: GPL
Group: Development/C++
Url: http://wiki.etersoft.ru/UniSet

Packager: Pavel Vainerman <pv@altlinux.ru>
BuildArch: noarch

# Git: https://github.com/philsquared/Catch
Source: %name-%version.tar

#BuildRequires:

%description
Catch stands for C++ Automated Test Cases in Headers 
and is a multi-paradigm automated 
test framework for C++ and Objective-C (and, maybe, C). 
It is implemented entirely in a set of header files, 
but is packaged up as a single header for extra convenience.

%prep
%setup

%build

%install
mkdir -p %buildroot%_includedir
mv -f *.hpp %buildroot%_includedir

%files
%_includedir/*.hpp

%changelog
* Thu Oct 02 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt1
- moved catch.hpp directly into %_includedir

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.2
- test build

* Tue Sep 30 2014 Pavel Vainerman <pv@altlinux.ru> 1.0-alt0.1
- initial commit


