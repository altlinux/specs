# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-HTML-Quoted
Version:        0.04
Release:        alt1_9
Summary:        Extract structure of quoted HTML mail message
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/HTML-Quoted/
Source0:        http://www.cpan.org/authors/id/T/TS/TSIBLEY/HTML-Quoted-0.04.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Parser.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)

BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/ReadmeFromPod.pm)
Source44: import.info


%description
Extract structure of quoted HTML mail message.

%prep
%setup -q -n HTML-Quoted-%{version}
rm -r inc

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_4
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- update to new release by fcimport

* Sun May 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_4
- fc import

