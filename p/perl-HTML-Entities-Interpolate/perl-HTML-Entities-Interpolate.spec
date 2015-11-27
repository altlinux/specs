# BEGIN SourceDeps(oneline):
BuildRequires: perl(Capture/Tiny.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Slurper.pm) perl(HTML/Entities.pm) perl(Test/Pod.pm) perl(Test/Stream.pm) perl(Tie/Function.pm)
# END SourceDeps(oneline)
%define module_version 1.08
%define module_name HTML-Entities-Interpolate
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.08
Release: alt1
Summary: Call HTML::Entities::encode_entities, via a hash, within a string
Group: Development/Perl
License: artistic_2
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/R/RS/RSAVAGE/%{module_name}-%{module_version}.tgz
BuildArch: noarch

%description
From summary: %summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes Changelog.ini LICENSE
%perl_vendor_privlib/H*

%changelog
* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- new version

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_3
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.05-alt1
- initial import by package builder

