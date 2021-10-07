%def_without cmake

%define soname 0

Name: memtailor
Version: 0
Release: alt1.git123afe0
Summary: C++ library of special purpose memory allocators

License: GPL-2.0+ and BSD-3-Clause
Group: System/Libraries
Url: https://github.com/Macaulay2/memtailor

Source: %name-%version.tar.gz
# fedora patches
Patch: memtailor-gtest.patch

%if_with cmake
BuildPreReq: rpm-build-ninja
BuildRequires: cmake
%endif
BuildRequires: gcc-c++ libgtest-devel

%description
Memtailor is a C++ library of special purpose memory allocators.
It currently offers an arena allocator and a memory pool.
The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a
memtailor allocator can also be more convenient due to the ability to
free many allocations at one time.
The Memtailor memory pool is useful if you need to do many allocations
of a fixed size.  For example a memory pool is well suited to allocate
the nodes in a linked list.
You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation
has the further benefits that it stays within the C++ standard, it will
not cause a stack overflow, you can have multiple arena allocators at
the same time and allocation is not tied to a function invocation.

%package  -n lib%name%soname
Summary: %summary
Group: System/Libraries

%description  -n lib%name%soname
Memtailor is a C++ library of special purpose memory allocators.
It currently offers an arena allocator and a memory pool.
The main motivation to use a memtailor allocator is better and more
predictable performance than you get with new/delete.  Sometimes a
memtailor allocator can also be more convenient due to the ability to
free many allocations at one time.
The Memtailor memory pool is useful if you need to do many allocations
of a fixed size.  For example a memory pool is well suited to allocate
the nodes in a linked list.
You can think of the Memtailor arena allocator as being similar to stack
allocation.  Both kinds of allocation are very fast and require you to
allocate/deallocate memory in last-in-first-out order.  Arena allocation
has the further benefits that it stays within the C++ standard, it will
not cause a stack overflow, you can have multiple arena allocators at
the same time and allocation is not tied to a function invocation.

%package -n lib%name-devel
Summary: Development files for memtailor
Group: Development/Other

%description -n lib%name-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch -p0
#sed -i 's|STATIC|SHARED|' src/CMakeLists.txt
sed -i 's|LIBRARY DESTINATION lib|LIBRARY DESTINATION %_lib|' \
  CMakeLists.txt

%build
%if_with cmake
%cmake \
  -GNinja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
#
cmake --build "%_cmake__builddir" -j%__nprocs
%else
export GTEST_PATH=%_prefix
%autoreconf
%configure \
  --disable-static \
  --enable-shared \
  --with-gtest=yes \
#
%make_build
%endif

%install
%if_with cmake
%cmake_install
%else
%makeinstall_std
%endif
# packed into %%doc
rm -rf %buildroot%_prefix/licenses

%files -n lib%name%soname
%doc README.md license.txt
%_libdir/lib%name.so.%{soname}*

%files -n lib%name-devel
%_libdir/lib%name.so
%_includedir/%name.h
%dir %_includedir/%name/
%_includedir/%name/*.h
%_pkgconfigdir/%name.pc

%changelog
* Wed Oct 06 2021 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git123afe0
- Initial build for ALT Sisyphus.
- Built as require for Singular.
- Applied the patch from fedora.
