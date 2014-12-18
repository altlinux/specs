Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Cwd.pm) perl(File/Spec/Functions.pm) perl(List/Util.pm) perl(Module/Build/Tiny.pm) perl(Moose/Role.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Getopt/OptionTypeMap.pm) perl(POE.pm) perl(Sub/Exporter.pm) perl(Test/Builder.pm) perl(YAML.pm) perl(namespace/autoclean.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-MooseX-Daemonize
Version:        0.19
Release:        alt1_1
Summary:        Role for daemonizing your Moose based application
License:        GPL+ or Artistic

URL:            http://search.cpan.org/dist/MooseX-Daemonize/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/MooseX-Daemonize-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Devel/AssertOS.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
BuildRequires:  perl(MooseX/Types/Path/Class.pm)
BuildRequires:  perl(Sub/Exporter/ForMethods.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Fatal.pm)
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

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_1
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_4
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_2
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- fc import

