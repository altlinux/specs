%define module_version 1.27
%define module_name File-PathInfo
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(Test/Simple.pm) perl-devel
# END SourceDeps(oneline)
%define upstream_name    File-PathInfo
%define upstream_version 1.27

Name:       perl-%{upstream_name}
Version:    1.27
Release:    alt3

Summary:    Oo access to path variables stat data about a file on disk
License:    perl
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://cpan.org.ua/authors/id/L/LE/LEOCHARRE/%module_name-%module_version.tar.gz

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Smart/Comments.pm)
BuildRequires: perl(Time/Format.pm)
BuildArch: noarch
Source44: import.info

%description
This provides an object oriented interface to things you want to know about
a file, such as extension, absolute path, relative path, size, filename
(without extension), etc. It is a sort of swissarmy knife of file info.

A lot of times you need to know a file's absolute path, it's absolute
location, maybe it's relative location to something else (like DOCUMENT
ROOT), then you need to maybe know the relative path and relative location
for a file. You need to know if a file is a directory, what it's extension
is. You can commonly use regexes to do this.

This module provides commonly needed variables.

%prep
%setup -n %module_name-%module_version

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%perl_vendor_privlib/*




%changelog
* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.27-alt3
- regenerated from template by package builder

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.27-alt2_2
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 1.27-alt2_1
- rebuild to get rid of unmets

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1_1
- converted for ALT Linux by srpmconvert tools

