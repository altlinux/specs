# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Filter/Util/Call.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(threads/shared.pm) perl-podlators
# END SourceDeps(oneline)
# Only need manual requires for "use base XXX;" prior to rpm 4.9
%global rpm49 0

Name:           perl-Array-Diff
Version:        0.07
Release:        alt2_19
# Because 0.07 compares newer than 0.05002 in Perl world
# but not in RPM world :-(
Epoch:          1
Summary:        Find the differences between two arrays
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Array-Diff/
Source0:        http://www.cpan.org/authors/id/T/TY/TYPESTER/Array-Diff-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Algorithm/Diff.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
%if ! %{rpm49}
Requires:       perl(Class/Accessor/Fast.pm)
%endif
Source44: import.info

%description
This module compares two arrays and returns the added or deleted elements in
two separate arrays. It's a simple wrapper around Algorithm::Diff.

If you need more complex array tools, check Array::Compare.

%prep
%setup -q -n Array-Diff-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT

%check
make test

%files
%doc Changes LICENSE README
%dir %{perl_vendor_privlib}/Array/
%{perl_vendor_privlib}/Array/Diff.pm

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_19
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_18
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_15
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt2_14
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_14
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_13
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_11
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_9
- update to new release by fcimport

* Sun May 27 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.07-alt1_7
- fc import

