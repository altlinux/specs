# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(IPC/Run.pm) perl(JSON.pm) perl(JSON/XS.pm) perl(Scalar/Util.pm) perl(YAML.pm) perl(YAML/Syck.pm) perl(YAML/XS.pm) perl(base.pm) perl(overload.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Kwalify
%define upstream_version 1.23

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Kwalify schema for data structures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch:  noarch
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
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml  README
%perl_vendor_privlib/*
/usr/bin/pkwalify
/usr/share/man/man1/pkwalify.1*

%changelog
* Tue Feb 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- update by mgaimport

* Mon Feb 24 2020 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_6
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_3
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_2
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru>  1.21-alt1_1
- mageia import by cas@ requiest

