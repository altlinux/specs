%define		php5_extension	suhosin

Name:	 	php5-%php5_extension
Version:	0.9.33
Release:	alt1

Summary:	Advanced PHP5 protection system
Group:		System/Servers
License:	PHP Licence
URL:		http://www.hardened-php.net/suhosin/

Source0:	%php5_extension-%version.tar
Source1:	php-%php5_extension.ini
Source2:	php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires:	php5-devel = %php5_version

%description
Suhosin is an advanced protection system for PHP servers

%prep
%setup -q -n %php5_extension-%version

%build
phpize

%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
	--enable-suhosin \
	--with-pic
%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS Changelog

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 0.9.33-alt1
- new version for php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt8
- Rebuild with php5-5.3.8.20110823-alt1

* Tue Mar 22 2011 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt7
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt6
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt5
- Rebuilf with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt4
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt3
- Rebuild with php5-5.3.3.20100722-alt2

* Wed Sep 22 2010 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt2
- link with libcrypto (closes: 24138)

* Mon Aug 16 2010 Anton Farygin <rider@altlinux.ru> 0.9.32.1-alt1
- new version

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 0.9.31-alt2
- Rebuild with php5-5.2.14.20100721-alt1

* Sun Jun  7 2010 Sergey Kurakin <kurakin@altlinux.org> 0.9.31-alt1
- 0.9.31
- config file updated: 3 more options, some defaults changed

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 0.9.29-alt3
- rebuild with new php5

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 0.9.29-alt2
- Rebuild with new php5 build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 0.9.29-alt1
- 0.9.29, thanks to Sergey Kurakin

* Mon Jan 11 2010 Sergey Kurakin <kurakin@altlinux.org> 0.9.27-alt4
- rebuild with new php5 stable release 5.2.12 (20091216)

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 0.9.27-alt3
- rebuild with php5 (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 0.9.27-alt2
- rebuild with php5 (5.2.9.20090205).

* Sun Sep 21 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.27-alt1
- new version (0.9.27).

* Sun Jun 29 2008 Alexey Gladkov <legion@altlinux.ru> 0.9.24-alt1
- new version (0.9.24).

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 0.9.23-alt1
- new version (0.9.23).
- rebuild with php5 (5.2.5).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.20-alt1
- new version (0.9.20).
- rebuild with new php5 (5.2.3).

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.19-alt1
- new version (0.9.19).
- rebuild with new php5 (5.2.2).

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 0.9.18-alt2
- Rebuild due libmm soname changes.

* Fri Mar 16 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.18-alt1
- version 0.9.18.
- add default suhosin.ini from Mandriva.

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 0.9.16-alt1
- new version (0.9.16).
- rebuild with php 5.2.1.

* Tue Nov 07 2006 Alexey Gladkov <legion@altlinux.ru> 0.9.11-alt1
- first build for ALT linux.
