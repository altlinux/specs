%define dist PadWalker
Name: perl-%dist
Version: 1.92
Release: alt1.2

Summary: Inspect lexical variables in any subroutine which called you
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
PadWalker is a module which allows you to inspect (and even change!)
lexical variables in any subroutine which called you. It will only
show those variables which are in scope at the point of the call.

PadWalker is particularly useful for debugging. It's even
used by Perl's built-in debugger. (It can also be used
for evil, of course.)

I wouldn't recommend using PadWalker directly in production
code, but it's your call. Some of the modules that use
PadWalker internally are certainly safe for and useful
in production.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PadWalker*
%perl_vendor_autolib/PadWalker*

%changelog
* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.92-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.92-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.92-alt1
- automated CPAN update

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.9-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.7-alt1.1
- NMU for unknown reason

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 1.7-alt1
- first build for ALT Linux Sisyphus
