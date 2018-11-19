# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %_var
%define upstream_name    File-SearchPath
%define upstream_version 0.07

%{?perl_default_filter}

Name: perl-File-SearchPath
Version: 0.07
Release: alt2

Summary: Search for a file in an environment variable path
License: GPL+ or Artistic
Group: Development/Perl

Url: http://search.cpan.org/dist/%upstream_name
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://search.cpan.org/CPAN/authors/id/T/TJ/TJENNESS/%upstream_name-%upstream_version.tar

BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
This module provides the ability to search a path-like environment variable for
a file (that does not necessarily have to be an executable).

%prep
%setup -n %upstream_name-%upstream_version

%build
%_bindir/perl Build.PL --installdirs=vendor
./Build

%check
./Build test

%install
./Build install --destdir=%buildroot

%files
%doc ChangeLog META.json META.yml  README
%perl_vendor_privlib/File/SearchPath.pm

%changelog
* Sun Nov 18 2018 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- initial build for ALT Sisyphus

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update by mgaimport

* Tue Oct 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.06-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- converted for ALT Linux by srpmconvert tools

