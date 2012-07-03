Name: lcdtest
Version: 1.08
Release: alt1.qa2

Summary: The LCD screen quality testing utility

License: GPL
Group: System/Configuration/Hardware
Url: http://www.brouhaha.com/~eric/software/lcdtest/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www.brouhaha.com/~eric/software/lcdtest/download/%name-%version.tar.bz2
Source1: %name.desktop
Patch: lcdtest-1.02-alt-man-double_content_fix.patch

# manually removed: esound bk cvs ghostscript-utils rcs tetex-latex
# Automatically added by buildreq on Thu Sep 20 2007
BuildRequires: flex gcc-c++ libSDL-devel libSDL_image-devel scons swig

BuildRequires: netpbm

# due bug in IMG_ReadXPMFromArray
Requires: libSDL_image > 1.2.5-alt1
BuildRequires: desktop-file-utils

%description
lcdtest is a utility to display LCD monitor test patterns. It may be
useful for adjusting the pixel clock frequency and phase on LCD monitors
when using analog inputs, and for finding pixels that are stuck on
or off. lctest uses the SDL library, and is known to work on Linux
and Windows.

%description -l ru_RU.KOI8-R
lcdtest отображает различные паттерны, позволяющие судить о
качестве изображения на жидкокристаллическом мониторе и наличии таких
дефектов, как "битые пикселы". lcdtest использует библиотеку SDL, она
тестировалась в Linux и Windows.

%prep
%setup -q
#patch -p1

%build
scons

%install
scons install destdir=%buildroot bindir=%_bindir mandir=%_man1dir
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Utility \
	--remove-category=Application \
	--add-category=Settings \
	--add-category=HardwareSettings \
	--add-category=X-ALTLinux-VideoSettings \
	%buildroot%_desktopdir/lcdtest.desktop

%files
%doc README
%_bindir/%name
%_man1dir/%name.1.*
%_desktopdir/%name.desktop

%changelog
* Mon May 23 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.08-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for lcdtest

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.08-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for lcdtest
  * postclean-05-filetriggers for spec file

* Thu Sep 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- new version 1.08 (with rpmrb script)
- scons used now for build
- fix desktop file permissions (bug #12847)

* Sat Mar 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.02-alt1
- add desktop menu, add requires for new libSDL_image

* Fri Mar 23 2007 Slava Semushin <php-coder@altlinux.ru> 1.02-alt0
- Updated to 1.02
- Install man page
- Fixed double content in man page
- Spec improvements:
  + Better Summary
  + s/%%make/%%make_build/
  + Don't use macros for install command
  + More strict name in %%files section

* Thu Jul 21 2005 Vitaly Lipatov <lav@altlinux.ru> 1.01-alt1
- new version

* Mon May 16 2005 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt1
- first build for ALT Linux Sisyphus
