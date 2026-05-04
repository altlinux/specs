%def_disable snapshot
%define _name editorconfig
%define srcname %_name-core-c
%def_enable docs
%def_disable static
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_disable check

Name: %_name
Version: 0.12.11
Release: alt1

Summary: Parser for EditorConfig files written in C
Group: Development/Other
License: BSD-2-Clause
Url: https://editorconfig.org

Vcs: https://github.com/editorconfig/editorconfig-core-c.git

%if_disabled snapshot
Source: https://github.com/%name/%srcname/archive/v%version/%srcname-%version.tar.gz
%else
Source: %srcname-%version.tar
%endif
Patch: %srcname-0.12.5-alt-static_build.patch

Requires: lib%name = %EVR

BuildRequires(pre): cmake >= 3.5.1
BuildRequires: gcc-c++ libpcre2-devel
%{?_enable_docs:BuildRequires: doxygen}

%description
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

%package -n lib%name
Summary: EditorConfig shared library
Group: System/Libraries

%description -n lib%name
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

This package contains shared EditorConfig library.

%package -n lib%name-devel
Summary: Development files for EditorConfig library
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
EditorConfig makes it easy to maintain the correct coding style when
switching between different text editors and between different projects.
The EditorConfig project maintains a file format and plugins for various
text editors which allow this file format to be read and used by those
editors.

This package contains files needed for development EditorConfig plugins.

%prep
%setup -n %srcname-%version
%patch -b .static

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake %{?_disable_docs:-DBUILD_DOCUMENTATION=OFF} \
    %{?_disable_static:-DBUILD_STATIC_LIBS=OFF}
%nil
%cmake_build

%install
%cmakeinstall_std

%check
%cmake_build -t tests

%files
%_bindir/%_name
%_bindir/%_name-%version
%{?_enable_docs:%_man1dir/%_name.1.*}
%{?_enable_docs:%_man5dir/%{_name}*}
%doc CHANGELOG README.md LICENSE

%files -n lib%name
%_libdir/lib%_name.so.0*
%{?_enable_static:%exclude %_libdir/*.a}

%files -n lib%name-devel
%_includedir/%_name/
%_libdir/lib%_name.so
%_libdir/cmake/EditorConfig/
%_pkgconfigdir/%_name.pc
%{?_enable_docs:%_man3dir/%{_name}*
%doc %_cmake__builddir/doc/html}

%changelog
* Sun May 03 2026 Yuri N. Sedunov <aris@altlinux.org> 0.12.11-alt1
- 0.12.11

* Sun Jun 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.12.10-alt0.1
- updated to v0.12.9-13-gc8e2d77

* Thu Jun 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.8-alt1
- 0.12.8

* Sun Mar 31 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.7-alt1
- 0.12.7

* Sat Jan 21 2023 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Fri Aug 27 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1.1
- disabled static build

* Sun Jun 20 2021 Yuri N. Sedunov <aris@altlinux.org> 0.12.5-alt1
- 0.12.5

* Sun Aug 30 2020 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4
- fixed License tag

* Thu Jun 13 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1.1
- fixed build if "docs" disabled

* Thu Jan 03 2019 Yuri N. Sedunov <aris@altlinux.org> 0.12.3-alt1
- first build for Sisyphus

