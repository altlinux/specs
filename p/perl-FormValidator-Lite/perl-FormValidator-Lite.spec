Name: perl-FormValidator-Lite
Version: 0.29
Release: alt1

Summary: FormValidator::Lite perl module
Group: Development/Perl
License: Perl

Url: %CPAN FormValidator-Lite
# Cloned from git git://github.com/tokuhirom/formvalidator-lite.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Class-Load perl-Test-Requires perl-CGI perl-Class-Accessor-Lite perl-YAML perl-Module-Build perl-Test-Base perl-unicore perl-Email-Valid-Loose

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/FormValidator/Lite*
%doc TODO Changes

%changelog
* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 0.29-alt1
- New version 0.29

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt1
- initial build
