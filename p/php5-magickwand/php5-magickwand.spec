%define		php5_extension	magickwand
%define 	real_name	MagickWandForPHP
%define		real_version	1.0.9

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release.1

Summary:	PHP5 extension to access the ImageMagick MagickWand API

License:	OpenSource
Group:		System/Servers
URL:		http://www.magickwand.org/

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

Patch0:		php5-magickwand-1.0.9-alt-rpath_fix.patch

BuildRequires(pre): rpm-build-php5

BuildRequires: php5-devel = %php5_version
BuildRequires: libImageMagick-devel

%description
MagickWand for PHP is a native PHP interface to the new ImageMagick
MagickWand API.

It is an almost complete port of the ImageMagick C API, excluding some
X-Server related functionality, and progress monitoring.

The functionality of the MagickWand API is pretty much unparalelled in
the PHP imaging world, allowing the PHP programmer read/write/manipulate
access to multiple image formats, along with vector drawing, pixel-level
manipulation, and special effects capabilities and more.

%prep
%setup -T -c
tar xvf %SOURCE0
%patch0

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS README AUTHOR LICENSE

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Fri Jun 08 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with new libImageMagick

* Tue Feb 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- rebuild for php5-5.3.10.20120202-alt1

* Wed Jan 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.8.20110823-alt2
- Updating MagickWand to 1.0.9
- Fix RPATH and underlinking issues

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1.1
- Rebuild with php5-5.3.8.20110823-alt1

* Tue Apr 26 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1.1
- build with libImageMagick instead of libImageMagick-noHDRI

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- Rebuild with php5-5.2.12.20091216-alt4

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- Rebuild with new php (5.2.12.20091216-alt1)

* Tue Sep 01 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Initial build for ALT Linux Sisyphus

