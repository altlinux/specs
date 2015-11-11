%define _unpackaged_files_terminate_build 1
%define module_version 2015.103
%define module_name Time-ParseDate
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(Time/Local.pm) perl(Time/Piece.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2015.103
Release: alt1
Summary: Parse and format time values
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/M/MU/MUIR/modules/Time-ParseDate-%{version}.tar.gz
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
* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2015.103-alt1
- automated CPAN update

* Thu Apr 03 2014 Igor Vlasenko <viy@altlinux.ru> 2013.1113-alt2
- moved to Sisyphus (Obsoletes: perl-Time-modules)

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 2013.1113-alt1
- regenerated from template by package builder

* Sat Sep 28 2013 Igor Vlasenko <viy@altlinux.ru> 2013.0920-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 2013.0917-alt1
- initial import by package builder

