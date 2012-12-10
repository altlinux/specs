# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(Test.pm) perl(Test/More.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Kwalify
%define upstream_version 1.21

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Kwalify schema for data structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch: noarch
Source44: import.info

%description
Kwalify is a Perl implementation for validating data structures against the
Kwalify schema. For a schema definition, see the
http://www.kuwata-lab.com/kwalify/ruby/users-guide.01.html manpage, but see
also below the /SCHEMA DEFINITION manpage.

validate($schema_data, $data)
    Validate _$data_ according to Kwalify schema specified in
    _$schema_data_. Dies if the validation fails.

    *validate* may be exported.

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
%doc Changes README META.yml
%perl_vendor_privlib/*
/usr/bin/pkwalify
/usr/share/man/man1/pkwalify.1.*



%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  1.21-alt1_1
- mageia import by cas@ requiest

