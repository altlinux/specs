%define sover 3

Name: SheenBidi
Version: 3.0.0
Release: alt1

Summary: A lightweight, fast and stable implementation of the Unicode Bidirectional Algorithm
License: Apache-2.0
Group: System/Libraries

Url: https://github.com/Tehreer/%name
Vcs: https://github.com/Tehreer/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/Tehreer/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
%name is a lightweight, fast and stable implementation of the Unicode Bidirectional Algorithm (UBA).

It is being used by multiple open source and commercial projects in different domains such as:

    - Game Engine: Defold
    - Games: Watch Dogs: Legion, SuperTuxKart, VVVVVV, DevilutionX, Monaco 2
    - Multimedia: SFML, JUCE, Tracktion Engine, Rive Runtime
    - Text: Raqm, Tehreer Android, Tehreer Cocoa
    - Mapping: VTS Browser
    - Web: Dropflow, Itemizer

Features:

    - Object Based Design: Facilitates modular and maintainable code.
    - Core Level Optimization: Ensures high performance.
    - Thread Safe Architecture: Suitable for multithreaded applications.
    - Lightweight API: Simplifies integration.
    - Encoding Support: UTF-8, UTF-16, and UTF-32.


%package -n lib%name%sover
Summary: A lightweight, fast and stable implementation of the Unicode Bidirectional Algorithm
Group: System/Libraries

%description -n lib%name%sover
%name is a lightweight, fast and stable implementation of the Unicode Bidirectional Algorithm (UBA).

It is being used by multiple open source and commercial projects in different domains such as:

    - Game Engine: Defold
    - Games: Watch Dogs: Legion, SuperTuxKart, VVVVVV, DevilutionX, Monaco 2
    - Multimedia: SFML, JUCE, Tracktion Engine, Rive Runtime
    - Text: Raqm, Tehreer Android, Tehreer Cocoa
    - Mapping: VTS Browser
    - Web: Dropflow, Itemizer

Features:

    - Object Based Design: Facilitates modular and maintainable code.
    - Core Level Optimization: Ensures high performance.
    - Thread Safe Architecture: Suitable for multithreaded applications.
    - Lightweight API: Simplifies integration.
    - Encoding Support: UTF-8, UTF-16, and UTF-32.

%package -n lib%name-devel
Summary: Header files and development libraries for %name
Group: Development/C++

%description -n lib%name-devel
This package contains the header files and development libraries for %name.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc README.md
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/lib%name.so
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/*.cmake
%_pkgconfigdir/sheenbidi.pc

%changelog
* Fri May 15 2026 Nazarov Denis <nenderus@altlinux.org> 3.0.0-alt1
- Initial build for ALT Linux
