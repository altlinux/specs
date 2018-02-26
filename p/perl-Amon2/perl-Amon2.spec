Name: perl-Amon2
Version: 3.35
Release: alt1
Summary: Amon2 - lightweight web application framework

Group: Development/Perl
License: Perl
Url: %CPAN Amon2

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Module-Install perl-Module-Install-Repository perl-Module-Install-AuthorTests perl-Test-Requires perl-Plack perl-Data-OptList perl-MRO-Compat perl-Text-Xslate perl-JSON perl-Module-Find perl-Mouse perl-Router-Simple perl-Router-Simple-Sinatraish perl-Class-Accessor perl-Text-Xslate-Bridge-TT2Like perl-Data-Section-Simple perl-Plack-Middleware-ReverseProxy perl-HTTP-Session perl-HTML-FillInForm-Lite perl-CGI perl-Encode-JP perl-Plack-Middleware-Session

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/amon2-setup.pl
%perl_vendor_privlib/Amon2*
%doc TODO Changes 

%changelog
* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 3.35-alt1
- New version 3.35

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 3.32-alt1
- New version 3.32

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 3.31-alt1
- New version 3.31

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 2.49-alt1
- initial build
