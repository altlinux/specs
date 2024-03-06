Name: simpleini
Version: 4.22
Release: alt1

Summary: Cross-platform C++ library to read and write INI-style configuration files
License: MIT
Group: System/Libraries

Url: https://github.com/brofield/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

BuildArch: noarch

# https://github.com/brofield/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: libgtest-devel

%description
%name is a cross-platform library that provides a simple API to read and
write INI-style configuration files. It supports data files in ASCII, MBCS and
Unicode. It is designed explicitly to be portable to any platform and has been
tested on Windows, WinCE and Linux. Released as open-source and free using the
MIT licence.

%package -n lib%name-devel
Summary: Cross-platform C++ library to read and write INI-style configuration files
Group: Development/C

%description -n lib%name-devel
%name is a cross-platform library that provides a simple API to read and
write INI-style configuration files. It supports data files in ASCII, MBCS and
Unicode. It is designed explicitly to be portable to any platform and has been
tested on Windows, WinCE and Linux. Released as open-source and free using the
MIT licence.

%prep
%setup

%build
%cmake -DSIMPLEINI_USE_SYSTEM_GTEST:BOOL=TRUE
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name-devel
%doc README.md
%_includedir/SimpleIni
%_datadir/cmake/SimpleIni

%changelog
* Wed Mar 06 2024 Nazarov Denis <nenderus@altlinux.org> 4.22-alt1
- Initial build for ALT Linux
