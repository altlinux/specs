%def_without test
%define module_version 2.37
%define module_name TermReadKey
# BEGIN SourceDeps(oneline):
BuildRequires: libsowing-devel perl(AutoLoader.pm) perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Fcntl.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.37
Release: alt2.1
Summary: simple control over terminal driver modes
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/J/JS/JSTOWE/TermReadKey-%{version}.tar.gz
Provides: perl-Term-ReadKey = %version
Obsoletes: perl-Term-ReadKey < 2.31

%description
Term::ReadKey is a compiled perl module dedicated to providing simple
control over terminal driver modes (cbreak, raw, cooked, etc.,) support for
non-blocking reads, if the architecture allows, and some generalized handy
functions for working with terminals. One of the main goals is to have the
functions as portable as possible, so you can just plug in "use
Term::ReadKey" on any architecture and have a good likelihood of it working.

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README example
%perl_vendor_archlib/T*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.37-alt2.1
- rebuild with new perl 5.26.1

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 2.37-alt2
- fixed summary and description (closes: #33637)

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1.1
- rebuild with new perl 5.24.1

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 2.37-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.33-alt1
- new version

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1.1
- rebuild with new perl 5.20.1

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 2.32-alt1
- automated CPAN update

* Thu Nov 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.31-alt2
- upload to Sisyphus, uses CPAN name, obsoletes perl-Term-ReadKey

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 2.31-alt1
- regenerated from template by package builder

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 2.30-alt1
- initial import by package builder

