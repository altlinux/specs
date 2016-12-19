Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(Moose.pm)
Name:           perl-Config-GitLike
Version:        1.16
Release:        alt1_5
Summary:        Git-compatible config file parsing
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/Config-GitLike/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/Config-GitLike-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(Any/Moose.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(MooX/Types/MooseLike/Base.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/More.pm)


Source44: import.info

%description
This module handles interaction with configuration files of the style used
by the version control system Git. It can both parse and modify these
files, as well as create entirely new ones.

%prep
%setup -q -n Config-GitLike-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_1
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Mon Dec 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_4
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_4
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- update to new release by fcimport

* Wed Jan 09 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_3
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1_1
- fc import

