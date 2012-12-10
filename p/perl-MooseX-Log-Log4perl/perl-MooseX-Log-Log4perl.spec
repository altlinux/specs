# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(Log/Log4perl/Appender/TestBuffer.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-MooseX-Log-Log4perl
Version:    0.46
Release:    alt2_1
# see lib/MooseX/Log/Log4perl.pm
License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    A Logging Role for Moose based on Log::Log4perl
Source:     http://search.cpan.org/CPAN/authors/id/L/LA/LAMMEL/MooseX-Log-Log4perl-%{version}.tar.gz
Url:        http://search.cpan.org/dist/MooseX-Log-Log4perl
BuildArch:  noarch

BuildRequires: perl(Any/Moose.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(Test/More.pm)
# optional tests
BuildRequires: perl(Test/Pod.pm)
Source44: import.info


%description
A logging role building a very lightweight wrapper to Log::Log4perl for use
with your the Moose classes. The initialization of the Log4perl instance must
be performed prior to logging the first log message. Otherwise the default
initialization will happen, probably not doing the things you expect.

For compatibility the 'logger' attribute can be accessed to use a common
interface for application logging.

For simple logging needs use MooseX::Log::Log4perl::Easy to directly add
log_<level> methods to your class instance.

%prep
%setup -q -n MooseX-Log-Log4perl-%{version}

perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build
PERL5_CPANPLUS_IS_RUNNING=1 %{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'


%check
make test

%files
%doc README Changes t/
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt2_1
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.46-alt1_1
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.45-alt1_1
- fc import

