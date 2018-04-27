# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(Test/Pod.pm) perl(base.pm) perl(inc/Module/Package.pm) perl-podlators
# END SourceDeps(oneline)
%define upstream_name    File-Share
%define upstream_version 0.25

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_5

Summary:    Extend File::ShareDir to Local Libraries
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/ShareDir.pm)
BuildArch:  noarch
Source44: import.info

%description
THis module is a dropin replacement for the File::ShareDir manpage. It
supports the 'dist_dir' and 'dist_file' functions, except these functions
have been enhanced to understand when the developer's local './share/'
directory should be used.

NOTE: module_dist and module_file are not yet supported, because (afaik)
there is no well known way to populate per-module share files. This may
change in the future.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc CONTRIBUTING Changes LICENSE META.json META.yml  README
%perl_vendor_privlib/*

%changelog
* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt3_5
- to Sisyphus as perl-Dancer2 dep

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_5
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_4
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.25-alt2_1
- rebuild to get rid of unmets

* Sat Aug 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update by mgaimport

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update by mgaimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update by mgaimport

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_2
- mga update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.02-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- converted for ALT Linux by srpmconvert tools

