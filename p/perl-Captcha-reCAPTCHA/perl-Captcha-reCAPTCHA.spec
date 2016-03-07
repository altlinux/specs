# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CGI/Simple.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Captcha-reCAPTCHA
Version:        0.97
Release:        alt2_9
Summary:        Perl implementation of the reCAPTCHA API
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Captcha-reCAPTCHA/
Source0:        http://search.cpan.org/CPAN/authors/id/P/PH/PHRED/Captcha-reCAPTCHA-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(HTML/Tiny.pm)
BuildRequires:  perl(LWP/UserAgent.pm)
# Tests
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(HTTP/Response.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
reCAPTCHA is a hybrid mechanical turk and captcha that allows visitors who
complete the captcha to assist in the digitization of books.

%prep
%setup -q -n Captcha-reCAPTCHA-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
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

