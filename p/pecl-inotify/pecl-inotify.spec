%define php5_extension inotify
%define pecl_name inotify

Name: pecl-%pecl_name
Version: 0.1.4
Release: alt6

Summary: The inotify extension allows to use inotify functions in a PHP script

License: PHP
Group: Development/Other
Url: http://pecl.php.net/package/%pecl_name

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://pecl.php.net/get/%pecl_name-%version.tar

BuildPreReq: rpm-build-pecl

# Automatically added by buildreq on Wed Oct 27 2010
BuildRequires: gcc-c++ glibc-devel-static php5-devel re2c

%description
The inotify extension allows to use inotify functions in a PHP script.

%prep
%setup -n %pecl_name-%version

%build
cd %pecl_name-%version
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl_install
%pecl_install_doc CREDITS README

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* Sat Feb 11 2012 Anton Farygin <rider@altlinux.ru> 0.1.4-alt6
- Rebuild with php5-5.3.10.20120202-alt1

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 0.1.4-alt5
- Rebuild with php5-5.3.8.20110823-alt1

* Wed Mar 23 2011 Anton Farygin <rider@altlinux.ru> 0.1.4-alt4
- Rebuild with php5-5.3.6.20110317-alt1

* Wed Mar 02 2011 Anton Farygin <rider@altlinux.ru> 0.1.4-alt3
- Rebuild with php5-5.3.5.20110105-alt2

* Tue Feb 08 2011 Anton Farygin <rider@altlinux.ru> 0.1.4-alt2
- Rebuild with php5-5.3.5.20110105-alt1

* Wed Oct 27 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- initial build for ALT Linux Sisyphus

