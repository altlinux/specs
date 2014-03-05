%define _unpackaged_files_terminate_build 1
%define dist MooseX-Types-Structured
Name: perl-%dist
Version: 0.30
Release: alt1

Summary: Structured Type Constraints for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/MooseX-Types-Structured-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Devel-PartialDump perl-MooseX-Types-DateTime perl-Test-Fatal perl(Module/Build/Tiny.pm)

%description
A structured type constraint is a standard container L<Moose> type constraint,
such as an ArrayRef or HashRef, which has been enhanced to allow you to
explicitly name all the allowed type constraints inside the structure.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/MooseX

%changelog
* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- initial revision
