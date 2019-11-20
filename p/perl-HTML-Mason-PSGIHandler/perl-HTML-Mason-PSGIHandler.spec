Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(FindBin.pm) perl(IO/Handle.pm) perl(IPC/Open3.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-HTML-Mason-PSGIHandler
Version:        0.53
Release:        alt1_18
Summary:        PSGI handler for HTML::Mason
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/HTML-Mason-PSGIHandler
Source0:        https://cpan.metacpan.org/authors/id/R/RU/RUZ/HTML-Mason-PSGIHandler-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(CGI/PSGI.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(HTML/Mason.pm)
BuildRequires:  perl(Plack/Test.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
HTML::Mason::PSGIHandler is a PSGI handler for HTML::Mason. It's based on
HTML::Mason::CGIHandler and allows you to process Mason templates on any
web servers that support PSGI.

%prep
%setup -q -n HTML-Mason-PSGIHandler-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_18
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_14
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_9
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_2
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1_1
- update to new release by fcimport

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_9
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_6
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1_4
- fc import

