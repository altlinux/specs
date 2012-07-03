Name: luit
Version: 1.1.1
Release: alt2
Summary: Locale and ISO 2022 support for Unicode terminals
Group: System/X11
Url: http://xorg.freedesktop.org
Source: %name-%version.tar.bz2
License: MIT
Packager: Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Thu Apr 14 2011
# optimized out: pkg-config
BuildRequires: libfontenc-devel zlib-devel

BuildRequires: xorg-util-macros

%description
Luit is a filter that can be run between an arbitrary application and a UTF-8
terminal emulator. It will convert application output from the locale's
encoding into UTF-8, and convert terminal input from UTF-8 into the locale's
encoding.

%prep
%setup
test %version = 1.1.1 && sed -i '/<stdlib.h>/a\
int posix_openpt (int __oflag) __wur;
' sys.c

%build
%autoreconf
%configure
%make

%install
%makeinstall

%files
%doc README
%_bindir/luit
%_man1dir/luit.1*

%changelog
* Thu Jun 07 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt2
- Fix gcc4.6 build

* Tue Apr 17 2012 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1

* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1.1
- Recalculate buildreq

* Wed Nov 03 2010 Fr. Br. George <george@altlinux.ru> 1.1.0-alt1
- Autobuild version bump to 1.1.0

* Sun Sep 26 2010 Fr. Br. George <george@altlinux.ru> 1.0.5-alt1
- Autobuild version bump to 1.0.5

* Tue Dec 02 2008 Fr. Br. George <george@altlinux.ru> 1.0.3-alt1
- Version up
- Implement upstream syncing scheme

* Tue Oct 10 2006 Sergey Vlasov <vsu@altlinux.ru> 1.0.1-alt2
- Run autoreconf to make configure.ac changes really do something
  (otherwise the locale.alias path is not set properly).
- Spec file cleanup:
  + removed unneeded braces;
  + removed unneeded "-n %%name-%%version" from %%setup;
  + replaced %%_mandir/man1 by %%_man1dir;
  + removed explicit .1x.gz suffix from man page filename.

* Sun Oct 01 2006 Fr. Br. George <george@altlinux.ru> 1.0.1-alt1
- Initial build from MDV
- FC locale.alias path patch applied

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Wed May 17 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-17 00:06:32 (27478)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository
