%define php5_extension	rrdtool

Name: php5-rrdtool
Version: %php5_version
Release: %php5_release.1

Summary: RRDtool module for PHP5
Group: System/Servers
License: PHP Licence

Source0: %name.tgz
Source1: php-%php5_extension.ini
Source2: php-%php5_extension-params.sh

Patch0: %name-1.2.10-alt-fix.patch

BuildRequires(pre): rpm-build-php5
BuildRequires: php5-devel = %php5_version

# Automatically added by buildreq on Tue Jan 02 2007
BuildRequires: librrd-devel php5-devel

%description
The php5-rrdtool includes a dynamic shared object (DSO) that adds
RRDtool support to PHP5. Install this package in addition to main PHP
package if you plan to use RRD.

%prep
%setup -q -n %name
%patch0 -p1

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
%add_optflags -fPIC -L%_libdir
export LDFLAGS=-lphp-%_php5_version
%configure --with-rrd
%php5_make top_srcdir=%_builddir/%name top_builddir=%_builddir/%name

%install
%php5_make install top_srcdir=%_builddir/%name top_builddir=%_builddir/%name
install -D -m 644 %SOURCE1 %buildroot/%php5_extconf/%php5_extension/config
install -D -m 644 %SOURCE2 %buildroot/%php5_extconf/%php5_extension/params

%files
%php5_extconf/%php5_extension
%php5_extdir/*
%doc INSTALL README USAGE

%post
%php5_extension_postin

%preun
%php5_extension_preun

%changelog
* Mon Feb 13 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1.1
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1.1
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1.1
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2.1
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1.1
- Rebuild with php5-5.3.5.20110105-alt1

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3.1
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2.1
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1.1
- Rebuild with php5-5.3.3.20100722-alt1

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1.1
- Rebuild with php5-5.2.14.20100721-alt1

* Thu Apr 22 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1.1
- Rebuild with new rrdtool

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

* Sun Jun 24 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.3-alt1
- rebuild with latest php5

* Fri May 18 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.2-alt1
- rebuild with latest php5

* Mon Apr 23 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.1-alt2
- rebuild with latest php5

* Wed Mar 07 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.1-alt1
- rebuild with PHP5.2.1

* Sat Jan 06 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.0-alt1.1
- fix extension config

* Mon Jan 01 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 5.2.0-alt1
- initial build for ALT Linux

