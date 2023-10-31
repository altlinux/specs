%define _unpackaged_files_terminate_build 1
%define m_distro Data-TreeDumper
Name: perl-Data-TreeDumper
Version: 0.41
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

# demo
rm -f %buildroot%_bindir/*.pl %buildroot%perl_vendor_privlib/Data/*.pl

%files
%perl_vendor_privlib/Data/TreeDumper*
%doc Todo README

%changelog
* Tue Oct 31 2023 Igor Vlasenko <viy@altlinux.org> 0.41-alt1
- new version

* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 0.40-alt2
- fixed unpackaged files

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1
- automated CPAN update

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt2
- Added perl-Class-ISA to buildrequires to fix build with perl 5.12

* Tue Aug 24 2010 Vladimir Lettiev <crux@altlinux.ru> 0.37-alt1
- initial build
