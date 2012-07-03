%define dist Net-SMTP-TLS
Name: perl-%dist
Version: 0.12
Release: alt1

Summary: An SMTP client supporting TLS and AUTH
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Digest-HMAC perl-IO-Socket-SSL perl-devel

%description
Net::SMTP::TLS is a TLS and AUTH capable SMTP client which offers an
interface that users will find familiar from Net::SMTP.  Net::SMTP::TLS
implements a subset of the methods provided by that module, but certainly
not (yet) a complete mirror image of that API.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Net

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.12-alt1
- initial revision
