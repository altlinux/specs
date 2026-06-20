%global mfx_ver_major 2
%global mfx_ver_minor 16
%def_without devel

Name: onevpl-intel-gpu
Version: 26.2.2
Release: alt1
Group: System/Configuration/Hardware
Summary: Intel oneVPL GPU Runtime
License: MIT
Url: https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
VCS: https://github.com/oneapi-src/oneVPL-intel-gpu
ExclusiveArch: x86_64
Source0: %name-%version.tar
BuildRequires(pre):rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libvpl-devel
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libva)
Requires: libvpl2

%description
Intel oneVPL GPU Runtime is a Runtime implementation of oneVPL API for Intel Gen
GPUs. Runtime provides access to hardware-accelerated video decode, encode and
filtering.

%if_with devel
%package -n libmfx-gen-devel
Group: System/Configuration/Hardware
Summary: Development files for %name
Requires: %name = %EVR

%description -n libmfx-gen-devel
The %name-devel package contains libraries and header files for
developing applications that use %name.
%endif

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md CONTRIBUTING.md
%_libdir/libmfx-gen.so.1.%mfx_ver_major
%_libdir/libmfx-gen.so.1.%mfx_ver_major.%mfx_ver_minor
%dir %_libdir/libmfx-gen
%_libdir/libmfx-gen/enctools.so

%if_with devel
%files -n libmfx-gen-devel
%_libdir/libmfx-gen.so
%_libdir/pkgconfig/libmfx-gen.pc
%endif

%changelog
* Sat Jun 20 2026 Anton Farygin <rider@altlinux.org> 26.2.2-alt1
- 26.1.4 -> 26.2.2

* Sat Mar 21 2026 Anton Farygin <rider@altlinux.org> 26.1.4-alt1
- 26.1.1 -> 26.1.4

* Sun Feb 01 2026 Anton Farygin <rider@altlinux.org> 26.1.1-alt1
- 25.4.5 -> 26.1.1

* Mon Dec 22 2025 Anton Farygin <rider@altlinux.org> 25.4.5-alt1
- 25.3.4 -> 25.4.5

* Sun Sep 14 2025 Anton Farygin <rider@altlinux.com> 25.3.4-alt1
- 25.3.1 -> 25.3.4

* Sat Aug 02 2025 Anton Farygin <rider@altlinux.com> 25.3.1-alt1
- 25.3.1

* Thu Mar 20 2025 Anton Farygin <rider@altlinux.ru> 25.1.4-alt1
- 25.1.4

* Sat Mar 30 2024 Anton Farygin <rider@altlinux.ru> 24.2.0-alt1
- 24.2.0

* Sun Feb 25 2024 Anton Farygin <rider@altlinux.ru> 24.1.3-alt1
- first build for ALT
