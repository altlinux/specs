%define dist Sane
Name: perl-%dist
Version: 0.05
Release: alt1

Summary: Perl extension for the SANE (Scanner Access Now Easy) Project

License: GPL or Artistic
Group: Development/Perl
URL: %CPAN %dist

Source: http://search.cpan.org/CPAN/authors/id/R/RA/RATCLIFFE/%dist-%version.tar

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libsane-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-Test-Pod

%description
Perl bindings for the SANE (Scanner Access Now Easy) Project.
This module allows you to access SANE-compatible scanners in a Perlish and
object-oriented way, freeing you from the casting and memory management in C,
yet remaining very close in spirit to original API.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Sane*
%perl_vendor_autolib/Sane

%changelog
* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 0.05-alt1
- new version 0.05 (with rpmrb script)

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt1.2
- rebuilt for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1.1
- rebuilt with perl 5.12

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 0.03-alt1
- initial build for ALT Linux Sisyphus
