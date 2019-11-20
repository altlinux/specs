Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Recognize terminal size
%bcond_without perl_Term_Table_enables_terminal
# Respect Unicode rules when breaking lines
%bcond_without perl_Term_Table_enables_unicode

Name:           perl-Term-Table
Version:        0.015
Release:        alt1_1
Summary:        Format a header and rows into a table
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-Table
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Term-Table-%{version}.tar.gz
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
%if %{with perl_Term_Table_enables_terminal}
# Term::ReadKey 2.32 not used if Term::Size::Any is available
# Prefer Term::Size::Any over Term::ReadKey
BuildRequires:  perl(Term/Size/Any.pm)
%endif
%if %{with perl_Term_Table_enables_unicode}
BuildRequires:  perl(Unicode/GCString.pm)
%endif
# Tests:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Test2/API.pm)
BuildRequires:  perl(Test2/Tools/Tiny.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
Requires:       perl(Importer.pm) >= 0.024
%if %{with perl_Term_Table_enables_terminal}
Requires:       perl(Term/ReadKey.pm) >= 2.320
# Prefer Term::Size::Any over Term::ReadKey
Requires:     perl(Term/Size/Any.pm) >= 0.002
%endif
%if %{with perl_Term_Table_enables_unicode}
Requires:     perl(Unicode/GCString.pm) >= 2013.100
%endif

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(Importer.pm)/d

%description
This Perl module is able to format rows of data into tables.

%prep
%setup -q -n Term-Table-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
export LANG=en_US.UTF-8
unset TABLE_TERM_SIZE
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1_1
- update to new release by fcimport

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.015-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_1
- update to new release by fcimport

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1_1
- new version

