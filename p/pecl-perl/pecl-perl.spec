%define php5_extension perl
%define pecl_name perl

Name: pecl-%pecl_name
Version: 1.0.0
Release: alt14

Summary: Embedded Perl

License: PHP
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pecl.php.net/get/%pecl_name-%version.tar.bz2
Patch0: php-5.3-pecl-build.patch

BuildPreReq: rpm-build-pecl

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-devel php5-devel

%description
This extension embeds Perl Interpreter into PHP. It allows execute
Perl files, evaluate Perl code, access Perl variables and instantiate
Perl objects.

%prep
%setup -c
%patch0 -p0

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
>>>>>>> 1.0.0-alt8.1

* Fri Jul 24 2009 Alexey Gladkov <legion@altlinux.ru> 1.0.0-alt2.1
- NMU: Rebuild with php5-5.2.11.20090722-alt1.

* Thu Jul 02 2009 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt2
- rebuild

* Sat Mar 01 2008 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- initial build for ALT Linux Sisyphus

