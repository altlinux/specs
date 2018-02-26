%define m_distro Data-TreeDumper
Name: perl-Data-TreeDumper
Version: 0.40
Release: alt1
Summary: dumps any data structure

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~nkh/Data-TreeDumper/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Check-ISA perl-Term-Size perl-Sort-Naturally perl-Class-ISA

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Data/TreeDumper*
%doc Changes Todo README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt2
- Added perl-Class-ISA to buildrequires to fix build with perl 5.12

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt1
- initial build
