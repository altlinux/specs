# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CGI/Simple.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Captcha-reCAPTCHA
Version:        0.98
Release:        alt1_1
Summary:        Perl implementation of the reCAPTCHA API
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Captcha-reCAPTCHA/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SU/SUNNYP/Captcha-reCAPTCHA-%{version}.tar.gz
# Do not disable host name verification, CPAN RT#117852
Patch0:         Captcha-reCAPTCHA-0.98-Do-not-disable-host-name-verification.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(HTML/Tiny.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(HTTP/Response.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
Requires:       perl(HTML/Tiny.pm) >= 0.904


# Filter under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(HTML.Tiny.pm\\)$/d

%description
reCAPTCHA is a hybrid mechanical Turk and captcha that allows visitors who
complete the captcha to assist in the digitization of books.

%prep
%setup -q -n Captcha-reCaptcha
%patch0 -p1
# Remove stray MacOS files, CPAN RT#117790
find -name '.*' -delete

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.98-alt1_1
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_10
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_9
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_8
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_2
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.97-alt2_1
- moved to Sisyphus (Tapper dep)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1_1
- update to new release by fcimport

* Mon Oct 22 2012 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1_1
- update to new release by fcimport

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.95-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_7
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1_5
- fc import

