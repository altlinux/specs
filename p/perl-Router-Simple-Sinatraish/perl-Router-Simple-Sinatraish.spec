Name: perl-Router-Simple-Sinatraish
Version: 0.03
Release: alt1

Summary: Router::Simple::Sinatraish - Sinatra-ish routers on Router::Simple
License: Perl
Group: Development/Perl

Url: %CPAN Router-Simple-Sinatraish
# CLoned from git://github.com/tokuhirom/Router-Simple-Sinatraish.git
Source: %name-%version.tar

BuildRequires: perl-devel perl-parent perl-Router-Simple perl-YAML perl-Module-Build perl-Test-Perl-Critic perl-Class-Accessor perl-Module-Pluggable
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
%perl_vendor_privlib/Router/Simple/Sinatraish.pm
%doc Changes LICENSE

%changelog
* Sun Sep 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1
- 0.02 -> 0.03

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
