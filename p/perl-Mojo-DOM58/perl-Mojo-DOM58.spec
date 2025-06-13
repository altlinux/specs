%define module_name Mojo-DOM58
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Encode.pm) perl(Encode/CN.pm) perl(Encode/JP.pm) perl(Encode/KR.pm) perl(Encode/TW.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(JSON/PP.pm) perl(List/Util.pm) perl(Role/Tiny.pm) perl(Scalar/Util.pm) perl(Test/More.pm) perl(constant.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 3.002
Release: alt1
Summary: Minimalistic HTML/XML DOM parser with CSS selectors
Group: Development/Perl
License: artistic_2
URL: https://github.com/Grinnz/Mojo-DOM58

Source0: http://www.cpan.org/authors/id/D/DB/DBOOK/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
the Mojo::DOM58 manpage is a minimalistic and relaxed pure-perl HTML/XML DOM parser based
on the Mojo::DOM manpage. It supports the HTML Living Standard
and Extensible Markup Language (XML) 1.0, and
matching based on CSS3 selectors. It will
even try to interpret broken HTML and XML, so you should not use it for
validation.
%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CONTRIBUTING.md Changes README examples
%perl_vendor_privlib/M*

%changelog
* Fri Jun 13 2025 Igor Vlasenko <viy@altlinux.org> 3.002-alt1
- automated CPAN update

* Wed Apr 16 2025 Igor Vlasenko <viy@altlinux.org> 3.001-alt2
- to Sisyphus as Alien-cmake3 dep

* Thu Jul 01 2021 Igor Vlasenko <viy@altlinux.ru> 3.001-alt1
- updated by package builder

* Wed Apr 14 2021 Igor Vlasenko <viy@altlinux.ru> 3.000-alt1
- updated by package builder

* Fri Jan 18 2019 Igor Vlasenko <viy@altlinux.ru> 2.000-alt1
- regenerated from template by package builder

* Tue Nov 14 2017 Igor Vlasenko <viy@altlinux.ru> 1.004-alt1
- regenerated from template by package builder

* Thu Oct 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.003-alt1
- regenerated from template by package builder

* Mon Apr 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.002-alt1
- regenerated from template by package builder

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.001-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 1.000-alt1
- regenerated from template by package builder

* Thu Jun 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- regenerated from template by package builder

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- initial import by package builder

