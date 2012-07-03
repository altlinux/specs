%define dist MooseX-LazyRequire
Name: perl-%dist
Version: 0.07
Release: alt1

Summary: Required attributes which fail only when trying to use them
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-MooseX-Types perl-Test-Exception perl-aliased perl-namespace-autoclean

%description
This module adds a lazy_required option to Moose attribute declarations.

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
* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- initial revision
