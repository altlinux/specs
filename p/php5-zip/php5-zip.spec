%define		php5_extension	zip

Name:	 	php5-%php5_extension
Version:	%php5_version
Release:	%php5_release
Summary:	ZIP functions
Group:		System/Servers
License:	PHP Licence

Source1:	php5-%php5_extension.ini
Source2:	php5-%php5_extension-params.sh

Prereq:		php5-libs >= %php5_version-%php5_release

BuildRequires(pre): rpm-build-php5

# Automatically added by buildreq on Mon Jun 26 2006
BuildRequires: zziplib-devel
BuildRequires: php5-devel = %php5_version

%description
This module enables you to transparently read ZIP compressed archives and the files inside them.

%prep
%setup -T -c
cp -pr %php5_extsrcdir/%php5_extension/* .

%build
phpize

BUILD_HAVE=`echo %php5_extension | tr '[:lower:]-' '[:upper:]_'`
export LDFLAGS="-lphp-%_php5_version" ### Stupid PHP not understand LDLIBS
%add_optflags -fPIC -L%_libdir
%configure --with-%php5_extension
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

* Thu Jul 23 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- Rebuild with new php (5.2.11.20090722).

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- Rebuild with new php snapshot.

* Wed Sep 24 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- Rebuild with new php snapshot.

* Thu Jul 03 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- new version (5.2.7).

* Sat Mar 29 2008 L.A. Kostis <lakostis@altlinux.ru> 5.2.5-alt1
- Rebuild with new php(5.2.5).

* Sun Jun 03 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.3-alt1
- rebuild for new php (5.2.3).

* Mon May 14 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- rebuild with for new php (5.2.2).

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- Rebuild due libmm soname change.

* Tue Mar 06 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- version for php5 (5.2.1).

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 4.4.6-alt0.1
- new version (4.4.6).

* Wed Sep 27 2006 Alexey Gladkov <legion@altlinux.ru> 4.4.4-alt2
- Bugfix rebuild.
- Relax Requires/BuildRequires.

* Wed Aug 23 2006 Alexey Gladkov <legion@altlinux.ru> 4.4.4-alt1
- new version (4.4.4)

* Mon Jun 26 2006 Alexey Gladkov <legion@altlinux.ru> 4.4.3.cvs20060626-alt1
- first build for ALT Linux
