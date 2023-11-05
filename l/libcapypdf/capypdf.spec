%def_disable snapshot

%define _name capypdf
%define api_ver 0

%def_enable check

Name: lib%_name
Version: 0.6.0
Release: alt1

Summary: CapyPDF is a library for generating PDF files
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/jpakkane/capypdf

%if_disabled snapshot
Source: %url/releases/download/%version/%_name-%version.tar.xz
%else
Vcs: https://github.com/jpakkane/capypdf.git
Source: %_name-%version.tar
%endif

%define fmt_ver 10.1.1

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(fmt) >= %fmt_ver
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(libtiff-4)
BuildRequires: pkgconfig(gtk4)
%{?_enable_check:BuildRequires: python3(PIL) fonts-ttf-google-noto-serif ghostscript-common}

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
sed -i 's|/usr/share/color/icc/ghostscript/a98.icc|/usr/share/ghostscript/10.01.1/iccprofiles/a98.icc|' test/capypdftests.py

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
* Sun Nov 05 2023 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Mon Oct 16 2023 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- first build for Sisyphus

