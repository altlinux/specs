# vim: set ft=spec: -*- rpm-spec -*-
%define php5_extension pam

Name: pecl-%php5_extension
Version: 1.0.3
Release: alt%php5_version.%php5_release

Summary: PAM integration
License: PHP
Group: Development/Other

Url: http://pecl.php.net/package/%php5_extension

# Source: http://pecl.php.net/get/%php5_extension-%version.tgz
Source: %name-%version.tar

Requires: pear-core

BuildRequires(pre): rpm-build-pecl
BuildRequires: php5-devel
BuildPreReq: pear-core
BuildPreReq: libpam0-devel

%description
This extension provides PAM (Pluggable Authentication Modules)
integration. PAM is a system of libraries that handle the authentication
tasks of applications and services. The library provides a stable API
for applications to defer to for authentication tasks.

%prep
%setup -c
cd %php5_extension-%version

%build
cd %php5_extension-%version
phpize
%pecl_configure '--with-php-config=%_bindir/php-config'
%make_build

%install
%pecl_install
%pecl_install_doc CREDITS README

%check
cd %php5_extension-%version
%make test

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Wed Nov 14 2012 Anton Farygin <rider@altlinux.ru> 1.0.3-alt3
- Rebuild with php5-5.3.18.20121017-alt1

* Tue Oct 02 2012 Anton Farygin <rider@altlinux.ru> 1.0.3-alt2
- Rebuild with php5-devel-5.3.17.20120913-alt1

* Fri May 04 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.3-alt1
- Initial build for ALT Linux Sisyphus
