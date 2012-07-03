%define m_distro PPIx-Utilities
Name: perl-PPIx-Utilities
Version: 1.001000
Release: alt1
Summary: PPIx::Utilities - Extensions to PPI.

Group: Development/Perl
License: Perl
Url: %CPAN %m_distro

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Exception-Class perl-Task-Weaken perl-Readonly perl-PPI perl-Module-Build perl-Test-Deep

%description
%summary

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/PPIx/Utilities*
%doc LICENSE Changes README 

%changelog
* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.001000-alt1
- initial build
