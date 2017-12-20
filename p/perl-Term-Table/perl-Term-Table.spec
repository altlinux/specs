Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Term-Table
Version:        0.012
Release:        alt1_1
Summary:        Format a header and rows into a table
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Term-Table/
Source0:        http://www.cpan.org/authors/id/E/EX/EXODIST/Term-Table-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(Importer.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Scalar/Util.pm)
# Optional run-time:
# Term::ReadKey 2.32 not used if Term::Size::Any is available
# Prefer Term::Size::Any over Term::ReadKey
BuildRequires:  perl(Term/Size/Any.pm)
BuildRequires:  perl(Unicode/GCString.pm)
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Test2/API.pm)
BuildRequires:  perl(Test2/Tools/Tiny.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
Requires:       perl(Importer.pm) >= 0.024
Requires:       perl(Term/ReadKey.pm) >= 2.320
# Prefer Term::Size::Any over Term::ReadKey
Requires:     perl(Term/Size/Any.pm) >= 0.002
Requires:     perl(Unicode/GCString.pm) >= 2013.100

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl\\(Importer.pm\\)$/d

%description
This Perl module is able to format rows of data into tables.

%prep
%setup -q -n Term-Table-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
export LANG=en_US.UTF-8
export TERM=xterm
#make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_1
- new version

