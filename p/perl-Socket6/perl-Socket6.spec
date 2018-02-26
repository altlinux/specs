%define module Socket6

Name: perl-%module
Version: 0.23
Release: alt1.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Socket6 Perl module
License: BSD-like
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Socket6/%module-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
Socket6 is a module that implements a IPv6 API for Perl programs.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_archlib/Socket6.pm
%perl_vendor_autolib/Socket6

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.23-alt1.2
- rebuilt for perl-5.14

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.23-alt1.1
- rebuilt for perl-5.12

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.23-alt1
- 0.23

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 0.22-alt1
- 0.22

* Thu Mar 06 2008 Victor Forsyuk <force@altlinux.org> 0.20-alt1
- 0.20

* Mon Aug 13 2007 Victor Forsyuk <force@altlinux.org> 0.19-alt1
- Initial build.
