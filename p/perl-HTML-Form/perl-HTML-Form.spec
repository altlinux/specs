%define _unpackaged_files_terminate_build 1
Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Warnings.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-HTML-Form
Version:        6.11
Release:        alt1
Summary:        Class that represents an HTML form element
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-Form
Source0:        http://www.cpan.org/authors/id/S/SI/SIMBABQUE/HTML-Form-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/TokeParser.pm)
BuildRequires:  perl(HTTP/Request.pm)
BuildRequires:  perl(HTTP/Request/Common.pm)
BuildRequires:  perl(HTTP/Response.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(URI.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)
Requires:       perl(HTML/TokeParser.pm)
Requires:       perl(HTTP/Request.pm) >= 6
Requires:       perl(HTTP/Request/Common.pm) >= 6.030


Source44: import.info

%description
Objects of the HTML::Form class represents a single HTML <form> ... </form>
instance. A form consists of a sequence of inputs that usually have names,
and which can take on various values. The state of a form can be tweaked
and it can then be asked to provide HTTP::Request objects that can be
passed to the request() method of LWP::UserAgent.

%prep
%setup -q -n HTML-Form-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%{perl_vendor_privlib}/*

%changelog
* Sun Feb 12 2023 Igor Vlasenko <viy@altlinux.org> 6.11-alt1
- automated CPAN update

* Fri Aug 26 2022 Igor Vlasenko <viy@altlinux.org> 6.10-alt1
- automated CPAN update

* Thu Aug 18 2022 Igor Vlasenko <viy@altlinux.org> 6.09-alt1
- automated CPAN update

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 6.07-alt1
- automated CPAN update

* Thu Feb 20 2020 Igor Vlasenko <viy@altlinux.ru> 6.06-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 6.05-alt1_1
- update to new release by fcimport

* Mon Oct 07 2019 Igor Vlasenko <viy@altlinux.ru> 6.05-alt1
- automated CPAN update

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1_1
- update to new release by fcimport

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_18
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_14
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_13
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_12
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_4
- update to new release by fcimport

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1_3
- fixed build by auto update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1
- automated CPAN update

* Sat Mar 10 2012 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- 6.00 -> 6.02

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt2
- rebuilt as plain src.rpm

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.00-alt1
- initial revision
