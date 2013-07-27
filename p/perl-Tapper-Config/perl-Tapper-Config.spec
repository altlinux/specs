# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/Rad.pm) perl(Class/C3.pm) perl(Compress/Bzip2.pm) perl(DateTime.pm) perl(DateTime/Format/Natural.pm) perl(IO/Socket.pm) perl(Kwalify.pm) perl(MRO/Compat.pm) perl(Moose.pm) perl(Net/OpenSSH.pm) perl(Perl6/Junction.pm) perl(Template.pm) perl(Test/Deep.pm) perl(Test/Exception.pm) perl(Try/Tiny.pm) perl(UNIVERSAL.pm) perl(YAML/XS.pm) perl(parent.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%add_findreq_skiplist %perl_vendor_privlib/Tapper/Config.pm
BuildRequires: perl-Tapper
%define upstream_name    Tapper-Config
%define upstream_version 4.1.3

Name:       perl-%{upstream_name}
Version:    4.1.3
Release:    alt1

Summary:    Tapper - Context sensitive configuration hub for all Tapper libs
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/T/TA/TAPPER/Tapper-Config-%{version}.tar.gz

BuildRequires: perl(File/ShareDir.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(Hash/Merge/Simple.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
BuildArch: noarch
Source44: import.info

%description
Tapper-Config provides a context-sensitive configuration hub for all Tapper
libraries.

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
%doc META.json META.yml Changes LICENSE README
%perl_vendor_privlib/*




%changelog
* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.3-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

