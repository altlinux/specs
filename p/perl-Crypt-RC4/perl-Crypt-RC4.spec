%define dist Crypt-RC4
Name: perl-%dist
Version: 2.02
Release: alt1

Summary: Perl implementation of the RC4 encryption algorithm
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 25 2011
BuildRequires: perl-devel

%description
A simple implementation of the RC4 algorithm, developed by RSA Security, Inc.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Crypt*

%changelog
* Tue Oct 25 2011 Alexey Tourbin <at@altlinux.ru> 2.02-alt1
- initial revision
