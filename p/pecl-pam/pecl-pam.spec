# vim: set ft=spec: -*- rpm-spec -*-

# %%branch_switch set %%branch_release use
#%%define branch_switch Mxx

%define php5_extension pam

Name: pecl-%php5_extension
Version: 1.0.3
Release: %branch_release alt1

Summary: PAM integration
License: PHP
Group: Development/Other

Url: http://pecl.php.net/package/%php5_extension
Packager: Aleksey Avdeev <solo@altlinux.ru>

# Source: http://pecl.php.net/get/%php5_extension-%version.tgz
Source: %name-%version.tar
Source10: %name-alt-makefile-test.patch

Requires: pear-core

BuildRequires(pre): rpm-build-pecl
BuildRequires(pre): rpm-macros-branch
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
patch -p1 <%SOURCE10
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
* Fri May 04 2012 Aleksey Avdeev <solo@altlinux.ru> 1.0.3-alt1
- Initial build for ALT Linux Sisyphus
