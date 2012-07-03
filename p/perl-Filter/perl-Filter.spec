%define dist Filter
Name: perl-%dist
Version: 1.39
Release: alt1

Summary: Source Filters
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
Source filters alter the program text of a module before Perl sees it,
much as a C preprocessor alters the source text of a C program before
the compiler sees it.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
mv t/pod.t t/pod.t.orig
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
%perl_vendor_archlib/Filter
%perl_vendor_autolib/Filter

%changelog
* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.37 -> 1.39
- build for perl-5.14
- rebuilt as palin src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.36 -> 1.37
- built for perl-5.12
- disabled build dependency on perl-Test-Pod

* Tue Mar 03 2009 Alexey Tourbin <at@altlinux.ru> 1.36-alt1
- 1.34 -> 1.36

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 1.34-alt1
- 1.32 -> 1.34
- perlfilter.pod not packaged (a copy in perl-pod is better)

* Wed Feb 28 2007 Alexey Tourbin <at@altlinux.ru> 1.32-alt2
- imported into git and adapted for gear
- replaced DynaLoader with XSLoader
- replaced Perl_ninstr() with memchr(3)

* Mon Aug 07 2006 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.30 -> 1.32

* Tue Dec 14 2004 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- initial revision (split off from perl-base)
