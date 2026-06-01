%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: nelson
Version: 1.17.0
Release: alt2

Summary: The Nelson Programming Language
License: LGPL-3.0 OR GPL-3.0
Group: Sciences/Mathematics
Url: https://nelson-lang.github.io/nelson-website/
Vcs: https://github.com/nelson-lang/nelson

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-python3

BuildRequires: gcc-c++
BuildRequires: pkgconfig(eigen3)
BuildRequires: pkgconfig(Qt6)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6Quick)
BuildRequires: pkgconfig(libffi)
BuildRequires: libgif-devel
BuildRequires: libtiff-devel
BuildRequires: boost-devel
BuildRequires: boost-filesystem-devel
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(openblas)
BuildRequires: pkgconfig(lapack)
BuildRequires: pkgconfig(hdf5)
BuildRequires: libgomp-devel
BuildRequires: openmpi-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: libgit2-devel
BuildRequires: pkgconfig(taglib)
BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(jack)
BuildRequires: pkgconfig(portaudio-2.0)
BuildRequires: pkgconfig(matio)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpcre2-32)
BuildRequires: pkgconfig(sndfile)
BuildRequires: boost-interprocess-devel
BuildRequires: boost-asio-devel
BuildRequires: patchelf

Requires: nelson-common

# no liblapacke-devel on loongson
ExcludeArch: loongarch64

%description
Nelson is a powerful, open-source numerical computational language,
developed to provide a comprehensive and intuitive environment for
engineers, scientists, and students. With over 1,200 built-in functions,
Nelson supports a wide range of tasks, from basic algebra to advanced
numerical simulations.

Originally inspired by languages like MATLAB and GNU Octave, Nelson
offers users a lightweight yet feature-rich experience. It is designed
to be easy to learn and use, with an emphasis on performance and
flexibility.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Nelson is a powerful, open-source numerical computational language,
developed to provide a comprehensive and intuitive environment for
engineers, scientists, and students. With over 1,200 built-in functions,
Nelson supports a wide range of tasks, from basic algebra to advanced
numerical simulations.

Originally inspired by languages like MATLAB and GNU Octave, Nelson
offers users a lightweight yet feature-rich experience. It is designed
to be easy to learn and use, with an emphasis on performance and
flexibility.

This package contains development files for Nelson.

%package common
Summary: Arch-independent files for %name
Group: Development/Other
BuildArch: noarch

%description common
Nelson is a powerful, open-source numerical computational language,
developed to provide a comprehensive and intuitive environment for
engineers, scientists, and students. With over 1,200 built-in functions,
Nelson supports a wide range of tasks, from basic algebra to advanced
numerical simulations.

Originally inspired by languages like MATLAB and GNU Octave, Nelson
offers users a lightweight yet feature-rich experience. It is designed
to be easy to learn and use, with an emphasis on performance and
flexibility.

This package contains arch-independent files of Nelson.

%prep
%setup
%patch -p1
sed -i "s/Categories=.*/Categories=Science;Math;DataVisualization;NumericalAnalysis;/" desktop/io.github.nelson_lang.Nelson.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

patchelf %buildroot%_libdir/Nelson/*.so* --add-rpath %_libdir/Nelson

patchelf %buildroot%_bindir/nelson*-exec --add-rpath %_libdir/Nelson
patchelf %buildroot%_bindir/nelson_f2c --add-rpath %_libdir/Nelson

%files
%_bindir/nelson
%_bindir/nelson-adv-cli
%_bindir/nelson-adv-cli-exec
%_bindir/nelson-cli
%_bindir/nelson-cli-exec
%_bindir/nelson-gui
%_bindir/nelson-gui-exec
%_bindir/nelson-sio-cli
%_bindir/nelson-sio-cli-exec
%_bindir/nelson_f2c
%_desktopdir/io.github.nelson_lang.Nelson.desktop
%dir %_libdir/Nelson
%_libdir/Nelson/*
%_iconsdir/hicolor/*/apps/nelson.png
%_datadir/metainfo/io.github.nelson_lang.Nelson.appdata.xml

%files common
%dir %_datadir/Nelson
%_datadir/Nelson/*

%files devel
%dir %_includedir/Nelson
%_includedir/Nelson/*
%dir %_libdir/cmake/Nelson
%_libdir/cmake/Nelson/*

%changelog
* Mon Jun 01 2026 Nikolay Strelkov <snk@altlinux.org> 1.17.0-alt2
- Exclude loongarch64 as not buildable because of missed liblapacke.
- Move arch-independent files to -common subpackage.
- Applied repocop fix for freedesktop-desktop.

* Sun May 31 2026 Nikolay Strelkov <snk@altlinux.org> 1.17.0-alt1
- Initial build for Sisyphus
