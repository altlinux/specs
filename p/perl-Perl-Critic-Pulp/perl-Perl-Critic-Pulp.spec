%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(AptPkg/Policy.pm) perl(B/Concise.pm) perl(Devel/Mallinfo.pm) perl(Digest/MD5.pm) perl(Encode.pm) perl(Fcntl.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Perl-Critic-Pulp
Version:        96
Release:        alt1
Summary:        Some add-on perlcritic policies
License:        GPLv3+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Perl-Critic-Pulp/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Perl-Critic-Pulp-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Perl/Critic.pm)
BuildRequires:  perl(Perl/Critic/Policy.pm)
BuildRequires:  perl(Perl/Critic/Utils.pm)
BuildRequires:  perl(Perl/Critic/Utils/PPI.pm)
BuildRequires:  perl(Perl/Critic/Violation.pm)
BuildRequires:  perl(Pod/Escapes.pm)
BuildRequires:  perl(Pod/MinimumVersion.pm)
BuildRequires:  perl(Pod/ParseLink.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(PPI.pm)
BuildRequires:  perl(PPI/Document.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(version.pm)
# Tests only:
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(PPI/Dumper.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests only:
BuildRequires:  perl(Perl/MinimumVersion.pm)
Requires:       perl(IO/String.pm) >= 1.02
Requires:       perl(List/MoreUtils.pm) >= 0.24
Requires:       perl(Perl/Critic.pm) >= 1.084
Requires:       perl(Pod/MinimumVersion.pm) >= 50
Requires:       perl(PPI.pm) >= 1.212
Requires:       perl(PPI/Document.pm)
# This is plug-in into Test::More. Depend on it even if not mentioned in the
# code.
Requires:       perl(Test/More.pm)

# Filter underspecified dependencies





# Filter private redefinitions

# Filter private parsers 









Source44: import.info
%filter_from_requires /perl\\(List.MoreUtils.pm\\)\\s*$/d
%filter_from_requires /perl\\(Perl.Critic.Policy.pm\\)\\s*$/d
%filter_from_requires /perl\\(Perl.Critic.Utils.pm\\)\\s*$/d
%filter_from_requires /perl\\(Perl.Critic.Utils.pm\\) >= 0\\.21$/d
%filter_from_requires /perl\\(Perl.Critic.PodParser.ProhibitVerbatimMarkup.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.MinimumVersion.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.PodParser.ProhibitVerbatimMarkup.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Policy.Documentation.ProhibitAdjacentLinks.Parser.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodMinimumVersionViolation.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodParser.ProhibitBadAproposMarkup.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodParser.ProhibitLinkToSelf.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodParser.ProhibitParagraphTwoDots.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodParser.ProhibitUnbalancedParens.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.PodParser.RequireLinkedURLs.pm\\)\\s*$/d
%filter_from_provides /perl\\(Perl.Critic.Pulp.ProhibitDuplicateHashKeys.Qword.pm\\)\\s*$/d

%description
This is a collection of add-on policies for Perl::Critic.  They're under
a "pulp" theme plus other themes according to their purpose (see "POLICY
THEMES" in Perl::Critic).

%prep
%setup -q -n Perl-Critic-Pulp-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=perl OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 26 2017 Igor Vlasenko <viy@altlinux.ru> 96-alt1
- automated CPAN update

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 95-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 94-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 93-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 92-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 90-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 89-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 88-alt1
- automated CPAN update

* Thu Oct 30 2014 Igor Vlasenko <viy@altlinux.ru> 85-alt1_3
- new release

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 85-alt1_2
- update to new release by fcimport

* Thu Jun 05 2014 Igor Vlasenko <viy@altlinux.ru> 85-alt1_1
- converted for ALT Linux by srpmconvert tools

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 85-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 82-alt1
- automated CPAN update

* Wed Apr 09 2014 Igor Vlasenko <viy@altlinux.ru> 81-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 80-alt2_1
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 80-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 79-alt1_2
- update to new release by fcimport

* Mon Mar 25 2013 Igor Vlasenko <viy@altlinux.ru> 79-alt1_1
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 78-alt1_1
- update to new release by fcimport

* Wed Mar 13 2013 Igor Vlasenko <viy@altlinux.ru> 77-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 76-alt1_2
- update to new release by fcimport

* Tue Jan 29 2013 Igor Vlasenko <viy@altlinux.ru> 76-alt1_1
- update to new release by fcimport

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 75-alt1_1
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 74-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 73-alt1_3
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 70-alt1_1
- fc import

