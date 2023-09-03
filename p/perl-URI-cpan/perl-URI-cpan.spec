%define _unpackaged_files_terminate_build 1
%define module_name URI-cpan
# BEGIN SourceDeps(oneline):
BuildRequires: perl(CPAN/DistnameInfo.pm) perl(Carp.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(Test/More.pm) perl(URI.pm) perl(URI/_generic.pm) perl(parent.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.009
Release: alt1
Summary: perl module %module_name
Group: Development/Perl
License: perl
URL: https://github.com/rjbs/URI-cpan

Source0: http://www.cpan.org/authors/id/R/RJ/RJBS/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/U*

%changelog
* Sun Sep 03 2023 Igor Vlasenko <viy@altlinux.org> 1.009-alt1
- automated CPAN update

* Tue Dec 21 2021 Igor Vlasenko <viy@altlinux.org> 1.008-alt1
- automated CPAN update

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

