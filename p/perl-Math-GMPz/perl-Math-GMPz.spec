BuildRequires: libgmp-devel
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Config.pm) perl(DynaLoader.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Math/BigInt.pm) perl(overload.pm) perl(subs.pm)
#BuildRequires: perl(Math/GMPf.pm) perl(Math/GMPq.pm) perl(Math/MPFR.pm)
# END SourceDeps(oneline)
%define module_version 0.38
%define module_name Math-GMPz
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.38
Release: alt1
Summary: perl interface to the GMP library's integer (mpz) functions..
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/S/SI/SISYPHUS/Math-GMPz-%{version}.tar.gz

%description
A bignum module utilising the Gnu MP (GMP) library..
   Basically this module simply wraps nearly all of
   the integer functions provided by that library.
   The documentation below extensively plagiarises
   the documentation at http://gmplib.org.
   See the Math::GMPz test suite for examples of
   usage.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README CHANGES
%perl_vendor_archlib/M*
%perl_vendor_autolib/*

%changelog
* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.37-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- initial import by package builder

