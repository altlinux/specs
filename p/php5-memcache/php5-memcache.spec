# Package name without php prefix
%define		php5_extension	memcache
###############################################################
Name:	 	php5-%php5_extension
Version:	2.2.6
Release:	alt7
Group:		System/Servers
License:	PHP Licence

URL:		http://pecl.php.net/package/memcache

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version zlib-devel
Requires: php5-libs = %php5_version

Summary:	memcached extension for PHP5

Source0:	php5-%php5_extension-%version.tar
Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh
Patch:		php5-memcache-alt-inc.patch

%description 
The php5-%php5_extension package contains a dynamic shared object (DSO) for PHP5. The
php-%php5_extension module allows you to work with memcached through handy OO
and procedural interfaces. If you need memcached(1) support for PHP5
applications, you will need to install this package and PHP5.

%prep
%setup -q -n php5-%php5_extension-%version
%patch -p2

%build
export CFLAGS="%optflags"

phpize
%configure --enable-memcache --with-zlib-dir=/usr
%php5_make

%install
%php5_make_install
%__install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
%__install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS README

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 2.2.6-alt7
- Rebuild with php5-5.3.10.20120202-alt1

* Sun Sep 18 2011 Anton Farygin <rider@altlinux.ru> 2.2.6-alt6
- rebuilt to reduce dependence on the php-devel

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 2.2.6-alt5
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 2.2.6-alt4
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 2.2.6-alt3
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 2.2.6-alt2
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 14 2010 Anton Farygin <rider@altlinux.ru> 2.2.6-alt1
- Rebuild with new php5
- add requires to versioned php5-libs 

* Thu Mar 25 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.2.5-alt2
-  Rebuild with new php snapshot.

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 2.2.5-alt1
- New version (2.2.5).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 2.2.4-alt2
- Rebuild with new php snapshot.

* Tue Sep 23 2008 Alexey Gladkov <legion@altlinux.ru> 2.2.4-alt1
- New version (2.2.4).

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 2.2.3-alt2
- rebuild with new php5 (5.2.7).

* Sun Mar 30 2008 L.A. Kostis <lakostis@altlinux.ru> 2.2.3-alt1
- new stable version (2.2.3).
- rebuild with new php5 (5.2.5).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt2
- rebuild with new php5 (5.2.3).

* Thu May 31 2007 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt1.1
- remove unnecessary requires.

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 2.1.2-alt1
- 2.1.2 version.
- fix detection of session support (port from php4 ext).

* Wed Apr 11 2007 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt2
- rebuild due libmm soname change.

* Sat Mar 10 2007 L.A. Kostis <lakostis@altlinux.ru> 2.1.0-alt1
- php5 version.
- add URL.
- made from php-memcache package.

