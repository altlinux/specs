Name: delaboratory
Version: 0.7
Release: alt1

Summary: %name photo processor
Group: Graphics
License: GPLv3+
Url: http://code.google.com/p/%name/

Source: http://%name.googlecode.com/files/%name-%version.tar.gz
Patch: %name-0.7-alt-makefile.patch

BuildRequires: gcc-c++ libtiff-devel libwxGTK-devel libxml2-devel

%description
delaboratory is a color correction utility, it allows to modify
color/contrast of photo in a creative way - using curves, mixer and
blending in different colorspaces (RGB/BW, XYZ/LAB, CMY/CMYK, HSL/HSV)
with floating-point precision, each operation is stored as an adjustment
layer and you can watch a realtime preview.

delaboratory should be used in the middle of the workflow - after RAW
processing, before final retouch.

%prep
%setup -q
%patch

%build
%make_build

%install
%make BINDIR=%_bindir DESTDIR=%buildroot install

%files
%_bindir/%name
%doc README

%changelog
* Tue May 29 2012 Yuri N. Sedunov <aris@altlinux.org> 0.7-alt1
- 0.7

* Tue Nov 01 2011 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Thu Sep 22 2011 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4

* Thu Aug 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.3-alt1
- 0.3

* Sat Jun 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first build for Sisyphus



