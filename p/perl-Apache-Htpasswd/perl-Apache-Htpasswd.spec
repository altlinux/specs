%define dist Apache-Htpasswd

Name: perl-%dist
Version: 1.8
Release: alt2

Summary: This module comes with a set of methods to use with htaccess password files.
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Wed Feb 04 2009
BuildRequires: perl-Digest-SHA1 perl-devel

%description
This module comes with a set of methods to use with htaccess password
files. These files (and htaccess) are used to do Basic Authentication on
a web server.
The passwords file is a flat-file with login name and their associated
crypted password. You can use this for non-Apache files if you wish, but
it was written specifically for .htaccess style files.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README

%perl_vendor_privlib/Apache/Htpasswd.pm

%changelog
* Tue Nov 16 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.8-alt2
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec

* Wed Feb 04 2009 Sergey Y. Afonin <asy@altlinux.ru> 1.8-alt1
- Initial build for ALTLinux.
