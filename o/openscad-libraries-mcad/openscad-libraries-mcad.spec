Name: openscad-libraries-mcad
Version: 0.1
Release: alt1.git20141104

Summary: MCAD is a library of useful functions for OpenSCAD.
Packager: Dmitry Derjavin <dd@altlinux.org> 
License: LGPL
Group: Engineering
Url: https://github.com/SolidCode/MCAD

Source: %name-%version.tar

BuildArch: noarch

%define openscad_libdir %_datadir/openscad/libraries
%define mcaddir %openscad_libdir/MCAD

Requires: %openscad_libdir

%description
This library contains components commonly used in designing and
mocking up mechanical designs.

%prep
%setup

%install
mkdir -p -m755 %buildroot%mcaddir
cp -a *.py *.scad bitmap %buildroot%mcaddir

%files
%doc README.markdown
%mcaddir

%changelog
* Tue Dec 23 2014 Dmitry Derjavin <dd@altlinux.org> 0.1-alt1.git20141104
- Initial ALT Linux build.
