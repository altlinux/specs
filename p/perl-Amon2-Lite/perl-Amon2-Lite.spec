Name: perl-Amon2-Lite
Version: 0.07
Release: alt1

Summary: Amon2::Lite - Sinatra-ish framework on Amon2
Group: Development/Perl
License: Perl

Url: %CPAN Amon2-Lite
Source: %name-%version.tar

BuildRequires: perl-Module-Build perl-Amon2 perl-Test-Requires perl-Data-Section-Simple perl-Text-Xslate-Bridge-TT2Like

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Amon2/Lite*
%perl_vendor_privlib/Amon2/Setup/Flavor/Lite.pm
%doc LICENSE Changes

%changelog
* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build
