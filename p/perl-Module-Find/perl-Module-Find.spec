Packager: Michael Bochkaryov <misha@altlinux.ru>

%define dist Module-Find

Name: perl-Module-Find
Version: 0.15
Release: alt1

Summary: Module::Find - Find and use installed modules in a (sub)category

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/C/CR/CRENZ/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Mar 23 2007 (-bi)
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Module::Find lets you find and use modules in categories. This can be very
useful for auto-detecting driver or plugin modules. You can differentiate
between looking in the category itself or in all subcategories.

If you want Module::Find to search in a certain directory on your
harddisk (such as the plugins directory of your software installation),
make sure you modify @INC before you call the Module::Find functions.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/Module/Find.pm

%changelog
* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Sep 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- 0.10 -> 0.11
- spec cleanup

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Apr 23 2008 Michael Bochkaryov <misha@altlinux.ru> 0.06-alt1
- updated to 0.06 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 0.05-alt1
- first build for ALT Linux Sisyphus

