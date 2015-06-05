# BEGIN SourceDeps(oneline):
BuildRequires: perl(File/Basename.pm) perl(FileHandle.pm) perl(MIME/Base64.pm) perl(MIME/QuotedPrint.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-mime-construct
Epoch: 1
Version:        1.11
Release:        alt1
Summary:        Construct/send MIME messages from the command line 

Group:          Development/Perl
License:        GPLv2+
URL:            http://search.cpan.org/~rosch/mime-construct-%version
Source0:        http://search.cpan.org/CPAN/authors/id/R/RO/ROSCH/mime-construct-%version.tar.gz

BuildArch:      noarch

BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(MIME/Types.pm)
BuildRequires:  perl(Proc/WaitStat.pm)

%description
mime-construct constructs and (by default) mails MIME messages.
It is entirely driven from the command line, it is designed to be used
by other programs, or people who act like programs.

%prep
%setup -n mime-construct-%version

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor 
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'

%check
%make test

%files
%doc README debian/changelog debian/copyright
%_bindir/*
%_mandir/man?/*

%changelog
* Fri Jun 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.11-alt1
- Built for Sisyphus

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_13
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_12
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_8
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1_6
- fc import

