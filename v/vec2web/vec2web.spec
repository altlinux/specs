Name: vec2web
Version: 2.0.4.7
Release: alt4

Summary: Converter from DXF to other image formats
License: GPL
Group: Graphics
Url: http://www.ribbonsoft.com/vec2web.html

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-%version.tar.bz2
Patch0: vec2web-2.0.4.7-alt-build.patch
Patch1: vec2web-2.0.4.7-alt-compile-fix.patch

BuildPreReq: gcc-c++
BuildRequires(pre): libqt3-devel

%description
vec2web is a command line utility for QCad users who are trying to
automate format conversions. vec2web is based on the same technology as
QCad.
vec2web reads drawings in DXF format and outputs bitmaps and some other
formats: BMP, GIF, JPEG, PNG, XPM, XBM, PBM, PGM, PPM, Postscript and
DXML. vec2web can also be used to directly print a drawing to the
default printer.

%prep
%setup
%patch0 -p1
%patch1 -p1
%__subst 's, debug , ,' %name/src/%name.pro

%build
export PATH=$PATH:%_qt3dir/bin
pushd dxflib
%configure
%make_build
popd
pushd qcadlib
%make_build
popd
pushd %name
%make_build
popd

%install
install -pD -m755 %name/%name %buildroot%_bindir/%name

%files
%_bindir/*

%changelog
* Wed Oct 29 2008 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.4.7-alt4
- fix build

* Thu Aug 23 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.4.7-alt3
- Sisyphus build

* Thu Jul 19 2007 Dmitry V. Levin <ldv@altlinux.org> 2.0.4.7-alt2
- Fixed 64-bit arch support.

* Mon May 14 2007 Andrey Rahmatullin <wrar@altlinux.ru> 2.0.4.7-alt1
- initial build
