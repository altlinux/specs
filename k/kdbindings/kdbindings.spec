Name: kdbindings
Version: 1.1.0
Release: alt1

Summary: Reactive programming & data binding in C++
License: MIT and BSD-3-Clause
Group: Development/C++

Url: https://www.kdab.com/signals-slots-properties-bindings/
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/KDAB/KDBindings/archive/v%version/KDBindings-%version.tar.gz
Source: KDBindings-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

%description
Reactive programming & data binding in C++

From plain C++ you get:

   - Signals + Slots.
   - Properties templated on the contained type.
   - Property bindings allowing reactive code to be written without having to do all the low-level, error prone plumbing by hand.
   - Lazy evaluation of property bindings.
   - No more broken bindings.
   - Totally stand-alone "header-only" library. No heavy Qt dependency.
   - Can still be used with Qt if you so wish.

%package -n lib%name-devel
Summary: Reactive programming & data binding in C++
Group: Development/C++

%description -n lib%name-devel
Reactive programming & data binding in C++

From plain C++ you get:

   - Signals + Slots.
   - Properties templated on the contained type.
   - Property bindings allowing reactive code to be written without having to do all the low-level, error prone plumbing by hand.
   - Lazy evaluation of property bindings.
   - No more broken bindings.
   - Totally stand-alone "header-only" library. No heavy Qt dependency.
   - Can still be used with Qt if you so wish.

%prep
%setup -n KDBindings-%version

%build
%cmake
%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_defaultdocdir/KDBindings

%files -n lib%name-devel
%doc README.md
%_includedir/kdbindings
%_cmakedir/KDBindings

%changelog
* Mon Jun 30 2025 Nazarov Denis <nenderus@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux

