%define dist AI-DecisionTree
Name: perl-%dist
Version: 0.11
Release: alt2.1.1.1.1

Summary: Automatically Learns Decision Trees
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-AI-DecisionTree-0.11-alt-GraphViz.patch

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-GraphViz perl-devel

%description
The AI::DecisionTree module automatically creates so-called
"decision trees" to explain a set of training data.  A decision tree
is a kind of categorizer that use a flowchart-like process for
categorizing new instances.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/AI
%perl_vendor_autolib/AI

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- 0.08 -> 0.09
- built for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1.1.1
- rebuilt with perl 5.12

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.08-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- initial revision
