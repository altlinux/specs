Name:    postprocessd
Version: 0.3.0
Release: alt1

Summary: The raw picture to jpg processor
License: GPL-3.0+
Group:   Other
Url:     https://gitlab.com/megapixels-org/postprocessd

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc-c++
BuildRequires: libraw-devel
BuildRequires: libtiff-devel
BuildRequires: libjpeg-devel
BuildRequires: libexif-devel
BuildRequires: libopencv-devel
BuildRequires: scdoc
BuildRequires: libgomp-devel

%description
This is a project that creates a native postprocessing pipeline for Megapixels
that aims to improve the image quality.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%_bindir/postprocess*
%_man1dir/postprocess-single.1*
%_datadir/megapixels/postprocessor.d/postprocessd*

%changelog
* Tue Apr 30 2024 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus.
