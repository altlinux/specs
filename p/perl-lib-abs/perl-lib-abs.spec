Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-lib-abs
Version:        0.93
Release:        alt2_16
Summary:        Module lib that makes relative path absolute to caller
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/lib-abs
Source0:        https://cpan.metacpan.org/authors/id/M/MO/MONS/lib-abs-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/AutoInstall.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(Carp/Heavy.pm)
# DynaLoader not used
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(XSLoader.pm)
# Optional tests:
BuildRequires:  perl(Test/NoWarnings.pm)
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(Carp.pm)
Source44: import.info

%description
The main reason of this library is to transform relative paths to absolute
at the BEGIN stage, and push transformed to @INC. Relative path basis is
not the current working directory, but the location of file, where the
statement is (caller file). When using common lib, relative paths stays
relative to current working directory.

%prep
%setup -q -n lib-abs-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_16
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_12
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_10
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_9
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_8
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_2
- update to new release by fcimport

* Fri Nov 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_1
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2
- moved to Sisyphus (for Catalyst-Runtime update)

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_2
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.92-alt1_1
- initial fc import

