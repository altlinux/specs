%define _unpackaged_files_terminate_build 1
%define module_name Unicode-CaseFold
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(Benchmark.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(Unicode/UCD.pm) perl(XSLoader.pm) perl(charnames.pm) perl(strict.pm) perl(utf8.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.01
Release: alt1.1
Summary: Unicode case-folding for case-insensitive lookups.
Group: Development/Perl
License: perl
URL: http://metacpan.org/release/Unicode-CaseFold

Source0: http://www.cpan.org/authors/id/A/AR/ARODLAND/%{module_name}-%{version}.tar.gz

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README LICENSE Changes TODO
%perl_vendor_archlib/U*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2.1
- rebuild with new perl 5.20.1

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2
- moved to Sysiphus as perl-Text-Ngram dependency

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

