%define module Sort-Naturally

Name: perl-%module
Version: 1.03
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Sort::Naturally -- sort lexically, but sort numeral parts numerically
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Aug 07 2009
BuildRequires: perl-devel

%description
Sort::Naturally -- sort lexically, but sort numeral parts numerically.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Sort

%changelog
* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Aug 07 2009 Victor Forsyuk <force@altlinux.org> 1.02-alt1
- Initial build.
