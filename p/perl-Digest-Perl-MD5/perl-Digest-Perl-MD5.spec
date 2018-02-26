%define dist Digest-Perl-MD5
Name: perl-%dist
Version: 1.8
Release: alt1

Summary: Perl Implementation of Rivest's MD5 algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-devel

%description
This modules has the same interface as the much faster Digest::MD5.

%prep
%setup -q -n %dist-%version
chmod -c -x lib/Digest/Perl/MD5.pm

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Digest

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 1.8-alt1
- initial revision
