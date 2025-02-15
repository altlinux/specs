Name: simpleini
Version: 4.22
Release: alt2

Summary: Cross-platform C++ library to read and write INI-style configuration files
License: MIT
Group: System/Libraries

Url: https://github.com/brofield/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

BuildArch: noarch

# https://github.com/brofield/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

# https://github.com/brofield/simpleini/pull/76
Patch0: %name-4.22-change-defult-conversion.patch

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
%patch0 -p1

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
* Sat Feb 15 2025 Nazarov Denis <nenderus@altlinux.org> 4.22-alt2
- Add patch to change default conversion method to SI_NO_CONVERSION (ALT #53077)

* Wed Mar 06 2024 Nazarov Denis <nenderus@altlinux.org> 4.22-alt1
- Initial build for ALT Linux
