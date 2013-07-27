# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Deep.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(Test/Warn.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Text-CSV-Slurp
%define upstream_version 1.01

Name:       perl-%{upstream_name}
Version:    1.01
Release:    alt1

Summary:    Convert CSV into an array of hashes, or an array of hashes into CSV
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/B/BA/BABF/Text-CSV-Slurp-%{version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(IO/File.pm)
BuildRequires: perl(Test/Most.pm)
BuildRequires: perl(Text/CSV.pm)
BuildArch:  noarch
Source44: import.info

%description
Convert CSV into an array of hashes, or an array of hashes into CSV.

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
%doc Changes LICENSE META.yml  README
%perl_vendor_privlib/*

%changelog
* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.0-alt1_1
- mageia import by cas@ requiest

