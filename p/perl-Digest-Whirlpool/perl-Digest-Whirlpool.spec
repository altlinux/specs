%define dist Digest-Whirlpool
Name: perl-%dist
Version: 1.09
Release: alt1.2

Summary: A 512-bit, collision-resistant, one-way hash function
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Pod-Parser perl-Test-Pod

%description
WHIRLPOOL is a 512-bit, collision-resistant, one-way hash function
developed by Paulo S. L. M. Barreto and Vincent Rijmen. It has been
recommended by the NESSIE project (along with SHA-256/384/512) and
adopted as ISO/IEC 10118-3.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README THANKS
%_bindir/whirlpoolsum
%_man1dir/whirlpoolsum.1*
%perl_vendor_archlib/Digest
%perl_vendor_autolib/Digest

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.09-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.09-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1.1
- NMU for unknown reason

* Mon Jun 30 2008 Michael Bochkaryov <misha@altlinux.ru> 1.0.6-alt1
- first build for ALT Linux Sisyphus
