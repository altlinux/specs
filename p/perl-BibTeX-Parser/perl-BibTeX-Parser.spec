%define module_name BibTeX-Parser
# BEGIN SourceDeps(oneline):
BuildRequires: perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(IO/File.pm) perl(IO/String.pm) perl(LaTeX/ToUnicode.pm) perl(Test/More.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.01
Release: alt2
Summary: A pure perl BibTeX parser
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BO/BORISV/%{module_name}-%{version}.tar.gz
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
%doc LICENSE Changes README
%perl_vendor_privlib/B*

%changelog
* Sat Jan 06 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt2
- to Sisyphus as texlive dep

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- regenerated from template by package builder

* Mon Mar 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- regenerated from template by package builder

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- regenerated from template by package builder

* Sun Mar 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1
- regenerated from template by package builder

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.68-alt1
- regenerated from template by package builder

* Fri Feb 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.67-alt1
- regenerated from template by package builder

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- initial import by package builder

