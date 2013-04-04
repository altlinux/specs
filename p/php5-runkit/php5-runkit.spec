%define php5_extension runkit

Name: php5-%php5_extension
Version: 1.0.4.git
Release: alt%php5_version.%php5_release

Summary: Runkit extension for PHP

License: BSD like
Group: System/Servers
Url: https://github.com/zenovich/runkit

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildPreReq: rpm-build-pecl

# Automatically added by buildreq on Mon Mar 11 2013
# optimized out: gnu-config libstdc++-devel php5-libs
BuildRequires: gcc-c++ glibc-devel php5-devel re2c

%description
The runkit extension provides means to modify constants,
user-defined functions, and user-defined classes.
It also provides for custom superglobal variables
and embeddable sub-interpreters via sandboxing.

%prep
%setup

%build
phpize
%pecl_configure
%make_build

%install
%pecl_install
%pecl_install_doc README LICENSE

%post
%php5_extension_postin

%preun
%php5_extension_preun

%files
%pecl_files

%changelog
* %(date "+%%a %%b %%d %%Y") %{?package_signer:%package_signer}%{!?package_signer:%packager} %version-%release
- Rebuild with php5-%php5_version-%php5_release

* Mon Mar 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.4.git-alt2
- add postin/preun scripts

* Mon Mar 11 2013 Vitaly Lipatov <lav@altlinux.ru> 1.0.4.git-alt1
- initial build for ALT Linux Sisyphus
