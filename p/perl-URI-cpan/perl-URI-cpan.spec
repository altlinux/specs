%define module_version 1.007
%define module_name URI-cpan
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/DistnameInfo.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(URI.pm) perl(URI/_generic.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.007
Release: alt2
Summary: perl module %module_name
Group: Development/Perl
License: perl
URL: https://github.com/rjbs/URI-cpan

Source0: http://cpan.org.ua/authors/id/R/RJ/RJBS/%{module_name}-%{module_version}.tar.gz
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
%doc LICENSE README Changes
%perl_vendor_privlib/U*

%changelog
* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 1.007-alt2
- to Sisyphus as perl-Perl-PrereqScanner-NotQuiteLite dep

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.007-alt1
- regenerated from template by package builder

* Thu Apr 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.006-alt1
- regenerated from template by package builder

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1.005-alt1
- regenerated from template by package builder

* Tue Sep 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- initial import by package builder

