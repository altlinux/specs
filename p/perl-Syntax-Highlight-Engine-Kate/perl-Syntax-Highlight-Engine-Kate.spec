%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: gcc-c++ perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Path/Tiny.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Syntax-Highlight-Engine-Kate
Version:        0.13
Release:        alt1
Summary:        Port to Perl of the syntax highlight engine of the Kate text editor
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Syntax-Highlight-Engine-Kate/
Source0:        http://www.cpan.org/authors/id/M/MA/MANWAR/Syntax-Highlight-Engine-Kate-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(inc/Module/Install.pm)
BuildRequires:  perl(Module/Install/Metadata.pm)
BuildRequires:  perl(Module/Install/WriteAll.pm)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(File/Basename.pm)
# lib not used
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Term::ANSIColor not used
BuildRequires:  perl(XML/Dumper.pm)
BuildRequires:  perl(XML/TokeParser.pm)
# Tests:
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(diagnostics.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Term/ANSIColor.pm)
BuildRequires:  perl(Test/Differences.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Warn.pm)
BuildRequires:  perl(Time/HiRes.pm)
# Optional tests:
# Test::Pod 1.00 not used
Requires:       perl(base.pm)
Source44: import.info

%description
Syntax::Highlight::Engine::Kate is a port to perl of the syntax highlight
engine of the Kate text editor.

%prep
%setup -q -n Syntax-Highlight-Engine-Kate-%{version}
find -type f -exec chmod -c -x {} +
# Remove bundled modules
rm -rf ./inc
sed -i '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README REGISTERED
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- new version

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Fri Oct 11 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jan 19 2010 Artem Zolochevskiy <azol@altlinux.ru> 0.06-alt1
- initial build for Sisyphus

