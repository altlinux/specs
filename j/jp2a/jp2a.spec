# SPEC-file for jp2a
#
#

Name: jp2a
Version: 1.1.1
Release: alt1

Summary: an utility for converting JPEG images to ASCII
Summary(ru_RU.UTF-8): утилита для конвертации изображений JPEG в ASCII art

License: %gpl2only
Group: Text tools
URL: https://github.com/Talinx/jp2a
#URL: https://github.com/cslarsen/jp2a
#URL: http://jp2a.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Source1: %name.1

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Tue Jul 13 2021
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libncurses-devel libsasl2-3 libtinfo-devel perl pkg-config python-modules python2-base python3 python3-base python3-module-paste ruby ruby-stdlibs sh4 texlive
BuildRequires: doxygen libcurl-devel libjpeg-devel libpng-devel

BuildRequires: autoconf-archive

%description
jp2a is a small command-line utility for converting JPEG images
to ASCII art.

%description -l ru_RU.UTF-8
jp2a - небольшая утилита командной строки для конвертирования
изображений в формате JPEG в текcтовый вид ASCII art.

%define rman1dir %_mandir/ru/man1

%prep
%setup
%patch0 -p1

mv -f COPYING COPYING.GPL.orig
ln -s $(relative %_licensedir/GPL-2 %_docdir/%name/COPYING.GPL) COPYING.GPL

%build
%autoreconf
%configure
%make_build

%install
%makeinstall bashcompdir=%buildroot%_sysconfdir/bash_completion.d
install -pD -m0644 %SOURCE1 %buildroot%rman1dir/%name.1

%files
%doc AUTHORS ChangeLog README LICENSES
%doc --no-dereference COPYING.GPL
%_bindir/%name
%_man1dir/%{name}*
%rman1dir/%{name}*
%_sysconfdir/bash_completion.d/%name

/usr/share/man/ru/man1/

%changelog
* Thu Nov 25 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.1.1-alt1
- New version

* Tue Jul 13 2021 Nikolay A. Fetisov <naf@altlinux.org> 1.1.0-alt1
- New version
- Add Russian man page (Closes: 37227)

* Thu May 02 2019 Nikolay A. Fetisov <naf@altlinux.org> 1.0.7-alt1
- New version

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.6-alt1.0.qa1
- NMU: rebuilt for debuginfo.

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

