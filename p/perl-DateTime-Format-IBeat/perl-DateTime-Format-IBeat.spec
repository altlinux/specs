# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-IBeat
Version:        0.161
Release:        alt2_24
Summary:        Format times in .beat notation 

Group:          Development/Perl
License:        GPL+ or Artistic 
URL:            http://search.cpan.org/dist/DateTime-Format-IBeat
Source0:        http://backpan.perl.org/authors/id/E/EM/EMARTIN/DateTime-Format-IBeat-0.161.tar.gz

BuildArch:      noarch 
BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(DateTime.pm), perl(Test/More.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/Pod.pm)


Source44: import.info

%description
No Time Zones, No Geographical Borders 

How long is a Swatch .beat? In short, we have divided up the virtual and real 
day into 1000 beats. One Swatch beat is the equivalent of 1 minute 26.4 
seconds. That means that 12 noon in the old time system is the equivalent of 
500 Swatch .beats.


%prep
%setup -q -n DateTime-Format-IBeat-%{version}


%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

# American English...
mv LICENCE LICENSE

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
chmod -R u+w %{buildroot}/*


%check
make test


%files
%doc Artistic COPYING LICENSE Changes README
%{perl_vendor_privlib}/*


%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_24
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_23
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_21
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_20
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_19
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_18
- update to new release by fcimport

* Wed Feb 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_17
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_15
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt1_15
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt1_13
- fc import

