%define _unpackaged_files_terminate_build 1
%define dist IO-All
Name: perl-%dist
Version: 0.85
Release: alt1

Summary: IO::All of it to Graham and Damian!
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FR/FREW/IO-All-%{version}.tar.gz

BuildArch: noarch

# This dependency is in eval block
Requires: perl-Tie-File

# Automatically added by buildreq on Sun Nov 20 2011
BuildRequires: perl-Encode-TW perl-File-ReadBackwards perl-IO-String perl-MLDBM perl-Pod-Escapes perl-Tie-File perl-devel

%description
IO::All combines all of the best Perl IO modules into a single nifty
object oriented interface to greatly simplify your everyday Perl IO
idioms. It exports a single function called io, which returns a new
IO::All object.

%prep
%setup -q -n %dist-%version
# File::Spec::Win32:
#Can't locate object method "catfile" via package "File::Spec::Win32" at /usr/src/RPM/BUILD/IO-All-0.48/blib/lib/IO/All/Filesys.pm line 22.                     
rm t/os.t 

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IO

%changelog
* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.82-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.75-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- automated CPAN update

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.54-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.51-alt1
- automated CPAN update

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.50-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1
- automated CPAN update

* Sun Nov 20 2011 Alexey Tourbin <at@altlinux.ru> 0.44-alt1
- 0.36 -> 0.44

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.36-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.36-alt2
- fix directory ownership violation

* Tue Mar 20 2007 Vitaly Lipatov <lav@altlinux.ru> 0.36-alt1
- new version, return from orphaned

* Mon Jul 17 2006 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
