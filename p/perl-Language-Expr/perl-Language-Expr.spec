%add_findreq_skiplist %{perl_vendor_privlib}/Language/Expr/Compiler/*
%add_findreq_skiplist %{perl_vendor_privlib}/Language/Expr/Interpreter/*
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(List/Util.pm) perl(Moo/Role.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Language-Expr
Version:        0.19
Release:        alt2_4
Summary:        Simple mini-language for use in expression
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Language-Expr/
Source0:        http://www.cpan.org/authors/id/S/SH/SHARYANTO/Language-Expr-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(Regexp/Grammars.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(UUID/Tiny.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Data/Clone.pm)
BuildRequires:  perl(Data/Rmap.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(String/ShellQuote.pm)
BuildRequires:  perl(Test/Exception.pm)
Requires:       perl(JSON.pm)
Source44: import.info

%description
Language::Expr defines a simple, Perl-like expression mini-language. It
supports mathematical and string operators, arrays, hashes, variables, and
functions. See Language::Expr::Manual::Syntax for description of the
language syntax.

%prep
%setup -q -n Language-Expr-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} %{buildroot}/*

%check
# disabled for perl 5.18
%if %release != alt2_4
./Build test
%endif

%files
%doc Changes dist.ini LICENSE META.json README
%{perl_vendor_privlib}/*

%changelog
* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2_4
- moved to Sisyphus for Slic3r (by dd@ request)

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1_4
- initial fc import

