%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(Exporter.pm) perl(Module/Build.pm) perl(Test/More.pm) perl(Time/Local.pm) perl(XSLoader.pm) perl(base.pm)
# END SourceDeps(oneline)
%define module_version 0.04
%define module_name Time-TZOffset
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.04
Release: alt1.1.1.1
Summary: Show timezone offset strings like +0900
Group: Development/Perl
License: perl
URL: https://github.com/kazeburo/Time-TZOffset

Source: http://www.cpan.org/authors/id/K/KA/KAZEBURO/Time-TZOffset-%{version}.tar.gz

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1
- rebuild with new perl 5.22.0

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- rebuild with new perl 5.20.1

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- moved to Sisyphus as dependency

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

