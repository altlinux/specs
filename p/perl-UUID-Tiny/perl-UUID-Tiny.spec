# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Digest/SHA.pm) perl(Exporter.pm) perl(IO/File.pm) perl(IO/Handle.pm) perl(MIME/Base64.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-UUID-Tiny
Version:        1.04
Release:        alt1_3
Summary:        Pure Perl UUID Support With Functional Interface
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/UUID-Tiny/
Source0:        http://www.cpan.org/authors/id/C/CA/CAUGUSTIN/UUID-Tiny-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Digest/MD5.pm)
BuildRequires:  perl(Digest/SHA1.pm)
BuildRequires:  perl(Time/HiRes.pm)
Requires:       perl(Digest/SHA1.pm)
Source44: import.info

%description
UUID::Tiny is a lightweight, low dependency Pure Perl module for UUID
creation and testing. This module provides the creation of version 1 time
based UUIDs (using random multicast MAC addresses), version 3 MD5 based
UUIDs, version 4 random UUIDs, and version 5 SHA-1 based UUIDs.

%prep
%setup -q -n UUID-Tiny-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_3
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Sun Sep 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_4
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1_3
- initial fc import

