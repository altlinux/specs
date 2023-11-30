%define dist Test-Dynamic

Name: perl-Test-Dynamic
Version: 1.3.3
Release: alt5

Summary: Advanced automatic test counting for Test::More

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

Packager: Mikhail Pokidko <pma@altlinux.org>

BuildArch: noarch
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: perl-devel perl-Pod-Simple /usr/bin/pod2html

%description
This module helps to count your tests for you in an automatic way. When you add
or remove tests, Test::Dynamic will attempt to keep track of the total correct
number for you.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Test/Dynamic.pm

%changelog
* Thu Nov 30 2023 Igor Vlasenko <viy@altlinux.org> 1.3.3-alt5
- added BR: /usr/bin/pod2html

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt4
- fixed build

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.3.3-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 1.3.3-alt3
- sysiphus_check fixes #2

* Tue Sep 02 2008 Mikhail Pokidko <pma@altlinux.org> 1.3.3-alt2
- sysiphus_check fixes

* Thu May 15 2008 Mikhail Pokidko <pma@altlinux.org> 1.3.3-alt1
- first build for ALT Linux Sisyphus

