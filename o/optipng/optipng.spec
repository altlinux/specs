Name: optipng
Version: 0.6.2
Release: alt1

Summary: Optimizer for png files

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: zlib/libpng
Group: Graphics
Url: http://optipng.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar.bz2

%description
The main purpose of OptiPNG is to *optimize* PNG files, i.e. to reduce
their size to a minimum, without losing any information. In order to
achieve this goal, OptiPNG performs the following tasks:

- It losslessly reduces the bit depth, the color type and the color
  palette of the image. This step reduces the size of the uncompressed
  image, which, indirectly, reduces the size of the compressed image
  (i.e. the size of the PNG file).

- It runs a suite of compression methods and strategies, and selects
  the compression parameters that yield the smallest output file.

%prep
%setup -q

%build
%make -C src -f scripts/gcc.mak

%install
install -D -m755 src/optipng %buildroot%_bindir/%name
install -D -m644 man/%name.1 %buildroot%_man1dir/%name.1

%files
%doc README.txt LICENSE.txt doc/*
%_bindir/%name
%_man1dir/*

%changelog
* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)
- add man page

* Wed Dec 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- new version 0.5.4 (with rpmrb script)

* Sat Sep 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt1
- initial build for ALT Linux Sisyphus
- spec from PLD
