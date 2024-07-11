%def_with tests

Name:           libwbxml
Version:        0.11.10
Release:        alt1
Summary:        Library and tools to parse, encode and handle WBXML documents
Group:          System/Libraries
License:        LGPLv2+
URL:            https://github.com/%name/%name
Source:         %name-%version.tar
Patch0:         %name-alt-includes-dir.patch

BuildRequires(pre): cmake >= 2.4
BuildRequires:  libcheck-devel
BuildRequires:  libexpat-devel
# Tests:
%if_with tests
BuildRequires:  perl
BuildRequires:  ctest
Obsoletes:      wbxml2 <= 0.9.3
%endif

%description
The WBXML Library (libwbxml) contains a library and its associated tools
to parse, encode and handle WBXML documents. The WBXML format is a
binary representation of XML, defined by the Wap Forum, and used to
reduce bandwidth in mobile communications.

%package devel
Group:         Development/C
Summary:       Development files of %name
Requires:      %name = %version-%release
Provides:      wbxml2-devel = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%cmake -DENABLE_INSTALL_DOC:BOOL=OFF \
       -DCMAKE_INSTALL_LIBDIR=%_libdir
%cmake_build

%install
%cmake_install

%if_with tests
%check
cd %_cmake__builddir
export LD_LIBRARY_PATH=$(pwd)/src:$LD_LIBRARY_PATH
ctest
%endif

%files
%doc BUGS ChangeLog README References THANKS TODO
%_bindir/*
%_libdir/libwbxml2.so.*

%files devel
%_includedir/*
%_libdir/libwbxml2.so
%_pkgconfigdir/libwbxml2.pc
%_libdir/cmake/libwbxml2/*.cmake

%changelog
* Wed Jun 19 2024 Andrey Cherepanov <cas@altlinux.org> 0.11.10-alt1
- New version.

* Sun Jun 09 2024 Andrey Cherepanov <cas@altlinux.org> 0.11.9-alt2
- Packaged includes to /usr/include without subdirectory.

* Sat Jun 08 2024 Andrey Cherepanov <cas@altlinux.org> 0.11.9-alt1
- New version.

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 0.11.8-alt1
- New version.

* Tue Apr 27 2021 Arseny Maslennikov <arseny@altlinux.org> 0.11.7-alt1.1
- NMU: spec: adapted to new cmake macros.

* Thu Apr 16 2020 Andrey Cherepanov <cas@altlinux.org> 0.11.7-alt1
- New version.

* Thu Oct 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.11.6-alt1.1
- NMU: changed CMake Modules install path

* Wed Aug 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.6-alt1
- New version

* Thu Feb 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.5-alt1
- new version 0.11.5

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.11.4-alt1
- Initial build in Sisyphus (thanks Fedora for spec)

