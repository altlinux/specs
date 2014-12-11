# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Devel/PPPort.pm) perl(Exporter.pm) perl(ExtUtils/CBuilder.pm) perl(HTML/Entities.pm) perl(Module/Build.pm) perl(Module/Build/Pluggable/PPPort.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(XSLoader.pm) perl(autodie.pm) perl(parent.pm)
# END SourceDeps(oneline)
%define module_version 1.09
%define module_name HTML-Escape
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.09
Release: alt2.1
Summary: Extremely fast HTML escape
Group: Development/Perl
License: perl
URL: https://github.com/tokuhirom/HTML-Escape

Source0: http://cpan.org.ua/authors/id/T/TO/TOKUHIROM/%module_name-%module_version.tar.gz

%description
From summary: %summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_archlib/H*
%perl_vendor_autolib/*

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt2.1
- rebuild with new perl 5.20.1

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt2
- moved to Sisyphus as dependency

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.09-alt1
- regenerated from template by package builder

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- initial import by package builder

