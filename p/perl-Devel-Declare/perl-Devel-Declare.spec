%define dist Devel-Declare
Name: perl-%dist
Version: 0.006008
Release: alt1

Summary: Adding keywords to perl, in perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-B-Hooks-EndOfScope perl-B-Hooks-OP-Check perl-ExtUtils-Depends perl-Pod-Escapes perl-Sub-Name perl-Test-Warn

%description
Devel::Declare can install subroutines called declarators which locally
take over Perl's parser, allowing the creation of new syntax.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.006008-alt1
- initial revision
