Name: perl-Router-Simple
Version: 0.09
Release: alt1
Summary: Router::Simple perl module

Group: Development/Perl
License: Perl
Url: %CPAN Router-Simple

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-base perl-Class-Accessor perl-parent perl-Module-Install perl-Module-Install-AuthorTests perl-Perl-Critic perl-Test-Perl-Critic perl-Module-Pluggable

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
* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
