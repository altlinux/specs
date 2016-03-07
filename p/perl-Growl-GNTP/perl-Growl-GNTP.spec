# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Encode.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Growl-GNTP
Version:        0.20
Release:        alt2_8
Summary:        Perl implementation of GNTP Protocol (Client Part)
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Growl-GNTP/
Source0:        http://www.cpan.org/authors/id/M/MA/MATTN/Growl-GNTP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Crypt/CBC.pm)
BuildRequires:  perl(Data/UUID.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Digest/SHA.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Filter/Util/Call.pm)
BuildRequires:  perl(IO/Socket/PortState.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Growl::GNTP is Perl implementation of GNTP Protocol (Client Part)

%prep
%setup -q -n Growl-GNTP-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes LICENSE README.md
%{perl_vendor_privlib}/*

%changelog
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

