# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(TAP/Parser.pm) perl(TAP/Parser/Aggregator.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/TAP/DOM.pm
%define upstream_name    TAP-DOM
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Accessors for TAP::DOM summary part
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/TAP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(parent.pm)
BuildArch: noarch
Source44: import.info

%description
The purpose of this module is A) to define a *reliable* data structure and
B) to help create this structure from TAP.

That is useful when you want to analyze the TAP in detail with "data
exploration tools", like Data::DPath.

``Reliable'' means that this structure is kind of an API that will not
change, so your data tools can, well, rely on it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%perl_vendor_privlib/*




%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- mageia import by cas@ requiest

