%define dist Tie-Simple
Name: perl-%dist
Version: 1.03
Release: alt1

Summary: Variable ties made easier
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Feb 26 2011
BuildRequires: perl-devel

%description
This module adds the ability to quickly create new types of tie objects
without creating a complete class. It does so in such a way as to try
and make the programmers life easier when it comes to single-use ties.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Tie

%changelog
* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- initial revision
