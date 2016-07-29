%define m_distro CPAN-Checksums
Name: perl-CPAN-Checksums
Version: 2.12
Release: alt1
Summary: CPAN::Checksums - Write a "CHECKSUMS" file for a directory as on CPAN

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~andk/CPAN-Checksums/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-Data-Compare perl-Digest-SHA perl-devel perl-Compress-Zlib perl-Compress-Bzip2
# Tests
BuildRequires: perl-Test-Pod-Coverage perl-Test-Pod

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CPAN/Checksums*
%doc README 

%changelog
* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.12-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.11-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.10-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.09-alt1
- automated CPAN update

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 2.08-alt1
- automated CPAN update

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 2.07-alt1
- New version 2.07

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 2.06-alt1
- New version 2.06

* Thu Jan 28 2010 Vladimir Lettiev <crux@altlinux.ru> 2.05-alt1
- initial build
