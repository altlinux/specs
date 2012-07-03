%define dist Readonly-XS

Name: perl-%dist
Version: 1.05
Release: alt1.2

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Companion module for perl-Readonly
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Readonly/%dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Readonly perl-devel

%description
Readonly::XS is a companion module for Readonly, to speed up read-only
scalar variables.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Readonly
%perl_vendor_autolib/Readonly

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1.2
- rebuilt for perl-5.14
- disabled dependency on perl-Readonly

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Mon Jul 13 2009 Victor Forsyuk <force@altlinux.org> 1.05-alt1
- 1.05

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.04-alt1
- Initial build.
