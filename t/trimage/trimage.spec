Name: trimage
Version: 1.0.5
Release: alt1
License: MIT
Summary: Tool for Losslessly Optimizing PNG and JPEG Files
Url: http://trimage.org/
Group: Graphics
Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar
BuildRequires: python-devel python-module-setuptools
Requires: advancecomp
Requires: jpegoptim
Requires: optipng
Requires: pngcrush
Requires: python-module-PyQt4
Requires: icon-theme-hicolor
BuildArch: noarch

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
%python_build

%install
%python_install
%__subst 's|#!/bin|#!/usr/bin|' %buildroot%_bindir/*

%files
%doc COPYING README resources/todo
%_bindir/*
%python_sitelibdir/*
%_mandir/man?/*
%_desktopdir/trimage.desktop
%_iconsdir/hicolor/scalable/apps/trimage.svg

%changelog
* Fri Aug 26 2016 Anton Midyukov <antohami@altlinux.org> 1.0.5-alt1
- Initial build for ALT Linux Sisyphus (Closes: 32411).
