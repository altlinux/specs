# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl-podlators
# END SourceDeps(oneline)
Name:       perl-CSS-Minifier 
Version:    0.01 
Release:    alt2_21
# lib/CSS/Minifier.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Perl
Summary:    Remove unnecessary whitespace from CSS files 
Source:     http://search.cpan.org/CPAN/authors/id/P/PM/PMICHAUX/CSS-Minifier-%{version}.tar.gz
Url:        http://search.cpan.org/dist/CSS-Minifier
BuildArch:  noarch

BuildRequires: perl(ExtUtils/MakeMaker.pm)
# tests
BuildRequires: perl(Test/More.pm)


Source44: import.info

%description
This module removes unnecessary whitespace from CSS. The primary
requirement developing this module is to not break working stylesheets:
if working CSS is in input then working CSS is output. The Mac/Internet
Explorer comment hack will be minimized but not stripped and so will
continue to function.This module understands space, horizontal tab, new
line, carriage return, and form feed characters to be whitespace. Any
other characters that may be considered whitespace are not minimized.
These other characters include paragraph separator and vertical tab.For
static CSS files, it is recommended that you minify during the build
stage of web deployment. If you minify on-the-fly then it might be a
good idea to cache the minified file. Minifying static files on-the-fly
repeatedly is wasteful.

%prep
%setup -q -n CSS-Minifier-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README Changes 
%{perl_vendor_privlib}/*

%changelog
* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt2_21
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_21
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_20
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_19
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_17
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_16
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_15
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_14
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_13
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_12
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1_9
- fc import

