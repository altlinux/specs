%define		php5_extension	apc
%define 	real_name	APC
%define		real_version	3.1.10

Name:	 	php5-%{php5_extension}
Version:	%php5_version
Release:	%php5_release.2

Summary:	PHP5 Alternative PHP Cache

License:	PHP License
Group:		System/Servers
URL:		http://pecl.php.net/package/apc

Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

Source0:	%real_name-%real_version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
APC is a free, open, and robust framework for caching and 
optimizing PHP intermediate code.

%prep
%setup -c
##%setup -T -c
##tar xvf %SOURCE0

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension \
	--with-libdir=%_lib \
	--enable-apc \
	--enable-apc-mmap \
	#

%php5_make

%install
%php5_make_install
install -D -m 644 -- %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 -- %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%doc CHANGELOG TECHNOTES.txt TODO NOTICE LICENSE

%php5_extconf/%php5_extension
%php5_extdir/*

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Wed May 16 2012 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.10.20120202-alt1.2
- New module version 3.1.10
- Fix default configuration

* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with php5-5.3.10.20120202-alt1

* Sat Sep 10 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1.1
- Rebuild with php5-5.3.8.20110823-alt1

* Thu Aug 18 2011 Nikolay A. Fetisov <naf@altlinux.ru> 5.3.6.20110317-alt1.1
- New module version 3.1.9
- Fix default configuration

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

* Sat Jul 25 2009 Nikolay A. Fetisov <naf@altlinux.ru> 5.2.11.20090722-alt1
- Initial build for ALT Linux Sisyphus

