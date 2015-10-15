%define module_version 0.721
%define module_name XML-Parser-Lite
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Test.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(XMLRPC/Lite.pm) perl(diagnostics.pm) perl(re.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.721
Release: alt1
Summary: Lightweight regexp-based XML parser
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/P/PH/PHRED/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/X*

%changelog
* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.721-alt1
- regenerated from template by package builder

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.718-alt1
- regenerated from template by package builder

* Tue Sep 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.717-alt1
- initial import by package builder

