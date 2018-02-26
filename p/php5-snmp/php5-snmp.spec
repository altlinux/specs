%define php5_extension	snmp

Name: php5-snmp
Version: %php5_version
Release: %php5_release

Summary: SNMP module for PHP5
Group: System/Servers
License: PHP Licence


Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

Requires: net-snmp-mibs
BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

# Automatically added by buildreq on Mon Jan 01 2007
BuildRequires: libnet-snmp-devel

%description
The php-snmp package includes a dynamic shared object (DSO) that adds 
NET-SNMP software support to PHP5.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure \
  --with-snmp=%_usr \
  --with-openssl-dir=%_usr
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
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- Rebuild with php5-5.3.10.20120202-alt1

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

* Mon Sep 29 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.7.20080920-alt1
- rebuild with latest php5

* Tue Jul 22 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.7.20080627-alt1
- rebuild with latest php5

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.5-alt1
- rebuild with latest php5
- add net-snmp-mibs to 'Requires:' (#11734)

* Sun Jun 24 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.3-alt1
- rebuild with latest php5

* Fri May 18 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.2-alt1
- rebuild with latest php5

* Mon Apr 23 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.1-alt2
- rebuild with latest php5

* Wed Mar 07 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.1-alt1
- rebuild with PHP5.2.1

* Mon Jan 01 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.0-alt1
- initial build for ALT Linux

