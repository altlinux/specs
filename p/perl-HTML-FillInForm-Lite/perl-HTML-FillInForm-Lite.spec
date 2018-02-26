Name: perl-HTML-FillInForm-Lite
Version: 1.09
Release: alt1
Summary: HTML::FillInForm::Lite - Fills in HTML forms with data

Group: Development/Perl
License: Perl
Url: %CPAN HTML-FillInForm-Lite

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Install perl-Module-Install perl-Module-Install-Repository perl-CGI perl-autodie perl-Encode-JP

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
%doc Changes README 

%changelog
* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1
- initial build
