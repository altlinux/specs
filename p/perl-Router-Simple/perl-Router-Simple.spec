Name: perl-Router-Simple
Version: 0.17
Release: alt1
Summary: Router::Simple perl module

Group: Development/Perl
License: Perl
Url: %CPAN Router-Simple

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-base perl-Class-Accessor perl-parent perl-Module-Install perl-Module-Install-AuthorTests perl-Perl-Critic perl-Test-Perl-Critic perl-Module-Pluggable perl-Class-Accessor-Lite

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Router/Simple*
%doc Changes 

%changelog
* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Sun Jun 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- 0.09 -> 0.14

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
