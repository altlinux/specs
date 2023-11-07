Name: optipng
Version: 0.7.8
Release: alt1

Summary: Optimizer for png files

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: zlib/libpng
Group: Graphics
Url: http://optipng.sourceforge.net/

Source: http://prdownloads.sf.net/%name/%name-%version.tar

# Automatically added by buildreq on Sun Aug 04 2013
# optimized out: zlib-devel
BuildRequires: libpng-devel

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
%setup

%build
# non autotools configure
./configure --prefix=%prefix --mandir=%_mandir \
	--with-system-libpng --with-system-zlib
%make_build

%install
%makeinstall_std

%check
make test

%files
%doc README.txt LICENSE.txt doc/*
%_bindir/%name
%_man1dir/*

%changelog
* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 0.7.8-alt1
- new version 0.7.8 (with rpmrb script)

* Sat Jun 09 2018 Vitaly Lipatov <lav@altlinux.ru> 0.7.7-alt1
- new version 0.7.7 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.7.6-alt1
- new version 0.7.6 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 0.7.5-alt1
- new version 0.7.5 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt1
- new version 0.7.4 (with rpmrb script)
- build with system libpng

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 0.6.2-alt1
- new version 0.6.2 (with rpmrb script)
- add man page

* Wed Dec 27 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5.4-alt0.1
- new version 0.5.4 (with rpmrb script)

* Sat Sep 17 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4.8-alt1
- initial build for ALT Linux Sisyphus
- spec from PLD
