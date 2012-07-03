%define dist SQL-Statement
Name: perl-%dist
Version: 1.33
Release: alt1

Summary: SQL parsing and processing engine
License: GPL or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/SQL-Statement/
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Feb 13 2011
BuildRequires: perl-Clone perl-DBD-CSV perl-DBD-DBM perl-DBD-SQLite perl-Params-Util perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Soundex

%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine. While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complex nested search conditions,
and other features.

%prep
%setup -q -n %dist-%version

%ifdef __buildreqs
# don't check for conflicts under buildreq
perl -pi -e 's/ = CheckConflicts/ = 0 && CheckConflicts/' Makefile.PL
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/SQL

%changelog
* Sun Feb 13 2011 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.27 -> 1.33

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Sun Jun 28 2009 Michael Bochkaryov <misha@altlinux.ru> 1.20-alt1
- 1.20 version
- broken tests removed

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1
- NMU to fix directory ownership violation

* Sat Feb 02 2008 Michael Bochkaryov <misha@altlinux.ru> 1.15-alt1
- first build for ALT Linux Sisyphus

