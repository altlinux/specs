Name: trimage
Version: 1.0.6
Release: alt1.1
License: MIT
Summary: Tool for Losslessly Optimizing PNG and JPEG Files
Url: http://trimage.org/
Group: Graphics
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires: python3-devel python3-module-setuptools
Requires: advancecomp
Requires: jpegoptim
Requires: optipng
Requires: pngcrush
Requires: icon-theme-hicolor
BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir/%name

%description
Trimage is a cross-platform GUI and command-line interface to optimize
image files via optipng, pngcrush, advpng and jpegoptim, depending on
the filetype (currently, PNG and JPEG files are supported). It was
inspired by imageoptim. All image files are losslessy compressed on
the highest available compression levels. Trimage gives you various
input functions to fit your own workflow: a regular file dialog,
dragging and dropping and various command line options.

%prep
%setup

%build
%python3_build

%install
%python3_install
%__subst 's|#!/bin|#!/usr/bin|' %buildroot%_bindir/*

%files
%doc COPYING README.md
%_bindir/*
%python3_sitelibdir/*
%_mandir/man?/*
%_desktopdir/trimage.desktop
%_iconsdir/hicolor/scalable/apps/trimage.svg

%changelog
* Sun Nov 13 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.0.6-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Sun Jan 26 2020 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1
- new version 1.0.6
- build with python3

* Fri Aug 26 2016 Anton Midyukov <antohami@altlinux.org> 1.0.5-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32411).
