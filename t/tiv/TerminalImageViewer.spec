# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

Name: tiv
Version: 1.2
Release: alt1
Summary: Terminal Image Viewer
License: Apache-2.0 or GPL-3.0-or-later
Group: Graphics
Url: https://github.com/stefanhaustein/TerminalImageViewer

Source: %name-%version.tar
BuildRequires: gcc-c++
BuildRequires: libGraphicsMagick-c++-devel

%description
tiv is a small C++ program to display images in a (modern) terminal using
RGB ANSI codes and unicode block graphic characters.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
# Compile it the way it does not require to load ImageMagick-tools executable
# to load (almost all) its formats (i.e. convert).
# CImg developers didn't know that GraphicsMagick and ImageMagick are
# different libs, though. https://github.com/GreycLab/CImg/issues/400
%make_build -C src \
	CXXFLAGS="%optflags -D__POSIX_VERSION -Dcimg_use_magick $(pkg-config --cflags GraphicsMagick++)" \
	LDLIBS="$(pkg-config --libs GraphicsMagick++)"

%install
%makeinstall -C src

%check
src/tiv |& grep -Fw v%version
# Warning: failed to determine most reasonable sie: unrecognized system, defaulting to 80x24

%files
%doc LICENSE README.md
%_bindir/tiv

%changelog
* Thu Nov 02 2023 Vitaly Chikunov <vt@altlinux.org> 1.2-alt1
- First import v.1.2-3-gc29bdc7 (2023-10-03).
