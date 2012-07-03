%define php5_name      php5
%define _php5_version  5.3.10
%define _php5_major  5.3
%define _php5_snapshot 20120202
%define php5_release   alt1

%define rpm_build_version %_php5_version%([ -z "%_php5_snapshot" ] || echo ".%_php5_snapshot")

Name:		rpm-build-%php5_name
Version:	%rpm_build_version
Release:	%php5_release
Summary:	RPM helper macros to rebuild PHP5 packages

Group:		Development/Other
License:	GPL
BuildArch:	noarch
Source0:	php.rpm.macros.standalone

Conflicts:	php5-devel < 5.1.2.cvs20051203

%description
These helper macros provide possibility to rebuild
PHP5 packages by some Alt Linux Team Policy compatible way.

%install
mkdir -p %buildroot/%_sysconfdir/rpm/macros.d
cp %SOURCE0 %buildroot/%_sysconfdir/rpm/macros.d/%php5_name

subst 's,@php5_name@,%php5_name,'           %buildroot/%_sysconfdir/rpm/macros.d/%php5_name
subst 's,@_php5_version@,%_php5_version,'   %buildroot/%_sysconfdir/rpm/macros.d/%php5_name
subst 's,@php5_major@,%_php5_major,'   %buildroot/%_sysconfdir/rpm/macros.d/%php5_name
subst 's,@_php5_snapshot@,%_php5_snapshot,' %buildroot/%_sysconfdir/rpm/macros.d/%php5_name
subst 's,@php5_release@,%php5_release,'     %buildroot/%_sysconfdir/rpm/macros.d/%php5_name

%files
%_sysconfdir/rpm/macros.d/%php5_name

%changelog
* Fri Feb 10 2012 Anton Farygin <rider@altlinux.ru> 5.3.10.20120202-alt1
- new version

* Mon Sep 12 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt2
- next PHP build

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 5.3.8.20110823-alt1
- new version

* Fri Mar 24 2011 Anton Farygin <rider@altlinux.ru> 5.3.6.20110317-alt1
- new version

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 5.3.5.20110105-alt3
- new php build

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt2
- new php build

* Mon Feb 07 2011 Anton Farygin <rider@altlinux.ru> 5.3.5.20110105-alt1
- new version

* Fri Dec 10 2010 Anton Farygin <rider@altlinux.ru> 5.3.4.20101210-alt1
- new version

* Sat Oct 23 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt3
- new php build

* Wed Sep 22 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt2
- new php build

* Thu Aug 12 2010 Anton Farygin <rider@altlinux.ru> 5.3.3.20100722-alt1
- new version
- use major PHP version for versioning config files

* Wed Aug 04 2010 Anton Farygin <rider@altlinux.ru> 5.2.14.20100721-alt1
- new version

* Mon Mar 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.13.20100205-alt1
- new version

* Fri Feb 05 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt5
- bump php_release for new php5 build

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt4
- bump php_release for new php5 build

* Sat Jan 30 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt3
- bump php_release for new php5 build

* Fri Jan 29 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt2
- bump php_release for new php5 build

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 5.2.12.20091216-alt1
- new version
- minor spec cleanup (Sergey Kurakin)

* Wed Jul 22 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.11.20090722-alt1
- new cvs snapshot.

* Fri Feb 06 2009 Alexey Gladkov <legion@altlinux.ru> 5.2.9.20090205-alt1
- new cvs snapshot.

* Sat Sep 20 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080920-alt1
- new cvs snapshot.

* Sun Jun 29 2008 Alexey Gladkov <legion@altlinux.ru> 5.2.7.20080627-alt1
- new version.

* Sun May 13 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.2-alt1
- new version (5.2.2).

* Mon Apr 09 2007 Konstantin A. Lepikhov <lakostis@altlinux.org> 5.2.1-alt2
- bump php_release due libmm soname changes.
- remove rpm-build release (it gives more problems than benefits).

* Sun Mar 04 2007 L.A. Kostis <lakostis@altlinux.ru> 5.2.1-alt1
- new version (5.2.1).

* Wed Nov 08 2006 Alexey Gladkov <legion@altlinux.ru> 5.2.0-alt1
- new version (5.2.0)

* Thu Oct 19 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.6-alt1
- new version (5.1.6)

* Fri Aug 18 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.5-alt1
- new version (5.1.5)

* Fri Aug 11 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.4-alt1
- new version.
- removed cvs hardcode from _php5_snapshot.

* Sun Jan 22 2006 Alexey Gladkov <legion@altlinux.ru> 5.1.3.cvs20060122-alt1
- new version
- new macros - php5_env
- %%php5_sapi_preun delete .rpmnew .phpnew files before the package
  remove

* Mon Dec 26 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt2
- macros bugfix.

* Fri Dec 23 2005 Alexey Gladkov <legion@altlinux.ru> 5.1.2.cvs20051203-alt1
- first build for ALT linux.
