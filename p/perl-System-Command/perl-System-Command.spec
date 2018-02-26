%define m_distro System-Command
Name: perl-System-Command
Version: 1.04
Release: alt1
Summary: System::Command - Object for running system commands

Group: Development/Perl
License: Perl
Url: %CPAN %m_distro

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-Module-Build

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/System/Command*
%doc Changes README 

%changelog
* Fri Jun 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.04-alt1
- New version 1.0.4

* Thu Jun 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1
- initial build
