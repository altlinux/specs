Name: perl-HTML-StickyQuery
Version: 0.13
Release: alt1
Summary: HTML::StickyQuery - add sticky QUERY_STRING

Group: Development/Perl
License: Perl
Url: %CPAN HTML-StickyQuery

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-HTML-Parser perl-URI perl-parent perl-Module-Install perl-Module-Install-Repository perl-Module-Install-AuthorTests perl-CGI

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/StickyQuery.pm
%doc Changes README 

%changelog
* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- initial build
