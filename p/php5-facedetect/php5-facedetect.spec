%define		php5_extension	facedetect
%define 	real_name	facedetect
%define		real_version	1.1

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release

Summary:	PHP5 extension to detect faces on images

License:	PHP License
Group:		System/Servers
URL:		http://www.xarg.org/project/php-facedetect/

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

# git://github.com/infusion/PHP-Facedetect.git
Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh
Patch0:		%real_name-%real_version-alt-fix_libs.patch
Patch1:		php5-facedetect-5.6.33-opencv3.patch

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
BuildRequires: libopencv-devel

%description
Facedetect extension provides a PHP implementation of the OpenCV
library. The extension offers two functions, the first one returns
the number of faces found on the given image and the other an 
associative array of their coordinates. 

%prep
%setup -T -c
tar xvf %SOURCE0
%patch0 -p1
%patch1 -p1

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	#

/bin/ln -s -- config.h cvconfig.h
%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CREDITS

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%version-%release

* Sun May 19 2013 Aleksey Avdeev <solo@altlinux.ru> 5.3.25.20130509-alt1.1
- New module version 1.1 (20111228)

* Fri Apr 12 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 5.3.24.20130412-alt1
- Rebuild with php5-5.3.24.20130412-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.18.20121017-alt1
- Rebuild with php5-5.3.18.20121017-alt1

* Fri Sep 14 2012 Anton Farygin <rider@altlinux.ru> 5.3.17.20120913-alt1
- Rebuild with php5-5.3.17.20120913-alt1

* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Sat Sep 10 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Thu Aug 18 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.6.20110317-alt1.2
- New module version 1.0.1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1.1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2.1
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1.1
- Rebuild with php5-5.3.5.20110105-alt1

* Tue Nov 30 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3.1
- fixed build with libOpenCV 2 (thanks to real@)

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

* Sat Jul 25 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722)
- Fix build with OpenCV 1.1

* Wed Mar 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.9.20090205-alt1
- Initial build for ALT Linux Sisyphus

