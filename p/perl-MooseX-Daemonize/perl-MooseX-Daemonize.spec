# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Getopt/OptionTypeMap.pm) perl(Sub/Exporter.pm) perl(Test/Builder.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-MooseX-Daemonize
Version:        0.15
Release:        alt2_3
Summary:        Role for daemonizing your Moose based application
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/MooseX-Daemonize/
Source0:        http://search.cpan.org/CPAN/authors/id/M/MI/MICHAELR/MooseX-Daemonize-0.15.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
BuildRequires:  perl(MooseX/Types/Path/Class.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Moose.pm)


Source44: import.info

%description
Often you want to write a persistent daemon that has a pid file, and
responds appropriately to Signals. This module provides a set of basic
roles as an infrastructure to do that.

%prep
%setup -q -n MooseX-Daemonize-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- fc import

