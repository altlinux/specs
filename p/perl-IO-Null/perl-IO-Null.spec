Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-IO-Null
Version:        1.01
Release:        alt2_34
Summary:        Class for null filehandles
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Null
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBURKE/IO-Null-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
# Runtime
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Test.pm)
Source44: import.info

%description
IO::Null is a class for null filehandles.  Calling a constructor of
this class always succeeds, returning a new null filehandle.  Writing
to any object of this class is always a no-operation, and returns
true.  Reading from any object of this class is always no-operation,
and returns empty-string or empty-list, as appropriate.

%prep
%setup -q -n IO-Null-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc ChangeLog README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_34
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_30
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_28
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_27
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_26
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_25
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_24
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_22
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_21
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_19
- update to new release by fcimport

* Tue Aug 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2_18
- moved to Sysiphus as dependency

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_18
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_17
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_16
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- fc import

