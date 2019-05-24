# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Proc-Background
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_8

Summary:    Generic interface to Unix and Win32 background process management
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/B/BZ/BZAJAC/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(App/Cache.pm)
BuildRequires: perl(Class/Accessor/Chained.pm)

BuildArch: noarch
Source44: import.info

%description
This is a generic interface for placing processes in the background on both 
Unix and Win32 platforms. This module lets you start, kill, wait on, 
retrieve exit values, and see if background processes still exist.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendor_archlib}

%files
%doc Changes README
%{perl_vendor_privlib}/*
%{_mandir}/man1/*
%{_bindir}/*

%changelog
* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.10-alt3_8
- to Sisyphus as dependency

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_8
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.10-alt2_3
- rebuild to get rid of unmets

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_3
- mga update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- converted for ALT Linux by srpmconvert tools

