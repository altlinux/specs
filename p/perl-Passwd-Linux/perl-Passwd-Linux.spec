%define dist Passwd-Linux
Name: perl-%dist
Version: 1.2
Release: alt4.1

Summary: Perl module for manipulating the passwd and shadow files
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Passwd::Linux provides additional password routines.  It augments
the getpw* functions with setpwinfo, modpwinfo, rmpwnam, mgetpwnam.
You need to run the functions as root or as someone who has permission
to read/modify the shadow file.

%prep
%setup -q -n %dist-%version

# need root
mv test.pl test.pl.orig

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Passwd
%perl_vendor_autolib/Passwd

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.2-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.2-alt2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2-alt1.1.1
- rebuilt with perl 5.12

* Tue Oct 07 2008 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- NMU: fix for perlarchdir ownership

* Thu Dec 13 2007 Igor Zubkov <icesik@altlinux.org> 1.2-alt1
- first build for ALT Linux Sisyphus
