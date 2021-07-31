Name:      perl-File-CheckTree
Version:   4.42
Release:   alt3
Summary:   Run many file-test checks on a tree
License:   Perl
Group: 	   Development/Perl
URL:       https://metacpan.org/release/File-CheckTree
Source0:   https://cpan.metacpan.org/authors/id/R/RJ/RJBS/File-CheckTree-%{version}.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
# Run-time:
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(deprecate.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(if.pm)
# Tests:
BuildRequires: perl(overload.pm)
BuildRequires: perl(Test/More.pm)
Requires: perl(deprecate.pm)
Source44: import.info

%description
File::CheckTree::validate() routine takes a single multi-line string
consisting of directives, each containing a file name plus a file test to try
on it. (The file test may also be a "cd", causing subsequent relative file
names to be interpreted relative to that directory.) After the file test you
may put || die to make it a fatal error if the file test fails. The default is
|| warn.  The file test may optionally have a "!' prepended to test for the
opposite condition. If you do a cd and then list some relative file names, you
may want to indent them slightly for readability. If you supply your own die()
or warn() message, you can use $file to interpolate the file name.

%prep
%setup -q -n File-CheckTree-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sat Jul 31 2021 Andrey Cherepanov <cas@altlinux.org> 4.42-alt3
- Inital build for Sisyphus.

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 4.42-alt2_311
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 4.42-alt2_310
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 4.42-alt2_309
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_309
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_308
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_307
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_306
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_305
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_304
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_303
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_301
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_300
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_299
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_298
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_297
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_296
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_295
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_293
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_292
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_291
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_290
- update to new release by fcimport

* Fri May 31 2013 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1_1
- initial fc import

