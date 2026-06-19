%define _unpackaged_files_terminate_build 1
%define sover 0.48

Name: cpp-httplib
Version: 0.48.0
Release: alt1

Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
License: MIT
Group: System/Libraries

Url: https://github.com/yhirose/%name
Vcs: https://github.com/yhirose/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/yhirose/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: libssl-devel
BuildRequires: python3
BuildRequires: zlib-devel

%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%package -n lib%name%sover
Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
Group: System/Libraries

%description -n lib%name%sover
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C++

%description -n lib%name-devel
Header files for lib%name

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DHTTPLIB_COMPILE:BOOL=TRUE
%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_datadir/{doc,licenses}

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_libdir/cmake/httplib
%_libdir/lib%name.so
%_includedir/httplib.h

%changelog
* Fri Jun 19 2026 Nazarov Denis <nenderus@altlinux.org> 0.48.0-alt1
- New version 0.48.0.

* Sat Jun 13 2026 Nazarov Denis <nenderus@altlinux.org> 0.47.0-alt1
- New version 0.47.0.

* Thu Jun 04 2026 Nazarov Denis <nenderus@altlinux.org> 0.46.1-alt1
- New version 0.46.1.

* Tue May 26 2026 Nazarov Denis <nenderus@altlinux.org> 0.46.0-alt1
- New version 0.46.0.

* Sun May 17 2026 Nazarov Denis <nenderus@altlinux.org> 0.45.0-alt1
- New version 0.45.0.

* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.44.0-alt1
- New version 0.44.0.

* Sun May 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.43.4-alt1
- New version 0.43.4.

* Sun Apr 12 2026 Nazarov Denis <nenderus@altlinux.org> 0.42.0-alt1
- New version 0.42.0.

* Sat Mar 28 2026 Nazarov Denis <nenderus@altlinux.org> 0.40.0-alt1
- New version 0.40.0.

* Wed Mar 25 2026 Nazarov Denis <nenderus@altlinux.org> 0.39.0-alt1
- New version 0.39.0.

* Sun Mar 15 2026 Nazarov Denis <nenderus@altlinux.org> 0.38.0-alt1
- New version 0.38.0.

* Fri Mar 13 2026 Nazarov Denis <nenderus@altlinux.org> 0.37.2-alt1
- New version 0.37.2.

* Tue Mar 10 2026 Nazarov Denis <nenderus@altlinux.org> 0.37.1-alt1
- New version 0.37.1.

* Sun Mar 08 2026 Nazarov Denis <nenderus@altlinux.org> 0.37.0-alt1
- New version 0.37.0.

* Tue Mar 03 2026 Nazarov Denis <nenderus@altlinux.org> 0.36.0-alt1
- New version 0.36.0.

* Sun Mar 01 2026 Nazarov Denis <nenderus@altlinux.org> 0.35.0-alt1
- New version 0.35.0.

* Mon Feb 02 2026 Nazarov Denis <nenderus@altlinux.org> 0.30.2-alt1
- New version 0.30.2.

* Sun Jan 11 2026 Nazarov Denis <nenderus@altlinux.org> 0.30.1-alt1
- New version 0.30.1.

* Fri Jan 02 2026 Nazarov Denis <nenderus@altlinux.org> 0.30.0-alt1
- New version 0.30.0.

* Tue Dec 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.29.0-alt1
- New version 0.29.0.

* Thu Nov 27 2025 Nazarov Denis <nenderus@altlinux.org> 0.28.0-alt1
- New version 0.28.0.

* Tue Oct 28 2025 Nazarov Denis <nenderus@altlinux.org> 0.27.0-alt1
- New version 0.27.0.

* Sat Aug 30 2025 Nazarov Denis <nenderus@altlinux.org> 0.26.0-alt1
- New version 0.26.0.

* Sat Aug 09 2025 Kirill Sharov <sheriffkorov@altlinux.org> 0.25.0-alt2
- Include i586 arch.

* Fri Aug 08 2025 Nazarov Denis <nenderus@altlinux.org> 0.25.0-alt1
- New version 0.25.0.

* Wed Jul 30 2025 Nazarov Denis <nenderus@altlinux.org> 0.24.0-alt1
- New version 0.24.0.

* Fri Jul 18 2025 Nazarov Denis <nenderus@altlinux.org> 0.23.1-alt1
- New version 0.23.1.

* Thu Jul 10 2025 Nazarov Denis <nenderus@altlinux.org> 0.23.0-alt1
- New version 0.23.0.

* Tue Jul 01 2025 Nazarov Denis <nenderus@altlinux.org> 0.22.0-alt1
- New version 0.22.0.

* Tue Jun 10 2025 Nazarov Denis <nenderus@altlinux.org> 0.21.0-alt1
- New version 0.21.0.

* Sun May 04 2025 Nazarov Denis <nenderus@altlinux.org> 0.20.1-alt1
- New version 0.20.1.

* Sun Mar 23 2025 Nazarov Denis <nenderus@altlinux.org> 0.20.0-alt1
- New version 0.20.0.

* Sat Feb 15 2025 Nazarov Denis <nenderus@altlinux.org> 0.19.0-alt1
- New version 0.19.0.

* Sun Feb 09 2025 Nazarov Denis <nenderus@altlinux.org> 0.18.7-alt1
- New version 0.18.7.

* Fri Feb 07 2025 Nazarov Denis <nenderus@altlinux.org> 0.18.6-alt1
- New version 0.18.6.

* Fri Jan 17 2025 Nazarov Denis <nenderus@altlinux.org> 0.18.4-alt1
- New version 0.18.4.

* Mon Dec 09 2024 Nazarov Denis <nenderus@altlinux.org> 0.18.3-alt1
- New version 0.18.3.

* Sat Oct 19 2024 Nazarov Denis <nenderus@altlinux.org> 0.18.1-alt1
- New version 0.18.1.

* Sat Jun 10 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.6-alt1
- New version 0.12.6.

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.5-alt1
- Initial build for ALT Linux
