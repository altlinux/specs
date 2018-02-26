%define dist Proc-ProcessTable
Name: perl-%dist
Version: 0.45
Release: alt1.2

Summary: Perl extension to access the unix process table
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# mount /proc in hasher
BuildRequires: /proc

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Perl interface to the unix process table.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Proc
%perl_vendor_autolib/Proc

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.45-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt1.1
- rebuilt with perl 5.12

* Wed Apr 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1
- first build for ALT Linux Sisyphus
