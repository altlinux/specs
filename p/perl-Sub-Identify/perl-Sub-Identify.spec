%define dist Sub-Identify
Name: perl-%dist
Version: 0.04
Release: alt1.3

Summary: Retrieve names of code references
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod

%description
Sub::Identify allows you to retrieve the real name of code references.
For this, it uses perl's introspection mechanism, provided by the B module.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Sub
%perl_vendor_autolib/Sub

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.3
- rebuilt for perl-5.14

* Fri Nov 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1.2
- new release

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 0.04-alt1.1
- rebuilt for perl-5.12

* Fri Nov 13 2009 Michael Bochkaryov <misha@altlinux.ru> 0.04-alt1
- 0.04 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU fixing directory ownership violation

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- first build for ALT Linux Sisyphus
