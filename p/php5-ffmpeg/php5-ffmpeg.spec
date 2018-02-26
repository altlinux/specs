%define		php5_extension	ffmpeg
%define 	real_name	ffmpeg-php
%define		real_version	0.6.0

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 ffmpeg-php extension

License:	%gpl2plus
Group:		System/Servers
URL:		http://ffmpeg-php.sourceforge.net/

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar.bz2
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

Patch0:		php5-ffmpeg-0.6.0-alt-RGBA32.patch
Patch1:		php5-ffmpeg-libav-0.7.patch
Patch2:		php5-ffmpeg-0.6.0-alt-underlinking_libs.patch

BuildRequires(pre): rpm-build-php5 rpm-build-licenses
BuildRequires: php5-devel = %php5_version
BuildRequires: libavformat-devel libswscale-devel

Requires: php5-gd2

%description
ffmpeg-php is an extension for PHP that adds an easy to use, object-oriented
API for accessing and retrieving information from video and audio files.  It 
has methods  for returning  frames from  movie files  as images that  can be 
manipulated using PHP's  image functions.  This works well for automatically 
creating thumbnail images from movies.
ffmpeg-php is also useful for reporting the duration and bitrate of audio 
files (mp3, wma...). It can access many of the video formats supported by 
ffmpeg (mov, avi, mpg, wmv...)


%prep
%setup -T -c
tar xvfj %SOURCE0
# ./ffmpeg-php-X.X.X -> ./
mv -- %real_name-%real_version/* .
rm -fr -- %real_name-%{real_version}*

%patch0
%patch1 -p1
%patch2

mv -f -- LICENSE LICENSE.orig
ln -s -- $(relative %_licensedir/GPL-2 %_docdir/%name/LICENSE) LICENSE

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-skip-gd-check \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS ChangeLog EXPERIMENTAL TODO INSTALL
%doc --no-dereference LICENSE

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
Rebuild with 5.3.10.20120202-alt1

* Wed Jan 04 2012 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.8.20110823-alt2
- Fix RPATH and underlinking issues

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1
- added support for new ffmpeg API

* Thu Aug 18 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.6.20110317-alt1.1
- Fix build with new libav

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

* Wed Jul 29 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with php5-5.2.11.20090722-alt1

* Thu Feb 12 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1
- New version 0.6.0
- Rebuild with php5-5.2.9.20090205-alt1

* Sun Oct 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild for PHP 5.2.7.20080920

* Fri Jul 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.7.20080627-alt1
- New version 0.5.3.1

* Mon May 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1.1
- New version 0.5.2.1
  * Added gd image bounds checking
  * ffmpeg's logs are mapped to php's warnings and notices (no more stderr pollution)
  * Failure to find the proper codec is not a fatal error anymore
- Enable GD support

* Sun Apr 06 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.5-alt1
- Rebuild for PHP 5.2.5

* Sun Feb 03 2008 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.3-alt1.2
- Rebuild with libavformat52, fix #14213

* Fri Aug 10 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.3-alt1.1
- New version 0.5.1
  * Added $movie->hasVideo() function to test for video stream.
  * Copyright updated for better compatibilty with the PHP license.
  * Bug fixes in tests and build process.

* Wed Jun 06 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.3-alt1
- Rebuild for PHP 5.2.3-alt1

* Tue May 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.2-alt1
- Rebuild for PHP 5.2.2-alt1

* Tue Apr 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.1-alt2
- Initial build for ALT Linux Sisyphus

