# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(DBI.pm) perl(Date/Manip.pm) perl(DateTime/Duration.pm) perl(DateTime/Format/Builder.pm) perl(DateTime/Infinite.pm) perl(DateTime/LeapSecond.pm) perl(DateTime/TimeZone.pm) perl(File/Spec/Functions.pm) perl(List/MoreUtils.pm) perl(Math/BigInt.pm) perl(Module/Build.pm) perl(Module/Pluggable.pm) perl(Params/Validate.pm) perl(Test/MockTime.pm) perl(Test/NoWarnings.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-IBeat
Version:        0.161        
Release:        alt2_15
Summary:        Format times in .beat notation 

Group:          Development/Perl
License:        GPL+ or Artistic 
URL:            http://search.cpan.org/dist/DateTime-Format-IBeat
Source0: http://search.cpan.org/CPAN/authors/id/E/EM/EMARTIN/DateTime-Format-IBeat-%{version}.tar.gz

BuildArch:      noarch 
BuildRequires:  perl(Class/ISA.pm)
BuildRequires:  perl(DateTime.pm) perl(Test/More.pm)
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
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w %{buildroot}/*


%check
make test


%files
%doc Artistic COPYING LICENSE Changes README
%{perl_vendor_privlib}/*


%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt2_15
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt1_15
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.161-alt1_13
- fc import

