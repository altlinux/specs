%define _unpackaged_files_terminate_build 1

Name: log4qt
Version: 1.5.1
Release: alt2

Summary: Logging for the Qt cross-platform application framework.
License: Apache-2.0
Group: Development/Tools

Url: https://github.com/MEONMedical/Log4Qt
VCS: https://github.com/MEONMedical/Log4Qt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel

%define soversion 1.5
%define libname liblog4qt%soversion

%description
Log4Qt is a C++ port of the Apache Software Foundation Log4j
package using the Qt Framework.
It is intended to be used by open source and commercial Qt projects.

%package -n %libname
Group: System/Libraries
Summary: %name library

%description -n %libname
Log4Qt is a C++ port of the Apache Software Foundation Log4j
package using the Qt Framework.
It is intended to be used by open source and commercial Qt projects.

%package -n lib%name-devel
Summary: Logging for the Qt cross-platform application framework.
Group: Development/Tools

%description -n lib%name-devel
Log4Qt is a C++ port of the Apache Software Foundation Log4j
package using the Qt Framework.

This package contains development files for qRestAPI.

%prep
%setup
%ifarch %e2k
# unsupported as of lcc 1.27.14
sed -i 's,-Wsuggest-final-types -Wsuggest-final-methods,,' CMakeLists.txt
%endif

%build
%cmake
%cmake_build

%install
%cmake_install

%files -n %libname
%doc Readme.md LICENSE
%_libdir/liblog4qt.so.%soversion
%_libdir/liblog4qt.so.*

%files -n lib%name-devel
%doc Readme.md LICENSE
%_libdir/lib*.so
%_includedir/%name/*
%_libdir/cmake/Log4Qt/

%changelog
* Sun Mar 03 2024 Michael Shigorin <mike@altlinux.org> 1.5.1-alt2
- E2K: avoid lcc-unsupported options (mcst#8726).
- Minor spec cleanup.

* Mon Nov 20 2023 Elizaveta Morozova <morozovaes@altlinux.org> 1.5.1-alt1
- Initial build for ALT.

