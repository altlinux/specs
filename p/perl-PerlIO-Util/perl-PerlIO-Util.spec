%define dist PerlIO-Util
Name: perl-%dist
Version: 0.72
Release: alt2

Summary: A selection of general PerlIO utilities
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Module-Install perl-autodie perl-threads

%description
PerlIO::Util provides general PerlIO utilities: utility layers and utility
methods.

%prep
%setup -q -n %dist-%version
#rm -rv inc/

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO
%perl_vendor_autolib/PerlIO

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.72-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.71-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1.1
- NMU for unknown reason

* Sat Jun 21 2008 Michael Bochkaryov <misha@altlinux.ru> 0.42-alt1
- first build for ALT Linux Sisyphus
