Name: rapidyaml
Version: 0.4.1
Release: alt1

Summary: A library to parse and emit YAML
License: MIT
Group: System/Libraries

URL: https://github.com/biojppm/%name
Packager: Nazarov Denis <nenderus@altlinux.org> 

Source: https://github.com/biojppm/%name/releases/download/v%version/%name-%version-src.tgz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: python3-dev

%description
ryml is a C++ library to parse and emit YAML.

%package -n lib%name
Summary: A library to parse and emit YAML
Group: System/Libraries

%description -n lib%name
ryml is a C++ library to parse and emit YAML.

ryml parses both read-only and in-situ source buffers; the resulting
data nodes hold only views to sub-ranges of the source buffer. No
string copies or duplications are done.

%package -n libc4core
Summary: Utility library of %name
Group: System/Libraries

%description -n libc4core
ryml is a C++ library to parse and emit YAML.

%package -n lib%name-devel
Summary: Header files for rapidyaml, a library to parse and emit YAML
Group: Development/C++

%description -n lib%name-devel
ryml is a C++ library to parse and emit YAML.

This package contains development headers and examples.

%prep
%setup -n %name-%version-src

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=TRUE
%cmake_build

%install
%cmake_install

if [ "%_libdir" != "/usr/lib" ]; then
	mkdir -p %buildroot%_libdir
	mv %buildroot/usr/lib/* %buildroot%_libdir/
fi

%files -n lib%name
%{_libdir}/libryml.so.*

%files -n libc4core
%_libdir/libc4core.so.*

%files -n lib%name-devel
%doc README.md
%_includedir/*
%_libdir/cmake/c4core
%_libdir/cmake/ryml
%_libdir/libc4core.so
%_libdir/libryml.so

%changelog 
* Fri May 20 2022 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- Initial build for ALT Linux
