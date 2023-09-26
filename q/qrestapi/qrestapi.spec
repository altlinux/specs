%define _unpackaged_files_terminate_build 1

Name: qrestapi
Version: 0
Release: alt2.git.ea5e85a
Summary: Simple Qt library allowing to synchronously or asynchronously query a REST server
License: Apache-2.0
Group: Development/C++
Url: https://github.com/commontk/qRestAPI

# https://github.com/commontk/qRestAPI.git
Source: %name-%version.tar

Patch1: qrestapi-alt-install.patch
Patch2: qrestapi-alt-include-dirs.patch

BuildRequires: gcc-c++ cmake
BuildRequires: qt5-base-devel qt5-script-devel

%description
qRestAPI is a cross-platform Qt-based library allowing
to easily query any RESTful web services.

%package -n lib%name
Summary: Simple Qt library allowing to synchronously or asynchronously query a REST server
Group: System/Libraries

%description -n lib%name
qRestAPI is a cross-platform Qt-based library allowing to easily query any RESTful web services.

This package contains qRestAPI shared libraries.

%package -n lib%name-devel
Summary: Simple Qt library allowing to synchronously or asynchronously query a REST server
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
qRestAPI is a cross-platform Qt-based library allowing to easily query any RESTful web services.

This package contains development files for qRestAPI.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%cmake \
	-DBUILD_TESTING:BOOL=OFF \
	-DqRestAPI_QT_VERSION=5 \
	%nil

%cmake_build

%install
%cmakeinstall_std

%files -n lib%name
%doc LICENSE
%doc README.md
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/qRestAPI

%changelog
* Wed Jun 07 2023 Elizaveta Morozova <morozovaes@altlinux.org> 0-alt2.git.ea5e85a
- Built from ea5e85a1ecfb05174ab604d66fa3186ae9a45eda.
- Built on armh.

* Mon May 17 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0-alt1.git.ddc0cfc
- Initial build for ALT.
