Name: perl-HTML-Shakan
Version: 0.15
Release: alt1

Summary: HTML::Shakan - form html generator/validator
Group: Development/Perl
License: Perl

Url: %CPAN HTML-Shakan
# Cloned from git://github.com/tokuhirom/html-shakan.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Mouse perl-FormValidator-Lite perl-Test-Requires perl-List-MoreUtils perl-parent perl-Any-Moose perl-CGI perl-HTML-Scrubber perl-Lingua-JA-Regular-Unicode perl-DateTime perl-DateTime-Format-HTTP perl-Module-Build

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/Shakan*
# under construction
%exclude %perl_vendor_privlib/HTML/Shakan/Widgets/jQueryUI.pm
%doc TODO Changes

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- 0.15

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
