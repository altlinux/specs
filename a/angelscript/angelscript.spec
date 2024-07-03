%def_with cmake

Name: angelscript
Version: 2.36.1
Release: alt1

Summary: Flexible cross-platform scripting library

License: Zlib
Group: System/Libraries
Url: https://www.angelcode.com/angelscript/
Vcs: git://github.com/codecat/angelscript-mirror.git

Source: %name-%version.tar.gz
# Source-url: %url/sdk/files/%{name}_%version.zip

%if_with cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
%else
BuildRequires: meson
%endif
BuildRequires: gcc-c++

%description
The AngelScript library is a software library for easy integration of
external scripting to applications, with built-in compiler and virtual
machine. The scripting language is easily extendable to incorporate
application specific data types and functions. It is designed with C++
in mind, as such it shares many features with C++, for example syntax
and data types.

%package -n lib%name%version
Summary: Flexible cross-platform scripting library
Group: System/Libraries

%description -n lib%name%version
The AngelScript library is a software library for easy integration of
external scripting to applications, with built-in compiler and virtual
machine. The scripting language is easily extendable to incorporate
application specific data types and functions. It is designed with C++
in mind, as such it shares many features with C++, for example syntax
and data types.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
sed -i 's|lib/cmake/Angelscript|%_lib/cmake/Angelscript|' \
  %name/projects/cmake/CMakeLists.txt
sed -i '/DESTINATION/s|lib|%_lib|g' \
  %name/projects/cmake/CMakeLists.txt

%build
%add_optflags -fno-strict-aliasing
%if_with cmake
cd %name/projects/cmake/
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DBUILD_SHARED_LIBS:BOOL=ON
%cmake_build
%else
cd %name/projects/meson/
%meson
%meson_build
%endif

%install
%if_with cmake
cd %name/projects/cmake/
%cmake_install
%else
cd %name/projects/meson/
%meson_install
%endif

%files -n lib%name%version
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%doc docs/articles/*.html
%_libdir/lib%name.so
%_includedir/%name.h
%if_with cmake
%dir %_libdir/cmake/Angelscript/
%_libdir/cmake/Angelscript/Angelscript*.cmake
%endif

%changelog
* Tue Jul 02 2024 Leontiy Volodin <lvol@altlinux.org> 2.36.1-alt1
- Initial build for ALT Sisyphus (for supertuxkart).

