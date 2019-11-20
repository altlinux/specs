Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-IO-Socket-PortState
Version:        0.03
Release:        alt1_19
Summary:        Perl extension for checking the open or closed status of a port
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/IO-Socket-PortState
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMUEY/IO-Socket-PortState-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(IO/Socket/INET.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
Source44: import.info

%description
You can use it to check if a port is open or closed for a given host
and protocol.

%prep
%setup -q -n IO-Socket-PortState-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_19
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_15
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_13
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_12
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_11
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_8
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_5
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_4
- moved to Sisyphus for Slic3r (by dd@ request)

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

