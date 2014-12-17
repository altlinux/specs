Name: perl-HTML-Shakan
Version: 2.00
Release: alt1

Summary: HTML::Shakan - form html generator/validator
Group: Development/Perl
License: Perl

Url: %CPAN HTML-Shakan
# Cloned from git://github.com/tokuhirom/html-shakan.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Mouse perl-FormValidator-Lite perl-Test-Requires perl-List-MoreUtils perl-parent perl-Any-Moose perl-CGI perl-HTML-Scrubber perl-Lingua-JA-Regular-Unicode perl-DateTime perl-DateTime-Format-HTTP perl-Module-Build perl(HTML/Escape.pm) perl(Hash/MultiValue.pm)

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
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- 0.15

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- initial build
