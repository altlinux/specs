%define _unpackaged_files_terminate_build 1
%define module_name Importer
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.025
Release: alt1
Summary: Alternative but compatible interface to modules that export symbols.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/E/EX/EXODIST/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
This module acts as a layer between the Exporter manpage and modules which consume
exports. It is feature-compatible with the Exporter manpage, plus some much needed
extras. You can use this to import symbols from any exporter that follows
the Exporter manpages specification. The exporter modules themselves do not need to use
or inherit from the the Exporter manpage module, they just need to set `@EXPORT' and/or
other variables.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE README Changes
%perl_vendor_privlib/I*

%changelog
* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.025-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 0.024-alt1
- automated CPAN update

* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt2
- to Sisyphus

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- regenerated from template by package builder

* Tue Mar 22 2016 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- initial import by package builder

