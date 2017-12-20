%define m_distro Test-Script
Name: perl-Test-Script
Version: 1.23
Release: alt1
Summary: Test::Script - Basic cross-platform tests for scripts

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~adamk/Test-Script/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-IPC-Run3 perl-Probe-Perl perl(Test/Tester.pm) perl(Test2/V0.pm) perl(Capture/Tiny.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc author.yml LICENSE README Changes
%perl_vendor_privlib/Test/Script*
%doc Changes README

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Tue Jan 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.07-alt1
- initial build
