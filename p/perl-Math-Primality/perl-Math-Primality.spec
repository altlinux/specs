# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/GMPz.pm) perl(Module/Build.pm) perl(POSIX.pm) perl(Test/Exception.pm) perl(Test/More.pm) perl(base.pm) perl(bigint.pm) perl(constant.pm) perl(integer.pm) perl(strict.pm) perl(warnings.pm)
# END SourceDeps(oneline)
%define module_version 0.08
%define module_name Math-Primality
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.08
Release: alt2
Summary: Check for primes with Perl
Group: Development/Perl
License: perl
URL: http://github.com/leto/math--primality

Source0: http://cpan.org.ua/authors/id/L/LE/LETO/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
%summary

%package scripts
Summary: %module_name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %module_name

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
rm %buildroot%perl_vendor_privlib/Math/aks.pl

%files
%doc README Changes README.md LICENSE examples
%perl_vendor_privlib/M*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- initial import by package builder

