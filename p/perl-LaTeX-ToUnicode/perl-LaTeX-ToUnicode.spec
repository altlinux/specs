%define module_version 0.05
%define module_name LaTeX-ToUnicode
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper/Concise.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(FindBin.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt2
Summary: Convert LaTeX commands to Unicode
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://mirror.yandex.ru/mirrors/cpan/authors/id/B/BO/BORISV/%{module_name}-%{module_version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{module_version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/L*

%changelog
* Sat Jan 06 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2
- to Sisyphus as texlive dep

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- regenerated from template by package builder

* Fri Mar 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- regenerated from template by package builder

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

