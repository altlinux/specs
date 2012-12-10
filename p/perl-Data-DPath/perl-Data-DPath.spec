# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Data-DPath
%define upstream_version 0.47

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Magic functions available inside filter conditions
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/XSAccessor.pm)
BuildRequires: perl(Class/XSAccessor/Array.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Iterator/Util.pm)
BuildRequires: perl(List/MoreUtils.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(POSIX.pm)
BuildRequires: perl(Safe.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(Sub/Exporter.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Text/Balanced.pm)
BuildRequires: perl(aliased.pm)
BuildRequires: perl(constant.pm)
BuildRequires: perl(feature.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
no description found

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
%doc Changes LICENSE META.json META.yml README
%perl_vendor_privlib/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  0.47-alt1_1
- mageia import by cas@ requiest

