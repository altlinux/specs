Name: perl-Text-Xslate-Bridge-TT2Like
Version: 0.00010
Release: alt1
Summary: Text::Xslate::Bridge::TT2Like - TT2 Variable Method Clone For Text::Xslate

Group: Development/Perl
License: Perl
Url: %CPAN Text-Xslate-Bridge-TT2Like

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Text-Xslate perl-Module-Install perl-Module-Install-AuthorTests perl-Mouse perl-Test-Requires

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Text/Xslate/Bridge/TT2Like.pm
%doc Changes 

%changelog
* Sun Dec 04 2011 Vladimir Lettiev <crux@altlinux.ru> 0.00010-alt1
- New version 0.00010

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 0.00008-alt1
- initial build
