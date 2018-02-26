%define dist MooseX-TransactionalMethods
Name: perl-%dist
Version: 0.008
Release: alt1

Summary: Syntax sugar for transactional methods
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Moose perl-Pod-Escapes perl-aliased perl-devel

%description
This method exports the "transactional" declarator that will enclose
the method in a txn_do call.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/MooseX

%changelog
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.008-alt1
- initial revision
