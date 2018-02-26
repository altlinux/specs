%define m_distro DateTime-Format-HTTP
Name: perl-DateTime-Format-HTTP
Version: 0.40
Release: alt1
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
* Sat Jul 30 2011 Vladimir Lettiev <crux@altlinux.ru> 0.40-alt1
- initial build
