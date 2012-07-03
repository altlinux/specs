%define dist MooseX-Types-Structured
Name: perl-%dist
Version: 0.28
Release: alt1

Summary: Structured Type Constraints for Moose
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Devel-PartialDump perl-MooseX-Types-DateTime perl-Test-Fatal

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.28-alt1
- initial revision
