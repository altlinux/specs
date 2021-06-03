%define _unpackaged_files_terminate_build 1

Name: pystring
Version: 1.1.3
Release: alt1.git.281419d
Summary: C++ functions matching the interface and behavior of python string methods with std::string
License: BSD-3-Clause
Group: Development/C++
Url: https://github.com/imageworks/pystring

# https://github.com/imageworks/pystring.git
Source: %name-%version.tar

# Taken from Fedora
Source1: CMakeLists.txt

BuildRequires: gcc-c++
BuildRequires: cmake

%description
Pystring is a collection of C++ functions which match the interface
and behavior of python's string class methods using std::string.
Implemented in C++, it does not require or make use of a python interpreter.
It provides convenience and familiarity for common string operations
not included in the standard C++ library.
It's also useful in environments where both C++ and python are used.

Overlapping functionality (such as index and slice/substr)
of std::string is included to match python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

Note: Despite the infrequent updates, this repo is not dead/abandoned- just stable!
We use it every day at Imageworks.

%package -n lib%name
Summary: C++ functions matching the interface and behavior of python string methods with std::string
Group: Development/C++

%description -n lib%name
Pystring is a collection of C++ functions which match the interface
and behavior of python's string class methods using std::string.
Implemented in C++, it does not require or make use of a python interpreter.
It provides convenience and familiarity for common string operations
not included in the standard C++ library.
It's also useful in environments where both C++ and python are used.

Overlapping functionality (such as index and slice/substr)
of std::string is included to match python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

Note: Despite the infrequent updates,
this repo is not dead/abandoned - just stable!
We use it every day at Imageworks.

%package devel
Summary: C++ functions matching the interface and behavior of python string methods with std::string
Group: Development/C++
Requires: lib%name = %EVR

%description devel
Pystring is a collection of C++ functions which match the interface
and behavior of python's string class methods using std::string.
Implemented in C++, it does not require or make use of a python interpreter.
It provides convenience and familiarity for common string operations
not included in the standard C++ library.
It's also useful in environments where both C++ and python are used.

Overlapping functionality (such as index and slice/substr)
of std::string is included to match python interfaces.

Originally developed at Sony Pictures Imageworks.
http://opensource.imageworks.com/

Note: Despite the infrequent updates,
this repo is not dead/abandoned - just stable!
We use it every day at Imageworks.

This package contains development files for pystring.

%prep
%setup

install %SOURCE1 ./

%build
%cmake

%cmake_build

%install
%cmakeinstall_std

%check
pushd %_cmake__builddir
./test
popd

%files -n lib%name
%doc LICENSE
%doc README
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/*

%changelog
* Tue Jun 01 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.3-alt1.git.281419d
- Initial build for ALT.
