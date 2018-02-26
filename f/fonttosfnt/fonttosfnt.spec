Name: fonttosfnt
Version: 1.0.4
Release: alt2
Summary: Wrap a bitmap font in a sfnt (TrueType) wrapper
Group: System/X11
Url: http://cgit.freedesktop.org/xorg/app/fonttosfnt
Source: http://xorg.freedesktop.org/releases/individual/app/%name-%version.tar.bz2
Patch1: fonttosfnt-1.0.1-freetype_fix.patch
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Tue May 18 2010
BuildRequires: libfontenc-devel libfreetype-devel xorg-xproto-devel

BuildRequires: xorg-util-macros

%description
Fonttosfnt wraps a bitmap font in a sfnt (TrueType or OpenType) wrapper.

%prep
%setup -q -n %name-%version
%patch1 -p0 -b .freetype_fix

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%changelog
* Tue Apr 26 2011 Fr. Br. George <george@altlinux.ru> 1.0.4-alt2
- Fix build

* Tue May 18 2010 Fr. Br. George <george@altlinux.ru> 1.0.4-alt1
- Version up

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV

* Thu Aug 24 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-08-24 16:02:02 (57866)
- fixed the group

* Thu Aug 24 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-08-24 15:31:02 (57854)
- added a patch fixing compilation with newer freetype versions
  (thanks Stefan van der Eijk for the patch)

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:23:09 (27459)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
