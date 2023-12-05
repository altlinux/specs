%define _unpackaged_files_terminate_build 1
%define module_name LaTeX-ToUnicode
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper/Concise.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.54
Release: alt1
Summary: Convert LaTeX commands to Unicode
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/B/BO/BORISV/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%package scripts
Summary: %name scripts
Group: Development/Perl
BuildArch: noarch
Requires: %name = %EVR

%description scripts
scripts for %name

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/L*

%files scripts
%_bindir/ltx2unitxt

%changelog
* Tue Dec 05 2023 Igor Vlasenko <viy@altlinux.org> 0.54-alt1
- automated CPAN update

* Tue Aug 22 2023 Igor Vlasenko <viy@altlinux.org> 0.53-alt1
- automated CPAN update

* Mon Dec 14 2020 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sat Jan 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- to Sisyphus as texlive dep

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

