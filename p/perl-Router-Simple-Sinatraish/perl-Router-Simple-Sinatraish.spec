Name: perl-Router-Simple-Sinatraish
Version: 0.02
Release: alt1
Summary: Router::Simple::Sinatraish - Sinatra-ish routers on Router::Simple

Group: Development/Perl
License: Perl
Url: %CPAN Router-Simple-Sinatraish

BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-%release.patch
BuildRequires: perl-devel perl-parent perl-Router-Simple perl-YAML perl-Module-Install perl-Module-Install-AuthorTests perl-Test-Perl-Critic perl-Class-Accessor perl-Module-Pluggable

%description
%summary

%prep
%setup -q
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Router/Simple/Sinatraish.pm
%doc Changes 

%changelog
* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
