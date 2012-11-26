Name: perl-Dancer-Session-Cookie
Version: 0.15
Release: alt1

Summary: Encrypted cookie-based session backend for Dancer
Group: Development/Perl
License: perl

Url: %CPAN Dancer-Session-Cookie
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Crypt-CBC perl-devel perl-Test-Exception perl-Dancer perl-String-CRC32 perl-Test-NoWarnings perl-Crypt-Rijndael perl-YAML

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Dancer/Session/Cookie*
%doc Changes README

%changelog
* Mon Nov 26 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- initial build for ALTLinux

