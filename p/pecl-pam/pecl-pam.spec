# vim: set ft=spec: -*- rpm-spec -*-
%define php7_extension pam

Name: pecl-%php7_extension
Version: 1.0.3
Release: alt6.%php7_version.%php7_release

Summary: PAM integration
License: PHP
Group: Development/Other

Url: http://pecl.php.net/package/pam

# Source: http://pecl.php.net/get/%php7_extension-%version.tgz
Source: %name-%version.tar

Patch1: pecl-pam-php7.patch

Requires: pear-core

BuildRequires(pre): rpm-build-pecl-php7
BuildRequires: php7-devel
BuildPreReq: pear-core
BuildPreReq: libpam0-devel

%description
This extension provides PAM (Pluggable Authentication Modules)
integration. PAM is a system of libraries that handle the authentication
tasks of applications and services. The library provides a stable API
for applications to defer to for authentication tasks.

%prep
%setup -c
cd %php7_extension-%version
%patch1 -p1

%build
cd %php7_extension-%version
phpize
%pecl7_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl7_install
%pecl7_install_doc CREDITS README

%check
cd %php7_extension-%version
%make test || :

%post
%php7_extension_postin

%preun
%php7_extension_preun

%files
%pecl7_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php7-%php7_version-%php7_release

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- Rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- Rebuild with php5-devel-5.3.17.20120913-alt1

* Fri May 04 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.3-alt1
- Initial build for ALT Linux Sisyphus
