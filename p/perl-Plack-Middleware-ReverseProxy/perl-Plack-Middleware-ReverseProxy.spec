Name: perl-Plack-Middleware-ReverseProxy
Version: 0.15
Release: alt1
Summary: Plack::Middleware::ReverseProxy - supports app to run as a reverse proxy backend

Group: Development/Perl
License: Perl
Url: %CPAN Plack-Middleware-ReverseProxy

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-parent perl-Plack perl-YAML perl-Module-Install perl-Module-Install-AuthorTests perl-Module-Install-Repository perl-Test-Base

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Plack/Middleware/ReverseProxy.pm
%doc Changes README 

%changelog
* Sun Jun 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Sat Sep 15 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- 0.09 -> 0.14

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
