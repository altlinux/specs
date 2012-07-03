Name: perl-Dancer-Template-Xslate
Version: 0.03
Release: alt1

Summary: Dancer::Template::Xslate - Text::Xslate wrapper for Dancer
Group: Development/Perl
License: Perl

Url: %CPAN Dancer-Template-Xslate
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Dancer perl-Text-Xslate perl-Mouse perl-Module-Build

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Dancer/Template/Xslate.pm
%doc LICENSE Changes README

%changelog
* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1
- 0.02 -> 0.03

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- New version 0.02
- Dropped patches

* Mon Aug 08 2011 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt2
- added support for function map

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt1
- initial build
