%def_enable docs
%def_disable static
%{?_enable_static:%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}}
%def_disable check

Name: editorconfig
Version: 0.12.8
Release: alt1

Summary: Parser for EditorConfig files written in C
Group: Development/Other
License: BSD-2-Clause
Url: https://editorconfig.org

%define srcname %name-core-c
Vcs: https://github.com/%name/%srcname
Source: https://github.com/%name/%srcname/archive/v%version/%srcname-%version.tar.gz
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
%_bindir/%name
%_bindir/%name-%version
%{?_enable_docs:%_man1dir/%name.1.*}
%{?_enable_docs:%_man5dir/%{name}*}
%doc CHANGELOG README.md LICENSE

%files -n lib%name
%_libdir/lib%name.so.0*
%{?_enable_static:%exclude %_libdir/*.a}

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_libdir/cmake/EditorConfig/
%_pkgconfigdir/%name.pc
%{?_enable_docs:%_man3dir/%{name}*
%doc %_cmake__builddir/doc/html}

%changelog
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

