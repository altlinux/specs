%define dist Net-Amazon-EC2
Name: perl-%dist
Version: 0.14
Release: alt3

Summary: Perl interface to the Amazon Elastic Compute Cloud (EC2)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Digest-HMAC perl-Moose perl-Params-Validate perl-XML-Simple perl-devel perl-libwww

%description
This module is a Perl interface to Amazon's Elastic Compute Cloud.
It uses the Query API to communicate with Amazon's Web Services framework.

%prep
%setup -q -n %dist-%version
rm -fv lib/Net/Amazon/._EC2.pm

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/Net

%changelog
* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt3
- updated build dependencies

* Wed Sep 15 2010 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt2
- remove MacOS X resource fork file

* Sat Sep 04 2010 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt1
- initial build for ALT Linux Sisyphus
