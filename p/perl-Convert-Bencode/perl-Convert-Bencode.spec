Name: perl-Convert-Bencode
Version: 1.03
Release: alt1

Summary: Convert::Bencode - Functions for converting to/from bencoded strings
Group: Development/Perl
License: Perl

Url: %CPAN Convert-Bencode
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Convert/Bencode*
%doc LICENSE Changes Todo README 

%changelog
* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- initial build
