Name: perl-Amon2-Lite
Version: 0.08
Release: alt1

Summary: Amon2::Lite - Sinatra-ish framework on Amon2
Group: Development/Perl
License: Perl

Url: %CPAN Amon2-Lite
# Cloned from git://github.com/tokuhirom/Amon2-Lite.git
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
* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- 0.07 -> 0.08

* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1
- initial build
