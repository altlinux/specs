%define _unpackaged_files_terminate_build 1
%def_without test
%define module_name Devel-ebug
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Class/Accessor/Chained.pm) perl(Devel/StackTrace.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Which.pm) perl(FindBin.pm) perl(IO/Socket/INET.pm) perl(Module/Pluggable.pm) perl(PadWalker.pm) perl(Proc/Background.pm) perl(String/Koremutake.pm) perl(Term/ReadLine.pm) perl(Test/Expect.pm) perl(Test/More.pm) perl(YAML.pm) perl(base.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.64
Release: alt1
Summary: A simple, extensible Perl debugger
Group: Development/Perl
License: perl
URL: https://metacpan.org/pod/Devel::ebug

Source0: http://www.cpan.org/authors/id/P/PL/PLICEASE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
From summary: %summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description scripts
scripts for %module_name

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc author.yml Changes README
%perl_vendor_privlib/D*

%files scripts
%_man1dir/*
%_bindir/*

%changelog
* Thu Jul 15 2021 Igor Vlasenko <viy@altlinux.org> 0.64-alt1
- automated CPAN update

* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 0.63-alt2
- to Sisyphus as perl-Devel-Trepan dep

* Wed Jul 29 2020 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- updated by package builder

* Tue May 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- updated by package builder

* Tue Mar 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1
- regenerated from template by package builder

* Thu Mar 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- regenerated from template by package builder

* Thu Sep 01 2016 Igor Vlasenko <viy@altlinux.ru> 0.57-alt1
- regenerated from template by package builder

* Tue May 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- regenerated from template by package builder

* Thu Apr 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.55-alt1
- initial import by package builder

