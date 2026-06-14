Name: rapidyaml
Version: 0.15.2
Release: alt1

Summary: A library to parse and emit YAML
License: MIT
Group: System/Libraries

Url: https://github.com/biojppm/%name
Vcs: https://github.com/biojppm/%name
Packager: Nazarov Denis <nenderus@altlinux.org> 

Source: https://github.com/biojppm/%name/releases/download/v%version/%name-%version-src.tgz

Patch3500: rapidyaml-loongarch64.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: python3-dev

%description
ryml is a C++ library to parse and emit YAML.

%package -n libryml
Summary: A library to parse and emit YAML
Group: System/Libraries

%description -n libryml
ryml is a C++ library to parse and emit YAML.

ryml parses both read-only and in-situ source buffers; the resulting
data nodes hold only views to sub-ranges of the source buffer. No
string copies or duplications are done.

%package -n libc4core
Summary: Utility library of %name
Group: System/Libraries

%description -n libc4core
ryml is a C++ library to parse and emit YAML.

%package -n libryml-devel
Summary: Header files for rapidyaml, a library to parse and emit YAML
Group: Development/C++

%description -n libryml-devel
ryml is a C++ library to parse and emit YAML.

This package contains development headers and examples.

%prep
%setup -n %name-%version-src
%patch3500 -p1

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_INSTALL_LIBDIR:PATH=%_lib \
	-DBUILD_SHARED_LIBS:BOOL=TRUE

%cmake_build

%install
%cmake_install

%files -n libryml
%_libdir/libryml.so.*

%files -n libc4core
%_libdir/libc4core.so.*

%files -n libryml-devel
%doc README.md
%_includedir/*
%_libdir/cmake/c4core
%_libdir/cmake/ryml
%_libdir/libc4core.so
%_libdir/libryml.so

%changelog 
* Sun Jun 14 2026 Nazarov Denis <nenderus@altlinux.org> 0.15.2-alt1
- Version 0.15.2

* Sat Jun 06 2026 Nazarov Denis <nenderus@altlinux.org> 0.14.0-alt1
- Version 0.14.0

* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.12.1-alt1
- Version 0.12.1

* Tue Apr 14 2026 Nazarov Denis <nenderus@altlinux.org> 0.11.1-alt1
- Version 0.11.1

* Sat Mar 14 2026 Nazarov Denis <nenderus@altlinux.org> 0.11.0-alt1
- Version 0.11.0

* Wed Oct 01 2025 Nazarov Denis <nenderus@altlinux.org> 0.10.0-alt1
- Version 0.10.0

* Sat Apr 12 2025 Nazarov Denis <nenderus@altlinux.org> 0.9.0-alt1
- Version 0.9.0

* Sun Feb 16 2025 Nazarov Denis <nenderus@altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Tue Aug 27 2024 Nazarov Denis <nenderus@altlinux.org> 0.7.2-alt1
- Version 0.7.2

* Fri Jun 14 2024 Nazarov Denis <nenderus@altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Wed May 15 2024 Nazarov Denis <nenderus@altlinux.org> 0.6.0-alt1
- Version 0.6.0

* Tue Nov 14 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.5.0-alt2
- NMU: fixed FTBFS on LoongArch

* Mon Nov 13 2023 Nazarov Denis <nenderus@altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Mon May 23 2022 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt3
- Fix libdir

* Sun May 22 2022 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt2
- Rename subpackages

* Fri May 20 2022 Nazarov Denis <nenderus@altlinux.org> 0.4.1-alt1
- Initial build for ALT Linux
