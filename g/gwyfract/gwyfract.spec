Name: gwyfract
Url: http://gwyddion.net/apps/gwyfract.php
Version: 0.8
Release: alt1
License: GPL
Packager: Boris Savelev <boris@altlinux.org>

Source: %name-%version.tar.bz2
Group: Sciences/Other
Summary: simple Mandelbrot set outside renderer

# Automatically added by buildreq on Fri Jul 03 2009
BuildRequires: libgmp-devel libgwyddion-devel

%description
gwyfract is a simple Mandelbrot set outside renderer.
It uses Gwyddion libraries for false color 2D data display, selections and some infrastructure.
Despite being a toy renderer, it has a few cool features:
    * smooth true-color set outside visualization based on renormalized inifinity limit (the math)
    * deep zoom, using GNU MP library for arbitrary precision math
    * multithreaded, with the number of calculation threads automatically adjusted to the number of available processor cores
    * false colours based on your favourite Gwyddion palettes
    * image ehnancement via unfair antialiasing
    * several iteration count to false colour mapping modes, including Gwyddion's adaptive mapping

%prep
%setup

%build
%configure
%make_build

%install
%makeinstall_std

%files
%doc README
%_bindir/%name

%changelog
* Fri Jul 03 2009 Boris Savelev <boris@altlinux.org> 0.8-alt1
- initial build for Sisyphus

