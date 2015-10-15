Name: perl-JavaScript-Value-Escape
Version: 0.07
Release: alt1
Summary: JavaScript::Value::Escape - Avoid XSS with JavaScript value interpolation

Group: Development/Perl
License: Perl
Url: %CPAN JavaScript-Value-Escape

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Install perl-Module-Install-AuthorTests perl-Module-Install-Repository

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/JavaScript/Value/Escape.pm
%doc Changes README*

%changelog
* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- initial build
