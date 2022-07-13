Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Exception/LessClever.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		perl-Parallel-Runner
Version:	0.013
Release:	alt3_27
Summary:	An object to manage running things in parallel processes
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Parallel-Runner
Source0:	https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Parallel-Runner-%{version}.tar.gz
Patch0:		Parallel-Runner-0.013-T::E.patch
BuildArch:	noarch
BuildRequires:	rpm-build-perl
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Child.pm)
BuildRequires:	perl(POSIX.pm)
BuildRequires:	perl(Module/Build.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
BuildRequires:	perl(Test/Exception.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Time/HiRes.pm)
Source44: import.info

%description
There are several other modules to do this, you probably want one of them. This
module exists as a super-specialized parallel task manager. You create the
object with a process limit and callbacks for what to do while waiting for a
free process slot, as well as a callback for what a process should do just
before exiting.

You must explicitly call $runner->finish() when you are done. If the runner is
destroyed before its children are finished, a warning will be generated and
your child processes will be killed, by force if necessary.

If you specify a maximum of 1 then no forking will occur, and run() will block
until the coderef returns. You can force a fork by providing a boolean true
value as the second argument to run(), which will force the runner to fork
before running the coderef; however, run() will still block until the child
exits.

%prep
%setup -q -n Parallel-Runner-%{version}

# Use Test::Exception rather than Text::Exception::LessClever
%patch0

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
# %{_fixperms} $R%{buildroot}

%check
./Build test

%files
%doc CHANGES README
%{perl_vendor_privlib}/Parallel/

%changelog
* Wed Jul 13 2022 Igor Vlasenko <viy@altlinux.org> 0.013-alt3_27
- to Sisyphus as perl-Sub-HandlesVia build dep

* Tue Jul 05 2022 Igor Vlasenko <viy@altlinux.org> 0.013-alt2_27
- update to new release by fcimport

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.013-alt2_26
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.013-alt2_25
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.013-alt2_24
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.013-alt2_23
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.013-alt2_22
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_22
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_21
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_20
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_19
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_18
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_17
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_16
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_15
- update to new release by fcimport

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_14
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_12
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_11
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_8
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_5
- update to new release by fcimport

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_4
- fc import

