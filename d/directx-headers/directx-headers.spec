%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%def_disable test

Name: directx-headers
Version: 1.619.1
Release: alt1

Summary: Official DirectX headers available under an open source license
Group: Development/C++
License: MIT

URL: https://github.com/microsoft/DirectX-Headers
Packager: L.A. Kostis <lakostis@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: gcc-c++ dos2unix

%description
This package provides the official Direct3D 12 headers. These headers are made
available under the MIT license rather than the traditional Windows SDK
license.

Additionally, this package provides several helpers for using these headers.

%prep
%setup -n %name-%version
# better to be safe
find . -type f -exec dos2unix {} \;

%build
%meson \
%if_disabled test
 -D build-test=false
%else
 %nil
%endif
%meson_build -v

%install
%meson_install

%files
%doc *.md LICENSE
%_includedir/composition
%_includedir/directx
%_includedir/dxguids
%_includedir/wsl
%_libdir/*.a
%_pkgconfigdir/*.pc

%changelog
* Tue Apr 21 2026 L.A. Kostis <lakostis@altlinux.ru> 1.619.1-alt1
- Update to 1.619.1.

* Tue Mar 03 2026 L.A. Kostis <lakostis@altlinux.ru> 1.619.0-alt1
- Update to 1.619.0.

* Thu Oct 23 2025 L.A. Kostis <lakostis@altlinux.ru> 1.618.2-alt1
- Update to 1.618.2.

* Fri Jun 27 2025 L.A. Kostis <lakostis@altlinux.ru> 1.616.0-alt1
- Update to 1.616.0.

* Tue Feb 25 2025 L.A. Kostis <lakostis@altlinux.ru> 1.615.0-alt1
- Update to 1.615.0.

* Sun Nov 24 2024 L.A. Kostis <lakostis@altlinux.ru> 1.614.1-alt1
- Update to 1.614.1.

* Thu Aug 08 2024 L.A. Kostis <lakostis@altlinux.ru> 1.614.0-alt1
- Updated to 1.614.0.

* Thu May 16 2024 L.A. Kostis <lakostis@altlinux.ru> 1.613.1-alt1
- Updated to 1.613.1.

* Sat Jan 13 2024 L.A. Kostis <lakostis@altlinux.ru> 1.611.0-alt1
- Updated to 1.611.0.

* Fri May 12 2023 L.A. Kostis <lakostis@altlinux.ru> 1.610.2-alt1
- Updated to v1.610.2.

* Sun Apr 16 2023 L.A. Kostis <lakostis@altlinux.ru> 1.610.0-alt1
- Updated to v1.610.0.

* Tue Mar 21 2023 L.A. Kostis <lakostis@altlinux.ru> 1.608.2-alt1.b
- Updated to v1.608.2b.

* Fri Feb 24 2023 L.A. Kostis <lakostis@altlinux.ru> 1.608.2-alt1
- Initial build for ALTLinux.
