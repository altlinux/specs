%define dist MooseX-Method-Signatures
Name: perl-%dist
Version: 0.37
Release: alt1

Summary: Method declarations with type constraints and no source filter
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Context-Preserve perl-Devel-Declare perl-MooseX-AuthorizedMethods perl-MooseX-LazyRequire perl-MooseX-Meta-TypeConstraint-ForceCoercion perl-MooseX-TransactionalMethods perl-Parse-Method-Signatures perl-Task-Weaken perl-Test-Exception perl-Test-Pod perl-Text-Balanced

%description
Provides a proper method keyword, like "sub" but specifically for making
methods and validating their arguments against Moose type constraints.

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- initial revision
