Name: perl-Test-TinyMocker
Version: 0.05
Release: alt1

Summary: a very simple tool to mock external modules
Group: Development/Perl
License: perl

Url: %CPAN Test-TinyMocker
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/TinyMocker*
%doc AUTHORS Changes README

%changelog
* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Thu Aug 22 2013 Vladimir Lettiev <crux@altlinux.ru> 0.03-alt1
- initial build for ALTLinux

