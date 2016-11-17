%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Summary:	Typical installation tasks for system administrators
Name:		perl-Sysadm-Install
Version:	0.48
Release:	alt1
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Sysadm-Install/
Source:	http://www.cpan.org/authors/id/M/MS/MSCHILLI/Sysadm-Install-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	findutils
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(Archive/Tar.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Encode.pm)
BuildRequires:	perl(Expect.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Copy.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(File/Which.pm)
BuildRequires:	perl(HTTP/Request.pm)
BuildRequires:	perl(HTTP/Status.pm)
BuildRequires:	perl(Log/Log4perl.pm)
BuildRequires:	perl(Log/Log4perl/Util.pm)
BuildRequires:	perl(LWP/UserAgent.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Term/ReadKey.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(utf8.pm)
# Runtime
Requires:	perl(Archive/Tar.pm)
Requires:	perl(Encode.pm)
Requires:	perl(Expect.pm)
Requires:	perl(HTTP/Request.pm)
Requires:	perl(HTTP/Status.pm)
Requires:	perl(LWP/UserAgent.pm)
Source44: import.info

%description
"Sysadm::Install" executes shell-like commands performing typical
installation tasks: Copying files, extracting tarballs, calling "make".
It has a "fail once and die" policy, meticulously checking the result of
every operation and calling "die()" immediately if anything fails,
with optional logging of everything.

"Sysadm::Install" also supports a *dry_run* mode, in which it logs
everything, but suppresses any write actions.

%prep
%setup -q -n Sysadm-Install-%{version}

# Fix perl interpreter in eg/mkperl
perl -pi -e 's|/usr/local/bin/perl|/usr/bin/perl|;' eg/mkperl

# Note: not turning off exec bits in examples because they don't
# introduce any unwanted dependencies

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test TEST_VERBOSE=1

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
# %{_fixperms} %{buildroot}

%files
%doc Changes README eg/
# one-liner is an overly-generic name to include in %%{_bindir} and is included
# as %%doc if needed
%exclude %{_bindir}/one-liner
%{perl_vendor_privlib}/Sysadm/

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.47-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1_1
- update to new release by fcimport

* Mon May 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.44-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_2
- update to new release by fcimport

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.43-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1_2
- update to new release by fcimport

* Wed Jan 30 2013 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1_1
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1_1
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.40-alt2_1
- moved to Sisyphus

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.39-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.39-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1_1
- fc import

