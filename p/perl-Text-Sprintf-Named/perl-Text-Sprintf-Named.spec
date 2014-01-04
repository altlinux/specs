# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Text-Sprintf-Named
%define upstream_version 0.0401

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_3

Summary:    Sprintf-like function with named conversions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Warn.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(warnings/register.pm)
BuildArch:  noarch
Source44: import.info

%description
Text::Sprintf::Named provides a sprintf equivalent with named conversions.
Named conversions are sprintf field specifiers (like '"%s"' or '"%4d'")
only they are associated with the key of an associative array of
parameters. So for example '"%(name)s"' will emit the ''name'' parameter as
a string, and '"%(num)4d"' will emit the ''num'' parameter as a variable
with a width of 4.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README TODO
%perl_vendor_privlib/*

%changelog
* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.0401-alt3_3
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.0401-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.0401-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0401-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.0401-alt1_1
- converted for ALT Linux by srpmconvert tools

