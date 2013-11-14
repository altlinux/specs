# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(CPAN/HandleConfig.pm) perl(CPAN/Version.pm) perl(Config.pm) perl(DBI.pm) perl(English.pm) perl(Exporter.pm) perl(File/Spec/Functions.pm) perl(FindBin.pm) perl(Module/Build.pm) perl(Safe.pm) perl(Test/More.pm) perl(base.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    CPAN-SQLite
%define upstream_version 0.203

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Maintain and search a minimal CPAN database
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CPAN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Archive/Tar.pm)
BuildRequires: perl(CPAN/DistnameInfo.pm)
BuildRequires: perl(CPAN/Index.pm)
BuildRequires: perl(Compress/Zlib.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/HomeDir.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IO/Zlib.pm)
BuildRequires: perl(LWP/Simple.pm)
BuildRequires: perl(parent.pm)
BuildArch:  noarch
Source44: import.info

%description
This package is used for setting up, maintaining, and searching a CPAN
database consisting of the information stored in the three main CPAN
indices: _$CPAN/modules/03modlist.data.gz_,
_$CPAN/modules/02packages.details.txt.gz_, and
_$CPAN/authors/01mailrc.txt.gz_. It should be considered at an alpha stage
of development.

One begins by creating the object as

  my $obj = CPAN::SQLite->new(%%args);

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%{make}

%check
make test

%install
%makeinstall_std

%files
%doc Changes INSTALL META.json META.yml  README
%{_bindir}/*
%{_mandir}/man1/*
%perl_vendor_privlib/*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.203-alt1_2
- moved to Sisyphus

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.203-alt1_1
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.202-alt2_2
- rebuild to get rid of unmets

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.202-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.202-alt1_1
- converted for ALT Linux by srpmconvert tools

