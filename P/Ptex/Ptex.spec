%define git a3729367596c827ace086f4baa6cab89b6a7f439
%define soname 2.5

%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%def_disable static
%def_enable test

Name: Ptex
Version: 2.5.2
Release: alt1
Summary: Per-Face Texture Mapping for Production Rendering

Group: System/Libraries
License: BSD-3-Clause
Url: https://github.com/wdas/ptex
Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires: gcc-c++ zlib-devel /usr/bin/doxygen graphviz
BuildRequires: libdeflate-devel
%if_enabled test
BuildRequires: ctest
%endif

%description
Ptex is a texture mapping system developed by
Walt Disney Animation Studios for production-quality rendering.

%package -n ptxinfo
Summary: lib%{name} information utility
Group: Development/Tools
Requires: lib%{name} = %EVR

%description -n ptxinfo
lib%{name} information utility

%package -n lib%{name}%{soname}
Summary: %{name} library
Group: System/Libraries
Provides: lib%{name} = %EVR
Conflicts: libPtex2 < %EVR
Obsoletes: libPtex2 < %EVR

%description -n lib%{name}%{soname}
Ptex is a texture mapping system developed by
Walt Disney Animation Studios for production-quality rendering.

%package docs
Summary: Ptex documentation
Group: Documentation
Requires: lib%{name}-devel = %EVR
BuildArch: noarch

%description docs
Documentation for Ptex

%package -n lib%{name}-devel
Summary: Ptex headers and libraries
Group: Development/C++
Requires: lib%{name}%{soname} = %EVR

%description -n lib%{name}-devel
Development headers and static libraries for %{name}

%prep
%setup
%patch -p1

%build
export FLAVOR=profile
%cmake \
  -DCMAKE_INSTALL_LIBDIR=%_libdir \
  -DPTEX_SHA=%{git} \
  -DPTEX_VER=v%{version} \
%if_disabled static
  -DPTEX_BUILD_STATIC_LIBS=OFF \
%endif
%nil
%cmake_build

%if_enabled test
%check
%ctest
%endif

%install
%cmake_install

%files -n ptxinfo
%_bindir/ptxinfo

%files -n lib%{name}%{soname}
%doc LICENSE README.md
%_libdir/lib%{name}.so.%soname

%files docs
%_defaultdocdir/%name

%files -n lib%{name}-devel
%_includedir/*.h
%_libdir/cmake/%{name}
%_libdir/lib%{name}.so
%_pkgconfigdir/ptex.pc

%changelog
* Mon Apr 20 2026 L.A. Kostis <lakostis@altlinux.ru> 2.5.2-alt1
- 2.5.2.

* Thu Jan 22 2026 Anton Farygin <rider@altlinux.org> 2.5.1-alt1
- 2.4.3 -> 2.5.1

* Sun Jul 21 2024 Anton Farygin <rider@altlinux.ru> 2.4.3-alt1
- update to 2.4.3
- libPtex2 was renamed according shared libs policy

* Wed Nov 15 2023 L.A. Kostis <lakostis@altlinux.ru> 2.4.2-alt0.1.gea6890e
- Initial build for ALTLinux.
