Name: re2c
Version: 0.13.5
Release: alt1

Summary: re2c - A tool for generating C-based recognizers from regular expressions

Group: Development/Other
License: Public Domain
Url: http://sourceforge.net/projects/re2c/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

# Automatically added by buildreq on Sat Nov 11 2006
BuildRequires: gcc-c++ linux-libc-headers

%description
re2c is a great tool for writing fast and flexible lexers. It has
served many people well for many years and it deserves to be
maintained more actively. re2c is on the order of 2-3 times faster
than a flex based scanner, and its input model is much more
flexible.

%prep
%setup -q

%build
%configure

make re2c
#regenerate file scanner.cc
rm -f scanner.cc
./re2c scanner.re > scanner.cc
rm -f re2c scanner.o
make

%install
mkdir -p %buildroot%_bindir/
install -m 0755 re2c %buildroot%_bindir/

mkdir -p %buildroot%_man1dir
install -m 0755 re2c.1 %buildroot%_man1dir/

%files
%_bindir/re2c
%_man1dir/re2c.1*
%doc README examples doc/* lessons

%changelog
* Mon Sep 21 2009 Vitaly Lipatov <lav@altlinux.ru> 0.13.5-alt1
- new version 0.13.5 (with rpmrb script)

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt0.1
- new version 0.11.0 (with rpmrb script)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.10.6-alt0.1
- initial build for ALT Linux Sisyphus
