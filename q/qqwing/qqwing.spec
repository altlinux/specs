Name: qqwing
Version: 1.3.3
Release: alt1

Summary: Command-line Sudoku solver and generator
Group: Games/Boards
License: GPLv2+
Url: http://%name.com/

Source: http://%name.com/%name-%version.tar.gz

Requires: lib%name = %version-%release
BuildRequires: gcc-c++

%description
QQwing is a command-line Sudoku solver and generator.

%package -n lib%name
Summary: Library for Sudoku solving and generation
Group: System/Libraries

%description -n lib%name
lib%name is a C++ library for solving and generating Sudoku puzzles.

%package -n lib%name-devel
Summary: Development files for lib%name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name.

%prep
%setup

%build
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.*
%doc README AUTHORS

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name.hpp
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc

%changelog
* Sun Nov 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- first build for Sisyphus

