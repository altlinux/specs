# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Cwd.pm) perl(FindBin.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    rlib
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_10

Summary:    Manipulate @INC at compile time with relative paths
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch:  noarch
Provides:   perl(rlib.pm)
Source44: import.info

%description
rlib works in the same way as lib, except that all paths in 'LIST' are
treated as relative paths.

If rlib is used from the 'main' package then the paths in 'LIST' are
assumed to be relative to where the current script '$0' is located. This is
done by using the FindBin package.

If rlib is used from within any package other tha 'main' then the paths in
'LIST' are assumed to be relative to the root of the library where the file
for that package was found.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc  README
%perl_vendor_privlib/*

%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.02-alt3_10
- to Sisyphus as perl-Devel-Trepan dep

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_10
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_9
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_8
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2_5
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 0.02-alt2_4
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_4
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_3
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_1
- converted for ALT Linux by srpmconvert tools

