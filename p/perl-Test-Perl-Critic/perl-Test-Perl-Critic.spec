%define m_distro Test-Perl-Critic
Name: perl-Test-Perl-Critic
Version: 1.04
Release: alt1
Summary: Test::Perl::Critic - Use Perl::Critic in test programs

Group: Development/Perl
License: Perl
Url: %CPAN %m_distro

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Perl-Critic perl-Module-Build perl-Module-Pluggable perl(MCE/Grep.pm)

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Perl/Critic.pm
%doc LICENSE Changes README

%changelog
* Thu Mar 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.02-alt1
- initial build
