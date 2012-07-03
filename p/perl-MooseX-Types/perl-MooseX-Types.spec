BuildRequires: perl(Module/Build.pm)
%define dist MooseX-Types
Name: perl-%dist
Version: 0.30
Release: alt1

Summary: Organise your Moose types in libraries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DR/DROLSKY/MooseX-Types-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Dec 22 2010
BuildRequires: perl-Carp-Clan perl-Module-Install perl-Moose perl-Test-Fatal perl-Test-Requires perl-namespace-clean

%description
The types provided with Moose are by design global. This package helps
you to organise and selectively import your own and the built-in types in
libraries. As a nice side effect, it catches typos at compile-time too.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX*

%changelog
* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 0.25-alt1
- 0.22 -> 0.25

* Thu Jun 10 2010 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.21 -> 0.22

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.21-alt1
- initial revision
