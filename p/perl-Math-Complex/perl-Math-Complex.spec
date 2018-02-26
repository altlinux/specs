Name: perl-Math-Complex
Version: 1.59
Release: alt1

Summary: Math::Complex - complex numbers and associated mathematical functions
Group: Development/Perl
License: Perl

Url: %CPAN Math-Complex
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
%perl_vendor_privlib/Math/*
%doc TODO ChangeLog 

%changelog
* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 1.59-alt1
- 1.59

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.58-alt1
- automated CPAN update

* Tue Nov 02 2010 Vladimir Lettiev <crux@altlinux.ru> 1.56-alt1
- initial build
