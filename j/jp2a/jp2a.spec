# SPEC-file for jp2a
#
#

%define version 1.0.6
%define release alt1

Name: jp2a
Version: %version
Release: %release.0

Summary: an utility for converting JPEG images to ASCII
Summary(ru_RU.UTF-8): утилита для конвертации изображений JPEG в ASCII art

License: GPL v.2
Group: Terminals
URL: http://jp2a.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2
BuildPreReq: libjpeg-devel libcurl-devel

%description
jp2a is a small command-line utility for converting JPEG images
to ASCII art.

%description -l ru_RU.UTF-8
jp2a - небольшая утилита командной строки для конвертирования
изображений в формате JPEG в текcтовый вид ASCII art.

%prep
%setup

%__mv -f COPYING COPYING.GPL.orig
%__ln_s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING.GPL) COPYING.GPL

%build
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog README man/jp2a.html LICENSES
%doc --no-dereference COPYING.GPL
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Fri Mar 30 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.6-alt1.0
- Rebuilt due to libcurl.so.3 -> libcurl.so.4 soname change.

* Mon Jan 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.6-alt1
- New version 1.0.6
  * Support for GCC 2.95.4 (old C compilers in general)
  
* Mon Sep 25 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.5-alt1
- New version 1.0.5
  * Fixed problem with --invert / --background=light / --background=dark with HTML output.
  * Updated configure script from autoconf 2.59 to 2.60
  
* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.4-alt1
- New version 1.0.4
  * minor feature enhancements in HTML output
  * new options '--html-no-bold', '--html-title', '--html-raw' for HTML output
  * Added option to --fill ANSI background colors.

* Thu Aug 17 2006 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.0-alt1
- New version 1.0.0
  * HTML manual added
  * small code fixes

* Wed Aug 09 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.22-alt1
- New version 0.9.22
  * added color output for text (ANSI colors) and HTML (CSS colors)
  * several bugfixes and enhancements, see ChangeLog for details

* Thu Jul 27 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.20-alt1
- New version 0.9.20
  * improvements in output quality
  * several bugfixes and enhancements, see ChangeLog for details

* Wed Jul 19 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.18-alt1
- Initial build for ALT Linux Sisyphus

* Wed Jul 12 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.9.13-alt0
- Initial build

