%define m_distro Test-HexString
Name: perl-Test-HexString
Version: 0.03
Release: alt1
Summary: Test::HexString test binary strings with hex dump diagnostics

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~pevans/Test-HexString/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Module-Build

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/HexString*
%doc LICENSE Changes README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt1
- initial build
