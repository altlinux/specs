# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Safe-Isa
Version:        1.000002
Release:        alt1_1
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Safe-Isa/
Source0:        http://www.cpan.org/authors/id/M/MS/MSTROUT/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)


Source44: import.info

%description
How many times have you found yourself writing:

  if ($obj->isa('Something')) {

and then shortly afterwards cursing and changing it to:

  if (Scalar::Util::blessed($obj) and $obj->isa('Something')) {

Right. That's why this module exists.

%prep
%setup -q -n Safe-Isa-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;


%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.000002-alt1_1
- new version

