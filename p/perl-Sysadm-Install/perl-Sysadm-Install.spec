# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(File/Spec/Functions.pm) perl(Log/Log4perl/Util.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Summary:	Typical installation tasks for system administrators
Name:		perl-Sysadm-Install
Version:	0.40
Release:	alt2_1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/Sysadm-Install/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MS/MSCHILLI/Sysadm-Install-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Archive/Tar.pm)
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Encode.pm)
BuildRequires:	perl(Expect.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Copy.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(HTTP/Request.pm)
BuildRequires:	perl(HTTP/Status.pm)
BuildRequires:	perl(Log/Log4perl.pm)
BuildRequires:	perl(LWP/UserAgent.pm)
BuildRequires:	perl(Term/ReadKey.pm)
# For test suite
BuildRequires:	perl(Test/More.pm)
# Runtime deps not automatically picked up by RPM
Requires:	perl(Archive/Tar.pm)
Requires:	perl(Config.pm)
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

%files
%doc Changes README eg
# one-liner is an overly-generic name to include in %%{_bindir} and is included
# as %%doc if needed
%exclude %{_bindir}/one-liner
%{perl_vendor_privlib}/Sysadm/

%changelog
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

