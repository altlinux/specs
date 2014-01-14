Name: perl-TOML
Version: 0.92
Release: alt1

Summary: Parser for Tom's Obvious, Minimal Language.
Group: Development/Perl
License: Perl

Url: %CPAN TOML
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl(Text/Balanced.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/TOML*
%doc Changelog README

%changelog
* Tue Jan 14 2014 Vladimir Lettiev <crux@altlinux.ru> 0.92-alt1
- initial build for ALTLinux

