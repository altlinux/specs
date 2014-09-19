Name: pcf2bdf
Version: 1.04
Release: alt1.git20120717

Summary: Pcf2bdf is a font de-compiler
Summary(ru_RU.KOI8-R): Pcf2bdf - декомпилятор шрифтов
License: BSD
# NB! ALM24's rpm has no System/X11 group, use System/XFree86 instead
Group: System/X11
Url: http://www.tsg.ne.jp/GANA/S/pcf2bdf/

Source0: %url%name-%version.tgz

# Automatically added by buildreq on Tue Nov 30 2004 (-bi)
BuildRequires: gcc-c++ libstdc++-devel

%description
Pcf2bdf converts X font from Portable Compiled Format (PCF) to Bitmap
Distribution Format (BDF). It can also accept a compressed/gzipped PCF
file as input, but gzip must be found in your PATH.

%description -l ru_RU.KOI8-R
Pcf2bdf конвертирует шрифты X из формата PCF в формат BDF. Он также может
получать PCF файл, сжатый gzip, но для этого в PATH должен находиться
gzip.

%prep
%setup -c -n %name-%version

%build
%make CFLAGS="${CFLAGS:-%optflags}" -f Makefile.gcc

%install
%make -f Makefile.gcc BINPATH="%buildroot%_bindir" MANPATH="%buildroot%_man1dir" install

%files
%doc README.txt pcf.txt
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Fri Sep 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.04-alt1.git20120717
- Snapshot from git

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.04-alt1.1.qa1
- NMU: rebuilt for debuginfo.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.04-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Dec 07 2004 Andrei Bulava <abulava@altlinux.ru> 1.04-alt1
- initial build for ALT Linux

