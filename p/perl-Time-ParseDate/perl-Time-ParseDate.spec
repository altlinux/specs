%define module_version 2013.1113
%define module_name Time-ParseDate
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Time/Local.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2013.1113
Release: alt2
Summary: Parse and format time values
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/M/MU/MUIR/modules/%module_name-%module_version.tar.gz
BuildArch: noarch

Provides: perl-Time-modules = %version
Obsoletes: perl-Time-modules < %version
Conflicts: perl-Time-modules < %version

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/T*

%changelog
* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 2013.1113-alt2
- moved to Sisyphus (Obsoletes: perl-Time-modules)

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 2013.1113-alt1
- regenerated from template by package builder

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 2013.0920-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 2013.0917-alt1
- initial import by package builder

