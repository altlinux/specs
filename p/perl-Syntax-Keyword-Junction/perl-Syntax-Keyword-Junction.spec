%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(Sub/Exporter/Progressive.pm) perl(Test/More.pm) perl(Test/Requires.pm) perl(base.pm) perl(if.pm) perl(overload.pm) perl(syntax.pm)
# END SourceDeps(oneline)
%define module_version 0.003007
%define module_name Syntax-Keyword-Junction
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.003007
Release: alt1
Summary: Perl6 style Junction operators in Perl5
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/F/FR/FREW/Syntax-Keyword-Junction-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/S*

%changelog
* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.003007-alt1
- automated CPAN update

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.003006-alt2
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.003006-alt1
- initial import by package builder

