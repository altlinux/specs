Name: perl-Class-Accessor-Lite
Version: 0.05
Release: alt1
Summary: Class::Accessor::Lite - a minimalistic variant of Class::Accessor

Group: Development/Perl
License: Perl
Url: %CPAN Class-Accessor-Lite

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-Module-Install perl-Module-Install-ReadmeFromPod

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Class/Accessor/Lite*
%doc Changes README 

%changelog
* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.05-alt1
- initial build
