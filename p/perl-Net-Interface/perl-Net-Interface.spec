%define dist Net-Interface

Name: perl-%dist
Version: 1.012
Release: alt2
Packager: Sergey Y. Afonin <asy@altlinux.ru>

Summary: Perl extension to access network interfaces
License: %perl_license
Group: Development/Perl

Url: %CPAN %dist
Source: %dist-%version.tar.gz

Patch100: Net-Interface-1.012-overflow.patch

BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-devel

%description
Net::Interface is a module that allows access to the host
network interfaces in a manner similar to ifconfig(8).

%prep
%setup -q -n %dist-%version

%patch100 -p0

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes
%perl_vendor_archlib/Net*
%perl_vendor_autolib/Net*

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 1.012-alt2
- rebuilt for perl-5.14

* Wed Apr 06 2011 Sergey Y. Afonin <asy@altlinux.ru> 1.012-alt1
- New version
- Attempt to fix "Always overflow destination buffer" in code for IPv6
  (untested patch; CPAN bug 57658)

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1.1
- rebuilt with perl 5.12

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.09-alt1
- New version
- fixed directory ownership violation

* Mon May 07 2007 Sergey Y. Afonin <asy@altlinux.ru> 0.08-alt1
- New version

* Tue Jul 27 2004 Alexander V. Denisov <rupor at altlinux dot ru> 0.04.1-alt1
- Initial build for ALTLinux
