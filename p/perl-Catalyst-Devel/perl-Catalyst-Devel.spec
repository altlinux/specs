%define dist Catalyst-Devel
Name: perl-%dist
Version: 1.34
Release: alt1

Summary: Catalyst Development Tools
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/Catalyst-Devel/
Source: http://www.cpan.org/authors/id/B/BO/BOBTFISH/Catalyst-Devel-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Jan 16 2011 (-bi)
BuildRequires: perl-Catalyst-Runtime perl-Class-C3 perl-Config-General perl-File-ChangeNotify perl-File-Copy-Recursive perl-File-ShareDir perl-Module-Install perl-Template perl-Test-Exception perl-Test-Pod perl-Test-Pod-Coverage perl(Test/Fatal.pm)

%description
The Catalyst::Devel package includes a variety of modules useful
for the development of Catalyst applications, but not required
to run them. This is intended to make it easier to deploy
Catalyst apps. The runtime parts of Catalyst are now known as
Catalyst::Runtime.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Catalyst*
%perl_vendor_privlib/Module*
%dir %perl_vendor_privlib/auto
%dir %perl_vendor_privlib/auto/share
%dir %perl_vendor_privlib/auto/share/dist
%dir %perl_vendor_privlib/auto/share/dist/%dist
%perl_vendor_privlib/auto/share/dist/%dist/*

%changelog
* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Sun Jan 16 2011 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.28 -> 1.30
- packaged /usr/share/perl5/auto/share/dist/Catalyst-Devel/*

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.08 -> 1.27

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.08-alt2
- fix directory ownership violation

* Mon Jul 14 2008 Michael Bochkaryov <misha@altlinux.ru> 1.08-alt1
- 1.08 version build
- spec file cleanup
- buildreq updated

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 1.02-alt1
- first build for ALT Linux Sisyphus

