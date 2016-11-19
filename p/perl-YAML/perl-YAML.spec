%define _unpackaged_files_terminate_build 1
%define dist YAML
Name: perl-%dist
Version: 1.19
Release: alt1

Summary: YAML Ain't Markup Language
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TI/TINITA/YAML-%{version}.tar.gz
Patch: YAML-1.15-alt-fixes.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-Filter perl-Pod-Escapes perl-URI perl-devel perl(Test/YAML.pm) perl(Test/Base.pm) perl(Test/Base.pm)

%description
The YAML.pm module implements a YAML Loader and Dumper based on the
YAML 1.0 specification.  YAML is a generic data serialization language
that is optimized for human readability.  It can be used to express the
data structures of most modern programming languages (including Perl).

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

# avoid dependency on perl-devel
%add_findreq_skiplist */Test/YAML*

%files
%doc Changes README
%perl_vendor_privlib/YAML*

%changelog
* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.90-alt1
- automated CPAN update

* Mon Feb 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1
- automated CPAN update

* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.88-alt1
- automated CPAN update

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.87-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 0.86-alt1
- automated CPAN update

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.85-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.84-alt1
- 0.77 -> 0.84
- fixed build with perl-5.16 (Closes: #27721)

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.77-alt1
- 0.71 -> 0.77

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.71-alt1
- 0.66 -> 0.71

* Sat May 17 2008 Alexey Tourbin <at@altlinux.ru> 0.66-alt1
- 0.65 -> 0.66

* Sat Aug 18 2007 Alexey Tourbin <at@altlinux.ru> 0.65-alt1
- 0.62 -> 0.65

* Wed Dec 20 2006 Alexey Tourbin <at@altlinux.ru> 0.62-alt1
- 0.60 -> 0.62
- fixed dependency on B::Deparse (cpan #24018)

* Sun Jul 02 2006 Alexey Tourbin <at@altlinux.ru> 0.60-alt1
- 0.58 -> 0.60
- fixed t/bugs-rt.t so that it works with recent CGI.pm

* Thu Apr 20 2006 Alexey Tourbin <at@altlinux.ru> 0.58-alt1
- 0.39 -> 0.58

* Thu Jun 23 2005 Alexey Tourbin <at@altlinux.ru> 0.39-alt1
- 0.36 -> 0.39

* Fri Mar 11 2005 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- 0.35 -> 0.36
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.35-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Apr 27 2004 Alexey Tourbin <at@altlinux.ru> 0.35-alt1
- initial revision
