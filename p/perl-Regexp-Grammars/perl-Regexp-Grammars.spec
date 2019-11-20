Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Data/Show.pm) perl(IO/Prompter.pm) perl(Smart/Comments.pm) perl(charnames.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Regexp-Grammars
Version:	1.052
Release:	alt1_2
Summary:	Add grammatical parsing features to perl regular expressions
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Regexp-Grammars
Source0:	https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Regexp-Grammars-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	rpm-build-perl
BuildRequires:	perl(Module/Build.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Data/Dumper.pm)
BuildRequires:	perl(B/Hooks/Parser.pm)
BuildRequires:	perl(List/Util.pm)
BuildRequires:	perl(Moose.pm)
BuildRequires:	perl(Moose/Util/TypeConstraints.pm)

%filter_from_provides /perl.Regexp.pm./d


Source44: import.info
%add_findprov_skiplist %{_docdir}


%description
This module adds a small number of new regular expressions constructs that
can be used to implement complete recursive-descent parsing.

These constructs use the grammar patterns that were added to perl's
regular expressions in perl 5.10.

%prep
%setup -q -n Regexp-Grammars-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

# %{_fixperms} %{buildroot}

%check
./Build test

%files
%doc Changes README demo/
%{perl_vendor_privlib}/Regexp/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.052-alt1_2
- update to new release by fcimport

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.052-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 1.051-alt1
- automated CPAN update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_1
- update to new release by fcimport

* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.049-alt1_1
- update to new release by fcimport

* Mon Oct 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.049-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.048-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.048-alt1_2
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.048-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.047-alt1
- automated CPAN update

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1_4
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1_2
- update to new release by fcimport

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 1.045-alt1
- automated CPAN update

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.044-alt1_1
- update to new release by fcimport

* Mon Dec 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.044-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.043-alt1
- automated CPAN update

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.042-alt1_1
- update to new release by fcimport

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.042-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.041-alt1_3
- update to new release by fcimport

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.041-alt1
- automated CPAN update

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.040-alt1_1
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.040-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.039-alt1
- automated CPAN update

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.038-alt1_1
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.038-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.033-alt2_2
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.033-alt2_1
- moved to Sisyphus for Slic3r (by dd@ request)

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.033-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.031-alt1_1
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.030-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.030-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.028-alt1_1
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.026-alt1_1
- initial fc import

