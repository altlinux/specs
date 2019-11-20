Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Cwd.pm) perl(Data/Dumper.pm) perl(File/Spec/Functions.pm) perl(Module/Build.pm) perl(POE.pm) perl(Sub/Exporter.pm) perl(YAML.pm) perl(namespace/autoclean.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-Daemonize
Version:        0.21
Release:        alt1_11
Summary:        Role for daemonizing your Moose based application
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/MooseX-Daemonize
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-Daemonize-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Devel/AssertOS.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(MooseX/Getopt.pm)
BuildRequires:  perl(MooseX/Types/Path/Class.pm)
BuildRequires:  perl(Sub/Exporter/ForMethods.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/Moose.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
Often you want to write a persistent daemon that has a pid file, and
responds appropriately to Signals. This module provides a set of basic
roles as an infrastructure to do that.

%prep
%setup -q -n MooseX-Daemonize-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README
%doc --no-dereference LICENCE
%{perl_vendor_privlib}/MooseX*
%{perl_vendor_privlib}/Test*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_11
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_7
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_3
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_2
- update to new release by fcimport

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1.1
- rebuild to restore role requires

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_2
- update to new release by fcimport

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

