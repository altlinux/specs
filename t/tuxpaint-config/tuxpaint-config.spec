#
# spec file for package tuxpaint-config
#
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild

Name: tuxpaint-config
Summary: Configuration tool for Tux Paint
Url: http://www.tuxpaint.org/
License: GPL v2 or later
Group: Graphics
Version: 0.0.12
Release: alt1.1
Requires: tuxpaint

Source: %name-%version.tar.gz
Patch1: tuxpaint-config-docpath.patch
Patch2: tuxpaint-config-desktop.patch
# Automatically added by buildreq on Wed Mar 20 2013
# optimized out: fontconfig libX11-devel libXext-devel libstdc++-devel xorg-xproto-devel
BuildRequires: gcc-c++ libXft-devel libXinerama-devel libcairo-devel libfltk-devel libpaper-devel libpixman-devel

BuildRequires: desktop-file-utils libXfixes-devel

%description
Tux Paint has a rich set of configuration options, controllable via
command-line options or configuration files. This configuration tool
provides a point-and-click interface for administrators to tailor
Tux Paint to suit the needs of their users.

%prep
%setup -q
find . -name CVS | xargs rm -rf
%patch1
%patch2

%build
make  PREFIX=%prefix X11_ICON_PREFIX=/usr/include/X11/pixmaps/

%install
mkdir -p %buildroot%_bindir
make PREFIX=%buildroot%prefix X11_ICON_PREFIX=%buildroot%_includedir/X11/pixmaps/ DOC_PREFIX=%buildroot%_defaultdocdir/%name install
install -D -m644 src/%name.desktop %buildroot%_desktopdir/%name.desktop

# fix file permissions
find %buildroot%_defaultdocdir/%name -type f -exec chmod 644 {} \;
find %buildroot%_mandir -type f -exec chmod 644 {} \;

desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=System \
	--remove-category=SystemSetup \
	--add-category=Game \
	--add-category=KidsGame \
	%buildroot%_desktopdir/tuxpaint-config.desktop

#find_lang %name
# XXX this turns all the text to ???s
#files -f %name.lang
%files
%_bindir/tuxpaint-config
%doc %_defaultdocdir/%name
%dir %_includedir/X11/pixmaps
%_includedir/X11/pixmaps/tuxpaint-config.xpm
%_man1dir/*
%_datadir/tuxpaint-config/
%_pixmapsdir/*.png
%_desktopdir/*.desktop

%changelog
* Thu Nov 28 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.12-alt1.1
- Fixed build

* Wed Mar 20 2013 Fr. Br. George <george@altlinux.ru> 0.0.12-alt1
- Version up

* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.0.10-alt1.2.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for tuxpaint-config

* Fri Apr 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1.2
- Rebuilt with FLTK 1.3.0.r8575

* Mon Apr 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.10-alt1.1
- Rebuilt with libfltk13

* Wed Apr 23 2008 Alexandra Panyukova <mex3@altlinux.ru> 0.0.10-alt1
- build for ALTLinux

* Tue Mar  4 2008 lars@linux-schulserver.de
- update to 0.0.10
  - Added "Allow screensaver" option, to match new
    Tux Paint feature.
  - Added newly supported Tux Paint locales:
    + Australian English
    + Azerbaijani
    + Canadian English
    + Khmer
    + Macedonian
    + Occitan
    + Zapoteco
* Mon Jan 14 2008 lars@linux-schulserver.de
- initial package 0.0.9
