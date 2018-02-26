%define dist Term-Size
Name: perl-%dist
Version: 0.207
Release: alt1.2

Summary: Perl module for get the size of the terminal
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod

%description
Term::Size is a Perl module which provides a straightforward way to get
the size of the terminal (or window) on which a script is running.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Term
%perl_vendor_autolib/Term

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.207-alt1.2
- rebuilt with perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.207-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.207-alt1
- automated CPAN update

* Wed Mar 02 2005 Eugene Vlasov <eugvv@altlinux.ru> 0.2-alt1
- First build for Sisyphus

