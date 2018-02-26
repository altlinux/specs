%define dist Algorithm-NaiveBayes
Name: perl-%dist
Version: 0.04
Release: alt1

Summary: Bayesian prediction of categories
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Algorithm-NaiveBayes-0.04.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon May 17 2004
BuildRequires: perl-Module-Build perl-devel

%description
This module implements the classic "Naive Bayes" machine learning
algorithm.  It is a well-studied probabilistic algorithm often used
in automatic text categorization.  Compared to other algorithms (kNN,
SVM, Decision Trees), it's pretty fast and reasonably competitive
in the quality of its results.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Algorithm*

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.03-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed May 19 2004 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- 0.02 -> 0.03, Sisyphus release
- license clarified: the same as perl (cpan #6328)

* Mon May 17 2004 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- initial revision (license is unclear, presumably the same as perl)
