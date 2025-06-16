%define _name iniparser
# .so.0 is for version 3.x, .so.1 is 4.x
# since 4.2.2 -- so.4
%define sover 4

%def_enable docs
%def_disable check

Name: lib%_name
Version: 4.2.6
Release: alt1

Group: Development/C
Summary: Simple C library for parsing "INI-style" files
License: MIT
Url: http://ndevilla.free.fr/iniparser/

Vcs: https://github.com/ndevilla/iniparser.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
%{?_enable_docs:BuildRequires: doxygen}
%{?_enable_check:BuildRequires: ctest}

%description
iniParser is an ANSI C library to parse "INI-style" files,
often used to hold application configuration information.

%package -n %name%sover
Summary: Simple C library for parsing "INI-style" files
Group: System/Libraries
Provides: %name = %EVR

%description -n %name%sover
iniParser is an ANSI C library to parse "INI-style" files,
often used to hold application configuration information.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name%sover = %EVR

%description devel
This package contains the header files, development files and
documentation for %_name library.

%prep
%setup
%patch -p1
# fix pc-file
#sed -i 's|\/lib|/%_lib|
#        s|\(-I${includedir}\)|\1/%_name|' %_name.pc

%build
%cmake \
    -DBUILD_STATIC_LIBS=OFF \
    %{?_enable_docs:-DBUILD_DOCS=ON} \
    %{?_enable_check:-DBUILD_TESTS=ON \
    -DBUILD_STATIC_LIBS=ON}
%nil
%cmake_build

%install
%cmake_install
%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir
install -pm644 LICENSE %buildroot%docdir/
%{?_enable_docs:cp -ar %_cmake__builddir/html} %buildroot%docdir/

%check
%cmake_build -t test

%files -n %name%sover
%_libdir/%name.so.%{sover}*
%dir %docdir
%docdir/LICENSE

%files devel
%_libdir/%name.so
%_includedir/%_name/
%_pkgconfigdir/%_name.pc
%_libdir/cmake/%_name/
%{?_enable_docs:%docdir/html
%exclude %_datadir/doc/%_name/}


%changelog
* Mon Jun 16 2025 Yuri N. Sedunov <aris@altlinux.org> 4.2.6-alt1
- 4.2.6 (ported to CMake build system, soname bumped)

* Thu May 16 2024 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Sun Apr 28 2024 Yuri N. Sedunov <aris@altlinux.org> 4.2-alt1
- 4.2
- enabled %%check

* Tue Dec 21 2021 Yuri N. Sedunov <aris@altlinux.org> 4.1-alt1
- updated to v4.1-11-gdeb85ad (bumped soname)
- moved headers to %%_includedir/iniparser
- added .pc file

* Thu Apr 26 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt2
- great spec cleanup thanks to ldv@

* Wed Apr 25 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 3.1-alt1
- initial build

