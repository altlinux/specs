%define dist Proc-PID-File

Name: perl-%dist
Version: 1.27
Release: alt2

Summary: functions for manipulations with pidfiles
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Mon May 07 2007
BuildRequires: perl-devel

%description
This Perl module is useful for writers of daemons and other processes that
need to tell whether they are already running, in order to prevent multiple
process instances.  The module accomplishes this via *nix-style I<pidfiles>,
which are files that store a process identifier.


%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes

%perl_vendor_privlib/Proc/PID*

%changelog
* Wed Nov 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.27-alt2
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec

* Wed May 12 2010 Sergey Y. Afonin <asy@altlinux.ru> 1.27-alt1
- new version

* Tue Nov 18 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.24-alt3
- added packager

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 1.24-alt2
- fixed directory ownership violation

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 1.24-alt1
- Initial build for ALTLinux 
