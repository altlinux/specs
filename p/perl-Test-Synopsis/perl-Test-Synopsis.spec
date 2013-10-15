# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Data/Dumper.pm) perl(ExtUtils/MM_Unix.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(FileHandle.pm) perl(Filter/Util/Call.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Socket.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl(overload.pm) perl(threads/shared.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-Synopsis
Version:	0.06
Release:	alt3_19
Summary:	Test your SYNOPSIS code
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-Synopsis/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MI/MIYAGAWA/Test-Synopsis-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(base.pm)
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(ExtUtils/Manifest.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
BuildRequires:	perl(Test/Pod.pm)
# Test::Perl::Critic -> Perl::Critic -> List::MoreUtils -> Test::LeakTrace -> Test::Synopsis
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Test/Perl/Critic.pm)
%endif
# RHEL-7 package cannot have buildreqs from EPEL-7 (aspell-en), so skip the
# spell check there; we won't need Test::Spelling either in that case
%if 0%{?rhel} < 7
BuildRequires:	aspell-en
BuildRequires:	perl(Test/Spelling.pm)
%endif
Requires:	perl(Test/Builder/Module.pm)
Source44: import.info

%description
Test::Synopsis is an (author) test module to find .pm or .pod files under your
lib directory and then make sure the example snippet code in your SYNOPSIS
section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code with
sub) and doesn't actually run the code.

%prep
%setup -q -n Test-Synopsis-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test
make test TEST_FILES="xt/*.t"

%files
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3_19
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_19
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_17
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_16
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_14
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_9
- fc import

