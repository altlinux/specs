# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(List/Util.pm) perl(Test/More.pm) perl(Time/HiRes.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Parallel-Prefork
Version:        0.13
Release:        alt2_4
Summary:        Simple prefork server framework
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Parallel-Prefork/
Source0:        http://www.cpan.org/authors/id/K/KA/KAZUHO/Parallel-Prefork-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl(Class/Accessor/Lite.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Proc/Wait3.pm)
BuildRequires:  perl(Scope/Guard.pm)
BuildRequires:  perl(Test/Requires.pm)
BuildRequires:  perl(Parallel/Scoreboard.pm)
BuildRequires:  perl(Test/SharedFork.pm)
Source44: import.info

%description
Parallel::Prefork is much like Parallel::ForkManager, but supports graceful
shutdown and run-time reconfiguration.

%prep
%setup -q -n Parallel-Prefork-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Jan 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_4
- import for Sisyphus (required for RT)

* Tue Jan 15 2013 Andrew Kornilov <hiddenman@altlinux.ru> 0.13-alt1
- initial build for ALT Linux Sisyphus

