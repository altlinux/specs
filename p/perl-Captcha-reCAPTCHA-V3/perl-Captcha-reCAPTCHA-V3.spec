%define _unpackaged_files_terminate_build 1
# tests need network and google.com
%define _without_test 1
%define module_name Captcha-reCAPTCHA-V3
Name: perl-%module_name
Version: 0.05
Release: alt1
Summary: A Perl implementation of reCAPTCHA API version v3
Group: Development/Perl
License: perl
URL: https://github.com/worthmine/Captcha-reCAPTCHA-V3

Source0: http://www.cpan.org/authors/id/W/WO/WORTHMINE/%{module_name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: perl-HTTP-Tiny perl(LWP/UserAgent.pm)
BuildRequires: perl-JSON
BuildRequires: perl-Module-Build-Tiny

%description
Captcha::reCAPTCHA::V3 - A Perl implementation of reCAPTCHA API version v3

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md
%perl_vendor_privlib/C*
%perl_vendor_privlib/auto/*

%changelog
* Thu Jan 27 2022 Igor Vlasenko <viy@altlinux.org> 0.05-alt1
- automated CPAN update

* Sat Jan 08 2022 Igor Vlasenko <viy@altlinux.org> 0.04-alt1
- automated CPAN update

* Sat Jan 01 2022 Igor Vlasenko <viy@altlinux.org> 0.03-alt1
- automated CPAN update

* Thu Oct 01 2020 Oleg Solovyov <mcpain@altlinux.org> 0.01-alt1
- initial build for ALT (ported from autoimports)

