Name: half
Version: 2.2.0
Release: alt1

Summary: A C++ half-precision floating point type
License: MIT
Group: Development/C++

Url: https://%name.sourceforge.net/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://sourceforge.net/projects/%name/files/%name/%version/%name-%version.zip

BuildArch: noarch

BuildRequires: gcc-c++
BuildRequires: unzip

%description
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%package -n lib%name-devel
Summary: A C++ half-precision floating point type
Group: Development/C++

%description -n lib%name-devel
This is a C++ header-only library to provide an IEEE-754 conformant
half-precision floating point type along with corresponding arithmetic
operators, type conversions and common mathematical functions. It aims
for both efficiency and ease of use, trying to accurately mimic the
behaviour of the builtin floating point types at the best performance
possible. It automatically uses and provides C++11 features when
possible, but stays completely C++98-compatible when neccessary.

%prep
%setup -c
# change dos endings to unix
sed -i "s|\r||g" include/half.hpp
sed -i "s|\r||g" LICENSE.txt
sed -i "s|\r||g" README.txt

%install
%__mkdir_p %buildroot%_includedir
%__install -Dp -m0644 include/%name.hpp %buildroot%_includedir

%files -n lib%name-devel
%doc LICENSE.txt README.txt
%_includedir/%name.hpp

%changelog
* Sat Nov 02 2024 Nazarov Denis <nenderus@altlinux.org> 2.2.0-alt1
- Initial build for ALT Linux

