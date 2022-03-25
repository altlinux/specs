%define _unpackaged_files_terminate_build 1
%define dist POE
Name: perl-%dist
Version: 1.370
Release: alt1

Summary: Portable multitasking and networking framework for any event loop
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/B/BI/BINGOS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Curses perl-IO-Stty perl-IO-Tty perl-Term-Cap perl-Term-ReadKey perl-devel perl-libwww perl(IO/Pipely.pm) perl(Test/More.pm)

%description
POE is a framework for cooperative, event driven multitasking and
networking in Perl.  Other languages have similar frameworks.  Python
has Twisted.  TCL has "the event loop".

POE provides a unified interface for several other event loops,
including select(), IO::Poll, Glib, Gtk, Tk, Wx, and Gtk2.  Many of
these event loop interfaces were written by others, with the help of
POE::Test::Loops.  They may be found on the CPAN.

POE achieves its its high degree of portability to different operating
systems and Perl versions by being written entirely in Perl.  CPAN
hosts optional XS modules for POE if speed is more desirable than
portability.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# XXX Can't locate object method "loop_ignore_signal" via package "POE::Kernel"
%define __spec_autodep_custom_pre export PERL5OPT='-I%buildroot%perl_vendor_privlib -MPOE'

%add_findreq_skiplist */POE/Test/Sequence.pm

%files
%doc CHANGES README HISTORY examples
%perl_vendor_privlib/POE*

%changelog
* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 1.370-alt1
- automated CPAN update

* Wed Feb 12 2020 Igor Vlasenko <viy@altlinux.ru> 1.368-alt1
- automated CPAN update

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.367-alt1
- automated CPAN update

* Tue Dec 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.358-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.356-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.354-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 1.312-alt1
- 1.289 -> 1.312

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.289-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.289-alt1
- automated CPAN update

* Thu Oct 15 2009 Michael Bochkaryov <misha@altlinux.ru> 1.280-alt1
- 1.280 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1.1
- NMU fixing directory ownership violation

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 1.003-alt1
- 1.003 version

* Tue May 20 2008 Michael Bochkaryov <misha@altlinux.ru> 1.0002-alt1
- first build for ALT Linux Sisyphus
