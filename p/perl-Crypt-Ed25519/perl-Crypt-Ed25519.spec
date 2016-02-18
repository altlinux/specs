%define dist Crypt-Ed25519

Name: perl-%dist
Version: 1.03
Release: alt1

Summary: bare-bones Ed25519 public key signing/verification system
License: %perl_license
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
# optimized out: perl-devel
BuildRequires: perl-Canary-Stability perl-Encode

%description
bare-bones Ed25519 public key signing/verification system

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 1.03-alt1
- initial build
