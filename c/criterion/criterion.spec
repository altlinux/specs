Name: criterion
Version: 2.3.3
Release: alt1

Summary: A cross-platform C and C++ unit testing framework for the 21th century

License: MIT
Group: Development/C++
Url: https://github.com/Snaipe/Criterion

BuildRequires: rpm-macros-cmake cmake gcc-c++

# Source-url: https://github.com/Snaipe/Criterion/archive/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-postsubmodules-%version.tar

%description
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name-devel
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
A dead-simple, yet extensible, C and C++ unit testing framework.

%package -n lib%name
Summary: A cross-platform C and C++ unit testing framework for the 21th century
Group: Development/C++

%description -n lib%name
A dead-simple, yet extensible, C and C++ unit testing framework.

%prep
%setup -a1

%build
%cmake
# -DCTESTS=ON
%cmake_build

%install
%cmakeinstall_std
rm -rf %buildroot%_datadir/locale/
# FIXME
rm -rf %buildroot/tmp/
# fix /usr/lib64
[ -d %buildroot%_libdir ] || mv %buildroot%_prefix/lib %buildroot%_libdir

%files -n lib%name
%_libdir/libcriterion.so.*

%files -n lib%name-devel
%_includedir/criterion/
%_libdir/libcriterion.so
%_datadir/pkgconfig/criterion.pc

%changelog
* Wed Mar 13 2019 Vitaly Lipatov <lav@altlinux.ru> 2.3.3-alt1
- initial build for ALT Sisyphus

