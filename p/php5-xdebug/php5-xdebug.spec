%define php5_extension	xdebug

Name: php5-%php5_extension
Version: %php5_version
Release: %php5_release.1

Summary: xdebug extensions
Group: System/Servers
License: PHP Licence

Packager: Denis Klimov <zver@altlinux.ru>

Source: php5-%php5_extension.tar
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

%description
The Xdebug extension helps you debugging your script by providing
a lot of valuable debug information. The debug information that
Xdebug can provide includes the following:
    * stack traces and function traces in error messages with:
          o full parameter display for user defined functions
          o function name, file name and line indications
          o support for member functions
    * memory allocation
    * protection for infinite recursions

Xdebug also provides:
    * profiling information for PHP scripts
    * code coverage analysis
    * capabilities to debug your scripts interactively with a debug client

%prep
%setup -n php5-%php5_extension
%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--with-%php5_extension=%_usr
%php5_make

%install
install -D -m 644 modules/xdebug.so %buildroot%php5_extdir/xdebug.so
install -D -m 644 %SOURCE1 %buildroot%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot%php5_extconf/%php5_extension/params
echo "zend_extension=%php5_extdir/xdebug.so" >%buildroot%php5_extconf/%php5_extension/config

%files
%php5_extconf/%php5_extension
%php5_extdir/xdebug.so

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with php5-5.3.10.20120202-alt1

* Mon Sep 12 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1.1
- updated to xdebug 2.1.2
- fixed ini-file (closes: #26275)

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

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

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Tue Feb 10 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- NMU: Rebuild with php5-5.2.9.20090205-alt1.

* Mon Oct 13 2008 Denis Klimov <zver@altlinux.ru> 5.2.7.20080920-alt1
- Initial build for ALTLinux
