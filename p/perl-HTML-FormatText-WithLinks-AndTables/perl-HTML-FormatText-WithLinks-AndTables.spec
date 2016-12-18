# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-FormatText-WithLinks-AndTables
Version:        0.07
Release:        alt1
Summary:        Converts HTML to Text with tables in tact
License:        Artistic 2.0
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-FormatText-WithLinks-AndTables/
BuildArch:      noarch

Source:        http://www.cpan.org/authors/id/D/DA/DALEEVANS/HTML-FormatText-WithLinks-AndTables-%{version}.tar.gz

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/FormatText/WithLinks.pm)
BuildRequires:  perl(HTML/TreeBuilder.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info

%description
This module was inspired by HTML::FormatText::WithLinks which has proven to
be a useful "lynx -dump" work-alike. However one frustration was that no
other HTML converters I came across had the ability to deal effectively
with HTML <TABLE>s. This module can in a rudimentary sense do so. The aim
was to provide facility to take a simple HTML based email template, and to
also convert it to text with the <TABLE> structure intact for inclusion as
"multi-part/alternative" content. Further, it will preserve both the
formatting specified by the <TD> tag's "align" attribute, and will also
preserve multi-line text inside of a <TD> element provided it is broken
using <BR/> tags.

%prep
%setup -q -n HTML-FormatText-WithLinks-AndTables-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README.pod
%{perl_vendor_privlib}/*

%changelog
* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_9
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_6
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_5
- update to new release by fcimport

* Tue Mar 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_3
- build for Sisyphus

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_5
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_3
- fc import

