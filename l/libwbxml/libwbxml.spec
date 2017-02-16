%def_with tests

Name:           libwbxml
Version:        0.11.5
Release:        alt1
Summary:        Library and tools to parse, encode and handle WBXML documents
Group:          System/Libraries
License:        LGPLv2+
URL:            https://github.com/%name/%name
Source:         %name-%version.tar

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
%setup -q

%build
%cmake -DENABLE_INSTALL_DOC:BOOL=OFF
%cmake_build

%install
%cmakeinstall_std

%if_with tests
%check
cd BUILD
export LD_LIBRARY_PATH=`pwd`/src:$LD_LIBRARY_PATH
ctest
%endif

%files
%doc BUGS ChangeLog README References THANKS TODO COPYING GNU-LGPL
%_bindir/*
%_libdir/libwbxml2.so.*

%files devel
%_includedir/*
%_libdir/libwbxml2.so
%_pkgconfigdir/libwbxml2.pc
%_datadir/CMake/Modules/FindLibWbxml2.cmake

%changelog
* Thu Feb 16 2017 Andrey Cherepanov <cas@altlinux.org> 0.11.5-alt1
- new version 0.11.5

* Mon Nov 23 2015 Andrey Cherepanov <cas@altlinux.org> 0.11.4-alt1
- Initial build in Sisyphus (thanks Fedora for spec)

