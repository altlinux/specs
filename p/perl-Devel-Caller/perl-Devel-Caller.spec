%define dist Devel-Caller
Name: perl-%dist
Version: 2.05
Release: alt1.2

Summary: Meatier versions of caller()
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-PadWalker perl-devel

%description
Devel::Caller module provides meatier versions of "caller" function.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.05-alt1.1
- rebuilt with perl 5.12

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.03 -> 2.05

* Mon Jul 21 2008 Michael Bochkaryov <misha@altlinux.ru> 2.03-alt1
- first build for ALT Linux Sisyphus
