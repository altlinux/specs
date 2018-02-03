%define php5_extension perl
%define pecl_name perl

Name: pecl-%pecl_name
Version: 1.0.1
Release: alt23%ubt
# see commit a3d7db22eb7964ea9cb39ea2f866d10df26655d4
# of git://github.com/do-aki/php-ext-perl.git
Patch0: %name-1.0.1-alt-fix_php5.4.patch

Summary: Embedded Perl

License: PHP
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pecl.php.net/get/%pecl_name-%version.tar.bz2

BuildPreReq: rpm-build-pecl
BuildRequires(pre): rpm-build-ubt

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-devel php5-devel

%description
This extension embeds Perl Interpreter into PHP. It allows execute
Perl files, evaluate Perl code, access Perl variables and instantiate
Perl objects.

%prep
%setup -c
%patch -p2

%build
cd %pecl_name-%version
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

# Disabled due disabled proc_open
# make test

%install
%pecl_install
%pecl_install_doc CREDITS EXPERIMENTAL README TODO

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* Wed Jan 31 2018 Anton Farygin <rider@altlinux.ru> 1.0.1-alt23%ubt
- rebuild with php5-5.6.33

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt22%ubt.1
- rebuild with new perl 5.26.1

* Fri Nov 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.1-alt22%ubt
- rebuild with php5-5.6.32

* Fri Jul 07 2017 Anton Farygin <rider@altlinux.ru> 1.0.1-alt21%ubt
- rebuild with php5-5.6.31

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt20%ubt.1
- rebuild with new perl 5.24.1

* Mon Jan 30 2017 Anton Farygin <rider@altlinux.ru> 1.0.1-alt20%ubt
- rebuild with php5-5.6.30

* Wed Dec 14 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt19%ubt
- rebuild with php5-5.6.28

* Wed Nov 16 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt18%ubt
- rebuild with php5-5.6.28

* Mon Oct 17 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt18
- rebuild with php5-5.6.27

* Mon Sep 26 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt17
- Rebuild with php5-5.6.26

* Fri Aug 26 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt16
- rebuild with php5-5.6.25

* Mon Jul 25 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt15
- rebuild with php5-5.6.24

* Mon Jun 27 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt14
- rebuild with php5-5.6.23

* Mon May 30 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt13
- rebuild with php5-5.6.22

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt12
- rebuild with php5-5.6.21

* Tue Apr 05 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt11
- rebuild with php5-5.6.20

* Mon Mar 28 2016 Anton Farygin <rider@altlinux.ru> 1.0.1-alt10
- rebuild with php5-5.6.19

* Mon Dec 21 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt9
- rebuild with php5-5.6.16

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt8.1
- rebuild with new perl 5.22.0

* Mon May 18 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt8
- rebuild with php5-5.5.25

* Fri Apr 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt7
- rebuild with php5-5.5.24

* Tue Feb 24 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt6
- rebuild with php5-5.5.22

* Fri Jan 23 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt5
- rebuild with php5-5.5.21

* Thu Jan 15 2015 Anton Farygin <rider@altlinux.ru> 1.0.1-alt4
- rebuild with php5-5.5.20

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3.1
- rebuild with new perl 5.20.1

* Mon Dec 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt3
- spec fixes for new perl 5.20.1 (dropped prev. changelog -- was always new)

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0.1-alt2.5.3.25.20130509.alt1
- built for perl 5.18

* Tue May 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1.0.1-alt1.5.3.25.20130509.alt1
- New version: 1.0.1

* Mon May 13 2013 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.0-alt17.5.3.25.20130509.alt1
- Rebuild with php5-5.3.25.20130509-alt1

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.0-alt17
- Rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.0-alt16
- Rebuild with PHP 5.3.17.20120913-alt1

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt15
- rebuilt for perl-5.16

* Tue Feb 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.0-alt14
- Rebuild with php5-5.3.8.20110823-alt1

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 1.0.0-alt13
- Rebuilt for perl-5.14

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt12
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt11
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt10
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt9
- Rebuild with php5-5.3.5.20110105-alt1

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0.0-alt8.1
- rebuilt with perl 5.12

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt8
- Rebuild with php5-5.3.3.20100722-alt3

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt7
- Rebuild with php5-5.3.3.20100722-alt2

* Thu Sep 02 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt6
- Rebuild with php5-5.3.3.20100722-alt1

* Thu Aug 05 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt5
- Rebuild with php5-5.2.14.20100721-alt1

* Tue Mar 09 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt4
- Rebuild with php5-5.2.13.20100205-alt1

* Mon Feb 01 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt3
- Rebuild with php5-5.2.12.20091216=alt4

* Thu Jan 28 2010 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2.2
- NMU: Rebuild with php5-5.2.12.20091216=alt1.

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 1.0.0-alt2.1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Thu Jul 02 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- rebuild

* Sat Mar 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus
