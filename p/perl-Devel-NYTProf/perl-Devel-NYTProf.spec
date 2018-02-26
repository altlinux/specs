%define dist Devel-NYTProf
Name: perl-%dist
Version: 4.06
Release: alt2

Summary: Powerful fast feature-rich perl source code profiler
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-JSON-Any perl-Moose perl-Test-Pod perl-Test-Pod-Coverage zlib-devel

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

rm %buildroot%perl_vendor_archlib/Devel/benchmark.pl
rm -rv %buildroot%perl_vendor_archlib/Devel/auto

# disable dependency on Apache
%add_findreq_skiplist */Devel/NYTProf/Apache.pm

%files
%doc Changes README
%_bindir/nytprof*
%_man1dir/nytpro*.1*
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 4.06-alt2
- rebuilt for perl-5.14
- disabled dependency on Apache

* Sat Dec 04 2010 Vladimir Lettiev <crux@altlinux.ru> 4.06-alt1
- New version 4.06

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 4.05-alt1.1
- rebuilt with perl 5.12

* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 4.05-alt1
- New version 4.05

* Mon Aug 23 2010 Vladimir Lettiev <crux@altlinux.ru> 4.04-alt1
- initial build
