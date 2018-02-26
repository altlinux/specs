Name: sozi
Version: 11.10.a
Release: alt1

Summary: Makes SVG animated presentations that can be played in a browser

Group: Graphics
License: GPLv3+
Url: http://sozi.baierouge.fr/
Packager: Paul Wolneykien <manowar@altlinux.ru>

Source: %name-%version.tar

# Require Inkscape instead of 'inkex' module
%define _python_req_skip inkex
Requires: inkscape

BuildRequires: cmake
# FIXME: cmake requires a C++ compiler
BuildRequires: gcc-c++

BuildArch: noarch

%define inkscape_dir %_datadir/inkscape
%define inkscape_extensions_dir %inkscape_dir/extensions

%description
Sozi is a small program that can create and play animated presentations.

Unlike in most presentation applications, a Sozi document is not
organised as a slideshow, but rather as a poster where the content of
your presentation can be freely laid out. Playing such a presentation
consists in a series of translations, zooms and rotations that allow to
focus on the elements you want to show.

Sozi is based on open standards. It is free software distributed
according to the terms of the GPL 3.0.

%prep
%setup

%build
cmake -DCMAKE_INSTALL_PREFIX=%buildroot%_usr \
      -Dinkscape_path=%buildroot%inkscape_dir \
      -Dminifier_type=sed
%make_build

%install
%makeinstall

%files
%_includedir/*
%inkscape_extensions_dir/*
%_datadir/%name
%doc README samples

%changelog
* Tue Nov 15 2011 Paul Wolneykien <manowar@altlinux.ru> 11.10.a-alt1
- Initial release for ALT Linux.
