%define _unpackaged_files_terminate_build 1
%define dist Term-ANSIColor
Name: perl-Term-ANSIColor
Version: 4.06
Release: alt1

Summary: Color output using ANSI escape sequences
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RR/RRA/Term-ANSIColor-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Aug 06 2011
BuildRequires: perl-devel perl(Module/Build.pm)

%description
Term::ANSIColor provides constants and simple functions for sending ANSI
text attributes, most notably colors.  It can be used to set the current
text attributes or to apply a set of attributes to a string and reset
the current text attributes at the end of that string.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
rm t/pod*.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Term

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 4.06-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 4.05-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 4.04-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 4.03-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 4.02-alt1
- automated CPAN update

* Mon Oct 01 2012 Vladimir Lettiev <crux@altlinux.ru> 3.02-alt1
- 3.01 -> 3.02

* Sat Aug 06 2011 Alexey Tourbin <at@altlinux.ru> 3.01-alt1
- 3.00 -> 3.01

* Tue Sep 21 2010 Alexey Tourbin <at@altlinux.ru> 3.00-alt1
- initial revision, for perl-5.12
