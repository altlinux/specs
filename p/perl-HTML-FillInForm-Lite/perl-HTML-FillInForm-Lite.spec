Name: perl-HTML-FillInForm-Lite
Version: 1.14
Release: alt1

Summary: HTML::FillInForm::Lite - Fills in HTML forms with data
Group: Development/Perl
License: Perl

Url: %CPAN HTML-FillInForm-Lite
# Cloned from git://github.com/gfx/p5-HTML-FillInForm-Lite.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build-Tiny perl-CGI perl-autodie perl-Encode-JP perl(Test/Requires.pm)

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/FillInForm/Lite*
%doc Changes README.md

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.10-alt1
- 1.09 -> 1.10

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1
- initial build
