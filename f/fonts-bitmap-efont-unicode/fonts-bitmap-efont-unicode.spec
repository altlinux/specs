# spec file for package efont-unicode (Version 0.4.0)
# Copyright (c) 2003 SuSE Linux AG, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
# Please submit bugfixes or comments via http://www.suse.de/feedback/

%define origname efont-unicode

Name: fonts-bitmap-efont-unicode
Version: 0.4.2
Release: alt2

Summary: Unicode fonts collection by /efont/
License: distributable
Group: System/Fonts/X11 bitmap

Url: http://openlab.ring.gr.jp/efont
Source: %url/dist/unicode-bdf/%origname-bdf-%version-src.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
# Automatically added by buildreq on Wed Mar 12 2008
BuildRequires: bdfresize bdftopcf mkfontdir

BuildRequires: rpm-build-fonts >= 0.3
PreReq: chkfontpath

Provides: %origname = %version-%release
Obsoletes: %origname < 0.4.2-alt2

%define fontdir %_bitmapfontsdir/%origname

%description
Unicode fonts developed by /efont/ openlab. This font package includes
12, 14, 16, and 24 pixel ISO-10646 fonts.

Authors:
--------
    Kazuhiko  <kazuhiko/ring.gr.jp>

%prep
%setup -q -n %origname-bdf-%version-src
%configure --with-fontdir=%fontdir

%build
%make
mkfontdir

%install
%bitmap_fonts_install %origname

%post
%post_fonts

%postun
%postun_fonts

%files -f %origname.files
%doc README* COPYRIGHT ChangeLog

%changelog -n efont-unicode
* Wed Mar 12 2008 Michael Shigorin <mike@altlinux.org> 0.4.2-alt2
- renamed and refurbished to conform to fonts policy
  (this is the current upstream version)
- spec cleanup

* Wed May 18 2005 Michael Shigorin <mike@altlinux.ru> 0.4.2-alt1
- 0.4.2
- moved from misc dir to efont
- added mkfontdir call (ouch!)
- spec cleanup

* Fri Apr 29 2005 Michael Shigorin <mike@altlinux.ru> 0.4.0-alt1
- built for ALT Linux (used in gfxboot)
- based on SuSE 9.0 package

* Sat Mar 08 2003 - mfabian@suse.de
- Bug #24755: add more missing properties to the bdf headers:
  ADD_STYLE_NAME, PIXEL_SIZE, POINT_SIZE, RESOLUTION_X,
  RESOLUTION_Y, and AVERAGE_WIDTH.
  If these properties are missing they cannot be queried via
  freetype2. Being able to query POINT_SIZE and AVERAGE_WIDTH
  from freetype2 is useful to find out whether a font is
  single-width or double-width.
* Thu Jan 09 2003 - mfabian@suse.de
- add missing properties to the bdf headers:
  FOUNDRY, FAMILY_NAME, WEIGHT_NAME, SLANT, SETWIDTH_NAME
  CHARSET_REGISTRY, and CHARSET_ENCODING.
  This is necessary to make these fonts work with Xft.
- move fonts from /usr/X11R6/lib/X11/fonts/ucs/misc to
  /usr/X11R6/lib/X11/fonts/misc
* Thu Nov 15 2001 - mfabian@suse.de
- update to 0.4.0 (includes 10 pixel fonts now)
- build from sources instead of using the pre-built bdf files
  (saves 8 MB in the source rpm and enables use to build the
  "full-witdh" fonts as well, which are very useful with
  xterm in UTF-8 mode).
- add efont-unicode-bdf-0.4.0.patch to build "full-width" only
  fonts as well and to fix the XLFD for "full-width" fonts to
  something like:
  "-efont-fixed-medium-r-normal-*-16-160-75-75-c-160-iso10646-1"
  (i.e. "fixed" instead of "biwidth", "c" instead of "p"
  and twice the average width than the "half-width" font.
* Tue Sep 04 2001 - mfabian@suse.de
- update to version 0.3.1 (includes 24 pixel fonts now)
* Fri Mar 09 2001 - ro@suse.de
- added xf86
* Wed Feb 28 2001 - ro@suse.de
- fixed typo in specfile
* Wed Jan 31 2001 - violiet@suse.de
- efont-unicode-bdf renamed to efont-unicode.
* Mon Jan 29 2001 - violiet@suse.de
- NEW efont-unicode-bdf package version to 0.2.
