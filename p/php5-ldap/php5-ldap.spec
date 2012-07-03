%define php5_extension	ldap

Name: php5-%php5_extension
Version: %php5_version
Release: %php5_release

Summary: LDAP module for PHP5
Group: System/Servers
License: PHP Licence

Packager: Vladimir V Kamarzin <vvk@altlinux.ru>
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version
#BuildRequires: php5-devel = %php5_version-alt2

BuildRequires: libldap-devel libsasl2-devel

%description
The %name includes a dynamic shared object (DSO) that adds
Lightweight Directory Access Protocol (LDAP) support to PHP. LDAP is a
set of protocols for accessing directory services over the Internet.
PHP is an HTML-embedded scripting language. If you need LDAP support
for PHP applications, you will need to install this package in addition
to the php package.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build

phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDLIBS=-lphp-%_php5_version
%configure \
	--with-%php5_extension=%_usr \
	--with-ldap-sasl=%prefix \
	--with-libdir=$(echo "%_libdir" | cut -d '/' -f3)
%php5_make

%install
%php5_make_install
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc CREDITS

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- Rebuild with php5-5.3.5.20110105-alt2

* Thu Feb 17 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
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

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- fixed link with libsasl2 (closes #21775)
- rebuild with new php5

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1.1
- NMU: Rebuild with php5-5.2.12.20091216

* Thu Sep 24 2009 ALT QA Team Robot <ldv@altlinux.org> 5.2.11.20090722-alt1.1
- Automated blind dumb rebuild with libldap-devel-2.4.16-alt4.4.

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Tue Feb 10 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- NMU: Rebuild with php5-5.2.9.20090205-alt1.

* Mon Oct 06 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 5.2.7.20080920-alt1
- Rebuild with new php

* Thu Jul 10 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.7.20080627-alt1
- Rebuild with php 5.2.7.20080627

* Wed Apr 02 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.5-alt1
- Rebuild with php 5.2.5

* Tue Jul 17 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.3-alt1
- Rebuild with new php

* Fri May 18 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.2-alt1
- Rebuild with new php

* Tue Apr 10 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.1-alt2.1
- Rebuild due libmm soname change.

* Fri Mar 23 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.1-alt2
- Fix building on x86_64

* Fri Mar 23 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.1-alt1
- Rebuild with new php

* Mon Dec 11 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 5.2.0-alt1
- 5.2.0
- Resurrected from orphaned
- Added php5-ldap-alt-configure.patch for fix building
- Build --with-ldap-sasl

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new snapshot.

* Sun Dec 25 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- new version.

* Tue Oct 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.6-alt0.cvs20051003
- new version;

* Thu Aug 04 2005 Alexey Gladkov <legion@altlinux.ru> 5.0.5-alt0.cvs20050729
- new cvs snapshot.

* Wed Jul 13 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.M24.1
- Built for 5.0.4-alt0.M24.1

* Mon Jul 04 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.4
- rebuilt with alt0.4

* Fri Jul 01 2005 Sir Raorn <raorn@altlinux.ru> 5.0.4-alt0.3
- built for php5-5.0.4
