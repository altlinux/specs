# BEGIN SourceDeps(oneline):
BuildRequires: perl(DateTime/Locale.pm)
# END SourceDeps(oneline)
%define m_distro DateTime-Format-HTTP
Name: perl-DateTime-Format-HTTP
Version: 0.42
Release: alt2
Summary: DateTime::Format::HTTP - Date conversion routines

Group: Development/Perl
License: Perl
Url: %CPAN %m_distro

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-HTTP-Date perl-DateTime perl-Module-Build

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/DateTime/Format/HTTP*
%doc LICENSE Changes README 

%changelog
* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0.42-alt2
- fixed build

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1
- automated CPAN update

* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.40-alt1
- initial build
