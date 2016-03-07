# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Eval-LineNumbers
Version:        0.34
Release:        alt1_6
Summary:        Add line numbers to hereis blocks that contain perl source code
License:        Artistic 2.0 or LGPLv2+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Eval-LineNumbers/
Source0:        http://www.cpan.org/authors/id/M/MU/MUIR/modules/Eval-LineNumbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
This module adds a line number to hereis text that is going to be
eval'ed so that error messages will point back to the right place.

%prep
%setup -q -n Eval-LineNumbers-%{version}
iconv --from=ISO-8859-1 --to=UTF-8 Changes > Changes.utf-8 && mv Changes.utf-8 Changes

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Eval

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1_2
- update to new release by fcimport

* Tue Oct 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1_1
- update to new release by fcimport

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- build for Sisyphus

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_6
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_3
- fc import

