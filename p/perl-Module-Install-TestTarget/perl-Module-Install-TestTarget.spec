%define m_distro Module-Install-TestTarget
Name: perl-Module-Install-TestTarget
Version: 0.19
Release: alt1
Summary: Module::Install::TestTarget assembles custom test targets for make

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~xaicron/%m_distro/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Module-Install perl-Test-Requires

%description
Module::Install::TestTarget creates make test variations with code
snippets. This helps module developers to test their distributions
with various conditions.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/Install/TestTarget.pm
%doc Changes README 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Thu Feb 17 2011 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt1
- initial build
