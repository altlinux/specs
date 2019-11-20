Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Encode.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Growl-GNTP
Version:        0.21
Release:        alt1_11
Summary:        Perl implementation of GNTP Protocol (Client Part)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Growl-GNTP
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MATTN/Growl-GNTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Crypt/CBC.pm)
BuildRequires:  perl(Data/UUID.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Filter/Util/Call.pm)
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part)

%prep
%setup -q -n Growl-GNTP-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README.md
%{perl_vendor_privlib}/*

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

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- converted for ALT Linux by srpmconvert tools

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_8
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_7
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_5
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_4
- update to new release by fcimport

* Tue Feb 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2_3
- moved to Sisyphus for Slic3r (by dd@ request)

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_2
- initial fc import

