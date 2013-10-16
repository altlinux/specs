%define module_version 0.13
%define module_name Hash-AsObject
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm) perl(diagnostics.pm) perl-devel
# END SourceDeps(oneline)
%define upstream_name    Hash-AsObject
%define upstream_version 0.13

Name:       perl-%{upstream_name}
Version:    0.13
Release:    alt2

Summary:    Treat hashes as objects with accessors
License:    perl
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://cpan.org.ua/authors/id/N/NK/NKUITSE/%module_name-%module_version.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildArch: noarch
Source44: import.info

%description
A Hash::AsObject is a blessed hash that provides read-write access to its
elements using accessors. (Actually, they're both accessors and mutators.)

It's designed to act as much like a plain hash as possible; this means, for
example, that you can use methods like 'DESTROY' to get or set hash
elements with that name. See below for more information.

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
%doc Changes README
%perl_vendor_privlib/*




%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- build for Sisyphus (required for perl update)

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- converted for ALT Linux by srpmconvert tools

