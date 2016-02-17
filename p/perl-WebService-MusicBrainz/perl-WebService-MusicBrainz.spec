# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl(URI/Escape.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    WebService-MusicBrainz
%define upstream_version 0.93

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2_7

Summary:    No summary found
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/WebService/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/Accessor.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(URI.pm)
BuildRequires: perl(XML/LibXML.pm)
BuildRequires: perl(Module/Build/Compat.pm)
BuildArch: noarch
Source44: import.info

%description
This module will act as a factory using static methods to return specific
web service objects;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%if 0
%check
%make test
%endif

%install
%makeinstall_std

%files
%doc Changes META.yml README
%perl_vendor_privlib/*




%changelog
* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_2
- build for Sisyphus

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt2_1
- build for Sisyphus

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.93-alt1_1
- converted for ALT Linux by srpmconvert tools

