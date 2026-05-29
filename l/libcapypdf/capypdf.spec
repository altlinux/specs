%def_disable snapshot

%define _name capypdf
%define api_ver 0

%def_enable devtools
# Rendered image is different
%def_disable check

Name: lib%_name
Version: 0.21.0
Release: alt1

Summary: CapyPDF is a library for generating PDF files
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/jpakkane/capypdf

Vcs: https://github.com/jpakkane/capypdf.git

%if_disabled snapshot
Source: %url/releases/download/%version/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson >= 1.5.1 gcc-c++
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libtiff-4)
%{?_enable_devtools:BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(gtk4)}
%{?_enable_check:BuildRequires: python3(PIL) /usr/bin/clang-format
BuildRequires:fonts-ttf-google-noto-serif fonts-ttf-google-noto-sans
BuildRequires: ghostscript-common}

%description
CapyPDF is a library for generating PDF files. It aims to be very low
level. It does not have its own document model, it merely exposes PDF
primitives directly.

%package devel
Summary: development files for CapyPDF
Group: Development/C++
Requires: %name = %EVR

%description devel
CapyPDF development files.

%package -n python3-module-%_name
Summary: CapyPDF Python3 module
Group: Development/Python3
BuildArch: noarch

%description -n python3-module-%_name
This package provides Python3 bindings for CapyPDF library.

%prep
%setup -n %_name-%version
sed -i 's|truetype\/noto|ttf/google-noto|' test/%{_name}tests.py

# https://bugzilla.altlinux.org/48030
%define gs_ver 10.06.0
sed -i 's|/usr/share/color/icc/ghostscript/a98.icc|/usr/share/ghostscript/%gs_ver/iccprofiles/a98.icc|' test/capypdftests.py

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%doc readme.md

%files devel
%_includedir/%_name-%api_ver
%_libdir/%name.so
%_pkgconfigdir/%_name.pc

%files -n python3-module-%_name
%python3_sitelibdir_noarch/%_name.py
%python3_sitelibdir_noarch/__pycache__/*


%changelog
* Fri May 29 2026 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Sun Feb 08 2026 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Sun Jan 18 2026 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Mon Oct 27 2025 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Tue Oct 08 2024 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0

* Thu Mar 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.9.0-alt1
- 0.9.0

* Wed Jan 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.8.0-alt1
- 0.8.0

* Tue Dec 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Oct 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

